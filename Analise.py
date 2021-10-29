import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")



df = pd.read_excel("AdventureWorks.xlsx" )
df["Valor Venda"].sum()
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])
df["lucro"] = df["Valor Venda"] - df["custo"]

df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
print(plt.xlabel("Total"))
print(plt.ylabel("produto"))

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro anual")
plt.xlabel("Ano")
plt.ylabel("Receita");
