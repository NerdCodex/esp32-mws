from MWS.webserver import mws
from MWS.render_template import *

app = mws()

def home(urlargs):
    name = urlargs.get("{name}")
    return render_template("templates/index.html", var={"name":name})

app.add_route("/{name}", home)

if __name__ == "__main__":
    app.run()