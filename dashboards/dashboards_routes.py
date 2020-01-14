from flask import Blueprint, render_template
from flask import current_app as app


dashboards_bp = Blueprint("dashboards_bp", __name__, template_folder="templates")


@dashboards_bp.route("/dashboards", methods=["GET"])
def dashboards():
    dashboards = ["dashboard 1", "dashboard 2", "dashboard 3"]
    menu_description = "This is the dashboards page for the Knowledge Base web application."
    return render_template("dashboards.html", title="Dashboards", menu_title="Dashboards", menu_description=menu_description, action_item="dashboard", items=dashboards)
