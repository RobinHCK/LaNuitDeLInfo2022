import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
import random

font = {'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

def create_directory(dir):

    if not os.path.exists(dir):
        os.mkdir(dir)

def load_data(root_dir):

    art = pd.read_csv(root_dir + 'art_coverage_by_country_clean.csv')
    art_pediatric = pd.read_csv(root_dir + 'art_pediatric_coverage_by_country_clean.csv')

    cases_adults = pd.read_csv(root_dir + 'no_of_cases_adults_15_to_49_by_country_clean.csv')

    deaths = pd.read_csv(root_dir + 'no_of_deaths_by_country_clean.csv')
    living = pd.read_csv(root_dir + 'no_of_people_living_with_hiv_by_country_clean.csv')

    mother_to_child = pd.read_csv(root_dir + 'prevention_of_mother_to_child_transmission_by_country_clean.csv')

    return art.dropna(), art_pediatric.dropna(), cases_adults.dropna(), deaths.dropna(), living.dropna(), mother_to_child.dropna()

def variable_to_string(var, globals_dict):

    return [var_name for var_name in globals_dict if globals_dict[var_name] is var]

def generate_array_of_colors(n):

    # random.seed(-1)

    colors = []

    r = int(np.random.randn(1)[0] * 256)
    g = int(np.random.randn(1)[0] * 256)
    b = int(np.random.randn(1)[0] * 256)

    step = 256 / n

    for _ in range(n):

        r += step
        g += step
        b += step

        r = int(r) % 256
        g = int(g) % 256
        b = int(b) % 256

        colors.append((r / 255, g / 255, b / 255, 0.4))
        colors.append((r / 255, g / 255, b / 255, 1.0))

    return colors

def get_n_regions(dataFrames, column_region='WHO Region'):

    return min([len(np.unique(dataFrame[column_region])) for dataFrame in dataFrames])

def plot_stats_art(df, colors, column_art_recieving='Reported number of people receiving ART',
                               column_hiv_living='Estimated number of people living with HIV_median',
                               column_art_coverage_among_hiv='Estimated ART coverage among people living with HIV (%)_median',
                               column_region='WHO Region',
                               column_country='Country',
                               output_dir = 'stats_data/'):

    n_countries = len(np.unique(df[column_country]))
    n_regions = len(np.unique(df[column_region]))
    regions = np.unique(df[column_region])

    fig, ax = plt.subplots(1, 1, figsize=(50,30))

    plotted_bars = 0

    i_color = 0

    for _region in range(n_regions):

        df_region = df.loc[(df[column_region] == regions[_region])]

        art = np.asarray(df_region[column_art_recieving], dtype=np.float128)
        hiv = np.asarray(df_region[column_hiv_living], dtype=np.float128)
        
        ax.bar(np.arange(len(hiv)) + plotted_bars, hiv, label=regions[_region] + ' - HIV Living', color=colors[i_color])
        ax.bar(np.arange(len(art)) + plotted_bars, art, label=regions[_region] + ' - ART Receiving', color=colors[i_color+1])
        plotted_bars = plotted_bars + len(art)
        i_color = i_color + 2
    
    ax.set_yscale('log')
    ax.legend()

    ax.set_xticks(range(plotted_bars))
    ax.set_xticklabels(np.asarray(df[column_country]), rotation=90)

    create_directory(output_dir)
    create_directory(output_dir + 'ART/')

    plt.savefig(output_dir + 'ART/ART_regions.svg')
    plt.savefig(output_dir + 'ART/ART_regions.png')

def plot_stats_art_children(df, colors, column_art_recieving='Reported number of children receiving ART',
                                        column_art_needing='Estimated number of children needing ART based on WHO methods_median',
                                        column_region='WHO Region',
                                        column_country='Country',
                                        output_dir = 'stats_data/'):

    n_countries = len(np.unique(df[column_country]))
    n_regions = len(np.unique(df[column_region]))
    regions = np.unique(df[column_region])

    fig, ax = plt.subplots(1, 1, figsize=(40,30))
    plt.rcParams["figure.autolayout"] = True

    plotted_bars = 0

    i_color = 0

    for _region in range(n_regions):

        df_region = df.loc[(df[column_region] == regions[_region])]

        art_receiving = np.asarray(df_region[column_art_recieving], dtype=np.float128)
        art_needing = np.asarray(df_region[column_art_needing], dtype=np.float128)
        
        ax.bar(np.arange(len(art_needing)) + plotted_bars, art_needing, label=regions[_region] + ' - ART needing', color=colors[i_color])
        ax.bar(np.arange(len(art_receiving)) + plotted_bars, art_receiving, label=regions[_region] + ' - ART Receiving', color=colors[i_color+1])
        plotted_bars = plotted_bars + len(art_receiving)
        i_color = i_color + 2
    
    ax.set_yscale('log')
    ax.legend()

    ax.set_xticks(range(plotted_bars))
    ax.set_xticklabels(np.asarray(df[column_country]), rotation=90)

    create_directory(output_dir)
    create_directory(output_dir + 'ART/')

    plt.savefig(output_dir + 'ART/ART_children_regions.svg')
    plt.savefig(output_dir + 'ART/ART_children_regions.png')