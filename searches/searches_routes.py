from flask import Blueprint, render_template, url_for, redirect, request
from forms import SearchesForm
from cloud_sql import insert_record, update_record, \
                      search_table, show_record, delete_record


searches_bp = Blueprint("searches_bp", __name__, template_folder="templates")


@searches_bp.route("/searches", methods=["GET"])
def list_searches():
    searches = search_table("Searches", "title")
    description = "This is the searches page for the Knowledge Base web application."
    return render_template("lists.html", title="Searches", header="Searches", description=description, items=searches)


@searches_bp.route("/searches/<search_id>", methods=["GET"])
def view_entry(search_id):
    search = show_record("Searches", search_id)
    return render_template("record.html", title=f"Searches | {search[1]}", header=search[1], description=search[2])


@searches_bp.route("/searches/new", methods=["GET", "POST"])
def add_search():
    form = SearchesForm()

    try:
        if form.validate_on_submit():
            insert_record("Searches", title=form.data.get("title"), description=form.data.get("description"))
            return redirect(url_for("searches_bp.list_searches"))
    except Exception as err:
        form.title.errors = [err]
    return render_template("new_search.html", title="Searches | New", form=form)


@searches_bp.route("/searches/<search_id>/edit", methods=["GET", "POST"])
def edit_search(search_id):
    form = SearchesForm()
    search = show_record("Searches", search_id)

    if request.method == "GET":
        form.title.data = search[1]
        form.description.data = search[2]

    try:
        if form.validate_on_submit():
            update_record("Searches", id=search[0], title=form.data.get("title"), description=form.data.get("description"))
            return redirect(url_for("searches_bp.list_searches"))
    except Exception as err:
        form.title.errors = [err]
    return render_template("edit_search.html", title="Searches | Edit", form=form)


@searches_bp.route("/searches/<search_id>/delete", methods=["GET"])
def delete_search(search_id):
    delete_record("Searches", search_id)
    searches = search_table("Searches", "title")
    description = "This is the searches page for the Knowledge Base web application."
    return render_template("lists.html", title="Searches", header="Searches", description=description, items=searches)
