from mysqlconnection import connectToMySQL

class User:
    db="users_schema"
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all_users(cls):
        query =""" 
        SELECT * FROM users;
        """
        results = connectToMySQL(cls.db).query_db(query)
        
        all_users=[]
        
        for user in results:
            all_users.append(cls(user))
        return all_users