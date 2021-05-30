import sqlite3


class Users1:
    """Creates database with users table includes:
       create query
       insert query
       select query
    """

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

    def select_user_by_id(self, username):
        conn = sqlite3.connect('project_users_database.db')
        print("Opened database successfully")
        str1 = "select * from existing_clients_logins;"

        """strsql = "SELECT username, password  from " +  self.__tablename + " where " + self.__userId + "=" \
            + str(username)
        """
        print(str1)
        cursor = conn.execute(str1)
        for row in cursor:
            print("username = ", row[0])
            print("password = ", row[1])

        print("Operation done successfully")
        conn.close()


    def print_users(self):
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



c = Users1()
# c.print_users()
c.create_users_list()
print(c.users_list)