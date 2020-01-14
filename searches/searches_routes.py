from flask import Blueprint, render_template
from flask import current_app as app


searches_bp = Blueprint("searches_bp", __name__, template_folder="templates")


@searches_bp.route("/searches", methods=["GET"])
def searches():
    searches = ["search 1", "search 2", "search 3"]
    menu_description = "This is the searches page for the Knowledge Base web application."
    return render_template("searches.html", title="Searches", menu_title="Searches", menu_description=menu_description, action_item="search", items=searches)
