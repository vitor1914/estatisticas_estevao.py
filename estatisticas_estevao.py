import matplotlib.pyplot as plt

# Estatísticas do Estêvão na temporada
estatisticas = {
    "Minutos jogados": 1542,
    "Gols": 12,
    "Assistências": 8,
    "Finalizações": 45,
    "Passes decisivos": 35,
    "Dribles certos": 60,
    "Faltas sofridas": 50
}

# Exibir estatísticas
print("=== Estatísticas do Estêvão ===")
for chave, valor in estatisticas.items():
    print(f"{chave}: {valor}")

# Gerar gráfico de barras
plt.figure(figsize=(10, 5))
plt.bar(estatisticas.keys(), estatisticas.values(), color="blue")
plt.xlabel("Categorias")
plt.ylabel("Quantidade")
plt.title("Estatísticas do Estêvão na Temporada")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Salvar e exibir gráfico
plt.tight_layout()
plt.savefig("estatisticas_estevao.png")
plt.show()
