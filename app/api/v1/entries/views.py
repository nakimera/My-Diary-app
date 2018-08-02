import random
import datetime
from flask import Blueprint, request, jsonify
from app.api.v1.entries.models import Entry
from app.api.v1.auth.auth import token_required

mod = Blueprint('entry', __name__)

entryIds = []
entries_list = []

def get_entry_by_entryId(entryId):
    for entry in entries_list:

        if entry.entryId == int(entryId):
            return entry
    return None

def convert_entry_to_dict(entry):
    if not entry:
        return {}
    return dict([
            ('entry_date', entry.entry_date),
            ('title', entry.title),
            ('details', entry.details)
        ])


@mod.route('', methods=['POST', 'GET'])
@token_required
def entry():

    if request.method == 'POST':

        data = request.get_json(force=True)
        entry_date = datetime.datetime.now()
        title = data.get("title", None)
        details = data.get("details", None)
        user_entry = Entry(entry_date, title, details)
        entries_list.append(user_entry)

        if user_entry.title == "" or user_entry.title == " ":
            return jsonify({"message" : "Please enter a title"}), 400

        elif user_entry.details == "" or user_entry.details == " ":
            return jsonify({"message" : "Please enter details"}), 400

        return jsonify({
            "message" : "Entry successfully added",
            "data": convert_entry_to_dict(user_entry)
        }), 201

    if request.method == 'GET':

        all_entries = []

        for each_entry in entries_list:
            each_entry = convert_entry_to_dict(each_entry)
            all_entries.append(each_entry)
        
        return jsonify({
            "message" : "All entries successfully retrieved",
            "data" : all_entries
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
            if key == "date":
                one_entry.date = value
            elif key  == "title":
                one_entry.title = value
            elif key  == "details":
                one_entry.details = value
            
        return jsonify({
            "message": "Entry successfully updated",
            "status": True,
            "data": convert_entry_to_dict(one_entry)
            }), 200