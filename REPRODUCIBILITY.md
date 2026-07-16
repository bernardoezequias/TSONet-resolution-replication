# Reproducibility Notes

Each spatial resolution condition was trained once:

- 4.75 m/pixel
- 10 m/pixel
- 15 m/pixel
- 30 m/pixel

The same dataset split was used for all conditions.

The reported results are single-run results. Therefore, they do not capture
training variability due to random initialization, batch ordering, or GPU
non-determinism. For stronger statistical conclusions, each condition should
be repeated with multiple random seeds.

The main code modification is provided as:

```text
patches/resolution_degradation.patch
