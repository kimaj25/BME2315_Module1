import csv
class Dog: #this is the class for dog objects. It will hold all the attributes of a dog, and will also have methods to filter the list of all dogs based on those attributes. A class is a blueprint for creating objects, and an object is an instance of a class. A class can have attributes (variables) and methods (functions) that define the behavior of the objects created from that class. In this case, the Dog class has attributes such as breed, age, weight, name, and breedgroup, and methods such as get_age(), sum_ages(), instantiate_from_csv(), get_dog(), and filter().
    all_dogs = []
    def __init__(self, breed: str, age: float, weight: float, name: str = "n/a", breedgroup: str = "n/a"): #this is the constructor method for the Dog class. It will be called when a new dog object is created, and it will set the attributes of the dog object based on the parameters passed to it. The parameters are breed, age, weight, name, and breedgroup. The breed and age parameters are required, while the weight, name, and breedgroup parameters are optional and have default values of "n/a". The self parameter is a reference to the current instance of the class, and it is used to access the attributes and methods of the class.
        self.breed = breed #this line sets the breed attribute of the dog object to the value of the breed parameter passed to the constructor method. The self.breed syntax is used to access the breed attribute of the current instance of the class, while the breed parameter is a local variable that is only accessible within the constructor method. The same applies to the other attributes of the dog object.``
        self.age = age
        self.weight = weight
        self.name = name
        self.breedgroup = breedgroup
        Dog.all_dogs.append(self)

    def __repr__(self):  
        return f"{self.name}: ({self.breed} | {self.breedgroup} | {self.age} | {self.weight})" 

    def get_age(self): #our getter
        return self.age

    @classmethod
    def sum_ages(cls):
        total = 0
        for dog in Dog.all_dogs:
            total += dog.age
        return total

    @classmethod 
    def instantiate_from_csv(cls, filename: str):

        #the code below will open the .csv file and create a list of all the rows in your spreadsheet
        
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_dogs = list(reader)
        
        #the code below will create a dog object for each row, based on the data: 
        
            for row in rows_of_dogs:
                    Dog(
                    breed = row['Name'],
                    age = (int(row['Minimum Life Span']) + int(row['Maximum Life Span'])/2),
                    weight = (int(row['Minimum Weight']) + int(row['Maximum Weight'])/2),
                    breedgroup = row['Breed Group']
                )
    @classmethod #this method will return a dog object based on the breed you specify. If there are multiple dogs with the same breed, it will return the first one it finds. If there are no dogs with that breed, it will return None.
    def get_dog(cls, breed):
        for dog in Dog.all_dogs:
            if breed == dog.breed: 
                return dog


    @classmethod #this method will filter the list of all dogs based on the attributes you specify, and return a new list of dogs that match those attributes. If you don't specify an attribute, it will return all dogs.
    def filter(cls, list, breed:str ="any", age:int ="any", weight:int ="any", name:str ="any", breedgroup:str ="any"):
            all_dogs = list
            remove_list = []
            attr_list = (
                        breed,
                        age,
                        weight,
                        name,
                        breedgroup
                        )
            attr_name = (
                        "breed",
                        "age",
                        "weight",
                        "name",
                        "breedgroup"
                        )
            for attr in range(len(attr_list)): #this for loop will iterate through the list of attributes and check if the attribute is set to "any". If it is not, it will filter the list of all dogs based on that attribute and remove any dogs that do not match. It will then return the filtered list of dogs.
                if attr_list[attr] != "any":
                    for dog in all_dogs:
                        if getattr(dog,attr_name[attr]) != attr_list[attr]:
                            remove_list.append(dog)
                    all_dogs = [dog for dog in all_dogs if dog not in remove_list]
                    remove_list.clear()

            return all_dogs