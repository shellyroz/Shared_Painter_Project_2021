# Name: Shelly Rozman
# Python Version: 3.7.2
# Date: 14/3/2021

import sqlite3
import tkinter as tk
import tkinter.messagebox


class SignedUpUsers:
    """Creates database with users table includes:
       create query
       insert query
       select query
    """

    def __init__(self, tablename="new_clients_sign_ups", email="email", username="username", password="password"):
        self.__tablename = tablename
        self.__email = email
        self.__username = username
        self.__password = password
        self.users_list = []

        conn = sqlite3.connect('project_users_database.db')
        print("Opened database successfully")
        query_str = "CREATE TABLE IF NOT EXISTS " + tablename + "(" + self.__email + " " + \
                    " TEXT    NOT NULL ,"
        query_str += " " + self.__username + " TEXT PRIMARY KEY  NOT NULL ,"
        query_str += " " + self.__password + " TEXT    NOT NULL );"

        # conn.execute("drop table users")
        conn.execute(query_str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def __str__(self):
        return "table  name is ", self.__tablename

    def get_table_name(self):
        '''
        The function returns the table's title.
        :return: The table's title.
        :rtype: string.
        '''
        return self.__tablename

    def insert_user(self, email, username, password):
        '''
        The function inserts given information into the database.
        :param email: A given email address.
        :param username: A given username.
        :param password: A given password.
        '''
        conn = sqlite3.connect('project_users_database.db')
        insert_query = "INSERT INTO " + self.__tablename + " (" + self.__email + "," + self.__username + "," + self.__password + ") VALUES " \
                                                                                                            "(" + "'" + email + "'" + "," + "'" + username + "'" + "," + "'" + password + "'" + ");"
        print(insert_query)
        conn.execute(insert_query)

        conn.commit()
        conn.close()
        print("Record created successfully")

    def print_users(self):
        '''
        The function prints the information of all the users in the database.
        '''
        conn = sqlite3.connect('project_users_database.db')
        print("Opened database successfully")
        str1 = "select * from new_clients_sign_ups;"

        """strsql = "SELECT username, password  from " +  self.__tablename + " where " + self.__userId + "=" \
            + str(username)
        """
        print(str1)
        cursor = conn.execute(str1)
        for row in cursor:
            print("email = ", row[0])  # email
            print("username = ", row[1])  # username
            print("password = ", row[2])  # password

        print("Operation done successfully")
        conn.close()

    def create_users_list(self):
        '''
        The function creates a list of all the users' in the database information.
        '''
        conn = sqlite3.connect('project_users_database.db')
        print("Opened database successfully")
        str1 = "select * from new_clients_sign_ups;"

        cursor = conn.execute(str1)

        for row in cursor:
            email = row[0]
            username = row[1]
            password = row[2]

            this_user = [email, username, password]

            if this_user not in self.users_list:
                self.users_list.append(this_user)

        print("Operation done successfully")
        conn.close()

    def is_user_in_database(self, given_username, given_password):
        '''
        The function checks whether a user is in the database or not.
        :param given_username: The user's entered username.
        :param given_password: The user's entered password.
        :return: "U_ERROR" if the entered username does not match the existing password,
        "P_ERROR" if the entered password does not match the existing username, or "ERROR"
        if a different error has occurred/
        :rtype: string.
        '''
        for lst in self.users_list:
            if lst[1] == given_username and lst[2] == given_password:
                return lst[0]

            elif lst[1] != given_username and lst[2] == given_password:
                tk.Tk().withdraw()
                tk.messagebox.showerror(title="ERROR",
                                        message="The username you entered is incorrect. Please try again.")
                return "U_ERROR"

            elif lst[1] == given_username and lst[2] != given_password:
                tk.Tk().withdraw()
                tk.messagebox.showerror(title="ERROR",
                                        message="The password you entered is incorrect. Please try again.")
                return "P_ERROR"

    def is_username_in_database(self, entered_username):
        '''
        The function checks whether a username is in the database or not.
        :param entered_username: An entered username.
        :return: True if the username is in the database, and False otherwise.
        :rtype: bool.
        '''
        for lst in self.users_list:
            if entered_username == lst[1]:
                return True

        return False

    def email_by_username(self, entered_username):
        '''
        The function checks whether a username is in the database or not.
        :param entered_username: An entered username.
        :return: True if the username is in the database, and False otherwise.
        :rtype: bool.
        '''
        for lst in self.users_list:
            if entered_username == lst[1]:
                return lst[0]

        return "ERROR"

    def remove_old_record_from_users_list(self, entered_username):
        '''
        The function deletes an outdated record from the database's users list
        after changing a user's password.
        :param entered_username: The entered username of a client whose password was changed.
        '''
        def deep_index(lst, val):
            return [(i, sub.index(val)) for (i, sub) in enumerate(lst) if val in sub]

        full_index = deep_index(self.users_list, entered_username)

        place_to_delete = full_index[0][0]

        self.users_list.remove(self.users_list[place_to_delete])

    def change_password(self, entered_username, new_password):
        '''
        The function updates the database and inserts a given new password in the line of a given username.
        :param entered_username: A client's entered username.
        :param new_password: A client's entered new password.
        '''
        try:
            sqliteConnection = sqlite3.connect('project_users_database.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            #sql_update_query = """Update new_clients_sign_ups set password = 10000 where username = Betty"""
            cursor.execute("""UPDATE new_clients_sign_ups SET password=? WHERE username=? """, (new_password, entered_username))
            sqliteConnection.commit()
            print("Record Updated successfully ")
            print("Before deleting old record:")
            print(self.users_list)
            self.remove_old_record_from_users_list(entered_username)
            print("After deleting old record:")
            self.create_users_list()
            print(self.users_list)
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")