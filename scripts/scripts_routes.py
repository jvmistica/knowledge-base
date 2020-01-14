from flask import Blueprint, render_template
from flask import current_app as app


scripts_bp = Blueprint("scripts_bp", __name__, template_folder="templates")


@scripts_bp.route("/scripts", methods=["GET"])
def scripts():
    scripts = ["script 1", "script 2", "script 3"]
    menu_description = "This is the scripts page for the Knowledge Base web application."
    return render_template("scripts.html", title="Scripts", menu_title="Scripts", menu_description=menu_description, action_item="script", items=scripts)
