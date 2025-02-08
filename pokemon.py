import pandas as pd
pokemon = pd.read_csv("static/items.csv")

def data_info():
    pokemon.info(verbose = False)

def remove_duplicates():
    pokemon.drop_duplicates(inplace = True)

def change_amount(row, header, new_value):
    pokemon.loc[row, header] = new_value

def remove_item(item_name, amount):

def add_item(item_name, amount):

remove_duplicates()
print(pokemon.to_string())
