import random
import datetime
from flask import Blueprint, request, jsonify
from app.api.v1.entries.models import Entry
from app.api.v1.auth.auth import token_required

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

        data = request.get_json(force=True)
        title = data.get("title", None)
        details = str(data.get("details", None)).strip()
        entry_date = str(datetime.datetime.now()).strip()
        user_entry = Entry(entry_date, title, details)

        if not title:
            return jsonify({"message" : "Please enter a title"}), 400

        if not details:
            return jsonify({"message" : "Please enter details"}), 400
        
        entry_exists = user_entry.fetch_user_entries(user_id)

        user_entry.create_user_entry(user_id)
        
        return jsonify({
            "message" : "Entry successfully added",
            "my-entry": convert_entry_to_dict(user_entry)
        }), 201

    if request.method == 'GET':
        entry = Entry(None, None, None)
        entries = entry.fetch_user_entries(user_id)
        return jsonify({
            "message" : "All entries successfully retrieved",
            "data" : entries
        }), 200
    


@mod.route('/<entryId>', methods=['PUT', 'GET'])   
@token_required    
def indiv_entry(entryId): 
    one_entry = get_entry_by_entryId(entryId) 

    if not one_entry:
        return jsonify({
            "message" : "Entry not found",
            "status": False}), 404

    if request.method == 'GET':  
        return jsonify({
            "message": "Entry successfully retrieved",
            "status": True,
            "data": convert_entry_to_dict(one_entry)
            }), 200

    if request.method == 'PUT':
        data = request.get_json(force = True)

        for key, value in data.items():
            if key == "entry_date":
                one_entry.entry_date = value
            elif key  == "title":
                one_entry.title = value
            elif key  == "details":
                one_entry.details = value
            
        return jsonify({
            "message": "Entry successfully updated",
            "status": True,
            "data": convert_entry_to_dict(one_entry)
}), 200