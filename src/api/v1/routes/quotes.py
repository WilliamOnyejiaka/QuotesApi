from __future__ import annotations

from typing import List, Dict

from flask import jsonify, Blueprint, request
from src.api.v1.models.Quotes import Quotes
import random

quotes = Blueprint("quotes", __name__, url_prefix="/api/v1/quotes")


@quotes.get("/get-quotes")
def get_quotes():
    quotes_model = Quotes()
    results = quotes_model.find_all()
    data = []
    for result in results:
        data.append({
            'id': result["id"],
            'author': result['author'],
            'quote': result['quote']
        })

    return jsonify({
        'error': False,
        'data': data
    }), 200


# noinspection PyBroadException
@quotes.get("/get-quote/<quote_id>")
def get_quote(quote_id: str | int):
    quotes_model = Quotes()
    try:
        quote_id = int(quote_id)
    except:
        return jsonify({
            'error': True,
            'message': "id needed as integer"
        }), 400

    result = quotes_model.find(quote_id)
    quotes_model.close()

    data: Dict[int, str, str] | None = {
        'id': result["id"],
        'author': result['author'],
        'quote': result['quote']
    } if result is not None else {}

    return jsonify({
        'error': False,
        'data': data
    }), 200


@quotes.get("/random-quotes")
def random_quotes():
    number_of_quotes: str | int = request.args.get('number_of_quotes', 1)
    try:
        number_of_quotes = int(number_of_quotes)
    except:
        return jsonify({
            'error': True,
            'message': "number_of_quotes must be an integer"
        }), 400

    quotes_model: Quotes = Quotes()
    result: List = quotes_model.find_all()
    result_length: int = len(result)
    data: List = []
    generated_ids: List = []
    loop_range = range(number_of_quotes)

    for i in loop_range:
        random_id: int = random.randint(1, result_length)
        if random_id in generated_ids:
            loop_range = range(number_of_quotes - i)
        else:
            data.append(quotes_model.find(random_id))
            generated_ids.append(random_id)

    return jsonify({
        'error': False,
        'data': data
    }), 200
