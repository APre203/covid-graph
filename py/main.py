import data
import processing
import pandas as pd
import plotly.express as px
import csv



#Loads data based on a location given and returns a plotly graph of percentage of people fully vaccinated
def graph(locate):
  temp = {"x":[],"y":[]}
  dpc = data.load_data("saved_data.csv")
  u_dpc = processing.copy_matching(dpc,"location",locate)
  numeric_u_dpc = []
  for dics in u_dpc:
    numeric_u_dpc.append(data.make_values_numeric(["series_complete_pop_pct"],dics))
  lol = data.make_lists(["date","series_complete_pop_pct"],numeric_u_dpc)
  processing.sorter(lol)
  for lst in lol:
    temp["x"].append(lst[0])
    temp["y"].append(lst[1])
  
  df = pd.DataFrame(dict(
    Date = temp["x"],
    Amount = temp["y"]
  ))
  fig = px.line(df, x="Date", y="Amount", title=f"Percentage of Population Vaccinated in {locate}")
  fig.show()


import os.path

#Adds recent 5000 data to file (Add more to the limit if not everything loads)
def add_data():
  url = f'http://data.cdc.gov/resource/unsk-b7fc.json?$limit={5000}&$where=location!=%27US%27'
  datas = data.json_loader(url)
  heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer', 'administered_unk_manuf','series_complete_pop_pct']
  data.save_data(heads, datas, "total_data.csv")
  data.compare_data("saved_data.csv","total_data.csv")

#Loads data if file not found (Add more to the limit if not everything loads)
def load_data():
  csv_file = "saved_data.csv"
  if not os.path.isfile(csv_file):
    url = f'http://data.cdc.gov/resource/unsk-b7fc.json?$limit={50000}&$where=location!=%27US%27'
    datas = data.json_loader(url)
    heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer', 'administered_unk_manuf','series_complete_pop_pct']
    data.save_data(heads, datas, "saved_data.csv")
  else:
    add_data()

load_data()
graph('NY')

