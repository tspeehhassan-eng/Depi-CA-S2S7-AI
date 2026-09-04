import pandas as pd
def Read_data_file(file_path):
    df=pd.read_csv(file_path)
    return df
def Drop_unnecessary_features(df, cols_to_drop):
    df.drop(columns=cols_to_drop,inplace=True)
    return df
def Check_data_type(df):
    report = pd.DataFrame({
        "Data Type": df.dtypes,
        "Unique Values": df.nunique()
    })

    return report.T

    
