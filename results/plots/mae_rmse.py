resolutions = df["Resolution"].tolist()
x = list(range(len(resolutions)))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))

for index, metric in enumerate(["MAE", "RMSE"]):
    offsets = [
        position + (index - 0.5) * width
        for position in x
    ]

    bars = ax.bar(
        offsets,
        df[metric],
        width=width,
        label=metric,
    )

    ax.bar_label(
        bars,
        fmt="%.2f",
        padding=3,
        fontsize=9,
    )

ax.set_title(
    "Erros de estimativa de altura por resolução"
)
ax.set_xlabel("Resolução simulada")
ax.set_ylabel("Valor da métrica")
ax.set_xticks(x)
ax.set_xticklabels(resolutions)
ax.legend()

fig.tight_layout()

fig.savefig(
    "grafico_barras_erros_altura.png",
    dpi=300,
    bbox_inches="tight",
)

fig.savefig(
    "grafico_barras_erros_altura.pdf",
    bbox_inches="tight",
)

plt.close(fig)
