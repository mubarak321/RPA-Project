import logging
import pathlib

file_path = pathlib.Path.cwd().joinpath('Logs', 'userid_creation_logs.log')
file_path = str(file_path)
def logs():
    logging.basicConfig(filename=file_path,
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S %p')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return logger