from book import Book
class Ebook(Book):
   def __init__(self,title:str,author:str,isbn:str,year:int,genre:str,file_size:float,format:str):
      super().__init__(title,author,isbn,year,genre)
      self.file_size = file_size
      self.format = format

    