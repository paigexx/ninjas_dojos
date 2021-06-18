from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo: 
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def show_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("ninjas_dojos").query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL("ninjas_dojos").query_db(query, data)

    @classmethod
    def get_dojo(cls, data):
        query = "SELECT ninjas.id AS ninja_id, first_name, last_name, age, ninjas.created_at AS ninja_created_at, ninjas.updated_at AS ninja_updated_at, dojos.id AS dojo_id, name, dojos.created_at AS dojo_created_at, dojos.updated_at AS dojo_updated_at FROM ninjas LEFT JOIN dojos ON ninjas.dojo_id = %(dojo_id)s WHERE dojos.id = %(dojo_id)s;"
        results  = connectToMySQL("ninjas_dojos").query_db(query, data)
        print(results)



    # need to appy the  ninjas  into the list as an instance
