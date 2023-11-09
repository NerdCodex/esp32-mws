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
        if path in self.routes:
            response = self.routes[path]()
            connection.send(response.encode())
        
        else:
            self.not_found(connection)
        connection.close()
    
    def not_found(self, connection):
        response = 'HTTP/1.1 404 Not Found\nContent-Type: text/html\n\nNot Found'
        connection.send(response.encode())
        connection.close()
    
    def run(self, host="127.0.0.1", port=8080):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        print("ESP-32 Web Server is UP and Running....")
        print(f"Server is at: http://{host}:{port}/")
        while True:
            connection, addr = server.accept()
            self.handle_request(connection)