from flask import Flask

from file_content_rendering_app.api import (
    file_content_rendering_app,
)
from file_content_rendering_app.settings import (
    FLASK_DEBUG,
    FLASK_HOST,
    FLASK_PORT,
)

app = Flask(__name__)

# 1. File Content Rendering API
app.register_blueprint(file_content_rendering_app)

if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
    logger.info(
        f"Flask server started: Running on - http://{FLASK_HOST}:{FLASK_PORT}"
        + f" | Debug - {DEBUG} | CONFIG - {CONFIG}"
        + f" | app - {app.name}"
    )
