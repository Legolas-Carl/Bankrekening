from bmi import *

class Person:
    def __init__(self, name, age, gender, height, mass, occupation, favourite_food):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.mass = mass
        self.occupation = occupation
        self.favourite_food = favourite_food

    def walk(self):
        return f"{self.name} is going walkies!"

    def eat(self, food):
        if self.favourite_food != food:
            return f"{self.name} is eating {food}!"
        elif  self.favourite_food == food:
            return f"{self.name} is eating {food} and he's loving it!!!"

    def sleep(self):
        return f"{self.name} is in his bed, the lazy git!"

    def work(self):
        return f"{self.name} is going to work as a {self.occupation}!"

    def introduce(self):
        bmi = calc_bmi(self.mass, self.height)
        bmi_ow = determine_bmi_category(bmi)
        return (f"Hi, my name is {self.name}. I'm a {self.age}-old {self.gender} and I'm {bmi_ow}. My favourite food is {self.favourite_food}, and I work as a {self.occupation}.")

    def find_person(personen, person_id):
        for persoon in personen:
            if persoon.name == person_id:
                return persoon
        return None