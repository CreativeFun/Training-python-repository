import matplotlib.pyplot as plt
import pandas as pd
import missingno as msno
import seaborn as sns #seaborn użyty do rysowania wykresów
from matplotlib.ticker import PercentFormatter

"""
to_do zrobić model predykcyjny -> regresja logistyczna zobaczyć czy na pdostawie wprowadzonych(nowych) parametrów woda będzie pitna

drzewo decyzyjne 
"""

#Wczytanie pliku
df = pd.read_csv("water_potability.csv")
df = df.rename(columns={'ph':'pH'})

#Przedstawienie jak wygladaja dane w pliku
print(df.head())

#sprawdzenie czy w danych wystepuja puste pola  i ich liczba dla poszczególnej kolumny

print(df.isnull().sum())

#przedstawienie rozkladu danych z pustymi polami:
msno.matrix(df)
plt.show()
plt.legend()
#odrzucenie wierszy, w których wystepują luki
df = df.dropna()

#przedstawienie wartosci matematycznych [średnia,min, max, suma.....]
print(df.describe())

sns.countplot(y='Potability',data=df).set(title='Potability Plot')


plt.show()

sns.set(rc={'figure.figsize':(12,5)})
sns.histplot(df[df["Potability"] == 0]['Trihalomethanes'],  kde=False, label="Potable").set(title='Number of Trihalomethanes Plot')
sns.histplot(df[df["Potability"] == 1]['Trihalomethanes'],  kde=False, label="Not potable")
plt.legend()
# fig = plt.subplots(ncols=3)
plt.show()

plt.legend()


list1 = ['pH', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
       'Organic_carbon', 'Trihalomethanes', 'Turbidity', 'Potability']

corr = df.corr().sort_values(ascending=False, key=lambda x: abs(x), by="Potability")
sns.heatmap(corr, cmap="PRGn")


plt.show()

for col in df.drop("Potability", axis=1).columns:
    plt.figure(figsize=(12,8))
    sns.histplot(df[col])
    plt.title(f"{col}", size=15)
    plt.show()