from dojo_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_ninjas_dojo(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL('dojos_schema').query_db(query, data)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas
    
    @classmethod
    def create_ninja(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name , age, dojo_id ) VALUES ( %(fname)s , %(lname)s , %(age)s , %(dojo_id)s );"
        return connectToMySQL('dojos_schema').query_db( query, data )

    @classmethod
    def get_one_ninja(cls, ninja_id):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {'id': ninja_id}
        result = connectToMySQL('dojos_schema').query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None

