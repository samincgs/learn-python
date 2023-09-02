mood = "hungry"

match mood:
    case "hungry":
        print("I AM HUNGRY")
    case "hangry":
        print("I AM HANGRY")
    case "happy":
        print("I AM HAPPY")

# exercise
# create a variable with an itneger between 1-5, call it grade
# create a match when it is 1 'very good'
# very bad when it is 5

grade = 3

match grade:
    case 1:
        print("very good")
    case 2:
        print("good")
    case 3:
        print("okay")
    case 4:
        print("needs improvements")
    case 5:
        print("very bad")
    case _:
        print("not a valid num")
