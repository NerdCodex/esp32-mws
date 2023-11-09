from EWS.webserver import mws
from EWS.render_template import *

app = mws()

def home():
    return render_template("templates/index.html", var={"name":"Rakesh"})

app.add_route("/", home)

if __name__ == "__main__":
    app.run()