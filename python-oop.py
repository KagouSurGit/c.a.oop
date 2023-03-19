#python3 script.py
class Student:
  def __init__(self, name, age, house, year, magic):
    self.name = name
    self.age = age
    self.house = house
    self.study_year = year
    self.magic = magic

  def __repr__(self):
    if self.study_year == 1:
      return "This is {name}, a {age} year old {house} student, who has been in this house for {year} year. {magic} is the preferred magic.".format(name=self.name, age=self.age, house=self.house, year=self.study_year, magic=self.magic)
    else:
      return "This is {name}, a {age} year old {house} student, who has been in this house for {year} years. {magic} is the preferred magic.".format(name=self.name, age=self.age, house=self.house, year=self.study_year, magic=self.magic)

  def fight(self, other_house):
    if self.house == other_house.house:
      print("No one will fight, we respect our house.")
    else:
        print("We are from two different houses, may the best house win.")

  def friend(self, other_student):
    if self.magic == other_student.magic:
      print("We have the same type of magic, I think we could be friends.")
    else:
      print("Sorry, We cannot be friends. We don't have the same type of magic")

  def aventure(self, student_year):
    if self.study_year == student_year.study_year:
      print("We are in the same study year. Let's go on an aventure!")
    else:
      print("We are not in the same study year. See you around.")

student_alex = Student("Alex", 28, "Slytherin", 5, "Dark")
student_seb = Student("Sebastian", 25, "Slytherin", 1, "Fire")
student_magnus = Student("Magnus", 30, "Ravenclaw", 8, "Light")

#print(student_alex)
#print(student_seb)
#print(student_magnus)

class Class:
  def __init__(self, name, year, subject, grade):
    self.name = name
    self.year = year
    self.subject = subject
    self.grade = grade
    self.minimum_grade = 100

  def __repr__(self):
    if self.name == "Morning":
      return "This is a {name} class, in  year {year}. The chosen subject is {subject} and to pass, you need a minimum of {grade}.".format(name=self.name, year=self.year, subject=self.subject,grade=self.grade)
    else:
      return "This is an {name} class, in  year {year}. The chosen subject is {subject} and to pass, you need a minimum of {grade}.".format(name=self.name, year=self.year, subject=self.subject,grade=self.grade)

  def teach(self):
    if self.year >= 6 or self.year <= 10:
      print(" The Dark Arts lesson will be taught to you.")
    elif self.year < 6:
      print(" The Broom class can be taught to fly around.")
    elif self.year <= 4 or self.year >= 1:
      print(" You should go to Potion Class first, before going to more advance classes.")
    else:
      print(" You shound not be here at all.")

  def create(self):
    if self.subject == "Dark Arts Class":
      print("Let's see what we can do for you.")
    if self.subject == "Broom Flying Class":
      print("That's a good choice.")
    if self.subject == "Potion Class":
      print("we all have to go through this one.")

  def restart(self):
    if self.grade == self.minimum_grade:
      print("Lucky you!")
    if self.grade <= 99:
      print("You will have to retake the exams.")
    if self.grade >= 101:
      print("You have done a great job.")

class_Dark_Arts = Class("Afternoon", 7, "Dark Arts", 100)
class_Brooms = Class("Morning", 2, "Broom Flying", 105)
class_Potions = Class("Evening", 5, "Potion", 101)

#print(class_Dark_Arts)
#print(class_Brooms)
#print(class_Potions) name, age, house, year, magic

name_1 = input(" Welcome to this unknown wizarding school of magic, what is your name ? ")

age_1 = input("Be welcome " + str(name_1) + ". What is your age ? ")

house_1 = input("Thank you for your honesty. What is your house amongst Slytherin, Gryffindor, Hufflepuff and Ravenclaw ? ")

while house_1 != "Slytherin" and house_1 != "Ravenclaw" and house_1 != "Gryffindor" and house_1 != "Hufflepuff":
  house_1 = input("Please, choose and write carefully your house name. try again.")

year_1 = input("Really interesting ! What year are you in now ? Between 1 to 10")

if (int(year_1) == 0) or (int(year_1) >= 11):
  year_1 = input("You should not be here, what is your real study year ?")

magic_1 = input("Learning will be challeging. We teach four types of magic here. Dark, Light, Fire and Water. What is preferred type of magic ? ")

while magic_1 != "Dark" and magic_1 != "Light" and magic_1 != "Fire" and magic_1 != "Water":
  magic_1 = input("We do not teach that kind of magic here, what is your type of magic amongst the four mentioned ?")

student_1 = Student(name_1, age_1, house_1, year_1, magic_1)
print(student_1)

print("Now, let's see if you have a buddy match in this school.")

name_2 = input("Welcome to you. Tell us your name.")
age_2 = input("Hello " + name_2 + ", how old are you ?")
house_2 = input("Nice ! What is the name of your house ?")

while house_2 != "Slytherin" and house_2 != "Ravenclaw" and house_2 != "Gryffindor" and house_2 != "Hufflepuff":
  house_2 = input("Please, choose and right carefully your house name. try again.")

year_2 = input("Cool, it will be fun. How long have you been with us ?")

if (int(year_2) == 0) or (int(year_2) >= 11):
  year_2 = input("You should not be here, what is your real study year ?")

magic_2 = input("Great ! And now, what type of magic attracts you the most ?")

while magic_2 != "Dark" and magic_2 != "Light" and magic_2 != "Fire" and magic_2 != "Water":
  magic_2 = input("We do not teach that kind of magic here, what is your type of magic amongst the four mentioned ?")

student_2 = Student(name_2, age_2, house_2, year_2, magic_2)
print(student_2)

#while class_1 != "Dark Arts" and class_1 != "Broom Flying" and class_1 != "Potion":
#  class_1 = input("Please, try again, with the exact spelling. ")

#student_class_1 = print("Welcome " + student_1 + ", we will see if " + class_1 + " is the best fit for you. ")

fight_question = input("Do you want to fight ? Yes or No.")
if fight_question == "Yes":
  student_1.fight(student_2)
else:
  print("we are just students !")
#student_1.fight(student_2)
friend_question = input("Do you think we can be friends ? Yes or No")
if friend_question == "Yes":
  student_2.friend(student_1)
else:
  print("We are not here to make friends.")
#student_2.friend(student_1)
aventure_question = input("Let's go on an aventure !? Yes or No")
if aventure_question == "Yes":
  student_1.aventure(student_2)
else:
  print("As you want")

# name, year, subject, grade

time_of_day_class_1 = input("It was really nice to see the little interaction between you. Now, let's choose when you want to be taught. In the Morning; Afternoon or the Evening ?")

while time_of_day_class_1 != "Morning" and time_of_day_class_1 != "Afternoon" and time_of_day_class_1 != "Evening":
  time_of_day_class_1 = input("There are three types of time available for the classes. Try again with the right spelling.")

year_class_1 = input("Since you have told us that your year is "  + year_1 + ". Could you confirm your study year by entering your year again ? Please.")

subject_class_1 = input("Between those three subjects: \"Dark Arts Class\", \"Broom Flying Class\" and \"Potion Class\", which one would you like to start with ?")

while subject_class_1 != "Dark Arts Class" and subject_class_1 != "Broom Flying Class" and subject_class_1 != "Potion Class":
  subject_class_1 = input("We do not teach that, please insert the right class name.")

grade_1 = input("What do you think your grade should be for that class ? less than 99 ? more than 100 ? or 100")

class_1 = Class(time_of_day_class_1, year_class_1, subject_class_1, grade_1)
print(class_1)