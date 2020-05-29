from adoption_print import print_all 

def print1():
    for animal1 in animals_list:
        print(animal1.to_string())
    print(animals_list[1].to_string())
    print(animals_list[1].age)