import requests

def requestHandler(url:str)->dict:
    
    try:
        response = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0", "Accept-Language": "en-US, fr-FR", "referrer": "https://www.arrow.com/", "connection": "keep-alive"  })
        
        response.raise_for_status()        
        
        return {"data":response.json(), "content":response.content}
        
    except requests.exceptions.RequestException as e:

        return {"error":e}
    


def parser(code:any):
    pass