import shelve

class Tour_Datastore:
    
    def __init__(self):
        self.__datastore=shelve.open("data/Tour_Details/Tour_Detail_DB")

    def __delattr__(self):
         self.__datastore.close()

    def get_tours(self):
        return self.__datastore
    
    def add_tour(self,Tour):
         self.__datastore[Tour.get_id()]=Tour
         
    def get_tour(self,id_tour):
        return self.__datastore[id_tour]
    
# create a class for the attraction
class Attraction: 
    def __init__(self,touristSp:dict):
        self.__touristSp=touristSp
   
    def get_tr_spots(self):
        return self.__touristSp
#   create a class Tour to organise all the information for each tour 
class Tour:
    # create the constructor for the class Tour
    def __init__(self,id, location, urlimg, price, period,attraction:Attraction):
        self.__id=id
        self.__location=location
        self.__urlimg=urlimg
        self.__price=price
        self.__period=period
        self.__attraction=attraction
    # define a function to get the price from the object
    def get_price(self):
        return self.__price
        # define a function to get the period from an object tour
    def get_period(self):
        return self.__period
    # define a function to get the id from an object tour
    def get_id(self):
        return self.__id
    # define a function to get the location from an object tour
    def get_location(self):
        return self.__location
    # define a function to get the url of the image from an object tour
    def get_url_img(self):
        return self.__urlimg
    # define a function to get the list of the tourist attractions from an object tour
    def get_tourist_attraction(self):
        return self.__attraction


class Path_Img_Datastore:
    def __init__(self):
        self.__datastore=shelve.open("data/Imgs_Path/Path_Img_DB")

    def __delattr__(self):
         self.__datastore.close()

    def get_tours_paths(self):
        return self.__datastore
    
    def add_path_tour(self,Path_Img_Tour):
         self.__datastore[Path_Img_Tour.get_id_tour()]=Path_Img_Tour
         
    def get_path_imgs_tour(self,id_tour):
        return self.__datastore[id_tour]
    
    

# defined a class with all the url of the pictures for each tour
class Path_Img_Tour:
    def __init__(self, id:str,path_imgs:list):
        self.__id=id
        self.__path_imgs=path_imgs
    
    def get_path_imgs(self):
        return self.__path_imgs
    def get_id_tour(self):
        return self.__id
    
