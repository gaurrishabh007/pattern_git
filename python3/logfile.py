import logging
logging.basicConfig(filename='mylog.txt', level=logging.INFO)
logging.info("A New request Came: ")
try:
    x=int(input("enter first number: "))
    y=int(input("enter second number: "))
    print(x/y)

except ZeroDivisionError as msg:
    print("cannot divide with zero")

except ValueError as msg:
    print("enter only int values")
    logging.exception(msg)
logging.info("request processing completed")

