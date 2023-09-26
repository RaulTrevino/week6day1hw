from flask import request
from uuid import uuid4

from app import app
from database import mutant

@app.get('/mutant')
def get_users():
    return {'mutant':mutant}, 200


@app.post('/mutant')
def create_user():
    mutant_data = request.get_json()
    mutant[uuid4().hex]=mutant_data
    return mutant_data, 201


@app.put('/mutant/<user_id>')
def update_user(user_id):
    user_data = request.get_json()
    try:
        mutant = mutant[user_id]
        mutant['mutant']= user_data['mutant']
        return mutant,200
    except KeyError:
        return {'message':'mutant not found'},400




@app.delete('/mutant')
def delete_user():
    mutant_data = request.get_json()
    for i,mutant in enumerate(mutant):
        if mutant['username'] == mutant_data["username"]:
            mutant.pop(i)
    return {'message':f'{mutant_data["username"]} deleted'}, 202