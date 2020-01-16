from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app
from cloud_sql import *
from forms import ScriptsForm


scripts_bp = Blueprint("scripts_bp", __name__, template_folder="templates")


@scripts_bp.route("/scripts", methods=["GET"])
def list_scripts():
    create_table("Scripts")
    scripts = search_table("Scripts", "title")
    description = "This is the scripts page for the Knowledge Base web application."
    return render_template("lists.html", title="Scripts", header="Scripts", description=description, items=scripts)


@scripts_bp.route("/scripts/<script_id>", methods=["GET"])
def view_entry(script_id):
    script = show_record("Scripts", script_id)
    return render_template("record.html", title=f"Scripts | {script[0]}", header=script[0], description=script[1])


@scripts_bp.route("/scripts/new", methods=["GET", "POST"])
def add_script():
    form = ScriptsForm()
    if form.validate_on_submit():
        insert_record("Scripts", title=form.data.get("title"), description=form.data.get("description"))
        return redirect(url_for("scripts_bp.list_scripts"))
    return render_template("new_record.html", title="Scripts | New", form=form)
