class Dog():
    def __init__(self,breed,color,age):
        self.breed = breed
        self.color = color
        self.age = age
        
   #overrride dunder method
    def __eq__(self,other):
        if isinstance(other,Dog):
            return (self.breed == other.breed and self.color == other.color and self.age == other.age)
    
   #Accessors
    def get_breed(self):
        return self.breed    
       
    def get_color(self):
        return self.color 
    
    def get_age(self):
        return self.age
    
    #Mutators
    def set_breed(self,breed):
        self.breed = breed
        
    def set_color(self,color):
        self.color = color
        
    def set_age(self,age):
        self.age = age
        
    
    
    
    
