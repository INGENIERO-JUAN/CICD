import os

from flask import Flask, jsonify, request, send_from_directory

from feature_flags import is_feature_enabled


class Calculator:
    def suma(self, a: int, b: int) -> int:
        return a + b

    def resta(self, a: int, b: int) -> int:
        return a - b


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static")
    calc = Calculator()

    @app.get("/")
    def index():
        return send_from_directory("static", "index.html")

    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok"})

    @app.get("/api/flags")
    def flags():
        return jsonify({"feature_resta": is_feature_enabled("feature-resta", False)})

    @app.get("/api/suma")
    def suma():
        a = int(request.args["a"])
        b = int(request.args["b"])
        return jsonify({"result": calc.suma(a, b)})

    @app.get("/api/resta")
    def resta():
        if not is_feature_enabled("feature-resta", False):
            return jsonify({"error": "Operación no disponible"}), 403
        a = int(request.args["a"])
        b = int(request.args["b"])
        return jsonify({"result": calc.resta(a, b)})

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
