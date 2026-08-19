class Book:
    def __init__(self,title:str,author:str,isbn:str,year:int,genre:str):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.year=year
        self.genre=genre
        self.is_borrowed:bool=False
        self._borrow_count:int=0

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            self._borrow_count+=1
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False
    
    def is_available(self):
        if self.is_borrowed==False:
            return True
        else:
            return False
        
            

