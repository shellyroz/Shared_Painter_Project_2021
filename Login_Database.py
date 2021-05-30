# Name: Shelly Rozman
# Python Version: 3.7.2
# Date: 14/3/2021

import sqlite3


class LoggedInUsers:

    def __init__(self, tablename="existing_clients_logins", username="username", password="password"):
        self.__tablename = tablename
        self.__username = username
        self.__password = password
        self.users_list = []

        conn = sqlite3.connect('project_users_database.db')
        print("Opened database successfully")
        # query_str = "CREATE TABLE IF NOT EXISTS " + tablename + "(" + self.__username + " " + \
        #             " TEXT PRIMARY KEY  NOT NULL ,"
        query_str = "CREATE TABLE IF NOT EXISTS " + tablename + "(" + self.__username + " " + \
                    " TEXT    NOT NULL ,"
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
        : rtype: string.
        '''
        return self.__tablename

    def insert_user(self, username, password):
        '''
        The function inserts given information into the database.
        :param username: A given username.
        :param password: A given password.
        '''
        conn = sqlite3.connect('project_users_database.db')
        insert_query = "INSERT INTO " + self.__tablename + " (" + self.__username + "," + self.__password + ") VALUES " \
                                                                                                            "(" + "'" + username + "'" + "," + "'" + password + "'" + ");"
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
        str1 = "select * from existing_clients_logins;"

        """strsql = "SELECT username, password  from " +  self.__tablename + " where " + self.__userId + "=" \
            + str(username)
        """
        print(str1)
        cursor = conn.execute(str1)
        for row in cursor:
            print("username = ", row[0]) # username
            print("password = ", row[1]) # password

        print("Operation done successfully")
        conn.close()

    def create_users_list(self):
        '''
        The function creates a list of all the users' in the database information.
        '''
        conn = sqlite3.connect('project_users_database.db')
        print("Opened database successfully")
        str1 = "select * from existing_clients_logins;"

        cursor = conn.execute(str1)

        for row in cursor:
            username = row[0]
            password = row[1]

            this_user = [username, password]

            if this_user not in self.users_list:
                self.users_list.append(this_user)

        print("Operation done successfully")
        conn.close()

    def is_username_in_database(self, entered_username):
        '''
        The function checks whether a username is in the database or not.
        :param entered_username: An entered username.
        :return: True if the username is in the database, and False otherwise.
        :rtype: bool.
        '''
        for lst in self.users_list:
            if entered_username == lst[0]:
                return True

        return False

    def delete_user(self, username):
        '''
        This function deletes a given user from the database.
        :param username: A given user's username.
        '''
        self.create_users_list()

        if self.users_list != []:
            place_to_delete = 0
            for i in range(len(self.users_list)):
                if self.users_list[i][1] == username:
                    place_to_delete = i

            self.users_list.remove(self.users_list[place_to_delete])

        sqliteConnection = sqlite3.connect('project_users_database.db')
        cursor = sqliteConnection.cursor()
        cursor.execute('DELETE FROM existing_clients_logins WHERE username=?', (username,))
        sqliteConnection.commit()

        print("After deleting record: ")
        print(self.users_list)


    def delete_table(self):
        sqliteConnection = sqlite3.connect('project_users_database.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("DROP TABLE existing_clients_logins")
        print("Table dropped...")
        sqliteConnection.commit()
        sqliteConnection.close()



# c = LoggedInUsers()
# c.delete_user("try")
# c.delete_table()
