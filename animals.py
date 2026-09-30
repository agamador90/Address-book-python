class Dog():
    def __init__(self,breed,color,age):
        self._breed = breed
        self._color = color
        self._age = age
        
   #overrride dunder method
    def __eq__(self,other):
        if isinstance(other,Dog):
            return (self._breed == other._breed and self._color == other._color and self._age == other._age)
    
   #Accessors
    def get_breed(self):
        return self._breed    
       
    def get_color(self):
        return self._color 
    
    def get_age(self):
        return self._age
    
    #Mutators
    def set_breed(self,breed):
        self._breed = breed
        
    def set_color(self,color):
        self._color = color
        
    def set_age(self,age):
        self._age = age
        
    
    
    
    
