import requests

from consolemenu import ConsoleMenu, Screen
from consolemenu.items import FunctionItem
from consolemenu.prompt_utils import PromptUtils

class Google_Books_volumeInfo():
    title               = None
    authors             = None
    publisher           = None
    publishedDate       = None
    description         = None
    
    pageCount           = None
    printType           = None
    categories          = None
    maturityRating      = None
    allowAnonLogging    = None
    contentVersion      = None
    
    language            = None
    previewLink         = None
    infoLink            = None
    canonicalVolumeLink = None

    def __init__(self,json) -> None:
        self.title          = json.get('title')
        self.authors        = json.get('authors')
        self.publisher      = json.get('publisher')
        self.publishedDate  = json.get('publishedDate')
        self.description    = json.get('description')
        
        self.pageCount          = json.get('pageCount')
        self.printType          = json.get('printType')
        self.categories         = json.get('categories')
        self.maturityRating     = json.get('maturityRating')
        self.allowAnonLogging   = json.get('allowAnonLogging')
        self.contentVersion     = json.get('contentVersion')

        self.language               = json.get('language')
        self.previewLink            = json.get('previewLink')
        self.infoLink               = json.get('infoLink')
        self.canonicalVolumeLink    = json.get('canonicalVolumeLink')

class Google_Books_Items():
    kind        = None
    id          = None
    etag        = None
    selfLink    = None
    volumeInfo  = None
    def __init__(self,json) -> None:
        self.kind       = json.get('kind')
        self.id         = json.get('id')
        self.etag       = json.get('etag')
        self.selfLink   = json.get('selfLink')
        self.volumeInfo = Google_Books_volumeInfo(json['volumeInfo'])

class API_Google_books():
    URL         = 'https://www.googleapis.com/books/v1/volumes?q='
    kind        = None
    totalItems  = 0
    items       = []

    def __url_replace(self,url) -> str:
        return url.replace(" ","%20")

    def __url_request(self,url):
        return requests.get(url,headers={'content-type': 'application/json'})

    def __json_parsing(self,json,callback):
        self.kind       = json.get('kind')
        self.totalItems = json.get('totalItems')
        ([ self.items.append(Google_Books_Items(item)) for item in json['items'] ])

        callback()

    def __input_value(self,value) -> str:
        return input('{} : '.format(value))

    def __print_report(self):
        screen = Screen()
        screen.println('Nombre de résultats : {}'.format(self.totalItems))
        for item in self.items:
            screen.println('Titre : {}'.format(item.volumeInfo.title))
            screen.println('Lien : {}'.format(item.volumeInfo.infoLink))
            screen.println('----------')

        PromptUtils(screen).enter_to_continue() 

    # Intitle
    def get_intitle(self,value):
        terms = self.__input_value(value)

        response = self.__url_request('{}intitle+{}'.format(self.URL,self.__url_replace(terms)))
        data = response.json()
        self.__json_parsing(data,self.__print_report)
        
    # Inauthor
    def get_inauthor(self,value):
        terms = self.__input_value(value)

        response = self.__url_request('{}inauthor+{}'.format(self.URL,self.__url_replace(terms)))
        data = response.json()
        self.__json_parsing(data,self.__print_report)

    # Inpublisher
    def get_inpublisher(self,value):
        terms = self.__input_value(value)

        response = self.__url_request('{}inpublisher+{}'.format(self.URL,self.__url_replace(terms)))
        data = response.json()
        self.__json_parsing(data,self.__print_report)

    # Subject
    def get_subject(self,value):
        terms = self.__input_value(value)

        response = self.__url_request('{}subject+{}'.format(self.URL,self.__url_replace(terms)))
        data = response.json()
        self.__json_parsing(data,self.__print_report)

    # ISBN
    def get_isbn(self,value):
        terms = self.__input_value(value)

        response = self.__url_request('{}isbn+{}'.format(self.URL,self.__url_replace(terms)))
        data = response.json()
        self.__json_parsing(data,self.__print_report)

    # LCCN
    def get_lccn(self,value):
        terms = self.__input_value(value)

        response = self.__url_request('{}lccn+{}'.format(self.URL,self.__url_replace(terms)))
        data = response.json()
        self.__json_parsing(data,self.__print_report)
        
    # OCLC
    def get_oclc(self,value):
        terms = self.__input_value(value)

        response = self.__url_request('{}oclc+{}'.format(self.URL,self.__url_replace(terms)))
        data = response.json()
        self.__json_parsing(data,self.__print_report)
        
class Menu():
    menu = ConsoleMenu("Google Books", "Rechercher un livre avec l'api de Google")
    book = API_Google_books()

    def __init__(self) -> None:
        function_item_Intitle       = FunctionItem("Intitle",       self.book.get_intitle,      ["Enter Intitle"])
        function_item_Inauthor      = FunctionItem("Inauthor",      self.book.get_inauthor,     ["Enter Inauthor"])
        function_item_Inpublisher   = FunctionItem("Inpublisher",   self.book.get_inpublisher,  ["Enter Inpublisher"])
        function_item_Subject       = FunctionItem("Subject",       self.book.get_subject,      ["Enter Subject"])
        function_item_ISBN          = FunctionItem("ISBN",          self.book.get_isbn,         ["Enter ISBN"])
        function_item_LCCN          = FunctionItem("LCCN",          self.book.get_lccn,         ["Enter LCCN"])
        function_item_OCLC          = FunctionItem("OCLC",          self.book.get_oclc,         ["Enter OCLC"])
        
        self.menu.append_item(function_item_Intitle)
        self.menu.append_item(function_item_Inauthor)
        self.menu.append_item(function_item_Inpublisher)
        self.menu.append_item(function_item_Subject)
        self.menu.append_item(function_item_ISBN)
        self.menu.append_item(function_item_LCCN)
        self.menu.append_item(function_item_OCLC)

    def show(self):
        self.menu.show()

if __name__ == '__main__':
    menu = Menu()
    menu.show()