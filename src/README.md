# Scraping web de productos

En este proyecto realizamos scraping de datos de productos de un sitio web, limpia y analiza datos, y los guarda en un archivo CSV.

## Requistos

-Python 3.7+
-pandas
-beautifulsoup4
-requests
-matplotlib

## Instalación

Para instalar las dependencias creamos un archivo "txt" el cual guardamos todas las dependencias para su rapida instalación.
Su método de uso es utilizando pip y es con el comando siguiente.


```` bash

pip install -r .\dep.txt

````

## Arquitectuta de las carpetas
````bash
final-boss
|——— data/
|     |— raw/
|     |    |__ products.csv
|     |— processed/
|         |__ cleaned_products.csv
|
|——— notebooks/
|     |__ exploration.ipynb
|
|——— src/
|    |— analysis/
|        |__ __init__.py
|        |__ analysis.py
|     |— decorators/
|         |__ __init__.py
|         |__ decorators.py
|     |— scraping/
|         |__ __init__.py
|         |__ scraper.py
|__ dep.txt
|__ README.md
````bash


## Ejecución del programa

Para ejecutar el scraper hay que realizar es:

````bash

python .\src\scraping\scraper.py

````

## Ejecución para el análisis de datos

Para ejecutar el script para el análisis de datos lo que hay que realizar es:

````bash

python .\src\analysis\analysis.py

````

#### MILKA CHASI