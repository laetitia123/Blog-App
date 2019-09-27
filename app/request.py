
import urllib.request,json
from .models import Quotes
from config import Config



# Getting api key
api_key = None

# Getting the movie base url
base_url = None

def configure_request(app):
    # global api_key,base_url,quotes_base_url
    # api_key = app.config['MOVIE_API_KEY']
    # base_url = app.config['MOVIE_API_BASE_URL']
    base_url = app.config['QUOTES_API_BASE_URL']




def get_quotes():
    '''
    Function that gets the json responce to our url request
    '''
    random_quote=request.get(base_url)
    new_quote=random_quote.json()
    author=new_quote.get('author')
    quote=new_quote.get('quote')
    quotes_object=Quotes(author,quote)
    get_quotes_url = quotes_base_url.format()

    

    return quotes_object

