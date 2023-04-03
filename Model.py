import mysql.connector

class Model:
    """
    The Model part of the Pet Detective application.
    Creation date: February 10, 2023
    @author: Matt Ramey

    Attributes
    ------
    database : mysql.connector.connect
        The database connection.

    Methods
    ------
    retrieve_pets(size, sound_level, activity_level, hair_length, affection_level)
        Retrieves the pets that match the parameters.
    """

    def __init__(self):
        """
        Parameters
        ------
        database : mysql.connector.connect
            The database connection.
            pet_list : list of string tuples.
            The list of pets. Each pet is represented as
            a list of string tuples.
        """

        self.database = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Easy1982',
            port='3306',
            database='CST8333'
        )

    def retrieve_pets(self, size, sound_level, activity_level, hair_length, affection_level):
        """ Retrieves the pets that match the parameters. """
        # The database cursor.
        cursor = self.database.cursor()
        # The SQL query string.
        query_string = "SELECT * FROM PET WHERE Size = '" + size + "' AND SoundLevel = '" + sound_level + "' AND ActivityLevel = '" + activity_level + "' AND HairLength = '" + hair_length + "' AND AffectionLevel = '" + affection_level + "';"
        cursor.execute(query_string)
        # Search results.
        pets = cursor.fetchall()
        # Empty list of pet records.
        pet_list = []
        # Adds each result to the pet list.
        for pet in pets:
            pet_list.append(pet)
        return pet_list
