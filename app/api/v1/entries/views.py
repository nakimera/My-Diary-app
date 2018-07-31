from flask import Blueprint, make_response, request
from .models import Entry

mod = Blueprint('entry', __name__)

@mod.route('', methods=['POST', 'GET'])
def entries():
    # method to add an entry
    if request.method =='POST':
        return make_response('Entry succesfully added', 200)

    # method to retrieve all entries
    if request.method =='GET':
        return make_response('Entries succesfully retrieved', 200)

@mod.route('/<entriesId>', methods=['PUT', 'GET'])
def entry_by_id():
    # method to get an entry by id
    if request.method =='GET':
        return make_response('Entry succesfully retrieved', 200)

    # method to modify an entry
    if requset.method =='PUT':
        return make_response('Entry succesfully modified', 200)