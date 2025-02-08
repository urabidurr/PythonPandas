import pandas as pd
pokemon = pd.read_csv("static/items.csv")

def data_info():
    pokemon.info(verbose = False)

def change_amount(row, header, new_value):
    pokemon.loc[row, header] = new_value

def remove_item(item_name, amount):
    pokemon.drop(pokemon.loc[pokemon["Amount"]==item_name].index, inplace=True)

def add_item(item_name, cat, desc, amount):
    new_row = {"Item Name": item_name,"Category": cat, "Description": desc, "Amount": amount}
    pokemon.append(new_row, inplace = True)
#def sort_data():

def remove_duplicates():
    pokemon.drop_duplicates(inplace = True)

def check_amounts():
#Checks all of the values in the Amount column and if the value is higher than 999, set it to 999. If the value is negative, change the value  to 0.
    for x in pokemon.index:
        if pokemon.loc[x, "Amount"] > 999:
            change_amount(x, "Ammount", 999)
        elif pokemon.loc[x, "Amount"] <= 0:
            remove_item(pokemon["Amount"].loc[data.index[x]], "Amount")

#check_amounts()
#remove_duplicates()
print(pokemon.to_string())
