from flask import Flask, render_template
from dashboards.dashboards_routes import dashboards_bp
from notes.notes_routes import notes_bp
from recipes.recipes_routes import recipes_bp
from scripts.scripts_routes import scripts_bp
from searches.searches_routes import searches_bp


app = Flask(__name__)
app.register_blueprint(dashboards_bp)
app.register_blueprint(notes_bp)
app.register_blueprint(recipes_bp)
app.register_blueprint(scripts_bp)
app.register_blueprint(searches_bp)
app.config.from_object("config")


@app.route("/")
def home():
    menu_description = "This is the main page of the Knowledge Base web application."
    return render_template("index.html", title="Knowledge Base", menu_title="Main", menu_description=menu_description)


if __name__ == "__main__":
    app.run(debug=True)
