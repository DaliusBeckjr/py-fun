from mysqlconnection import connectToMySQL
class User:
    db = "vacation_schema"
    
    def __init__(self, data):
        # colimn names that are in the db:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.age = data['age']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # reason: we are creating this constructor method that we will use the 
        #  information from our db which is why we need the exact col. from our db
        #  to send to the constructor meth'd to create instances
    
    @classmethod
    def get_all_users(cls):
        query=""" 
            SELECT * FROM users;
        """
        
        results = connectToMySQL(cls.db).query_db(query)
        
        all_users=[]
        
        for user in results:
            all_users.append(cls(user))
        return all_users