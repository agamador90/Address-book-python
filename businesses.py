class Rescue():
    def __init__(self):
        self.capacity = 0
        self.inventory = []  
        
    def get_capacity(self):
        return self.capacity
    
    def set_capacity(self,capacity):
        self.capacity = capacity
        
    def get_inventory(self):
        return self.inventory
    
    def add_dog(self,dog):
        if len(self.inventory) < self.capacity:
            self.inventory.append(dog)         
    