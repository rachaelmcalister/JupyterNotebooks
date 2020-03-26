import pandas as pd
import numpy as np

def executeScriptsFromFile(filename, DBConnectionUser):
    query_filename = str(filename) + str('.txt')
    fd = open(query_filename, 'r')
    sqlFile = fd.read().replace("\n", " ")
    fd.close()
    query = str(sqlFile)
    column_file = str(filename) + str('_columns.txt')
    cf = open(column_file, 'r')
    columns = []
    for line in cf:
        columns.append(str(line.replace("\n", "")))
    cf.close()
    return pd.DataFrame(DBConnectionUser.query_database(query), columns=columns)

def calculate_conversion_CIs(p, n, num_decimal_places=3):
    SE = np.sqrt((p*(1-p))/n)
    lower_ci = np.round(p - 1.96*SE, num_decimal_places)
    upper_ci = np.round(p + 1.96*SE, num_decimal_places)
    return [lower_ci, upper_ci]