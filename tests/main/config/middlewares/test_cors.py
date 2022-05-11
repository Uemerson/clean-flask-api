from flask import request, jsonify


def test_should_enable_cors(app, client):
    @app.route("/test_cors", methods=["POST"])
    def test_cors():
        return jsonify(request.get_json())
    assert client.post("/test_cors", json={"name": "Uemerson Pinheiro Junior"}
                       ).headers['Access-Control-Allow-Origin'] == '*'
