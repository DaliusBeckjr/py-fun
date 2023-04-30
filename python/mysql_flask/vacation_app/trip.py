
class trip:
    db="vacation_schema"
    
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.duration = data['duration']
        self.departure_date = data['departure_date']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        