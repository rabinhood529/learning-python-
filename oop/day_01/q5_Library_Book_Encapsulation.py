class Book():

    total_books = 0


    def __init__(self, title, author, price, is_available):
        self.__title = title
        self.__author = author
        self.__price = price
        self.__is_available = True
    @property
    def title(self):
        return self.__title
    
    def author(self):
        return self.__author
        
    def price(self):
        return self.__price
    
    def price(self, value):
        if value > 0:
            self.__price = value 
        else:
            print("invalid price!")

    def is_available(self):
        return self.__is_available
    

    def borrow(self):
        if self.__is_available:
            self.is_available = False
            print("Book borrowed")
        else:
            print("BOok not available!")
    
    def return_book(self):
        if self.__is_available:
            self.__is_available = True
            print("BOOK RETURNED")
        
    def infor(self):
        print( self.__title,
        self.__author,
        self.__price ,
        self.__is_available )

    def get_total_books(cls, total_book):
        total_book += 

    def is_valid_price(price):
        if price > 0:
            return True
    
