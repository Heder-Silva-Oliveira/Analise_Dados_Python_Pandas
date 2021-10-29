import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

df = pd.read_excel("AdventureWorks.xlsx")
print(df.head())
