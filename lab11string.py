words=["dogs", "cats", "birds", "fish", "rabbits", "hamsters", "pigs", "mice", "rats", "turtles", "snakes"]

num=int(input("Enter the number of letters you want to input to display the words under the same number of letters: "))
for i in words:
    if len(i)>=num:
        print(i)