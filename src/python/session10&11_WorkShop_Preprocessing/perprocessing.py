import pandas as pd
def drop_cols(df, cols):
    return df.drop(columns=cols)
def Cols_type(df):
    return pd.DataFrame({"dtype":df.dtype(),"nunique":df.nunique() }).T
