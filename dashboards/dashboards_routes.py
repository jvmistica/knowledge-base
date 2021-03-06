from flask import Blueprint, render_template, url_for, redirect, request, Response
from forms import DashboardsForm
from cloud_sql import insert_record, update_record, \
                      search_table, show_record, delete_record


dashboards_bp = Blueprint("dashboards_bp", __name__, template_folder="templates")


@dashboards_bp.route("/dashboards", methods=["GET"])
def list_dashboards():
    dashboards = search_table("Dashboards", "title")
    description = "This is the dashboards page for the Knowledge Base web application."
    return render_template("lists.html", title="Dashboards", header="Dashboards", description=description, items=dashboards)


@dashboards_bp.route("/dashboards/<dashboard_id>", methods=["GET"])
def view_entry(dashboard_id):
    dashboard = show_record("Dashboards", dashboard_id)
    return render_template("record.html", title=f"Dashboards | {dashboard[1]}", header=dashboard[1], description=dashboard[2])


@dashboards_bp.route("/dashboards/new", methods=["GET", "POST"])
def add_dashboard():
    form = DashboardsForm()

    try:
        if form.validate_on_submit():
            if form.submit.data:
                insert_record("Dashboards", title=form.data.get("title"), description=form.data.get("description"))
            return redirect(url_for("dashboards_bp.list_dashboards"))
    except Exception as err:
        form.title.errors = [err]
    return render_template("dashboard.html", title="Dashboards | New", form=form, action="New")


@dashboards_bp.route("/dashboards/<dashboard_id>/edit", methods=["GET", "POST"])
def edit_dashboard(dashboard_id):
    form = DashboardsForm()
    dashboard = show_record("Dashboards", dashboard_id)

    if request.method == "GET":
        form.title.data = dashboard[1]
        form.description.data = dashboard[2]

    try:
        if form.validate_on_submit():
            if form.submit.data:
                update_record("Dashboards", id=dashboard[0], title=form.data.get("title"), description=form.data.get("description"))
            return redirect(url_for("dashboards_bp.list_dashboards"))
    except Exception as err:
        form.title.errors = [err]
    return render_template("dashboard.html", title="Dashboards | Edit", form=form, action="Edit")


@dashboards_bp.route("/dashboards/<dashboard_id>/delete", methods=["GET"])
def delete_dashboard(dashboard_id):
    delete_record("Dashboards", dashboard_id)
    dashboards = search_table("Dashboards", "title")
    description = "This is the dashboards page for the Knowledge Base web application."
    return render_template("lists.html", title="Dashboards", header="Dashboards", description=description, items=dashboards)


@dashboards_bp.route("/dashboards/download", methods=["GET"])
def download_dashboards():
    results = search_table("Dashboards", "title", "description")
    csv = "".join([f"{row[0]}, {row[1]}\n" for row in results])

    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=dashboards.csv"})
