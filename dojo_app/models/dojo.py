from dojo_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def create_dojo(cls, data ):
        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s );"
        return connectToMySQL('dojos_schema').query_db( query, data )

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"
        result = connectToMySQL('dojos_schema').query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None

