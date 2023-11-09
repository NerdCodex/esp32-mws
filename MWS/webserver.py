import socket


class mws():
    def __init__(self):
        self.routes = {}
    
    def add_route(self, path, HandlerFunction):
        self.routes[path] = HandlerFunction
    
    def handle_request(self, connection):
        request = connection.recv(1024).decode()
        if not request: return
        method, path, _ = request.split(' ', 2)
        for route, handler in self.routes.items():
            ispresent, pos = self.match(path, route)
            if ispresent:
                route_part = route.split("/")[pos]
                path_part = path.split("/")[pos]
                urlargs = {route_part:path_part}
                response = handler(urlargs)
                connection.send(response.encode())
                connection.close()
                return

    def match(self, path, route):
        path_parts = path.split("/")
        route_parts = route.split("/")
        if len(path_parts) != len(route_parts): return False, None
        for path_part, route_part in zip(path_parts, route_parts):
            if route_part.startswith("{") and route_part.endswith("}"):
                pos = route_parts.index(route_part)
                continue
            if path_part != route_part:
                return False, 0
        return True, pos


    def not_found(self, connection) -> None:
        response = 'HTTP/1.1 404 Not Found\nContent-Type: text/html\n\nNot Found'
        connection.send(response.encode())
        connection.close()
    
    def run(self, host="127.0.0.1", port=8080)-> None:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        print("ESP-32 Web Server is UP and Running....")
        print(f"Server is at: http://{host}:{port}/")
        while True:
            connection, addr = server.accept()
            self.handle_request(connection)