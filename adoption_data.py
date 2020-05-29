class Animals:
    """Holds data for each individual animal"""
    def __init__(self, name, ID, animal, age, size, color, status):
        self.name = name
        self.ID = ID
        self.animal = animal
        self.age = age
        self.size = size
        self.color = color
        self.status = status
    
    def to_string(self):
        """Serves as a way to display the data imported to animals_list from data text files"""
        return f"Name: {self.name}, ID: {self.ID}, Animal: {self.animal} , Age: {self.age} , Size: {self.size}, Color: {self.color}, Status: {self.status}"