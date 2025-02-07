import pandas as pd
pokemon = pd.read_csv("static/d1.csv")

def remove_duplicates():
#Removes any rows that have the same Item Name as a previous row

def check_amounts():
#Checks all of the values in the Amount column and if the value is higher than 999, set it to 999. If the value is negative, change the value  to 0.

def remove_row():
#Removes a row if its value is 0.

def change_value(row, header, new_value):
    pokemon.loc[row, header] = new_values

def add_item(item_name, header, new_value):
    
remove_duplicates()
print(pokemon.to_string())
