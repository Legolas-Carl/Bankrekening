from person import Person

persons = []

persons.append(Person(
    "Carl Giroulle",
    55,
    "Male",
    1.77,
    102,
    "Student",
    "Steak and Belgian Fries"
))

persons.append(Person(
    "Staf Coppens",
    40,
    "Male",
    1.73,
    75,
    "Presenter",
    "Pizza"
))

persons.append(Person(
    "Tom Waes",
    54,
    "Male",
    1.85,
    85,
    "Presenter",
    "A pint of lager"
))


selection = int(
    input(f"""
        **************************************
        **************************************
        **             The Simz            **
        **************************************
        **************************************
        **************************************
        ** 1) Create character              **
        ** 2) Exit                          **
        **************************************
        ** Select an option (1-2): """))

if selection == 1:

    ip_name =   input("Enter your character's name: ")
    ip_age =    float(input("Enter your character's age: "))
    ip_gender = input("Enter your character's gender (m/f/o): ")
    ip_height = float(input("Enter your character's height (in metres): "))
    ip_mass =   float(input("Enter your character's mass (in kilos): "))
    ip_occ =    input("Enter your character's occupation: ")
    ip_food =   input("Enter your character's favourite food: ")

    if ip_gender.lower == "m":
        persons.append(Person(ip_name, ip_age, "male", ip_height, ip_mass, ip_occ, ip_food))
    elif ip_gender.lower == "f":
        persons.append(Person(ip_name, ip_age, "female", ip_height, ip_mass, ip_occ, ip_food))
    else:
        persons.append(Person(ip_name, ip_age, "lgbtq+", ip_height, ip_mass, ip_occ, ip_food))

    my_person = Person.find_person(persons, ip_name)
    # print (my_person.name)
    print(my_person.introduce())

else:
    print ("""
        ********
        Bye Bey!
        ********""")



#my_person = Person.find_person(persons, "Staf Coppens")
#print (my_person.name)

#print (my_person.walk())
#print(my_person.eat("Brussels sprouts"))
#print(my_person.eat("Pizza Hawaii"))
#print(my_person.sleep())
#print(my_person.work())
#print(my_person.introduce())


