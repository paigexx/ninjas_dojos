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
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = %(dojo_id)s WHERE dojos.id = %(dojo_id)s;"
        results  = connectToMySQL("ninjas_dojos").query_db(query, data)
        print(results)
        # this gets the result of the query out  of a list and into a dictionary 
        dojo = cls(results[0])
        print(dojo)
        # you can print the dojos name here 
        print(dojo.name)
        

        for row in results:
            ninja_data = {
                "id": row["ninjas.id"], 
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age":row["age"],
                "dojo_id":row["dojo_id"],
                "created_at": row["ninjas.created_at"],
                "updated_at": row["ninjas.updated_at"]
            }
            

            dojo.ninjas.append(ninja.Ninja(ninja_data))
            print(dojo.ninjas)
        
        return dojo

        


    # need to appy the  ninjas  into the list as an instance
