import pickle
import matplotlib.pyplot as plt

with open('data/players_age.pkl', 'rb') as file:
    players_age = pickle.load(file)

ages = players_age.values()
x = [i for i in range(min(ages), max(ages)+1)]
y =
