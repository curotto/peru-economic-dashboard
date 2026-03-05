import pandas as pd

def get_pbi_data():
    data = {
        "año": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        "pbi_variacion": [3.3, 4.0, 2.5, 4.0, 2.2, -11.0, 13.3, 2.7, -0.6],
        "pbi_millones_soles": [482506, 502225, 514215, 535006, 546745, 486025, 551202, 566878, 563500]
    }
    return pd.DataFrame(data)

def get_inflacion_data():
    data = {
        "año": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        "inflacion": [4.4, 3.2, 2.8, 2.2, 1.9, 2.0, 6.4, 8.5, 3.2]
    }
    return pd.DataFrame(data)

def get_empleo_data():
    data = {
        "año": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        "desempleo": [3.5, 3.6, 3.1, 3.3, 3.0, 7.8, 5.1, 3.6, 4.2],
        "informalidad": [73.2, 72.0, 72.5, 71.1, 70.7, 75.0, 76.8, 74.9, 73.6]
    }
    return pd.DataFrame(data)