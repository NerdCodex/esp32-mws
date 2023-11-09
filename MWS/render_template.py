
class HTML:
    def __init__(self, path, var:dict={}):
        self.path = path
        self.var = var
        self.content = open(path, "r").read()
    
    def check_var(self):
        if self.var is not None:
            for variable, value in self.var.items():
                self.content = self.content.replace("{{"+f"{variable}:var"+"}}", value)
        else:
            pass
    
    def check_files(self):
        pass
    
    def run(self)-> str:
        self.check_var()
        self.check_files()
        response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
        response += self.content
        return response
        

def render_template(path, var:dict={}) ->str:
    html = HTML(path, var=var)
    response = html.run()
    return response
