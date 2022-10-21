number_grade = input("Enter your number grade here")

letter_grade = "F"

number_grade = int(number_grade)

if number_grade >= 90:
    letter_grade = "A"
    print(f"Good golly! You sure are smart! You got an {letter_grade}!")

else:
    letter_grade = "Not A"
    print(f"Sorry! Try harder! {letter_grade}")

