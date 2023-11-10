from MWS.webserver import mws
from MWS.templating import *

app = mws()

def home(urlargs):
    return render_templates("templates/home.html")

def hello(urlargs):
    name = urlargs.get("{name}")
    return render_templates("templates/index.html", var={"name":name})

app.add_route("/", home)
app.add_route("/hello/{name}", hello)


if __name__ == "__main__":
    app.run()