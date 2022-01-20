# -*- coding: utf-8 -*-
import os
from matplotlib import pyplot as plt


def clear_output():
    # TODO: Incite exception capture mechanism
    flag = input("(Press Enter key to move forward.)")
    if flag == '':
        os.system('clear')


def save_fig(fig_name, image_path, tight_layout=True):
    """Run to save pictures

    :param image_path: where to store the image
    :param fig_name: Picture Name
    """
    path = os.path.join(image_path, fig_name + ".png")
    print(f"Save figure '{fig_name}' in {image_path}.")
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format='png', dpi=300)


def save_data(df, df_name, path):
    """make a sheet to store the result

    :param df: dataset
    :param df_name: the name of the data sheet
    :param path: the path to store the data sheet
    """
    try:
        # drop the index in case that the dimensions change
        # store the result in the directory "results"
        df.to_excel(os.path.join(path, "{}.xlsx".format(df_name)), index=False)
        print(f"Successfully store the results of {df_name} in '{df_name}.xlsx' in {path}.")
    except ModuleNotFoundError:
        print("** Please download openpyxl by pip3 **")
        print("** The data will be stored in .csv file **")
        # store the result in the directory "results"
        df.to_csv(os.path.join(path, "{}.csv".format(df_name)))
        print(f"Successfully store the results of {df_name} in '{df_name}.csv' in {path}.")