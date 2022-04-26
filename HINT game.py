import random
top = input('Type a number: ')

if top.isdigit():
    top = int(top)

    if top <= 0:
        print('please type a number ')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top)
print(random_number)