import numpy as np
import matplotlib.pyplot as plt

from utils.utils import *

if __name__ == '__main__':

    root_dir = '/home/afawaz/phd/datasets/Aids/'
    art, art_pediatric, cases_adults, deaths, living, mother_to_child = load_data(root_dir=root_dir)

    dataFrames = [art, art_pediatric, cases_adults, deaths, living, mother_to_child]

    n_regions = get_n_regions(dataFrames)

    globals_dict = globals()
    dataFrames_names = [variable_to_string(dataFrame, globals_dict=globals_dict) for dataFrame in dataFrames]

    colors = generate_array_of_colors(n=n_regions)

    plot_stats_art(df=dataFrames[0], colors=colors)
    plot_stats_art_children(df=dataFrames[1], colors=colors)