import re
import base64

class HtmlParser:
    def __init__(self, content:str, args):
        self.content = content
        self.variables = re.findall(r'{{\s*([^}\s]+)\s*}}', self.content)
        self.args = args
        self.response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n"

    def _render(self):
        for html_variable in self.variables:
            if ":var" in html_variable:
                html_variable = html_variable.replace(":var", "")
                for input_variable, value in self.args.items():
                    if html_variable == input_variable:
                        self.content = self.content.replace("{{"+html_variable+":var}}", value)
                    else:
                        continue
            elif ":PYFILE" in html_variable:
                file_type, file_path = self.get_param(html_variable)
                self.file_to_binary(file_type, file_path)
        self.response += self.content
    
    def get_param(self, variable):
        file_type = re.findall(r'\((.*?)\)', variable)
        file_path = variable.replace(f":PYFILE({file_type[0]})", "")
        return file_type, file_path
    
    def file_to_binary(self, file_type, file_path):
        header = f"data:{file_type};base64, "
        file_content = open(file_path, "rb").read()
        binary_file_content = base64.b64encode(file_content)
        binary_file_content = header + binary_file_content.decode()
        self.content = self.content.replace("{{"+str(file_path)+":PYFILE("+str(file_type[0])+")}}", binary_file_content)
    
    def parse(self):
        self._render()
        return self.response

def render_templates(html_page, **args):
    content = open(html_page, "r").read()

    parser = HtmlParser(content=content, args=args)
    response = parser.parse()
    return response
