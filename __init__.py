import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3,7,2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

pokemon = pd.read_csv("d1.csv")

print(pokemon.to_string())
