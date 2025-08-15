import numpy as np

def data_clean (df,columns_df):
    df = df.rename(columns={"Unnamed: 0":"country"})
    df["country"] = df["country"].replace({"Europäische Union - 27 Länder (ab 2020)":"EU", "Belgien": "BE", "Bulgarien":"BG", "Dänemark":"DK", "Deutschland":"DE", "Estland":"EE",
                                                        "Finnland":"FI", "Frankreich":"FR", "Griechenland":"GR", "Irland":"IE", "Italien":"IT",
                                                        "Kroatien":"HR", "Lettland":"LV", "Litauen":"LT", "Luxemburg":"LU", "Malta":"MT", "Niederlande":"NL", 
                                                        "Österreich":"AT", "Polen":"PL", "Portugal":"PT", "Rumänien":"RO", "Schweden":"SE",
                                                        "Slowakei":"SK", "Slowenien":"SI", "Spanien":"ES", "Tschechien":"CZ", "Ungarn":"HU",
                                                        "Zypern":"CY"}, regex=True)
    df.at[0, "country"] = "EU"
    df = df.drop([28,29,30,31,32,33,34,35,36,37,38,39])
    for column in columns_df:
        df[column] = df[column].replace({":": np.nan}, regex=True)
    return df