formatter = "{} {} {} {}"


#using our 'formatter' variable to write different strings

print(formatter.format(1, 2, 3, 4)) #each value input for the space brackets are input
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter)) #will pull in the 'formatter' variable each time it's referenced here

# Below is a different way of formatting the inputs so it's easier to read the code
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
