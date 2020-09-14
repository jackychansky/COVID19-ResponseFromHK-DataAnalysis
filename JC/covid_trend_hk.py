import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
rcParams['figure.figsize'] =  20, 10

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

covid_fig = df_covid.plot(figsize = (20,10), title="Cumulative Covid Cases in Hong Kong")
covid_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidcum_hk.png")

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

df_covidnew.to_excel("FTDS_Aug2020_GroupProject1_Covid19/covidnew_hk.xlsx")

covidnew_fig = df_covidnew.plot(figsize = (20,10), title="New Covid Cases in Hong Kong")
covidnew_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidnew_hk.png")

# Extract Singapore data via API from Postman

url = "https://covid19-api.org/api/timeline/SG"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

# Initialize the primary dataframe for SG
data_sg = json.loads(response.text.encode('utf8'))
df_covid_sg = pd.DataFrame(data_sg)
df_covid_sg = df_covid_sg[["last_update", "cases", "deaths"]]
df_covid_sg.rename(columns={"last_update": "Date", "cases": "Confirmed", "deaths": "Death"}, inplace=True)

df_covid_sg['Date'] = pd.to_datetime(df_covid_sg['Date']).dt.strftime('%Y-%m-%d')
df_covid_sg.sort_values(by="Date", inplace=True)
df_covid_sg.set_index("Date", inplace=True)

covidcum_sg_fig = df_covid_sg.plot(figsize = (20,10), title="Cumulative Covid Cases in Singapore")
covidcum_sg_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidcum_sg.png")

# Convert the cumulative frequency graph to normal frequency graph for SG

confirmed_new = []
death_new = []
confirmed_new.append(df_covid_sg["Confirmed"][0])
death_new.append(df_covid_sg["Death"][0])
for n in range(1, len(df_covid_sg.index)):
    confirmed_new.append(df_covid_sg["Confirmed"][n] - df_covid_sg["Confirmed"][n-1])
    death_new.append(df_covid_sg["Death"][n] - df_covid_sg["Death"][n-1])

df_covidnew_sg = pd.DataFrame({"Date": list(df_covid_sg.index), "Confirmed": confirmed_new, "Death": death_new})
df_covidnew_sg.set_index("Date", inplace=True)

df_covidnew_sg.to_excel("FTDS_Aug2020_GroupProject1_Covid19/covidnew_sg.xlsx")

covidnew_sg_fig = df_covidnew.plot(figsize = (20,10), title="New Covid Cases in Singapore")
covidnew_sg_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidnew_sg.png")

# Extract Taiwan data via API from Postman
url = "https://covid19-api.org/api/timeline/TW"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
data_tw = json.loads(response.text.encode('utf8'))

# Initialize the primary dataframe for TW
df_covid_tw = pd.DataFrame(data_tw)
df_covid_tw = df_covid_tw[["last_update", "cases", "deaths"]]
df_covid_tw.rename(columns={"last_update": "Date", "cases": "Confirmed", "deaths": "Death"}, inplace=True)

df_covid_tw['Date'] = pd.to_datetime(df_covid_tw['Date']).dt.strftime('%Y-%m-%d')
df_covid_tw.sort_values(by="Date", inplace=True)
df_covid_tw.set_index("Date", inplace=True)

covidcum_tw_fig = df_covid_tw.plot(figsize = (20,10), title="Cumulative Covid Cases in Taiwan")
covidcum_tw_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidcum_tw.png")

# Convert the cumulative frequency graph to normal frequency graph for TW
confirmed_new = []
death_new = []
confirmed_new.append(df_covid_tw["Confirmed"][0])
death_new.append(df_covid_tw["Death"][0])
for n in range(1, len(df_covid_tw.index)):
    confirmed_new.append(df_covid_tw["Confirmed"][n] - df_covid_tw["Confirmed"][n-1])
    death_new.append(df_covid_tw["Death"][n] - df_covid_tw["Death"][n-1])

