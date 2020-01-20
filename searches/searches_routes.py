from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app
from cloud_sql import *
from forms import SearchesForm


searches_bp = Blueprint("searches_bp", __name__, template_folder="templates")


@searches_bp.route("/searches", methods=["GET"])
def list_searches():
    create_table("Searches")
    searches = search_table("Searches", "title")
    description = "This is the searches page for the Knowledge Base web application."
    return render_template("lists.html", title="Searches", header="Searches", description=description, items=searches)


@searches_bp.route("/searches/<search_id>", methods=["GET"])
def view_entry(search_id):
    search = show_record("Searches", search_id)
    return render_template("record.html", title=f"Searches | {search[0]}", header=search[0], description=search[1])


@searches_bp.route("/searches/new", methods=["GET", "POST"])
def add_search():
    form = SearchesForm()
    if form.validate_on_submit():
        insert_record("Searches", title=form.data.get("title"), description=form.data.get("description"))
        return redirect(url_for("searches_bp.list_searches"))
    return render_template("new_record.html", title="Searches | New", form=form)


@searches_bp.route("/searches/<search_id>/delete", methods=["GET"])
def delete_search(search_id):
    delete_record("Searches", search_id)
    searches = search_table("Searches", "title")
    description = "This is the searches page for the Knowledge Base web application."
    return render_template("lists.html", title="Searches", header="Searches", description=description, items=searches)
