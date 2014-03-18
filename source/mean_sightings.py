#!/usr/bin/env python
"""
Module containing functions to calculate mean number of sightings of a given
animal in a given sightings csv file.

Functions
---------
get_sightings - get number of sightings of focus animal in data set

"""

#import pandas as pd
#import numpy as np

#def get_sightings(filename, focusanimal):

    # Load table
 #   tab = pd.read_csv(filename)

    # Find number of records and total count of animals seen
  #  isfocus = (tab['Animal'] == focusanimal.capitalize())
   # totalrecs = np.sum(isfocus)
   # if totalrecs == 0:
#	meancount = 0
 #   else:
#	meancount = np.mean(tab['Count'][isfocus])

    # Return num of records and animals seen
 #   return totalrecs, meancount

import sys

import numpy as np
import pandas as pd

def get_sightings(filename, focusanimal):
    """
    Get number of sightings of a focus animal in a data set.

    Parameters
    ----------
    filename : str
        Path to file containing sightings data
    focusanimal : str
        Name of focus animal (not case sensitive)

    Returns
    -------
    result : tuple
        Tuple containing total count of number of focus animal seen and mean
        count of individuals per sighting event.

    Notes
    -----
    Data file must be csv format with Animal and Count columns containing
    animal name and count of individuals per sighting, respectively.

    
    Returns the total number of sightings and the meand number of animals seen per sighting in a file
    filename and focusanimal should both be strings.
    This will return 0,0 if the animal is not present
    """
    # Load table
    tab = pd.read_csv(filename)

    # Standardize capitalization of focusanimal
    focusanimal = focusanimal.capitalize()

    # Loop through all records, countings recs and animals
    totalrecs = 0
    totalcount = 0
    for i, rec in tab.iterrows(): # Iterate through DataFrame rows
        if rec['Animal'] == focusanimal:
            totalrecs += 1
            totalcount += rec['Count']
    if totalrecs == 0:
	meancount = 0	
    else:    
	meancount = totalcount/float(totalrecs)

    # Return num of records and animals seen
    return totalrecs, meancount
if __name__ == '__main__': # condition is valid only when called from command line and not when imported in IPython
    filename = sys.argv[1]
    focusanimal = sys.argv[2]
    print get_sightings(filename, focusanimal)
