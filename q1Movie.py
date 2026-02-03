class Movie:
    def __init__(self, title, rating):
        self.__title = title
        self.__rating = rating
        
    def get_title(self):
        return self.__title
    
    def get_rating(self):
        return self.__rating
        
    def set_title(self, title):
        self.__title = title
    
    def set_rating(self, rating):
        self.__rating = rating
        
movie1 = Movie("Spongebob", 10)

print("Title:", movie1.get_title())
print("Rating:", movie1.get_rating())

