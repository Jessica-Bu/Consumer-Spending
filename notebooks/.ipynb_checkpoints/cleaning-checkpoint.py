{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02f47d46-e11a-42ba-aa19-6b75a3e7326c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def data_clean(df,columns_df):\n",
    "    df = df.rename(columns={\"Unnamed: 0\":\"country\"})\n",
    "    df[\"country\"] = df[\"country\"].replace({\"Europäische Union - 27 Länder (ab 2020)\":\"EU\", \"Belgien\": \"BE\", \"Bulgarien\":\"BG\", \"Dänemark\":\"DK\", \"Deutschland\":\"DE\", \"Estland\":\"EE\",\n",
    "                                                        \"Finnland\":\"FI\", \"Frankreich\":\"FR\", \"Griechenland\":\"GR\", \"Irland\":\"IE\", \"Italien\":\"IT\",\n",
    "                                                        \"Kroatien\":\"HR\", \"Lettland\":\"LV\", \"Litauen\":\"LT\", \"Luxemburg\":\"LU\", \"Malta\":\"MT\", \"Niederlande\":\"NL\", \n",
    "                                                        \"Österreich\":\"AT\", \"Polen\":\"PL\", \"Portugal\":\"PT\", \"Rumänien\":\"RO\", \"Schweden\":\"SE\",\n",
    "                                                        \"Slowakei\":\"SK\", \"Slowenien\":\"SI\", \"Spanien\":\"ES\", \"Tschechien\":\"CZ\", \"Ungarn\":\"HU\",\n",
    "                                                        \"Zypern\":\"CY\"}, regex=True)\n",
    "    df.at[0, \"country\"] = \"EU\"\n",
    "    df = df.drop([28,29,30,31,32,33,34])\n",
    "    for column in columns_df:\n",
    "        df[column] = df[column].replace({\":\": np.nan}, regex=True)\n",
    "return df\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
