

#### Formatting the column names for dataframe #####

def col_names(dataframe):
    dataframe.columns = dataframe.columns.astype(str)
    dataframe.columns = dataframe.columns.str.strip(" ")
    dataframe.columns = dataframe.columns.str.lower()
    dataframe.columns = dataframe.columns.str.replace(" ","_")
    return dataframe

#### End of function ########

