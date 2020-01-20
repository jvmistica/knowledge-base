from flask import Blueprint, render_template, url_for, redirect
from flask import current_app as app
from cloud_sql import *
from forms import NotesForm

notes_bp = Blueprint("notes_bp", __name__, template_folder="templates")


@notes_bp.route("/notes", methods=["GET"])
def list_notes():
    notes = search_table("Notes", "title")
    description = "This is the notes page for the Knowledge Base web application."
    return render_template("lists.html", title="Notes", header="Notes", description=description, items=notes)


@notes_bp.route("/notes/<note_id>", methods=["GET"])
def view_entry(note_id):
    note = show_record("Notes", note_id)
    return render_template("record.html", title=f"Notes | {note[0]}", header=note[0], description=note[1])


@notes_bp.route("/notes/new", methods=["GET", "POST"])
def add_note():
    form = NotesForm()
    if form.validate_on_submit():
        insert_record("Notes", title=form.data.get("title"), description=form.data.get("description"))
        return redirect(url_for("notes_bp.list_notes"))
    return render_template("new_record.html", title="Notes | New", form=form)


@notes_bp.route("/notes/<note_id>/delete", methods=["GET"])
def delete_note(note_id):
    delete_record("Notes", note_id)
    notes = search_table("Notes", "title")
    description = "This is the notes page for the Knowledge Base web application."
    return render_template("lists.html", title="Notes", header="Notes", description=description, items=notes)
