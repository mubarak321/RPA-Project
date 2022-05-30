""" Fetching the user details from the config file """

import configparser
import pathlib


def get_app_details():

    """
    This function will fetch the user details from the config.ini file defined at the project root level.
    :return: TO_FGP, CRTPMUSR, user_type, default_level, menu_indicator, initial_program, WRKUSRPRF, pasia_path
    """

    # Config Object
    config = configparser.ConfigParser()

    # File Path
    file_path = pathlib.Path.cwd().joinpath('config.ini')

    # Reading the config.ini file
    config.read(file_path)
    pasia_path = config['App_Details']['pasia_path']

    return pasia_path