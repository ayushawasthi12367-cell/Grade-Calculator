# Grades calculator

print("************Welcome to the grades calculator program*******************")

grade = float(input("Enter your grade: "))

if 80 <= grade <= 100:
    print("You have A grade")
    print("Hard work always pays off.")

elif 60 <= grade < 80:
    print("You have B grade")
    print("You have more potential to improve your grade.")

elif 50 <= grade < 60:
    print("You have C grade")
    print("You have to work hard to improve your grade.")

elif 40 <= grade < 50:
    print("You are fail")
    print("Have to repeat the exam.")
    print("You have to fall to rise again.")

elif 0 <= grade < 40:
    print("You are fail")
    print("Have to repeat the course.")
    print("You have to fall to rise again.")

else:
    print("Invalid input! Please enter a grade between 0 and 100.")

print("************Thank you for using the grades calculator program*******************")