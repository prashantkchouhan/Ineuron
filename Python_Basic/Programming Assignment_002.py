import logging
logging.basicConfig(filename='Programming_assignment_002.log',level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')
import calendar
import math,cmath


class Python_prog_ass_02:
    logging.info('This is solution of python programming assignment-2')

    def km_to_mile(self):
        """Q 1. Write a Python program to convert kilometers to miles?"""
        print('Q.1 Write a Python program to convert kilometers to miles?')
        logging.info('km_to_mile function is to conevrt kilometer to miles')
        try:
            dist = float(input('Enter the distance in Kilometer : '))
            dist_mile = 0.6214*dist
            print('Distance in Mile is {:.2f}'.format(dist_mile))
            logging.info('Distance in Mile is {}'.format(dist_mile))
            print()
        except Exception as e:
            logging.error(e)

    def celcius_to_Fahrenheit(self):
        """Q2. Write a Python program to convert Celsius to Fahrenheit? """
        logging.info('celcius_to_Fahrenheit function is convert temperature')
        try:
            temp = float(input('Enter the temperature in Celcius : '))
            temp_ferh = (temp*(9/5))+32
            print('Temperature in Fahrenheit is {:.2f}'.format(temp_ferh))
            logging.info('Temperature in Fahrenheit is {:.2f}'.format(temp_ferh))
            print()
        except Exception as e:
            logging.exception(e)

    def calendar(self):
        """Q3. Write a Python program to display calendar?"""
        logging.info('Calendar function is to show calendar')
        try:
            year = int(input('Enter year for calendar : '))
            month = int(input('Enter month for calendar : '))
            print(calendar.month(year,month))
            print()
        except Exception as e:
            logging.exception(e)

    def quad_eq(self):
        """Q4. Write a Python program to solve quadratic equation?"""
        logging.info('quad_eq function is to solve quadratic equation')
        try:
            a = int(input("Enter coefficient of x2 :"))
            b = int(input('Enter coeficient of x :'))
            c = int(input('Enter constant :'))
            D = b ** 2 - 4 * a * c
            if D == 0:
                sol_1 = -b / (2 * a)
                sol_2 = -b / (2 * a)
                print('Real & Equal roots :', sol_1, sol_2)
                logging.info('Real & Equal roots : {}, {}'.format(sol_1, sol_2))
            elif D > 0:
                sol_1 = (-b + math.sqrt(D)) / (2 * a)
                sol_2 = (-b - math.sqrt(D)) / (2 * a)
                print('Real & Two different roots :', sol_1, sol_2)
                logging.info('Real & Two different roots : {}, {}'.format(sol_1, sol_2))
            else:
                sol_1 = (-b + cmath.sqrt(D)) / (2 * a)
                sol_2 = (-b + cmath.sqrt(D)) / (2 * a)
                print('Imaginary roots :', sol_1, sol_2)
                logging.info('Imaginary roots : {}, {}'.format(sol_1, sol_2))
            print()
        except Exception as e:
            logging.exception(e)

    def swap_var(self):
        """Q5. Write a Python program to swap two variables without temp variable?"""
        logging.info('swap_var is to swap the variables')
        try:
            a = int(input('Enter 1st variable'))
            b = int(input('Enter 2nd Variable'))
            logging.info('input variable {},{}'.format(a, b))
            a = a + b
            b = a - b
            a = a - b
            print('swap variable {},{}'.format(a, b))
            logging.info('input variable {},{}'.format(a, b))
        except Exception as e:
            logging.exception(e)


Q_ans = Python_prog_ass_02()
Q_ans.km_to_mile()
Q_ans.celcius_to_Fahrenheit()
Q_ans.calendar()
Q_ans.quad_eq()
Q_ans.swap_var()
