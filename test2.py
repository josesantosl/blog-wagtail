import requests
import json
import xlsxwriter #libreria per scrivere in excel

def main():
    url= requests.get('http://localhost:8000/api/v2/pages/?type=blog.Articolo')
    
    listArticoli = json.loads(url.text) #trasforma il testo del json in un dizionario.

    #apertura del file
    workbook = xlsxwriter.Workbook("outputTest2.xlsx")
    worksheet= workbook.add_worksheet()



    for row,item in enumerate(listArticoli['items']):
        print(item['title'])
        url= requests.get('http://localhost:8000/api/v2/pages/'+str(item['id'])+"/?format=json")
        print(url.text)
        pagina = json.loads(url.text)
        worksheet.write(row,0,pagina['title'])
        worksheet.write(row,1,pagina['descrizione'])
        worksheet.write(row,2,pagina['testo'])
        worksheet.write(row,3,pagina['data'])
        worksheet.write(row,4,pagina['autore']['id'])

    workbook.close()




if __name__ == "__main__":
    main()
