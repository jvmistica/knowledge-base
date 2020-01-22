from flask import Blueprint, render_template, url_for, redirect, request
from forms import RecipesForm
from cloud_sql import insert_record, update_record, \
                      search_table, show_record, delete_record


recipes_bp = Blueprint("recipes_bp", __name__, template_folder="templates")


@recipes_bp.route("/recipes", methods=["GET"])
def list_recipes():
    recipes = search_table("Recipes", "title")
    description = "This is the recipes page for the Knowledge Base web application."
    return render_template("lists.html", title="Recipes", header="Recipes", description=description, items=recipes)


@recipes_bp.route("/recipes/<recipe_id>", methods=["GET"])
def view_entry(recipe_id):
    recipe = show_record("Recipes", recipe_id)
    return render_template("record.html", title=f"Recipes | {recipe[1]}", header=recipe[1], description=recipe[2])


@recipes_bp.route("/recipes/new", methods=["GET", "POST"])
def add_recipe():
    form = RecipesForm()

    try:
        if form.validate_on_submit():
            insert_record("Recipes", title=form.data.get("title"), description=form.data.get("description"))
            return redirect(url_for("recipes_bp.list_recipes"))
    except Exception as err:
        form.title.errors = [err]
    return render_template("new_recipe.html", title="Recipes | New", form=form)


@recipes_bp.route("/recipes/<recipe_id>/edit", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    form = RecipesForm()
    recipe = show_record("Recipes", recipe_id)

    if request.method == "GET":
        form.title.data = recipe[1]
        form.description.data = recipe[2]

    try:
        if form.validate_on_submit():
            update_record("Recipes", id=recipe[0], title=form.data.get("title"), description=form.data.get("description"))
            return redirect(url_for("recipes_bp.list_recipes"))
    except Exception as err:
        form.title.errors = [err]
    return render_template("edit_recipe.html", title="Recipes | Edit", form=form)


@recipes_bp.route("/recipes/<recipe_id>/delete", methods=["GET"])
def delete_recipe(recipe_id):
    delete_record("Recipes", recipe_id)
    recipes = search_table("Recipes", "title")
    description = "This is the recipes page for the Knowledge Base web application."
    return render_template("lists.html", title="Recipes", header="Recipes", description=description, items=recipes)
