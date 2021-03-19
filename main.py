from counter import MySolution

# Input parameters for this case:
smallBox = 3
mediumBox = 6
largeBox = 9
collectBox = 3

# Create object
collector = MySolution(smallBox, mediumBox, largeBox, collectBox)

while True:
    while True:
        try:
            orderPieces = int(input('How many pieces do you want collect ? >>>>'))
            break
        except ValueError:
            print("Oops! That was no valid number. Try again..")
    if orderPieces == 0:
        print("Oh no, you want 0 pieces ?! That's impossible")
    else:
        if 0 < orderPieces <= 100:
            print(collector.count(orderPieces))
        else:
            print("You can collect pieces between 1 and 100. No more, no less!")
    if input('Do you want continue ? [y/n]') != 'y':
        break
