import json
from flask import Blueprint, jsonify, request

from src.api.v1.models.Quotes import Quotes

admin = Blueprint("admin", __name__, url_prefix="/api/v1/admin")


@admin.get("/create-table")
def create_table():
    (Quotes()).create_table()
    return jsonify({
        'error': False,
        'message': "table created successfully"
    }), 201


@admin.get("/fill-table")
def fill_table():
    quotes = Quotes()

    if (quotes.count_all())[0] > 0:
        return jsonify({
            'error': True,
            'message': "table filled already"
        }), 409

    with open("./quotes.json", encoding="UTF-8") as f:
        data = json.load(f)

    for quote in data['quotes']:
        quotes.insert_one((quote['author'], quote['quote'],))

    quotes.close()
    return jsonify({
        'error': False,
        'message': "table has been filled successfully"
    }), 200


@admin.route("/test")
def test():
    return "Hello"


@admin.delete("/drop-table")
def drop_table():
    (Quotes()).drop_table()
    return jsonify({
        'error': False,
        'message': "table dropped successfully"
    }), 200
