name, age = input("Please enter your goodname and age seperated by commas : ").split(",")
age = int(age)
if (name.strip().lower()[0]) == "a" and age >= 11:
    print("You can watch this movie....")
else:
    print("Sorry, you cant watch this movie....")
