import pandas as pd

marken = pd.DataFrame(columns=[
    "entwertung",
    "besitz"
])

def add_marke(michnr : str, entwertung : str, besitz : int):
    marken.loc[michnr] = [entwertung, besitz]


# add_marke("1", "o", 2)
# add_marke("2", "o", 1)


# marken.to_pickle("marken.pkl")

def read_marken():
    print(pd.read_pickle("marken.pkl"))

read_marken()
