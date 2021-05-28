from flask import Blueprint, Flask, render_template, request
from pathlib import Path

FLASK_HOST = "127.0.0.1"
FLASK_PORT = "5000"
DEBUG = True
base_dir = "/Users/akshayokali/akshaynayanravi/my_workspace/file_content_rendering_app"
text_files_dir = f"{base_dir}/file_content_rendering_app/app/text_files"

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
        with open(file_name, 'r') as f:
            text = f.read()
            text_split = text.split("\n")
            text_split = text_split[start_line:end_line]
            text = "\n".join(text_split)
    except (FileNotFoundError, UnicodeDecodeError) as error:
        error = error.__class__.__name__
        return f"{error} while opening file.", 400
    except Exception:
        return "Internal Error", 500

    return render_template('content.html', text=text)


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(file_content_rendering_app)
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=DEBUG)
    logger.info(
        f"Flask server started: Running on - http://{FLASK_HOST}:{FLASK_PORT}"
        + f" | Debug - {DEBUG} | CONFIG - {CONFIG}"
        + f" | app - {app.name}"
    )