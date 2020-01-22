from flask import Blueprint, render_template, url_for, redirect, request
from forms import ScriptsForm
from cloud_sql import insert_record, update_record, \
                      search_table, show_record, delete_record


scripts_bp = Blueprint("scripts_bp", __name__, template_folder="templates")


@scripts_bp.route("/scripts", methods=["GET"])
def list_scripts():
    scripts = search_table("Scripts", "title")
    description = "This is the scripts page for the Knowledge Base web application."
    return render_template("lists.html", title="Scripts", header="Scripts", description=description, items=scripts)


@scripts_bp.route("/scripts/<script_id>", methods=["GET"])
def view_entry(script_id):
    script = show_record("Scripts", script_id)
    return render_template("record.html", title=f"Scripts | {script[1]}", header=script[1], description=script[2])


@scripts_bp.route("/scripts/new", methods=["GET", "POST"])
def add_script():
    form = ScriptsForm()

    try:
        if form.validate_on_submit():
            insert_record("Scripts", title=form.data.get("title"), description=form.data.get("description"))
            return redirect(url_for("scripts_bp.list_scripts"))
    except Exception as err:
        form.title.errors = [err]
    return render_template("new_script.html", title="Scripts | New", form=form)


@scripts_bp.route("/scripts/<script_id>/edit", methods=["GET", "POST"])
def edit_script(script_id):
    form = ScriptsForm()
    script = show_record("Scripts", script_id)

    if request.method == "GET":
        form.title.data = script[1]
        form.description.data = script[2]

    try:
        if form.validate_on_submit():
            update_record("Scripts", id=script[0], title=form.data.get("title"), description=form.data.get("description"))
            return redirect(url_for("scripts_bp.list_scripts"))
    except Exception as err:
        form.title.errors = [err]
    return render_template("edit_script.html", title="Scripts | Edit", form=form)


@scripts_bp.route("/scripts/<script_id>/delete", methods=["GET"])
def delete_script(script_id):
    delete_record("Scripts", script_id)
    scripts = search_table("Scripts", "title")
    description = "This is the scripts page for the Knowledge Base web application."
    return render_template("lists.html", title="Scripts", header="Scripts", description=description, items=scripts)
