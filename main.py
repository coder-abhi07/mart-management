import mysql.connector as mc
import getpass
from tabulate import tabulate
import time


password = getpass.getpass("enter your password: ")
def connection():
    mydb = mc.connect(host = "localhost",
                      user = "root",
                      passwd = password,
                      database = "mart")
    if mydb.is_connected():
        return mydb
    return False

def create():
    mydb = mc.connect(host = "localhost",
                      user = "root",
                      passwd = password)
    
    mycursor = mydb.cursor()
    
    query = "create database if not exists mart"
    mycursor.execute(query)

    query = "use mart"
    mycursor.execute(query)

    query = "CREATE TABLE if not exists clothes (id varchar(10) DEFAULT NULL,name varchar(10) DEFAULT NULL,`type` varchar(10) DEFAULT NULL,`gender` char(1) DEFAULT NULL,`season` varchar(10) DEFAULT NULL,`price` int DEFAULT NULL)"
    mycursor.execute(query)
    query = "CREATE TABLE if not exists edibles (id varchar(5) DEFAULT NULL,name varchar(10) DEFAULT NULL,type varchar(10) DEFAULT NULL,price int DEFAULT NULL)"
    mycursor.execute(query)
    query = "CREATE TABLE if not exists `fruit` (`id` varchar(10) DEFAULT NULL,`name` varchar(10) DEFAULT NULL,`price` int DEFAULT NULL)"
    mycursor.execute(query)
    query = "CREATE TABLE if not exists `grocery` (`id` varchar(10) DEFAULT NULL,`name` varchar(10) DEFAULT NULL,`price` int DEFAULT NULL)"
    mycursor.execute(query)
    query = "CREATE TABLE if not exists `movie` (`id` varchar(5) DEFAULT NULL,`name` varchar(10) DEFAULT NULL,`price` int DEFAULT NULL,`hour` int DEFAULT NULL)"
    mycursor.execute(query)
    query = "CREATE TABLE if not exists `play_station` (`sno` int DEFAULT NULL,`name` varchar(10) DEFAULT NULL,`price_per_hour` int DEFAULT NULL)"
    mycursor.execute(query)
    query = "CREATE TABLE if not exists `ride` (`sno` int DEFAULT NULL,`name` varchar(10) DEFAULT NULL,`price` int DEFAULT NULL)"
    mycursor.execute(query)
    query = "CREATE TABLE if not exists `stock` (`id` varchar(5) DEFAULT NULL,`name` varchar(10) DEFAULT NULL,`price` int DEFAULT NULL,`qty` int DEFAULT NULL)"
    mycursor.execute(query)
    query = "CREATE TABLE if not exists `vegetables` (`id` varchar(10) DEFAULT NULL,`name` varchar(10) DEFAULT NULL,`price` int DEFAULT NULL)"
    mycursor.execute(query)
    query = "CREATE TABLE if not exists `workers` (`id` varchar(5) DEFAULT NULL,`name` varchar(10) DEFAULT NULL,`salary` int DEFAULT NULL,`phone` varchar(11) DEFAULT NULL,`address` varchar(10) DEFAULT NULL,`DOB` date DEFAULT NULL)"  
    mycursor.execute(query)
    

    

    
def generate(fn):
    functions = {'clothes': clothes, 'fruit': fruit, 'vegetable': vegetable, 'grocery': grocery, 'play_station': play_station, 'ride': ride, 'movie': movie, 'eat': eat, 'stock': stock, 'management': management}
    more = input("REDO (Y/N): ")
    if more.upper() == "Y":
        how_many = int(input("Frequency: "))
        for i in range(how_many):
           functions[fn]()
        main_menu = input("press Y to go back to main menu or any key to exit: ")
        if main_menu.upper() == "Y":
            return True
        else:
            return exit()

    elif more.upper() == "N":
        main_menu = input("press Y to go back to main menu or any key to exit: ")
        if main_menu.upper() == "Y":
            return True
        else:
            return exit()
    else:
        print("incorrect key")
        return exit()
    
def execute(query, printData = 0):
    mydb = connection()
    mycursor = mydb.cursor()

    mycursor.execute(query)
    
    rowCnt = mycursor.rowcount
    headers = mycursor.column_names
    
    data = mycursor.fetchall()
    if (len(data) > 0):
        print(tabulate(data, headers, tablefmt="psql"))
        rowCnt = 1
        
    if (rowCnt > 0 and printData):
        done()

    elif (rowCnt > 0):
        success()

    else:
        failure()

    mydb.commit()
    mycursor.close()
    mydb.close()

