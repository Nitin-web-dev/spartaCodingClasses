# Create a function that prints out a person’s gender (male or female) based on their “registration number”.


def check_gender(pin):
    num = int(pin.split('-')[1][0])
    if num % 2 == 0:
        print('female')
    else:
        print('male')


    

my_pin = '200101-4012345'
check_gender(my_pin)

# 'a#b'.split('#') ---> ['a', 'b']