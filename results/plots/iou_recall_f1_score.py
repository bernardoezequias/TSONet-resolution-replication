width = 0.22

fig, ax = plt.subplots(figsize=(9, 5))

for index, metric in enumerate(
    ["IoU", "Recall", "F1-Score"]
):
    offsets = [
        position + (index - 1) * width
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
        fmt="%.3f",
        padding=3,
        fontsize=8,
    )

ax.set_title(
    "Qualidade da segmentação por resolução"
)
ax.set_xlabel("Resolução simulada")
ax.set_ylabel("Valor da métrica")
ax.set_xticks(x)
ax.set_xticklabels(resolutions)
ax.legend()

fig.tight_layout()

fig.savefig(
    "grafico_barras_segmentacao.png",
    dpi=300,
    bbox_inches="tight",
)

fig.savefig(
    "grafico_barras_segmentacao.pdf",
    bbox_inches="tight",
)

plt.close(fig)
