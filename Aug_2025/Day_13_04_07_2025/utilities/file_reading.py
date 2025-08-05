import pandas as pd


def data_to_data_frame(hello): #Function definition with argument
    """Below code is with exception handling for dataframe conversion"""
    try:
        df = pd.DataFrame(hello)
        return  df
    except Exception as ex:
        return ex
