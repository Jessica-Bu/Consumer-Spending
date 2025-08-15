import numpy as np

def data_clean (df,columns_df):
    df = df.rename(columns={"Unnamed: 0":"country"})
    df["country"] = df["country"].replace({"Czechia":"Czech_Republic"}, regex=True)
    df.at[0, "country"] = "European_Union"
    df = df.drop([28,29,30,31,32,33,34,35,36,37])
    for column in columns_df:
        df[column] = df[column].replace({":": np.nan}, regex=True)
    return df