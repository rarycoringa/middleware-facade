from typing import Dict

from flask import Flask
from flask import jsonify

from marshmallow import Schema
from marshmallow import fields

app = Flask(__name__)

class MainSchema(Schema):
    name: str = fields.Str()
    version: str = fields.Str()

@app.route("/")
def main() -> MainSchema:
    main: Dict[str, str] = {"name": "Facade", "version": "v1.0"}
    response: MainSchema = MainSchema().dump(main)

    return jsonify(response), 200