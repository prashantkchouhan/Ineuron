import logging
logging.basicConfig(filename='Programming_assignment_002.log',level=logging.DEBUG,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')

class Python_prog_ass_03:
    logging.info('This is a solution of python programming assignment 3')

    def num_check(self):
        """Q1. Write a Python Program to Check if a Number is Positive, Negative or Zero?"""
        try:
            logging.info('num_check function is to check if a number is positive,negative or zero')
            number = int(input('Enter a number : '))
            logging.info('Entered number is {}'.format(number))
            if number == 0:
                print('{} is zero'.format(number))
                logging.info('{} is zero'.format(number))
            elif number > 0:
                print('{} is positive'.format(number))
                logging.info('{} is positive'.format(number))
            else:
                print('{} is negative'.format(number))
                logging.info('{} is negative'.format(number))
            print()
        except Exception as e:
            logging.exception(e)

    def even_odd(self):
        """Q2. Write a Python Program to Check if a Number is Odd or Even?"""
        logging.info('This function is to check if a number is odd and even')
        try:
            num = int(input('Enter a number : '))
            logging.info('Entered number : {}'.format(num))
            if num % 2 == 0:
                print('{} is even number'.format(num))
                logging.info('{} is even number'.format(num))
            else:
                print('{} is odd number'.format(num))
                logging.info('{} is odd number'.format(num))
        except Exception as e:
            logging.exception(e)

    def leap_year(self):
        """Q3. Write a Python Program to Check Leap Year?"""
        logging.info('This function is to check if a year is leap year')
        try:
            year = int(input('Enter year : '))
            logging.info('Entered year is {}'.format(year))
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print('{} is a leap year'.format(year))
                        logging.info('{} is a leap year'.format(year))
                    else:
                        print('{} is not a leap year'.format(year))
                        logging.info('{} is not a leap year'.format(year))
                else:
                    print('{} is a leap year'.format(year))
                    logging.info('{} is a leap year'.format(year))
            else:
                print('{} is not a leap year'.format(year))
                logging.info('{} is not a leap year'.format(year))
            print()
        except Exception as e:
                logging.exception(e)

    def primenum_check(self):
        """Q4. Write a Python Program to Check Prime Number?"""
        logging.info('primenum_check function is to check if number is prime')
        try:
            number = int(input('Enter a number : '))
            logging.info('Entered number is {}'.format(number))
            for i in range(2, (number // 2) + 1):
                if number % i == 0:
                    print('{} is not a prime number'.format(number))
                    logging.info('{} is not a prime number'.format(number))
                    break
            else:
                print('{} is a prime number'.format(number))
                logging.info('{} is a prime number'.format(number))
            print()
        except Exception as e:
            logging.exception(e)

    def p_num_range(self):
        """Q5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?"""
        logging.info('p_num_range is to print prime number between 1-10000')
        try:
            end_num = 10000
            for i in range(2, end_num + 1):
                for j in range(2, (i // 2) + 1):
                    if i % j == 0:
                        break
                else:
                    print(i, end=" ")
                    logging.info(i)
            print()
        except Exception as e:
            logging.info(e)


Q_ans = Python_prog_ass_03()
#Q_ans.num_check()
#Q_ans.even_odd()
Q_ans.leap_year()
Q_ans.primenum_check()
Q_ans.p_num_range()