df_covidnew_tw = pd.DataFrame({"Date": list(df_covid_tw.index), "Confirmed": confirmed_new, "Death": death_new})

df_covidnew_tw.to_excel("FTDS_Aug2020_GroupProject1_Covid19/covidnew_tw.xlsx")

df_covidnew_tw.set_index("Date", inplace=True)
covidnew_tw_fig = df_covidnew_tw.plot(figsize = (20,10), title="New Covid Cases in Taiwan")
covidnew_tw_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidnew_tw.png")

# Extract Korea data via API from Postman

url = "https://covid19-api.org/api/timeline/KR"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

# Initialize the primary dataframe for KR
data_kr = json.loads(response.text.encode('utf8'))
df_covid_kr = pd.DataFrame(data_kr)
df_covid_kr = df_covid_kr[["last_update", "cases", "deaths"]]
df_covid_kr.rename(columns={"last_update": "Date", "cases": "Confirmed", "deaths": "Death"}, inplace=True)

df_covid_kr['Date'] = pd.to_datetime(df_covid_kr['Date']).dt.strftime('%Y-%m-%d')
df_covid_kr.sort_values(by="Date", inplace=True)
df_covid_kr.set_index("Date", inplace=True)

covidcum_kr_fig = df_covid_kr.plot(figsize = (20,10), title="Cumulative Covid Cases in Korea")
covidcum_kr_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidcum_kr.png")

# Convert the cumulative frequency graph to normal frequency graph for KR

confirmed_new = []
death_new = []
confirmed_new.append(df_covid_kr["Confirmed"][0])
death_new.append(df_covid_kr["Death"][0])
for n in range(1, len(df_covid_kr.index)):
    confirmed_new.append(df_covid_kr["Confirmed"][n] - df_covid_kr["Confirmed"][n-1])
    death_new.append(df_covid_kr["Death"][n] - df_covid_kr["Death"][n-1])

df_covidnew_kr = pd.DataFrame({"Date": list(df_covid_kr.index), "Confirmed": confirmed_new, "Death": death_new})
df_covidnew_kr.set_index("Date", inplace=True)

df_covidnew_kr.to_excel("FTDS_Aug2020_GroupProject1_Covid19/covidnew_kr.xlsx")

covidnew_kr_fig = df_covidnew_kr.plot(figsize = (20,10), title="New Covid Cases in Korea")
covidnew_kr_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidnew_kr.png")

# Extract USA data via API from Postman

url = "https://covid19-api.org/api/timeline/US"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

# Initialize the primary dataframe for US

data_us = json.loads(response.text.encode('utf8'))
df_covid_us = pd.DataFrame(data_us)
df_covid_us = df_covid_us[["last_update", "cases", "deaths"]]
df_covid_us.rename(columns={"last_update": "Date", "cases": "Confirmed", "deaths": "Death"}, inplace=True)

df_covid_us['Date'] = pd.to_datetime(df_covid_us['Date']).dt.strftime('%Y-%m-%d')
df_covid_us.sort_values(by="Date", inplace=True)
df_covid_us.set_index("Date", inplace=True)

covidcum_us_fig = df_covid_us.plot(figsize = (20,10), title="Cumulative Covid Cases in USA")
covidcum_us_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidcum_us.png")

# Convert the cumulative frequency graph to normal frequency graph for US

confirmed_new = []
death_new = []
confirmed_new.append(df_covid_us["Confirmed"][0])
death_new.append(df_covid_us["Death"][0])
for n in range(1, len(df_covid_us.index)):
    confirmed_new.append(df_covid_us["Confirmed"][n] - df_covid_us["Confirmed"][n-1])
    death_new.append(df_covid_us["Death"][n] - df_covid_us["Death"][n-1])

df_covidnew_us = pd.DataFrame({"Date": list(df_covid_us.index), "Confirmed": confirmed_new, "Death": death_new})
df_covidnew_us.set_index("Date", inplace=True)

