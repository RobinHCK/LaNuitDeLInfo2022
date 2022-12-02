import numpy as np
import matplotlib.pyplot as plt

from utils.utils import *

if __name__ == '__main__':

    root_dir = '/home/afawaz/phd/datasets/Aids/'
    art, art_pediatric, cases_adults, deaths, living, mother_to_child = load_data(root_dir=root_dir)

    dataFrames = [art, art_pediatric, cases_adults, deaths, living, mother_to_child]

    n_regions = get_n_regions(dataFrames)

    # globals_dict = globals()
    # dataFrames_names = [variable_to_string(dataFrame, globals_dict=globals_dict) for dataFrame in dataFrames]

    # colors = generate_array_of_colors(n=n_regions)

    # plot_stats_art(df=dataFrames[0], colors=colors)
    # plot_stats_art_children(df=dataFrames[1], colors=colors)

    fig = plot_map(dataFrames[0], column_to_use='Reported number of people receiving ART', pal='jet',
                        title="Reported number of people receiving ART")

    upload_credentials()
    upload_chart(fig=fig, filename="ART_per_country")

    fig = plot_map(dataFrames[1], column_to_use='Reported number of children receiving ART', pal='jet',
                        title="Reported number of children receiving ART")

    upload_credentials()
    upload_chart(fig=fig, filename="ART_children_per_country")

    dataFrames[3] = dataFrames[3].groupby(['Country'], as_index=False)['Count_median'].mean()

    fig = plot_map(dataFrames[3], column_to_use='Count_median', pal='jet',
                        title="Number of Dead people due to HIV AIDS")
    
    upload_credentials()
    upload_chart(fig=fig, filename="Number_Death_per_country")

    dataFrames[4] = dataFrames[4].groupby(['Country'], as_index=False)['Count_median'].mean()

    fig = plot_map(dataFrames[4], column_to_use='Count_median', pal='jet',
                        title="Number of living people with HIV AIDS")
    
    upload_credentials()
    upload_chart(fig=fig, filename="Number_living_hiv_per_country")