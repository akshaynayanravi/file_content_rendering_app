from flask import Blueprint, render_template, request

from file_content_rendering_app.settings import BASE_DIR

text_files_dir = f"{BASE_DIR}/file_content_rendering_app/text_files"

file_content_rendering_app = Blueprint("file_content_renderer", __name__)


@file_content_rendering_app.route("/", methods=["GET"])
def render_file():
    file_name = request.args.get("file", "")
    start_line = request.args.get("start", "")
    end_line = request.args.get("end", "")

    if not file_name:
        file_name = f"{text_files_dir}/file1.txt"
    else:
        file_name = f"{text_files_dir}/{file_name}"
    if start_line:
        try:
            start_line = int(start_line)
        except (ValueError, TypeError):
            return f"Invalid input for start - {start_line}", 400
    if end_line:
        try:
            end_line = int(end_line) + 1
        except (ValueError, TypeError):
            return f"Invalid input for end - {end_line}", 400

    try:
        with open(file_name, "r") as f:
            text = f.read()
            if start_line and end_line:
                text_split = text.split("\n")
                text_split = text_split[start_line:end_line]
                text = "\n".join(text_split)
    except (FileNotFoundError, UnicodeDecodeError) as error:
        error = error.__class__.__name__
        return f"{error} while opening file.", 400
    except Exception:
        return "Internal Error", 500

    return render_template("content.html", text=text)
