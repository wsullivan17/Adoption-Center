class Animals:
    """Holds data for each individual animal"""
    def __init__(self, animal, age, status):
        self.animal = animal
        self.age = age
        self.status = status
    
    def to_string(self):
        return f"{self.animal} : {self.age} : {self.status}"

#dog1 = Animals("b", "c", "d")
#print(dog1.name)

number = 0
animals_list = []
with open("dog_data.txt", "r") as data:
     data_line = data.readlines()
     for x in data_line:
        lines = x.split('_')
        animals_list.append(Animals(lines[1], lines[2], lines[3]))

for animal1 in animals_list:
    print(animal1.to_string())

print(animals_list[1].to_string())
print(animals_list[1].age)
        #print(lines)
