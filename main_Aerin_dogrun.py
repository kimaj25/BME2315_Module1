from dog_Aerin import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 

dog1 = Dog("German Pinscher", 1, 43.0, "Rizzo")
dog2 = Dog("Golden Retriever", 3, 64.0, "Callypso")
dog3 = Dog("Chihuahua", 2, 15.6, "Cheeto")


#print(dog1)
#print(dog2.age) #I just want to retrieve the age of dog2, not the whole object


#print(dog3.get_age()) #call the getter method to retrieve the age of dog3


#For loop to iterate through the list of all dogs and sum their ages
total = 0

for dog in Dog.all_dogs:
    total += dog.age
print(total)
print(f"Total age of all dogs is: {total}")


print(Dog.sum_ages()) #class class method



with open("C:/Users/aerin/OneDrive/Desktop/COMP BME 2315 Fall 2026/Module 1/BME2315_Module 1/BME2315_Module1/dog data set.csv", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader) # Get the first row
        for h in headers:
            print(h)


Dog.instantiate_from_csv("C:/Users/aerin/OneDrive/Desktop/COMP BME 2315 Fall 2026/Module 1/BME2315_Module 1/BME2315_Module1/dog data set.csv")

print(Dog.get_dog("Pug"))



Dog.all_dogs.sort(key=Dog.get_age, reverse=False)

for dog in Dog.all_dogs:
    print(dog)

working_dogs = range(len(Dog.filter(Dog.all_dogs, breedgroup = "Working")))

print(f'Number of Working Dog breeds = {len(working_dogs)}')

toy_dogs = range(len(Dog.filter(Dog.all_dogs, breedgroup = "Toy")))

print(f'Number of Toy Dog breeds = {len(toy_dogs)}')

#Data Bar graphs

#Dog.instantiate_from_csv("C:/Users/aerin/OneDrive/Desktop/COMP BME 2315 Fall 2026/Module 1/BME2315_Module 1/BME2315_Module1/dog data set.csv") #for dataset but already done above, so commented out to avoid duplicate data
age_Working_dogs = [] #list to hold the ages of Working dogs
age_Toy_dogs = [] #list to hold the ages of Toy dogs

#Filter the list of all dogs to get the ages of Working and Toy dogs and append them to their respective lists
for dog in Dog.filter(Dog.all_dogs, breedgroup = "Working"): #for loop to iterate through the list of all dogs and filter for Working dogs, then append their ages to the age_Working_dogs list
    age_Working_dogs.append(dog.age) #this line appends the age of each Working dog to the age_Working_dogs list
for dog in Dog.filter(Dog.all_dogs, breedgroup = "Toy"): #for loop to iterate through the list of all dogs and filter for Toy dogs, then append their ages to the age_Toy_dogs list
    age_Toy_dogs.append(dog.age) #this line appends the age of each Toy dog to the age_Toy_dogs list


#the code below will calculate the mean and standard deviation of the ages of Working and Toy dogs, and store them in variables for later use in the bar graph
x_Working_dog_bar = (statistics.mean(age_Working_dogs))
x_Toy_dog_bar = (statistics.mean(age_Toy_dogs))
age_Working_dog_stdev = (statistics.stdev(age_Working_dogs))
age_Toy_dog_stdev = (statistics.stdev(age_Toy_dogs))

#the code below will print the mean and standard deviation of the ages of Working and Toy dogs to the console for verification
print(f'x_Working_dog_bar = {x_Working_dog_bar}, age_Working_dog_stdev {age_Working_dog_stdev}')
print(f'x_Toy_dog_bar = {x_Toy_dog_bar}, age_Toy_dog_stdev {age_Toy_dog_stdev}')


#the code below will create a bar graph of the mean ages of Working and Toy dogs, with error bars representing the standard deviation of the ages. The x-axis will be labeled with the breed groups, and the y-axis will be labeled with the mean age. The title of the graph will be "Mean Age of Working and Toy Dogs". The graph will be displayed using plt.show().
Dog_breedgroup_cols = ['Working Dogs', 'Toy Dogs']
mean_breedgroup = [x_Working_dog_bar, x_Toy_dog_bar]
stdev_breedgroup = [age_Working_dog_stdev, age_Toy_dog_stdev]
yerr = [np.zeros(len(mean_breedgroup)), stdev_breedgroup]

#the code below will create a bar graph of the mean ages of Working and Toy dogs, with error bars representing the standard deviation of the ages. The x-axis will be labeled with the breed groups, and the y-axis will be labeled with the mean age. The title of the graph will be "Mean Age of Working and Toy Dogs". The graph will be displayed using plt.show().
plt.bar(Dog_breedgroup_cols, mean_breedgroup, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average Lifespan of Breedgroups")
plt.xlabel("Breedgroup")
plt.ylabel("Average Lifespan (age)")
plt.show()



#Code for scatter plot
breed_age = []
breed_weight = []

#the code below will iterate through the list of all dogs and append their ages and weights to the breed_age and breed_weight lists, respectively. These lists will be used to create a scatter plot of the ages and weights of all dogs.
for dog in Dog.all_dogs:
    breed_age.append(dog.age)

for dog in Dog.all_dogs:
    breed_weight.append(dog.weight)

X = [breed_age]  # Independent variable
y = [breed_weight]   # Dependent variable


plt.scatter(X, y, color='blue')
plt.xlabel('Average Lifespan')
plt.ylabel('Average Weight')
plt.title('Scatter Plot of Average Lifespan vs Average Weight')
plt.show()