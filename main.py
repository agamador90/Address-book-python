#TO DO: import your Dog class and your Rescue class from their respective files that you create
from animals import Dog
from businesses import Rescue
import random
ImportError

#TO DO: create an instance of your Rescue class
rescue = Rescue()
#TO DO: set the capacity of the Rescue class to 20
rescue.set_capacity(20)

breed_options = ["Retriever", "Lab", "Poodle", "Dachshund", "Mutt"]
colors = ["Blue", "Brown", "Gray", "Black", "White", "Golden"]

# Add 10 random dogs
for i in range(10):
    breed = random.choice(breed_options)
    color = random.choice(colors)
    age = random.randint(1,3)
    #TO DO: using the add_dog method you write for your Rescue class, add a new instance of your Dog class to the Rescue using the breed, color, and age randomly generated in the lines above
    dog = Dog(breed,color,age)
    rescue.add_dog(dog)
 
try:  # error handling just in case the user enter a invalid age format 
    user_breed = input("Insert a dog breed(Retriever, Lab, Poodle, Dachshund, Mutt): ")
    user_color = input("Insert a dog color(Blue, Brown, Gray, Black, White, Golden): ")
    user_age = int(input("Insert dog age in years: "))
    search_dog = Dog(user_breed,user_color,user_age)   
    print("You are looking for a ", search_dog.get_color(),
      search_dog.get_breed(), " that is ", str(search_dog.get_age())+ " years old.")
    print() 

# flag for dog availability
    is_dog_available = False

# search through your rescue's inventory and compare each dog in inventory to the search_dog variable. If they are equal, then change the dog availability flag to true and break out of the search

    for dog in rescue._inventory:
        if dog == search_dog:
            is_dog_available = True
    if is_dog_available:
        print("We have that dog available!")
    else:
        print("We don't have that dog available, sorry!")
        
except: print("The dog age has to be a number!")
