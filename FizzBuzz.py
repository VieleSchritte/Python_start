# FizzBuzz is a typical task for checking elementary language skills: the script should print numbers in range from 1 to 100, but
# if the number is divisible by 3 => print 'Fizz'
# if the number is divisible by 5 => print 'Buzz'
# if the number is divisible by 3 and by 5 => print 'FizzBuzz'

i = 1
for i in range(1, 101):
    if (i % 3 == 0)and(i % 5 != 0):
        print('Fizz')
    elif(i % 3 != 0)and(i % 5 == 0):
        print('Buzz')
    elif(i % 3 == 0)and(i % 5 == 0):
        print('FizzBuzz')
    else:
        print(i)
       