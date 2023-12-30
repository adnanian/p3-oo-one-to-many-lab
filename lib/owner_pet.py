class Pet:
    

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of the defined values:  {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if (owner == None or isinstance(owner, Owner)):
            self._owner = owner
        else:
            raise Exception(f"{owner} must be of type Owner.")

class Owner:
    
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner.name == self.name]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            Pet.all[Pet.all.index(pet)].owner = self
        else:
            raise Exception(f"{pet} must be of type Pet.")
        
    def get_sorted_pets(self):
        owner_pets = self.pets()
        return sorted(owner_pets, key=lambda pet : pet.name)