from mysqlconnection import connectToMySQL

class User:
    db="users_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        
# the save method will be use to save our new user to the database
# crud method: Create
    @classmethod
    def save(cls, data);
    query="""
        INSERT INTO users (first_name, last_name, email) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s);
    """
    results = connectToMySQL(cls.db).query_db
    
# crud method: Read
    @classmethod
    def get_all_users(cls):
        query="""
        SELECT * FROM users;
        """

        results = connectToMySQL(db).query_db(query)
        users=[]
        for i in results:
            users.append(cls(i))
            return i 