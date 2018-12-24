
def checkStatement(number):
    assert number > 10 , "The number is less than 10 can't be taken"
    print("Yep, Number is greater than 10 :-)")


numb = int(input("Enter Number : "))

try:
    checkStatement(numb)
except AssertionError as e:
        print(e)
