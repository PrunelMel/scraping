import requests

def requestHandler(url:str)->dict:
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return {"status_code":response.status_code, "data":response.json()}
        else:
            return {"status_code":response.status_code, "message":""}
    
    except Exception as e:

        return {"error":e}
    


def parser(code:any):
    pass