df_covidnew_us.to_excel("FTDS_Aug2020_GroupProject1_Covid19/covidnew_us.xlsx")

covidnew_us_fig = df_covidnew_us.plot(figsize = (20,10), title="New Covid Cases in USA")
covidnew_us_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidnew_us.png")

# Extract Japan data via API from Postman

url = "https://covid19-api.org/api/timeline/JP"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

# Initialize the primary dataframe for JP

data_jp = json.loads(response.text.encode('utf8'))
df_covid_jp = pd.DataFrame(data_jp)
df_covid_jp = df_covid_jp[["last_update", "cases", "deaths"]]
df_covid_jp.rename(columns={"last_update": "Date", "cases": "Confirmed", "deaths": "Death"}, inplace=True)

df_covid_jp['Date'] = pd.to_datetime(df_covid_jp['Date']).dt.strftime('%Y-%m-%d')
df_covid_jp.sort_values(by="Date", inplace=True)
df_covid_jp.set_index("Date", inplace=True)

covidcum_jp_fig = df_covid_jp.plot(figsize = (20,10), title="Cumulative Covid Cases in Japan")
covidcum_jp_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidcum_jp.png")

# Convert the cumulative frequency graph to normal frequency graph for JP

confirmed_new = []
death_new = []
confirmed_new.append(df_covid_jp["Confirmed"][0])
death_new.append(df_covid_jp["Death"][0])
for n in range(1, len(df_covid_jp.index)):
    confirmed_new.append(df_covid_jp["Confirmed"][n] - df_covid_jp["Confirmed"][n-1])
    death_new.append(df_covid_jp["Death"][n] - df_covid_jp["Death"][n-1])

df_covidnew_jp = pd.DataFrame({"Date": list(df_covid_jp.index), "Confirmed": confirmed_new, "Death": death_new})
df_covidnew_jp.set_index("Date", inplace=True)

df_covidnew_jp.to_excel("FTDS_Aug2020_GroupProject1_Covid19/covidnew_jp.xlsx")

covidnew_jp_fig = df_covidnew_jp.plot(figsize = (20,10), title="New Covid Cases in Japan")
covidnew_jp_fig.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidnew_jp.png")

# Extract data via API from HKGOV for imported cases

import requests

url = "https://api.data.gov.hk/v2/filter?q=%7B%22resource%22%3A%22http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc%2Fenhanced_sur_covid_19_eng.csv%22%2C%22section%22%3A1%2C%22format%22%3A%22json%22%7D"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

raw_covid_details = json.loads(response.text)

df_covid_details = pd.DataFrame(raw_covid_details)
df_covid_details = df_covid_details[["Report date", "HK/Non-HK resident", "Case classification*"]]
df_covid_details.rename(columns={"Report date": "Date", "HK/Non-HK resident": "HK/Non-HK", "Case classification*": "Classification"}, inplace=True)

df_covid_details['Date'] = pd.to_datetime(df_covid_details['Date'], dayfirst=True)
df_covid_details.sort_values(by="Date", inplace=True)
df_covid_details.set_index("Date", inplace=True)

# Group the data to focus on Classification only
plt.close("all")

grouped = df_covid_details.groupby(df_covid_details.index)["Classification"].value_counts()
list_date = [grouped.index[n][0] for n in range(len(grouped))]
list_class = [grouped.index[n][1] for n in range(len(grouped))]
list_value = [grouped[n] for n in range(len(grouped))]
df_group = pd.DataFrame(list(zip(list_date, list_class, list_value)), columns=["Date", "Classification", "Total"])
df_group = df_group.set_index("Date")

df_group.to_excel("FTDS_Aug2020_GroupProject1_Covid19/covidhk_class.xlsx")

covid_class = sns.lineplot(data = df_group, x = df_group.index, y = df_group["Total"], hue = df_group["Classification"]).set_title("Classification of Covid Cases in Hong Kong")

covid_class.get_figure().savefig("FTDS_Aug2020_GroupProject1_Covid19/covidclass_hk.png")