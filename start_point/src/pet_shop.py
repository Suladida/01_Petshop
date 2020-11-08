# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(petshop_name):
    return petshop_name["name"]

def get_total_cash(total_cash):
    return(total_cash["admin"]["total_cash"])

def add_or_remove_cash(pet_shop_list, new_cash):
    pet_shop_list["admin"] ["total_cash"] += new_cash

def get_pets_sold(pets_sold):
    return (pets_sold["admin"]["pets_sold"])

def increase_pets_sold(pets_list, pets_sold):
    pets_list["admin"]["pets_sold"] += pets_sold

def get_stock_count(pet_shop_list):
    stock_count = len(pet_shop_list["pets"])
    return stock_count

def get_pets_by_breed(pet_shop_list, breed):
    pet_breed = []
    for pet in pet_shop_list["pets"]:
        if pet['breed'] == breed:
            pet_breed.append(pet)
    return pet_breed

def find_pet_by_name(pet_shop_list, input_name):
    pet_name = 0
    for pet in pet_shop_list["pets"]:
        pet_name = pet
        if pet_name['name'] == input_name:
            return pet_name
            pet_name.append(pet)
    return None

def remove_pet_by_name(pet_shop_list, input_name):
    for pet in pet_shop_list["pets"]:
        if pet["name"] == input_name:
            pet_shop_list["pets"].remove(pet)

def add_pet_to_stock(pet_shop_list, new_pet):
    pet_shop_list["pets"].append(new_pet)

def get_customer_cash(customer_list):
    return customer_list["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    total_pets = len(customer["pets"])
    return total_pets

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
