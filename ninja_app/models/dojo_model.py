from ninja_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # inouting a class method to get all dojos from the database

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s,NOW(),NOW());"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return result
    
    @staticmethod
    def validate_name(dojo):
        is_valid = True
        if len(dojo['name']) < 5:
            flash("Name needs to be at least 3 characters.")
            is_valid = False
        return is_valid
