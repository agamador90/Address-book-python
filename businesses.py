class Rescue():
    def __init__(self): #creating private variables
        self._capacity = 0
        self._inventory = []  
        
    def get_capacity(self):
        return self._capacity
    
    def set_capacity(self,capacity):
        self._capacity = capacity
        
    def get_inventory(self):
        return self._inventory
    
    def add_dog(self,dog):
        if len(self._inventory) < self._capacity:
            self._inventory.append(dog)         
    