import sqlite3
import tkinter as tk
import tkinter.messagebox


class Users:
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
        return self.__tablename

    def insert_user(self, email, username, password):
        conn = sqlite3.connect('project_users_database.db')
        insert_query = "INSERT INTO " + self.__tablename + " (" + self.__email + "," + self.__username + "," + self.__password + ") VALUES " \
                                                                                                            "(" + "'" + email + "'" + "," + "'" + username + "'" + "," + "'" + password + "'" + ");"
        print(insert_query)
        conn.execute(insert_query)
        conn.commit()
        conn.close()
        print("Record created successfully")

    def select_user_by_id(self, username):
        conn = sqlite3.connect('project_users_database.db')
        print("Opened database successfully")
        str1 = "select * from new_clients_sign_ups;"

        """strsql = "SELECT username, email, password  from " +  self.__tablename + " where " + self.__userId + "=" \
            + str(username)
        """
        print(str1)
        cursor = conn.execute(str1)
        for row in cursor:
            print("email = ", row[0])
            print("username = ", row[1])
            print("password = ", row[2])

        print("Operation done successfully")
        conn.close()


    def print_users(self):
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

            # elif lst[1] != given_username and lst[2] != given_password:
            #     tk.messagebox.showerror(title="ERROR",
            #                             message="Both the username and password you entered are incorrect. Please try again.")
            #     return "U&P_ERROR"

        return "ERROR"


    def is_username_in_database(self, entered_username):
        for lst in self.users_list:
            if entered_username == lst[1]:
                return True

        return False


    # def change_password(self, original_password, new_password):
    #     conn = sqlite3.connect('project_users_database.db')
    #     print("Opened database successfully")
    #
    #     # str1 = "UPDATE " + self.__tablename + " SET password = " + new_password + " WHERE password = " + original_password
    #     #
    #     # # cursor = conn.execute(str1)
    #     # conn.execute(str1)
    #     # sql = ''' UPDATE new_clients_sign_ups
    #     #               SET password = new_password ,
    #     #               WHERE password = WeDare'''
    #     # cur = conn.cursor()
    #     # cur.execute(sql)
    #     # conn.commit()
    #
    #     cur = conn.cursor()
    #     cur.execute("""UPDATE new_clients_sign_ups SET password=? WHERE password=? """, (new_password, original_password))



    def remove_old_record_from_users_list(self, entered_username):
        def deep_index(lst, val):
            return [(i, sub.index(val)) for (i, sub) in enumerate(lst) if val in sub]

        full_index = deep_index(self.users_list, entered_username)

        place_to_delete = full_index[0][0]

        self.users_list.remove(self.users_list[place_to_delete])




    def change_password(self, entered_username, new_password):
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



    # def to_change_password(self, entered_username, new_password):
    #     print("Before changing password:")
    #     print(self.users_list)
    #     for lst in self.users_list:
    #         if lst[1] == entered_username:
    #             self.change_password(entered_username, new_password)


    # def change_password(self, entered_username, new_password):
    #     place = 0
    #     print("Taylor")
    #     print(self.users_list)
    #     for i in range(len(self.users_list)):
    #         if entered_username == self.users_list[i][1]:
    #             place = i
    #
    #     self.users_list[place][2] = new_password
    #     self.create_users_list()
    #     print("The Queen")
    #     print(self.users_list)



# u = Users()
# u.insert_user("olivia@gamil.com", "Shelly", "TS1989")
# u.insert_user("meredith@gamil.com", "Betty", "20Lifetimes")
# u.insert_user("benjamin@gmail.com", "August", "Never13Mine")
# u.insert_user("taylorswift@gamil.com", "Taylor", "1989")

# u.select_user_by_id(1)

u = Users()
u.create_users_list()
print(u.users_list)

#u.change_password("Betty", "cardigans")
# u.create_users_list()
# print(u.users_list)
