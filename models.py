from datetime import datetime, timedelta

import psycopg2


def connect():
    conn = psycopg2.connect(
        host="database-1.ctjpvwq07ek9.us-east-2.rds.amazonaws.com",
        port='5432',
        database="avallon",
        user="postgres",
        password="postgres")
    return conn


def get_books():
    conn = connect()
    books = []
    sql = 'SELECT * FROM Books'
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            item = {
                'id': row[0],
                'title': row[1],
                'author': row[2],
                'available': row[3]
            }
            books.append(item)

    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

    return books


def add_book(book):
    conn = connect()
    cursor = conn.cursor()
    sql = 'Insert into Books(title,author,available) values (%s,%s,%s)'
    try:

        cursor.execute(sql, (book["title"], book["author"], book["available"]))
        conn.commit()
    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def add_user(user):
    conn = connect()
    cursor = conn.cursor()
    sql = "Insert into users(email,password,name,phone,admin) values (%s,%s,%s,%s,%s)"
    try:

        cursor.execute(sql, (user["email"], user["password"], user["name"], user["phone"], user["admin"]))
        conn.commit()
    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# def connection(email, password):
#     conn = connect()
#     cursor = conn.cursor()
#     results = None
#     sql = "Select * from users where email = '" + email + "'"
#
#     try:
#         print(sql)
#         cursor.execute(sql, (email))
#         results = cursor.fetchone()
#
#     except psycopg2.Error as e:
#         print(e)
#     finally:
#
#         cursor.close()
#         conn.close()
#         if password == results[2]:
#             user_id = results[0]
#             email = results[1]
#             name = results[3]
#             phone = results[4]
#             admin = results[5]
#             current_user = User(user_id, email, name, phone, admin)
#             return current_user
#         else:
#             return 'error'


def make_reservation(user_id, book_id):
    borrow_date = datetime.now()
    brought_date = borrow_date + timedelta(14)
    conn = connect()
    cursor = conn.cursor()
    sql_add_resa = 'Insert into reservation(book_id,user_id,borrow_date,brought_date) values (%s,%s,%s,%s)'
    sql_update_book = "Update books set available = 'False' where book_id = '" + str(book_id) + "'"
    try:
        cursor.execute(sql_add_resa, (book_id, user_id, borrow_date, brought_date))
        cursor.execute(sql_update_book)
        conn.commit()
    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def brought_book(book_id):
    conn = connect()
    cursor = conn.cursor()
    sql_drop_reservation = "Delete from reservation where book_id = '" + str(book_id) + "'"
    sql_update_book = "Update books set available = 'True' where book_id = '" + str(book_id) + "'"
    try:
        cursor.execute(sql_drop_reservation)
        cursor.execute(sql_update_book)
        conn.commit()
    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def get_reservation():
    reservation = []
    conn = connect()
    cursor = conn.cursor()
    sql_get_reserv = "SELECT * from reservation JOIN books on reservation.book_id = books.book_id JOIN users on " \
                     "reservation.user_id = users.user_id "
    try:
        cursor.execute(sql_get_reserv)
        results = cursor.fetchall()
        print(results)
        for row in results:
            item = {
                'brought_back': row[4],
                'title': row[6],
                'author': row[7],
                'renter': row[12],
                'phone_number': row[13]
            }
            reservation.append(item)
    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        return reservation


def add_book_in_area(area=0, rack=0, book_id=0):
    conn = connect()
    cursor = conn.cursor()
    sql_add_book_area = "Insert into location(area,rack,book_id) values (%s,%s,%s)"
    try:
        cursor.execute(sql_add_book_area, (area, rack, book_id))
        conn.commit()
    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
def modify_book_area(area=0, rack=0, book_id=0):
    conn = connect()
    cursor = conn.cursor()
    sql_add_book_area = "Update location set area = '"+area+"' , rack = '"+rack+"' where book_id = '" + str(book_id) + "'"
    try:
        cursor.execute(sql_add_book_area, (area, rack, book_id))
        conn.commit()
    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def remove_book_of_storage(book_id):
    conn = connect()
    cursor = conn.cursor()
    sql_remove_book_of_storage = "Delete from location where book_id = '" + str(book_id) + "'"
    try:
        cursor.execute(sql_remove_book_of_storage)
        conn.commit()
    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def get_available_book():
    available_book = []
    conn = connect()
    cursor = conn.cursor()
    sql_get_available_book = "Select * from location JOIN books on location.book_id = books.book_id"
    try:
        cursor.execute(sql_get_available_book)
        results = cursor.fetchall()
        print(results)
        for row in results:
            item = {
            'area': row[0],
            'rack': row[1],
            'title': row[4],
            'author': row[5]
            }
            available_book.append(item)
    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        return available_book

def get_specific_book_by_title(book_title):
    result = None
    conn = connect()
    cursor = conn.cursor()
    sql = "SELECT * from books where books.title = '"+str(book_title)+"'"
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        return result

def get_specific_book_by_author(book_author):
    author_books = []
    result = None
    conn = connect()
    cursor = conn.cursor()
    sql = "SELECT * from books where books.author = '"+str(book_author)+"'"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            item = {
                'title':row[1],
                'author':row[2],
                'available':row[3]
            }
            author_books.append(item)
    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        return author_books

def get_book_area(book_id):
    conn = connect()
    cursor = conn.cursor()
    sql = "SELECT * from location where location.book_id = '"+str(book_id)+"'"
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        item = {
            'area':result[0],
            'rack':result[1]
        }

    except psycopg2.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        return item

#
# class User():
#     def __init__(self, user_id, email, name, phone, admin):
#         self.user_id = user_id
#         self.email = email
#         self.name = name
#         self.phone = phone
#         self.admin = admin
