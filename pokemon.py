import pandas as pd
pokemon = pd.read_csv("static/d1.csv")

def check_duplicates():
    pokemon.duplicated()

def remove_duplicates():
    pokemon.drop_duplicates(inplace = True)
remove_duplicates()
print(pokemon.to_string())
