import requests

def requestHandler(url:str)->dict:
    
    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()        
        
        return {"data":response.json()}
        
    except requests.exceptions.RequestException as e:

        return {"error":e}
    


def parser(code:any):
    pass