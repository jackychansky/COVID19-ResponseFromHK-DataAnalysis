import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# Extract data via API from HKGOV
url = "https://api.data.gov.hk/v2/filter?q=%7B%22resource%22%3A%22http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc%2Flatest_situation_of_reported_cases_covid_19_eng.csv%22%2C%22section%22%3A1%2C%22format%22%3A%22json%22%2C%22sorts%22%3A%5B%5B1%2C%22asc%22%5D%5D%7D"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

# Initialize the primary dataframe
raw_covid = json.loads(response.text)
df_covid = pd.DataFrame(raw_covid)
df_covid = df_covid[["As of date", "Number of confirmed cases", "Number of death cases"]]
df_covid.rename(columns={"As of date": "Date", "Number of confirmed cases": "Confirmed", "Number of death cases": "Death"}, inplace=True)

# Convert to the date format and set it as index
df_covid['Date'] = pd.to_datetime(df_covid['Date'], dayfirst=True)
df_covid.sort_values(by="Date", inplace=True)
df_covid.set_index("Date", inplace=True)




# Convert the cumulative frequency graph to normal frequency graph
confirmed_new = []
death_new = []
confirmed_new.append(df_covid["Confirmed"][0])
death_new.append(df_covid["Death"][0])

for n in range(1, len(df_covid.index)):
    confirmed_new.append(df_covid["Confirmed"][n] - df_covid["Confirmed"][n-1])
    death_new.append(df_covid["Death"][n] - df_covid["Death"][n-1])

df_covidnew = pd.DataFrame({"Date": list(df_covid.index), "Confirmed": confirmed_new, "Death": death_new})

df_covidnew.set_index("Date", inplace=True)

df_covidnew.plot().get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/omg.png")