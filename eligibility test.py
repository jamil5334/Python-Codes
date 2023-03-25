#eligibility test
nationality=input("Enter nationality: ").lower()
age=int(input("Enter age: "))
if age>=18 and nationality=="kenyan":
    print("Eligible to vote")
else:
    print("NOT eligible to vote")