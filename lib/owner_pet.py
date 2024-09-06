class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all =[]
    def __init__(self,name,pet_type,owner=None):
        if(pet_type  not in Pet.PET_TYPES):
            raise Exception(f'{pet_type} is not a valid pet type')
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.add_pet_instance(self)
        

    @classmethod
    def add_pet_instance(cls,self):
        cls.all.append(self)
    
    def set_owner(self,owner):
        if not isinstance(owner,Owner):
            raise TypeError("Owner must be an already existing Owner object")
        self.owner = owner
class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, pet):
        if not isinstance(pet,Pet):
            raise TypeError("Pet must be an already existing Pet object")
        pet.set_owner(self)
    def get_sorted_pets(self):
        pets = self.pets()
        sorted_pets = sorted(pets, key=lambda pet: pet.name)
        return sorted_pets
    
try:
    owner1 = Owner("John")
    pet1 = Pet("Buddy", "dog")
    pet2 = Pet("Whiskers", "cat")
    pet3 = Pet("Charlie", "bird")

    owner1.add_pet(pet1)
    owner1.add_pet(pet2)
    owner1.add_pet(pet3)

    sorted_pets = owner1.get_sorted_pets()
    print(f"Owner={owner1.name}'s sorted pets by name: {[pet.name for pet in sorted_pets]}")

except Exception as e:
    print(e)

# Checking all pets added to Pet.all
print(f"All pets: {[pet.name for pet in Pet.all]}")

        
        
        
        