from app import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    breed = db.Column(db.String)
    sex = db.Column(db.String)
    age = db.Column(db.Integer)
    pic = db.Column(db.String) #image URL
    details = db.Column(db.String)

    events = db.relationship("Event", back_populates = "pet")

    @classmethod
    def from_dict(cls, pet_data):
        new_pet = Pet(
            name = pet_data["name"],
            species = pet_data["species"],
            breed = pet_data["breed"],
            sex = pet_data["sex"],
            age = pet_data["age"],
            pic = pet_data["pic"],
            details = pet_data["details"]
            # events = pet_data["events"]
        )
        return new_pet
    
    def to_dict(self):
        pet_dict = {}
        pet_dict["id"] = self.id
        pet_dict["name"] = self.name
        pet_dict["species"] = self.species
        pet_dict["breed"] = self.breed
        pet_dict["sex"] = self.sex
        pet_dict["age"] = self.age
        pet_dict["pic"] = self.pic
        pet_dict["details"] = self.details
        # pet_dict["events"] = self.events

        return pet_dict