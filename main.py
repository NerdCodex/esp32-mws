from MWS.webserver import mws
from MWS.render_template import *

app = mws()

def home(urlargs):
    return render_template("templates/home.html")

def hello(urlargs):
    name = urlargs.get("{name}")
    return render_template("templates/index.html", var={"name":name})

app.add_route("/", home)
app.add_route("/hello/{name}", hello)


if __name__ == "__main__":
    app.run()