def grocery():
    print("1. ADD ")
    print("2. VIEW ")
    print("3. REMOVE ")
    print()
    user = int(input("enter your choice: "))
    if user == 1:
        id = input("enter id : ")
        name = input("enter name : ")
        price = int(input("enter price: "))
        query = "insert into grocery values('{}','{}', {})".format(id, name, price)
        execute(query)

    elif user == 2:
        query = "select * from grocery"
        execute(query, 1)

    elif user == 3:
        id = input("enter item id: ")
        query = "delete from grocery where id = '{}'".format(id)
        execute(query)

def vegetable():
    print("1. ADD ")
    print("2. VIEW ")
    print("3. REMOVE ")
    print()
    user = int(input("enter your choice: "))
    if user == 1:
        id = input("enter id : ")
        name = input("enter name : ")
        price = int(input("enter price: "))
        query = "insert into vegetables values('{}','{}', {})".format(id, name, price)
        execute(query)

    elif user == 2:
        query = "select * from vegetables"
        execute(query, 1)

    elif user == 3:
        id = input("enter item id: ")
        query = "delete from vegetables where id = '{}'".format(id)
        execute(query)


def fruit():
    print("1. ADD ")
    print("2. VIEW ")
    print("3. REMOVE ")
    print()
    user = int(input("enter your choice: "))
    if user == 1:
        id = input("enter id : ")
        name = input("enter name : ")
        price = int(input("enter price: "))
        query = "insert into fruit values('{}','{}', {})".format(id, name, price)
        execute(query)

    elif user == 2:
        query = "select * from fruit"
        execute(query, 1)

    elif user == 3:
        id = input("enter item id: ")
        query = "delete from fruit where id = '{}'".format(id)
        execute(query)

def clothes():
    print("1. ADD ")
    print("2. VIEW ")
    print("3. REMOVE ")
    print()
    user = int(input("enter your choice: "))
    if user == 1:
        id = input("enter id : ")
        name = input("enter name : ")
        type = input("enter name : ")
        gender = input("enter name : ")
        season = input("enter name : ")
        price = int(input("enter price: "))
        query = "insert into clothes values('{}','{}', '{}','{}', '{}', {})".format(id, name, type, gender, season, price)
        execute(query)

    elif user == 2:
        query = "select * from clothes"
        execute(query, 1)

    elif user == 3:
        id = input("enter item id: ")
        query = "delete from clothes where id = '{}'".format(id)
        execute(query)


def play_station():
    print("1. ADD ")
    print("2. VIEW ")
    print("3. REMOVE ")
    print()
    user = int(input("enter your choice: "))
    if user == 1:
        sno = int(input("enter serial no (int value): "))
        name = input("enter name : ")
        price = int(input("enter price per hour: "))
        query = "insert into movie values({},'{}',{})".format(sno, name, price)
        execute(query)

    elif user == 2:
        query = "select * from play_station"
        execute(query, 1)

    elif user == 3:
        sno = input("enter serial number: ")
        query = "delete from play_station where id = {}".format(id)
        execute(query)


def ride():
    print("1. ADD RIDE")
    print("2. VIEW RIDE")
    print("3. REMOVE RIDE")
    print()
    user = int(input("enter your choice: "))
    if user == 1:
        sno = int(input("enter serial no (int value): "))
        name = input("enter name : ")
        price = int(input("enter price: "))
        query = "insert into movie values({},'{}',{})".format(sno, name, price)
        execute(query)

    elif user == 2:
        query = "select * from ride"
        execute(query, 1)


    elif user == 3:
        sno = input("enter serial number: ")
        query = "delete from ride where id = {}".format(id)
        execute(query)

def movie():
    print("1. ADD MOVIE")
    print("2. VIEW MOVIE")
    print("3. REMOVE MOVIE")
    print()
    user = int(input("enter your choice: "))
    if user == 1:
        id = input("enter movie id : ")
        name = input("enter name : ")
        price = int(input("enter price: "))
        hour = int(input("enter (movie length) hours: "))
        query = "insert into movie values('{}','{}',{},{})".format(id, name, price, hour)
        execute(query)

    elif user == 2:
        query = "select * from movie"
        execute(query, 1)

    elif user == 3:
        id = input("enter item id: ")
        query = "delete from movie where id = '{}'".format(id)
        execute(query)

def eat():
    print("1. ADD ITEM")
    print("2. VIEW ITEM")
    print("3. REMOVE ITEM")
    print()
    user = int(input("enter your choice: "))
    if user == 1:
        id = input("enter item id : ")
        name = input("enter name : ")
        type = input("enter type (drink, snack, ....)")
        price = int(input("enter price: "))

        query = "insert into edibles values('{}','{}','{}',{})".format(id, name, type, price)
        execute(query)

    elif user == 2:
        query = "select * from edibles"
        execute(query, 1)

    elif user == 3:
        id = input("enter item id: ")
        query = "delete from edibles where id = '{}'".format(id)
        execute(query)


