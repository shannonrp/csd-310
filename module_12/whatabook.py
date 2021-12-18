#Shannon Russell-Phipps
#Module 12.3 assignment WhatABook
#12/8/2021
import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu(): #show menu options for users
    print("\nPlease select an option from the below menu: ")
    print("1. View available books" "\n2. View store locations" "\n3. My account" "\n4. Close program")
    try:
        user_choice = int(input("Option: "))
        return user_choice
    except ValueError:
        print("\nInvalid option selected.")
        sys.exit(0)

def show_books(_cursor): #show list of available books
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = _cursor.fetchall()
    print("\nBooks:")
    for book in books:
        print("Book ID: {} \n Title: {} \n  Author: {} \n   Details: {}".format(book[0], book[1], book[2], book[3]))

def show_locations(_cursor): #show store locations
    _cursor.execute("SELECT store_id, locale FROM store")
    stores = _cursor.fetchall()
    print("\nStore locations:")
    for store in stores:
        print("Store ID: {} \n Location: {}".format(store[0], store[1]))

def show_account_menu(): #show user account menu
    try:
        print("\nPlease select an option from the below menu: ")
        print("1. View wishlist" "\n2. Add a new book" "\n3. Main Menu")
        user_account_choice = int(input("Option: "))
        return user_account_choice
    except ValueError:
        print("\nInvalid option selected.")
        sys.exit(0)

def show_wishlist(_cursor, _user_id): #show user's wishlist
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
                    
    wishlist= _cursor.fetchall()
    print("\nBooks on current wishlist:")
    for book in wishlist:
        print("\nTitle: {} \n Author: {}".format(book[4], book[5]))


def show_books_to_add(_cursor, _user_id): #show books not in user's current wishlist
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)
    _cursor.execute(query)
                    
    not_on_wishlist= _cursor.fetchall() #show books not on user's current wishilist
    print("\nBooks not on current wishlist: ")
    for book in not_on_wishlist:
        print("Book ID: {} \n Book name: {}".format(book[0], book[1]))

def validate_user(): #validate user's ID
    try:
        user_id = int(input("Please enter your user ID: "))
        if user_id < 0 or user_id > 3:
            print("\nInvalid user ID.")
            sys.exit(0)
        return user_id
    except ValueError:
        print("\nInvalid user ID")
        sys.exit(0)    

def add_book_to_wishlist(_cursor, _user_id, _book_id): #users can add new books to their wishlist
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES ({}, {})".format(_user_id, _book_id))


try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    print("Welcome to WhatABook!")

    user_option = show_menu()

    while user_option != 4: #while the user does not exit the program

        if user_option == 1: #to show all available books
            show_books(cursor)

        if user_option == 2: #To show store locations
            show_locations(cursor)

        if user_option == 3: #when user selects user menu, must validate the user id first
            users_id = validate_user()
            user_account_option = show_account_menu()

            while user_account_option != 3:

                if user_account_option == 1: #shows current wishlist
                    show_wishlist(cursor, users_id)

                if user_account_option == 2: #if user wants to add a new book to wishlist, show not in wishlist

                    show_books_to_add(cursor, users_id)
 
                    book_id = int(input("\nEnter the book ID of the book you would like to add to your wishlist : "))  #ask for book id
                    
                    add_book_to_wishlist(cursor, users_id, book_id) # add book to wishlist

                    db.commit() # commit the changes to the database 

                    print("\nBook id: {} was added to your wishlist!".format(book_id))
 
                if user_account_option < 0 or user_account_option > 3:  #to check for valid account option
                    print("\nInvalid selection")

                user_account_option = show_account_menu() #return to account menu
        
        if user_option < 0 or user_option > 4: #to check for valid account option
            print("\nInvalid selection")
            
        user_option = show_menu() #return to main menu


    print("\n Thank you for using WhatABook!") #exit program



except mysql.connector.Error as err:
    """ handle errors """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """
    
    db.close()