from flask import Blueprint, request, make_response, jsonify
from app import db
from app.models.Pet import Pet
# from app.routes.event_routes import read_all_events
from datetime import datetime
import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

pets_bp = Blueprint("pets", __name__, url_prefix = "/pets")


#CREATE new pet profile
@pets_bp.route("", methods = ["POST"])
def create_profile():
    request_body = request.get_json()
    new_pet = Pet.from_dict(request_body)

    # new_pet = Pet(
    #     name = request_body["name"],
    #     species = request_body["species"]
    # )
    db.session.add(new_pet)
    db.session.commit()

    return make_response(jsonify({
        "pet": new_pet.to_dict()
    }), 201)
    
#READ all pet profiles
@pets_bp.route("", methods = ["GET"])
def get_all_pets():
    pets = Pet.query.all()
    pets_response = []
    for pet in pets:
        pets_response.append(pet.to_dict())
    return make_response(jsonify(pets_response), 200)

#READ one pet profile
@pets_bp.route("<pet_id>", methods = ["GET"])
def get_one_pet(pet_id):
    pet = Pet.query.get(pet_id)
    # pet_events = read_all_events(pet_id)

    # turn below into a helper function?
    pet_events = []
    for event in pet.events:
        pet_events.append(event.to_dict())
    ###
    
    return make_response(jsonify({"pet": pet.to_dict(), "events": pet_events}), 200)
    
#UPDATE pet profile
@pets_bp.route("<pet_id>", methods = ["PATCH"])
def update_pet(pet_id):
    request_body = request.get_json()
    pet = Pet.query.get(pet_id)
    for key, value in request_body.items():
        setattr(pet, key, value)
    
    db.session.commit()

    return make_response(f"{pet.name}'s profile successfully updated.", 200)
#wow ok that was trickier than I expected
#didn't want to have to specify each and every attribute to be (potentially) updated, but also didn't want to create a new Pet object, with a new id
# this way, only the attributes to be updated need to be included in the request, so even if the model changes the route doesn't need to    
    
    
#DELETE pet profile
@pets_bp.route("<pet_id>", methods = ["DELETE"])
def delete_profile(pet_id): #can't bring myself to call it delete_pet lmao
    pet = Pet.query.get(pet_id)
    db.session.delete(pet)
    db.session.commit()

    return make_response(f"Profile for {pet.name} successfully deleted.", 200)

#DELETE all pet profiles
@pets_bp.route("", methods = ["DELETE"])
def delete_all_profiles():
    pets = Pet.query.all()
    for pet in pets:
        db.session.delete(pet)
    db.session.commit()
    return make_response("All profiles successfully deleted.", 200)