def stock():

    print("1. ADD STOCK")
    print("2. VIEW STOCK")
    print("3. REMOVE STOCK")
    print()
    user = int(input("enter your choice: "))
    if user == 1:
        id = input("enter stock id : ")
        name = input("enter name : ")
        price = int(input("enter price: "))
        qty = input("enter quantity: ")

        query = "insert into stock values('{}','{}',{},{})".format(id, name, price, qty)
        execute(query)

    elif user == 2:
        query = "select * from stock"
        execute(query, 1)

    elif user == 3:
        id = input("enter stock id: ")
        query = "delete from stock where id = '{}'".format(id)
        execute(query)
    
def worker():

    print("1. ADD WORKER")
    print("2. VIEW WORKER")
    print("3. REMOVE WORKER")
    print()
    user = int(input("enter your choice: "))
    if user == 1:
        id = input("enter worker id : ")
        name = input("enter name : ")
        salary = int(input("enter salary: "))
        phone = input("enter phone: ")
        address = input("enter address: ")
        dob = input("enter date of birth yyy-mm-dd: ")

        query = "insert into workers values('{}','{}',{},'{}','{}','{}')".format(id, name, salary, phone, address, dob)
        execute(query)

    elif user == 2:
        query = "select * from workers"
        execute(query, 1)

    elif user == 3:
        id = input("enter worker id: ")
        query = "delete from workers where id = '{}'".format(id)
        execute(query)

def management():
    print("1. CLOTHES")
    print("2. FRUIT")
    print("3. VEGETABLES")
    print("4. GROCERY")
    print("5. PLAY STATION")
    print("6. RIDE")
    print("7. MOVIE")
    print("8. DRINK AND EAT")
    print("9. STOCK")
    print()

    user = int(input("enter your choice: "))
    if user == 1:
        clothes()
        generate('clothes')
    elif user == 2:
        fruit()
        generate('fruit')
    elif user == 3:
        vegetable()
        generate('vegetable')
    elif user == 4:
        grocery()
        generate('grocery')
    elif user == 5:
        play_station()
        generate('play_station')
    elif user == 6:
        ride()
        generate('ride')
    elif user == 7:
        movie()
        generate('movie')
    elif user == 8:
        eat()
        generate('eat')
    elif user == 9:
        stock()
        generate('stock')

def buy_clothes():
    mydb = connection()
    mycursor = mydb.cursor()

    total = 0
    query = "select * from clothes"
    execute(query, 1)

    id = input("enter item id : ")
    query = "select price from clothes where id = '{}'".format(id)
    mycursor.execute(query)
    data = mycursor.fetchall()
    total += data[0][0]

    return total


def buy_fruit():
    mydb = connection()
    mycursor = mydb.cursor()

    total = 0
    query = "select * from fruit"
    execute(query, 1)

    id = input("enter item id : ")
    query = "select price from fruit where id = '{}'".format(id)
    mycursor.execute(query)
    data = mycursor.fetchall()
    total += data[0][0]

    return total

def buy_vegetable():
    mydb = connection()
    mycursor = mydb.cursor()

    total = 0
    query = "select * from vegetables"
    execute(query, 1)

    id = input("enter item id : ")
    query = "select price from vegetables where id = '{}'".format(id)
    mycursor.execute(query)
    data = mycursor.fetchall()
    total += data[0][0]

    return total

def buy_grocery():
    mydb = connection()
    mycursor = mydb.cursor()

    total = 0
    query = "select * from grocery"
    execute(query, 1)

    id = input("enter item id : ")
    query = "select price from grocery where id = '{}'".format(id)
    mycursor.execute(query)
    data = mycursor.fetchall()
    total += data[0][0]

    return total

def buy_play():
    mydb = connection()
    mycursor = mydb.cursor()

    total = 0
    query = "select * from play_station"
    execute(query, 1)

    id = int(input("enter item sno : "))
    query = "select  price_per_hour from play_station where sno = {}".format(id)
    mycursor.execute(query)
    data = mycursor.fetchall()
    total += data[0][0]

    return total

def buy_ride():
    mydb = connection()
    mycursor = mydb.cursor()

    total = 0
    query = "select * from ride"
    execute(query, 1)

    id = int(input("enter item sno : "))
    query = "select  price from ride where sno = {}".format(id)
    mycursor.execute(query)
    data = mycursor.fetchall()
    total += data[0][0]

    return total

def buy_movie():
    mydb = connection()
    mycursor = mydb.cursor()

    total = 0
    query = "select * from movie"
    execute(query, 1)

    id = input("enter movie id : ")
    query = "select price from movie where id = '{}'".format(id)
    mycursor.execute(query)
    data = mycursor.fetchall()
    total += data[0][0]

    return total

