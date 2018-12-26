def weight_class(you_max, my_max):
    print(f"My max is {my_max}, yours is {you_max}")
    print("That's pretty comparable!")
   
    

you_max = 225
my_max = 300

weight_class(225 + 300, 300 + 225)


hard_max = 205
red_max =315

weight_class(hard_max, red_max)



print("What's your weight class", end=' ')
input1 = int(input('> '))
print("What's your opponent's weight?", end=' ')
input2 = int(input('> '))


input_con = f"{round(input1 / 2.2046226, 3)} kgs"
input_con2 = f"{round(input2 /2.2046226, 3)} kgs"

weight_class(input_con, input_con2)