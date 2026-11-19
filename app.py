from flask import Flask, send_from_directory, request, redirect, url_for
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Serve HTML files dynamically
html_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]

for file_name in html_files:
    route_name = "/" + os.path.splitext(file_name)[0]  # "/index", "/about" etc.

    # Home page route
    if route_name == "/index":
        route_name = "/"

    # Dynamically create routes
    def make_route(f):
        return lambda f=f: send_from_directory(BASE_DIR, f)
    app.add_url_rule(route_name, file_name, make_route(file_name))

# Login page example
if "login.html" in html_files:
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            print(f"Login attempt: {username} / {password}")
            return redirect(url_for("index"))  # Redirect to home page
        return send_from_directory(BASE_DIR, "login.html")

# Serve **all files recursively** (CSS, JS, images, subfolders)
@app.route("/<path:filename>")
def serve_file(filename):
    file_path = os.path.join(BASE_DIR, filename)
    if os.path.exists(file_path):
        return send_from_directory(BASE_DIR, filename)
    return "File not found", 404

if __name__ == "__main__":
    print("Running website at http://127.0.0.1:8080")
    app.run(port=8080, debug=True)
