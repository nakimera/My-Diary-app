import datetime
import random

from flask import Blueprint, jsonify, request

from app.api.v1.auth.auth import token_required
from app.api.v1.entries.models import Entry

mod = Blueprint('entry', __name__)


def convert_entry_to_dict(entry):
    return dict([
        ('entry_date', entry.entry_date),
        ('title', entry.title),
        ('details', entry.details)
    ])



@mod.route('', methods=['POST', 'GET'])
@token_required
def entry(user_id):

    if request.method == 'POST':
        """
        Adds a user entry
        """    

        data = request.get_json(force=True)
        title = data.get("title", None)
        details = str(data.get("details", None)).strip()
        entry_date = str(datetime.datetime.now()).strip()
        user_entry = Entry(entry_date, title, details)

        if not title:
            return jsonify({"message": "Please enter a title"}), 400

        if not details:
            return jsonify({"message": "Please enter details"}), 400

        user_entry.create_user_entry(user_id)

        return jsonify({
            "message": "Entry successfully added",
            "my-entry": convert_entry_to_dict(user_entry)
        }), 201

    if request.method == 'GET':
        """
        Fetches all user entries
        """

        entry = Entry(None, None, None)
        entries = entry.fetch_user_entries(user_id)
        return jsonify({
            "message": "All entries successfully retrieved",
            "data": entries
        }), 200


@mod.route('/<entry_id>', methods=['PUT', 'GET'])
@token_required
def indiv_entry(user_id, entry_id):
    entry = Entry(None, None, None)

    one_entry = entry.fetch_user_entry(entry_id)

    if not one_entry:
        """
        Returns an entry by entry_id
        """

        return jsonify({
            "message": "Entry does not exist. Try again"
        }), 404

    if request.method == 'GET':
        entry = {}
        entry['entry_id'] = one_entry[0]
        entry['title'] = one_entry[2]
        entry['details'] = one_entry[3]
        entry['entry_date'] = one_entry[4]

        return jsonify({
            "message": "Entry successfully retrieved",
            "data": entry
        }), 200

    if request.method == 'PUT':
        """
        Modifies an entry
        """
        data = request.get_json(force=True)
        title = data.get("title", None)
        details = str(data.get("details", None)).strip()
        entry_date = str(datetime.datetime.now()).strip()
        one_entry = Entry(entry_date, title, details)
        
        one_entry.modify_entries(entry_id)
        
        entry = convert_entry_to_dict(one_entry)

        return jsonify({
                "message": "Entry successfully updated",
                "data": entry
            }), 200

           