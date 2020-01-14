from flask import Blueprint, render_template
from flask import current_app as app


recipes_bp = Blueprint("recipes_bp", __name__, template_folder="templates")


@recipes_bp.route("/recipes", methods=["GET"])
def recipes():
    recipes = ["recipe 1", "recipe 2", "recipe 3"]
    menu_description = "This is the recipes page for the Knowledge Base web application."
    return render_template("recipes.html", title="Recipes", menu_title="Recipes", menu_description=menu_description, action_item="recipe", items=recipes)
