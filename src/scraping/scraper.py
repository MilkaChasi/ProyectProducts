import requests
from bs4 import BeautifulSoup
import pandas as pd


def fech_page(url):
    
    """
    Obtener el contenido de una pagina.
    Args:
        url(str): URL de la página web a solicitar.
    Returns:
        str: Contenido HTML de la página web.
    Raises: 
        Sistem exit: Si ocurre un error en la solicitud HTTP.
        
    """
    response=requests.get(url)
    
    if response.status_code ==200:
        return response.content
    else:
        raise Exception(f"Failed to fetch page:{url}")
    
def parse_product(product):
    
    """
    Analizamos los detalles de un producto.
    Args:
        product(bs4.element.Tag): Objeto BeautifullSoup que contiene la información del producto.
    Returns:
        dict: Diccionario con título, descripción y precio del producto.
    
    """
    title= product.find("a",class_="title").text.strip()
    description = product.find("p", class_="description").text.strip()
    price = product.find("h4",class_="price").text.strip()
    return{
        "title":title,
        "description":description,
        "price":price
    }
    
def scrape(url):
    
    """
    Método principal del Scraping con soporte para multiples páginas.
    Args:
        url(str): URL de la página web a solicitar.
    Returns:
        pd.DataFrame: DataFrame de pandas con los datos de los productos.
 
    """
    page_content = fech_page(url)
    soup = BeautifulSoup(page_content,"html.parser")
   
    products = soup.find_all("div",class_="thumbnail")
    products_data=[]
    
    for product in products:
        products_info = parse_product(product)
        products_data.append(products_info) 
    return pd.DataFrame(products_data)
    
base_url="https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

df = scrape(base_url)
print(df)

df.to_csv("data/raw/products.csv", index=False)