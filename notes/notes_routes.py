from flask import Blueprint, render_template, url_for, redirect, request
from forms import NotesForm
from cloud_sql import insert_record, update_record, \
                      search_table, show_record, delete_record

notes_bp = Blueprint("notes_bp", __name__, template_folder="templates")


@notes_bp.route("/notes", methods=["GET"])
def list_notes():
    notes = search_table("Notes", "title")
    description = "This is the notes page for the Knowledge Base web application."
    return render_template("lists.html", title="Notes", header="Notes", description=description, items=notes)


@notes_bp.route("/notes/<note_id>", methods=["GET"])
def view_entry(note_id):
    note = show_record("Notes", note_id)
    return render_template("record.html", title=f"Notes | {note[1]}", header=note[1], description=note[2])


@notes_bp.route("/notes/new", methods=["GET", "POST"])
def add_note():
    form = NotesForm()

    try:
        if form.validate_on_submit():
            insert_record("Notes", title=form.data.get("title"), description=form.data.get("description"))
            return redirect(url_for("notes_bp.list_notes"))
    except Exception as err:
        form.title.errors = [err]
    return render_template("new_note.html", title="Notes | New", form=form)


@notes_bp.route("/notes/<note_id>/edit", methods=["GET", "POST"])
def edit_note(note_id):
    form = NotesForm()
    note = show_record("Notes", note_id)

    if request.method == "GET":
        form.title.data = note[1]
        form.description.data = note[2]

    try:
        if form.validate_on_submit():
            update_record("Notes", id=note[0], title=form.data.get("title"), description=form.data.get("description"))
            return redirect(url_for("notes_bp.list_notes"))
    except Exception as err:
        form.title.errors = [err]
    return render_template("edit_note.html", title="Notes | Edit", form=form)


@notes_bp.route("/notes/<note_id>/delete", methods=["GET"])
def delete_note(note_id):
    delete_record("Notes", note_id)
    notes = search_table("Notes", "title")
    description = "This is the notes page for the Knowledge Base web application."
    return render_template("lists.html", title="Notes", header="Notes", description=description, items=notes)
