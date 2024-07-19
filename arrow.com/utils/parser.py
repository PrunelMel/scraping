import requests

import bs4

def requestHandler(url:str)->dict:
    
    try:
        response = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0", "Accept-Language": "en-US, fr-FR", "referrer": "https://www.arrow.com/", "connection": "keep-alive", "accept": "text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8"})
        
        response.raise_for_status()        
        
        return {"staus_code":response.status_code, "headers":response.headers, "content":response.content}
        
    except requests.exceptions.RequestException as e:

        return {"error":e}
    


def parser(code:bytes|str):

    try:

        soup = bs4.BeautifulSoup(code, "html.parser")

        section = soup.find("section", id='ManufacturersTabs')

        return section

    except Exception as e:

        return {"error":e}
