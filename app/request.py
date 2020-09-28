import urllib, json
from .models import Quotes

quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def load_quote():

    try:
        with urllib.request.urlopen(quotes_url) as url:
            response = url.read()
            current_quote = json.loads(response)

            author = current_quote.get('author')
            quote = current_quote.get('quote')

            quote_displayed = Quotes(author,quote)
    except:
            author = 'Dancan'
            quote = 'For Every Problem There is A solution'

            quote_displayed = Quotes(author,quote)


    return quote_displayed



