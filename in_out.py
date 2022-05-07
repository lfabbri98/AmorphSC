import glob
import pandas as pd

def import_char(prefix_file):
    """
    Function that imports all file in a folder with a specific prefix, recorded
    by Keysight SMU. It also print on console the order of imported files.

    Parameters
    ----------
    prefix_file : string
        Prefix of files that have to be imported

    Returns
    -------
    char : float
        Array of imported files

    """
    
    files_char = glob.glob(prefix_file)
    char = []
    for j in files_char:
        csv = pd.read_csv(j, sep="\t", header=1, names=["VG", "IG", "tG", "VD", "ID", "tD"])
        char.append(csv)
        print(j)
    return char