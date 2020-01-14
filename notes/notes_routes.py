from flask import Blueprint, render_template
from flask import current_app as app


notes_bp = Blueprint("notes_bp", __name__, template_folder="templates")


@notes_bp.route("/notes", methods=["GET"])
def notes():
    notes = ["note 1", "note 2", "note 3"]
    menu_description = "This is the notes page for the Knowledge Base web application."
    return render_template("notes.html", title="Notes", menu_title="Notes", menu_description=menu_description, action_item="note", items=notes)
