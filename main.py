from matplotlib import pyplot as plt
import chart_studio
from create_html import write_html
from embedding_graphs import upload_chart, generate_iframe
from create_vizualization import plot_map
import numpy as np 
import pandas as pd



root = "/home/ayed/Bureau/de_la_nuit_l'info/"

cases =pd.read_csv(root + "archive/no_of_cases_adults_15_to_49_by_country_clean.csv")
deaths = pd.read_csv(root + "archive/no_of_deaths_by_country_clean.csv")
living = pd.read_csv(root + "archive/no_of_people_living_with_hiv_by_country_clean.csv")
coverage = pd.read_csv(root + "archive/art_coverage_by_country_clean.csv")
pediatric = pd.read_csv(root + "archive/art_pediatric_coverage_by_country_clean.csv")
prevention = pd.read_csv(root + "archive/prevention_of_mother_to_child_transmission_by_country_clean.csv")




fig = plot_map(living, 'Count_median', 'matter')

username = "izadeelvin99"
api_key = "SNYTOtwDQTKfZjGhSEyR"

chart_studio.tools.set_credentials_file(username=username, 
api_key=api_key)

upload_chart(fig, "living_per_country")

iframe = generate_iframe("https://plotly.com/~izadeelvin99/1/")

print(iframe)
