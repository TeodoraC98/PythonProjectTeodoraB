import shelve
from models import Tour
# create a different shelve object Favourite_Tour_DB to store the date of the tours
class Favourite_Tour_DB:
    def __init__(self):
        self.__datastore=shelve.open("data/Favourite_Tours/Favourite_DB")

    def __delattr__(self):
         self.__datastore.close()

    def add_favourite(self,Tour):
        self.__datastore[Tour.get_id()]=Tour
    def get_id(self):
       return self.__datastore[Tour.get_id()]

    def get_favourite_tour(self,id_tour):
        return self.__datastore[id_tour]
    
    def get_tours(self):
        return self.__datastore
    
    def delete_favourite_tour(self,id_tour):
        del self.__datastore[id_tour]

    def has_tour(self,id_tour):
        return bool(self.__datastore[id_tour])
     