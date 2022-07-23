import logging
logging.basicConfig(filename='Programming_assignment_001.log',level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')
from random import randint

class Python_prog_ass_01:
    logging.info('This is solution of python programming assignment 1')

    def welcome(self):
        """ Q1. Write a Python program to print Hello Python"""
        print('Q1. Write a Python program to print Hello Python')
        logging.info('Welcome function is to print Hello Python')
        try:
            print('Hello Python')
            print()
        except Exception as e:
            logging.exception(e)

    def arith_operation(self):
        """ Q2. Write a Python program to do arithmetical operations addition and division.?"""
        print('Q2. Write a Python program to do arithmetical operations addition and division')
        logging.info('arith_operation function is to perform addition and division operation')
        try:
            a = int(input('Enter 1st number : '))
            b = int(input('Enter 2nd number : '))
            logging.info('Number entered by user are {} and {}'.format(a,b))
            c = a + b
            d = a / b
            print('{} + {} = {}'.format(a,b,c))
            print('{} / {} = {:.2f}'.format(a, b, d))
            logging.info('Addition Result: {} + {} = {}'.format(a,b,c))
            logging.info('Division Result : {} + {} = {}'.format(a, b, d))
            print()
        except Exception as e:
            print('Please enter correct number')
            logging.error(e)

    def tri_area(self):
        """ Q3. Write a Python program to find the area of a triangle?"""
        print('Q3. Write a Python program to find the area of a triangle?')
        logging.info('tri_area is to calculate area of triangle using legth of sides')
        try:
            s1 = int(input('Enter the length of 1st Side :'))
            s2 = int(input('Enter the length of 2nd Side :'))
            s3 = int(input('Enter the length of 3rd Side :'))
            logging.info('Entered length of sides are {},{},{}'.format(s1,s2,s3))
            if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
                s = (s1+s2+s3)/2
                area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
                print('Area of triangle is {:.2f}'.format(area))
                logging.info('Area of triangle is {:.2f}'.format(area))
                print()
            else:
                print('Triangle is not possible, sum of two side is less than third side')
                logging.error('Triangle is not possible, sum of two side is less than other side')
                print()
        except Exception as e:
            print('Enter correct length of sides and sum of two side should be greater than third side')
            logging.exception(e)

    def swap(self):
        """ Q.4 Write a Python program to swap two variables?"""
        print('Q.4 Write a Python program to swap two variables?')
        logging.info('This program is to swap variable')
        try:
            var1 = input('Enter 1st Variable : ')
            var2 = input('Enter 2nd Variable : ')
            logging.info('Entered variable are : {} , {}'.format(var1,var2))
            var3 = var2
            var2 = var1
            var1 = var3
            print('Swap output : {} and {}'.format(var1,var2))
            logging.info('Swap output : {} and {}'.format(var1,var2))
            print()
        except Exception as e:
            logging.error(e)

    def generateRandomNumber(self):
        """ Q.5 Write a Python program to generate a random number?"""
        print('Q.5 Write a Python program to generate a random number?')
        logging.info('This program is to generate random number')
        try:
            start = int(input('Enter lowest value of range : '))
            end = int(input('Enter highest value of range : '))
            logging.info('Random number will get generated between {} and {}'.format(start,end))
            random_num = randint(start, end)
            print('Random number :', random_num)
            logging.info('Random number is {}'.format(random_num))
        except Exception as e:
            logging.error(e)
            print(e)


Q_ans = Python_prog_ass_01()
Q_ans.welcome()
Q_ans.arith_operation()
Q_ans.tri_area()
Q_ans.swap()
Q_ans.generateRandomNumber()
