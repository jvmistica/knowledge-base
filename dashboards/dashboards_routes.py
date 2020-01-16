from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app
from cloud_sql import *
from forms import DashboardsForm


dashboards_bp = Blueprint("dashboards_bp", __name__, template_folder="templates")


@dashboards_bp.route("/dashboards", methods=["GET"])
def list_dashboards():
    create_table("Dashboards")
    dashboards = search_table("Dashboards", "title")
    description = "This is the dashboards page for the Knowledge Base web application."
    return render_template("lists.html", title="Dashboards", header="Dashboards", description=description, items=dashboards)


@dashboards_bp.route("/dashboards/<dashboard_id>", methods=["GET"])
def view_entry(dashboard_id):
    dashboard = show_record("Dashboards", dashboard_id)
    return render_template("record.html", title=f"Dashboards | {dashboard[0]}", header=dashboard[0], description=dashboard[1])


@dashboards_bp.route("/dashboards/new", methods=["GET", "POST"])
def add_dashboard():
    form = DashboardsForm()
    if form.validate_on_submit():
        insert_record("Dashboards", title=form.data.get("title"), description=form.data.get("description"))
        return redirect(url_for("dashboards_bp.list_dashboards"))
    return render_template("new_record.html", title="Dashboards | New", form=form)
