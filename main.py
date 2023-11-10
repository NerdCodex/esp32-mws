from MWS.webserver import mws
from MWS.render_template import *

app = mws()

def home(urlargs):
    return render_templates("templates/index.html", music_name="Normal Music")

app.add_route("/", home)


if __name__ == "__main__":
    app.run()