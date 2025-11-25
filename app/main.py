from flask import Blueprint, jsonify, render_template

main_bp = Blueprint("main", __name__)

# Route interface web
@main_bp.route("/")
def home_page():
    return render_template(
        "index.html",
        title="Accueil",
        message="Bienvenue sur mon Projet-DevOps-Python"
    )

# Route API
@main_bp.route("/api/hello")
def api_hello():
    return jsonify({"message": "Hello from the API!"})
