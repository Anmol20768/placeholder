class parrot:
    species = 'bird'

    def __init__(self, name, age):
        self.name=name
        self.age= age

red =parrot('rio',15)
blu=parrot('ria',18)

print("the species is {}".format(red.species))
print("the species is {}".format(blu.species))
print("{} is {} years old".format(red.name,red.age))
print("{} is {} years old".format(blu.name,blu.age))