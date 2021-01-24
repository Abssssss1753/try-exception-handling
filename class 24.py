####################### Try Except Handling ###################
print("enter number 1")
n1=input()
print("enter number 2")
n2=input()
try:
    print("enter the result",
          int(n1)+int(n2))
except Exception as add:
    print(add)

print("this line is very very important")


############################# 2nd example#########################
try:
    print("enter the numerator")
    numerate=int(input())

    print("enter the denominator")
    denominator=int(input())

    result = numerate/denominator
    print(result)
except:
    print("denominator cannot be 0. please try agin")
print("program ends")

