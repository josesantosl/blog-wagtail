import requests
import json
import xlsxwriter #para excel

def main():
    url= requests.get('http://localhost:8000/api/v2/pages/?type=blog.Articolo')
    
    data = json.loads(url.text) #trasforma il testo del json in un dizionario.
    #print(data)

    for item in data['items']:
        print(item['title'])


if __name__ == "__main__":
    main()
