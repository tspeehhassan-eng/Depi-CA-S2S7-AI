from preprocessing import Read_data_file ,Drop_unnecessary_features,Check_data_type
from config import cols_to_drop
df = Read_data_file("Titanic.csv")
df= Drop_unnecessary_features(df,cols_to_drop)
report = Check_data_type(df)
print(report)