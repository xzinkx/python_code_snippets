# Using the tabulate library
# found on https://www.statology.org/create-table-in-python/

from tabulate import tabulate

#create data
data = [["Mavs", 99], 
        ["Suns", 91], 
        ["Spurs", 94], 
        ["Nets", 88]]


#define header names
col_names = ["Team", "Points"]


#display table
print(tabulate(data))
