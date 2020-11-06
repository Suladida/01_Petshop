# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(petshop_name):
    return petshop_name["name"]

def get_total_cash(total_cash):
    return(total_cash["admin"]["total_cash"])

def add_or_remove_cash(pet_shop_list, new_cash):
    pet_shop_list["admin"] ["total_cash"] += new_cash

