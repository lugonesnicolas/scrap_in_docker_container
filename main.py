import datetime
import pytz
import requests
import markdown
from bs4 import BeautifulSoup

def run():
    try:
        datetime_obj = datetime.datetime.now()
        fecha = datetime_obj.astimezone(pytz.timezone("America/Buenos_Aires")).strftime("%d/%m/%Y")
        hora = datetime_obj.astimezone(pytz.timezone("America/Buenos_Aires")).strftime("%H:%M:%S")
        
        response = requests.get("https://dolarhoy.com/")

        if response.status_code == 200:
            soup=BeautifulSoup(response.text,"html.parser")
            dolar = soup.find('div', class_="tile dolar")
            markdown_text = []
            markdown_text.append(f"# Scraper que corre desde un container, actualiza la informacion y se sube al repositorio GitHub\n\n")
            for i in dolar:
                bloques=i.find_all('div', class_="tile is-child")
                for j in bloques:
                    titulo=j.find('a', class_="title")
                    compra=j.find('div', class_="compra")
                    venta=j.find('div', class_="venta")
                    if titulo.text != 'Dólar Tarjeta':
                        markdown_text.append(f"{titulo.text}\n\n")
                        markdown_text.append(f"Compra {(compra.find('div', class_='val').text)}\n\n")
                        markdown_text.append(f"Venta {(venta.find('div', class_='val').text)}\n\n")
                        # print(f"Compra {(compra.find('div', class_='val').text)}")
                        # print(f"Venta {(venta.find('div', class_='val').text)}")
                    else:
                        markdown_text.append(f"{titulo.text}\n\n")
                        markdown_text.append(f"Venta {(venta.find('div', class_='val').text)}\n\n")
                        #print(f"Venta {(venta.find('div', class_='val').text)}")
                            
            print("Solicitud realizada correctamente")
            markdown_text.append(f"Datos actualizados el {fecha} a las {hora}\n\n")
            # Convert the list of Markdown text to a Markdown document
            markdown_document = markdown.markdown("".join(markdown_text))
            # Save the Markdown document to a file
            with open("README.md", "w") as f:
                f.write(markdown_document) 
        else:
            print("Algo salió mal")

    except requests.exceptions.ConnectionError:
        print("Error de conexión")
     

if __name__=='__main__':
    run()
