from adoption_data import Animals

animals_list = []
#data is split by "_". below splits the data and places it into array lines. 
#data from lines is then places into array animals_list using class Animals.
with open("dog_data.txt", "r") as data: 
    data_line = data.readlines()
    for x in data_line:
        lines = x.split('_')
        animals_list.append(Animals(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6]))
        
re_search = "y"

start = input("Hello, welcome to the Sullivan State Adoption Service. Hit the Enter Key to continue. ") #user must hit enter key to continue
while start != "":
    start = input("Hello, welcome to the Sullivan Adoption service. Hit the Enter Key to continue. ")

animal_selection = input("Would you like to search for Dogs or Cats? Type d for Dogs, and c for Cats. Any other key to adopt.") #select animal to adopt, only dogs for now...
if animal_selection == "d":
    while re_search == "y":
        dog_age = input("How old do you prefer your dog to be? Enter a number. ") #user enters which requirements they are looking for
        dog_size = input("How big do you prefer your dog to be? big, medium, or small. ")
        dog_color = input("Which color do you prefer your dog to be? black, brown, tan, or red. ")
        count = len(animals_list)   
        for search in animals_list:
            if dog_age == search.age and dog_size == search.size and dog_color == search.color: #searches for animals that meet requirements
                print("")
                print(search.to_string())
                print("")
            elif dog_age != search.age or dog_size != search.size or dog_color != search.color: #count: everytime an animal does not meet a requirement, 1 is subtracted from count. if count=0, that means no animal has been found.
                count = count - 1
                if count == 0:
                    print("That dog does not exist.")
                    print("")
        re_search = input("Would you like to search again? y for yes, any other key to exit to adoption service.") #adoption service
adopt = input("Would you like to adopt today? y or yes, any other key for no. ")
if adopt == "y":
    adopt_id = input("Type the ID of the animal you would like to adopt. ")
    for id_s in animals_list:
        if adopt_id == id_s.ID:
            if id_s.status == "adopted":
                print("Sorry, this animal is not available to adopt. ")
            else:
                print("")
                print("Thank you for adopting " + id_s.name + "!")
                id_s.status = "adopted"
                print(id_s.to_string())
                print("")
    
print("We hope to see you soon.")

with open("dog_data.txt", "w") as data2: #writes data from animals_list array into txt file
    for write in animals_list:
        string = (write.name + "_" + write.ID + "_" + write.animal + "_" + write.age + "_" + write.size + "_" + write.color + "_" + write.status + "_" )
        data2.writelines(string)
        data2.writelines("\n")