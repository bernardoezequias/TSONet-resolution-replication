from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


files = {
    "4.75 m": Path("results/raw_logs/test_metrics_log_original.txt"),
    "10 m": Path("results/raw_logs/test_metrics_log_10m.txt"),
    "15 m": Path("results/raw_logs/test_metrics_log_15m.txt"),
    "30 m": Path("results/raw_logs/test_metrics_log_30m.txt"),
}


def parse_total_metrics(path: Path) -> dict:
    lines = path.read_text(
        encoding="utf-8",
        errors="ignore",
    ).splitlines()

    header_index = None
    total_index = None

    for index, line in enumerate(lines):
        if (
            "MRE" in line
            and "MAE" in line
            and "RMSE" in line
            and "F1-Score" in line
        ):
            header_index = index

        if "Total Metrics:" in line:
            total_index = index
            break

    if header_index is None or total_index is None:
        raise ValueError(
            f"Não foi possível ler as métricas de {path}"
        )

    headers = [
        item.strip()
        for item in lines[header_index].split("|")
    ]

    values = [
        item.strip()
        for item in lines[total_index + 1].split("|")
    ]

    metrics = {}

    for header, value in zip(headers, values):
        if not header or not value or header == "Patch":
            continue

        try:
            metrics[header] = float(value)
        except ValueError:
            metrics[header] = value

    return metrics


rows = []

for resolution, path in files.items():
    metrics = parse_total_metrics(path)
    metrics["Resolution"] = resolution
    rows.append(metrics)

df = pd.DataFrame(rows)

columns = [
    "Resolution",
    "MRE",
    "MAE",
    "RMSE",
    "RMSE_all",
    "R2",
    "Precision",
    "IoU",
    "Recall",
    "F1-Score",
]

df = df[
    [column for column in columns if column in df.columns]
]

df.to_csv(
    "resultados_resolucoes_barras.csv",
    index=False,
)
