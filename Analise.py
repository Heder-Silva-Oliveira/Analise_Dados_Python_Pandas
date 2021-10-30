import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")



df = pd.read_excel("AdventureWorks.xlsx" )
df["Valor Venda"].sum()
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])
df["lucro"] = df["Valor Venda"] - df["custo"]
df_2008 = df[df["Data Venda"].dt.year == 2008]

df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("produto")
plt.show()

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro anual")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()

df_2008.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')
plt.show()
