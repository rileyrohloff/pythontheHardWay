people = 30
cars = 10
trucks = 15

#If statments that are comparing the above variables with boolean code. In this case: '<, >'

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's to many trucks.")
elif trucks < cars: 
    print("Maybe we should take the trucks.")
else: 
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else: 
    print("Fine, let's stay home then.")