from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app
from cloud_sql import *
from forms import RecipesForm


recipes_bp = Blueprint("recipes_bp", __name__, template_folder="templates")


@recipes_bp.route("/recipes", methods=["GET"])
def list_recipes():
    create_table("Recipes")
    recipes = search_table("Recipes", "title")
    description = "This is the recipes page for the Knowledge Base web application."
    return render_template("lists.html", title="Recipes", header="Recipes", description=description, items=recipes)


@recipes_bp.route("/recipes/<recipe_id>", methods=["GET"])
def view_entry(recipe_id):
    recipe = show_record("Recipes", recipe_id)
    return render_template("record.html", title=f"Recipes | {recipe[0]}", header=recipe[0], description=recipe[1])


@recipes_bp.route("/recipes/new", methods=["GET", "POST"])
def add_recipe():
    form = RecipesForm()
    if form.validate_on_submit():
        insert_record("Recipes", title=form.data.get("title"), description=form.data.get("description"))
        return redirect(url_for("recipes_bp.list_recipes"))
    return render_template("new_record.html", title="Recipes | New", form=form)


@recipes_bp.route("/recipes/<recipe_id>/delete", methods=["GET"])
def delete_recipe(recipe_id):
    delete_record("Recipes", recipe_id)
    recipes = search_table("Recipes", "title")
    description = "This is the recipes page for the Knowledge Base web application."
    return render_template("lists.html", title="Recipes", header="Recipes", description=description, items=recipes)
