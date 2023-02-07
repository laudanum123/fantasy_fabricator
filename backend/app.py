"""
    This is the main entry point of the application.
"""

from main import app


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
