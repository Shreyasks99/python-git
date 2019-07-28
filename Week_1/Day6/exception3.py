def cast_vote(age):
    assert age >=18,f"Age shouldn't be less than 18,it was {age}"
    print("Thank youfor voting")
try:
    age = int(input("Enter the age:"))
    cast_vote(age)
except AssertionError as a:
    print(a)
else:
    print(f"You entered the valid age:{age}")
finally:
    print("END")