def buy_food():
    mydb = connection()
    mycursor = mydb.cursor()

    total = 0
    query = "select * from edibles"
    execute(query, 1)

    id = input("enter item id : ")
    query = "select  price from edibles where id = '{}'".format(id)
    mycursor.execute(query)
    data = mycursor.fetchall()
    total += data[0][0]

    return total

def success():
    print("""
    +-++-++-++-++-++-++-+
    |S||U||C||C||E||S||S|
    +-++-++-++-++-++-++-+
    """)


def failure():
    print("""
    +-++-++-++-++-++-++-+
    |F||A||I||L||U||R||E|
    +-++-++-++-++-++-++-+

    NO DATA FOUND 
    """)


def done():
    print("""
    +-++-++-++-+
    |D||O||N||E|
    +-++-++-++-+
    """)

running = False

try:
    if (connection()):
        create()
        running = True
except Exception as e:
    print(e, "check your password again !!")

while running:
    try:
        print("==========================================================================================")
        print("                              :::::::::::::::::")
        print('''
             __      __ ___  _      ___   ___   __  __  ___ 
             \ \    / /| __|| |    / __| / _ \ |  \/  || __|
              \ \/\/ / | _| | |__ | (__ | (_) || |\/| || _| 
               \_/\_/  |___||____| \___| \___/ |_|  |_||___| ''')

        print()
        print("                    ---------------------------------------")
        print("                       WHAT WOULD YOU LIKE TO DO TODAY  ^_^ ")
        print("                    ---------------------------------------")
        print()
        print("                              :::::::::::::::::")
        print("==========================================================================================")
        print()
        print("1. BUY")
        print("2. PLAY, FUN AND RIDE")
        print("3. WATCH MOVIE")
        print("4. DRINK AND EAT")
        print("5. STOCK")
        print("6. INTERNAL MANAGEMENT")
        print("7. ABOUT")
        print("8. EXIT")
        print()

        user = int(input("enter your choice: "))
        if user == 1:
            print("1. CLOTHES")
            print("2. FRUIT")
            print("3. VEGETABLES")
            print("4. GROCERY")
            print("5. BACK TO MAIN MENU")
            print("6. EXIT")
            print()

            user = int(input("enter your choice: "))
            if user == 1:
                user = int(input("enter N (no of items you wanna buy ) :"))
                total = 0
                for i in range(user):
                    total += buy_clothes()
                print("total amt: ", total)
                time.sleep(1)

            elif user == 2:
                user = int(input("enter N (no of items you wanna buy ) :"))
                total = 0
                for i in range(user):
                    total += buy_fruit()
                print("total amt: ", total)
                time.sleep(1)

            elif user == 3:
                user = int(input("enter N (no of items you wanna buy ) :"))
                total = 0
                for i in range(user):
                    total += buy_vegetable()
                print("total amt: ", total)
                time.sleep(1)

            elif user == 4:
                user = int(input("enter N (no of items you wanna buy ) :"))
                total = 0
                for i in range(user):
                    total += buy_grocery()
                print("total amt: ", total)
                time.sleep(1)

            elif user == 5:
                continue

            elif user == 6:
                break

            else:
                print("incorrect key")
                break

        elif user == 2:
            print("1. PLAY STATION")
            print("2. RIDE")
            print("3. BACK TO MAIN MENU")
            print("4. EXIT")
            print()

            user = int(input("enter your choice: "))
            if user == 1:
                user = int(input("enter N (no of items you wanna buy ) :"))
                total = 0
                for i in range(user):
                    total += buy_play()
                print("total amt: ", total)
                time.sleep(1)

            elif user == 2:
                user = int(input("enter N (no of items you wanna buy ) :"))
                total = 0
                for i in range(user):
                    total += buy_ride()
                print("total amt: ", total)
                time.sleep(1)

            elif user == 3:
                continue

            elif user == 4:
                break


            else:
                print("incorrect key")
                break

        elif user == 3:
            user = int(input("enter N (no of items you wanna buy ) :"))
            total = 0
            for i in range(user):
                total += buy_movie()
            print("total amt: ", total)
            time.sleep(1)


        elif user == 4:
            user = int(input("enter N (no of items you wanna buy ) :"))
            total = 0
            for i in range(user):
                total += buy_food()
            print("total amt: ", total)
            time.sleep(1)
                    
        elif user == 5:
            user = input("enter password: ")
            if (user == "password"):
                stock()
            else:
                print("wrong password")
                

        elif user == 6:
            user = input("enter password: ")
            if (user == "password"):
                management()
            else:
                print("wrong passsword")

        elif user == 7:
            print("This project is made by ANKITA CHOUDHARY , Samridhi Chadha and Rakhi Roswami")
            break
        
        elif user == 8:
            break

        else:
            print("wrong input")
            break

        time.sleep(1)

    except Exception as e:
        print('\n', e)

