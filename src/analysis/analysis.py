import pandas as pd
import os
from ..decorators.decorators import timeit, logit

@logit
@timeit
def load_data(data_path):
    """
    Cargamos los datos desde un archivo CSV o Excel.
    Args:
        data_path(str): Ruta del archivo a cargar.
    Returns:
        pd.DataFrame: DataFrame de pandas con los datos cargados.
    Raises: 
        Value error: Si los datos del archivo no es soportado.
        
    """
    
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path)
    elif data_path.endswith(".xlsx"):
        df = pd.read_excel(data_path)
    else:
        raise ValueError("Unsupported file format")
    print("Data loaded successfeully")
    
    return df

@logit
@timeit
def clean_data(df):
    """
    Limpieza de datos.
    Args:
        df(pd.DataFrame): DataFrame con los datos a limpiar.
    Returns:
        pd.DataFrame: DataFrame con los datos limpios.
        
    """
    df["price"]=df["price"].replace(r"[\$,]", "", regex=True).astype(float)
    print("Data cleaned Successfully")
    return df


@logit
@timeit
def analyze_data(df):
    """
    Análisis básico de los datos.
    Args:
        df(pd.DataFrame): DataFrame con los datos a utilizar.
        
    """
    print("Basic Data Analysis:")
    print(df.describe())
    print("\nProducts with highest prices:")
    highestPrices=df.nlargest(5,"price")
    print(highestPrices)
    return highestPrices
   
   
@logit
@timeit 
def save_clean_data(df,outputh_path):
    """
    Guardar los datos limpios en un archivo CSV o Excel.
    Args:
        df(pd.DataFrame): DataFrame con los datos a guardar.
        outputh_path(str): Ruta del archivo de salida.
    Raises: 
        Value error: Si los datos del archivo no es soportado.
        
    """
    if outputh_path.endswith(".csv"):
        df.to_csv(outputh_path, index=False)
    elif outputh_path.endswith(".xlsx"):
        df.to_excel(outputh_path,index=False)
    else:
        raise ValueError("Unsupported file formt")
    print(f"Clean data saved to {outputh_path}")

if __name__=="__main__":
    data_path="data/raw/products.csv"
    outputh_path = "data/processed/cleaned_products.csv"
    
    df=load_data(data_path)
    df=clean_data(df)
    df=analyze_data(df)
    os.makedirs("data/processed", exist_ok=True)
    save_clean_data(df,outputh_path)