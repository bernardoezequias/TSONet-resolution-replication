# Dataset

This repository does not include the [PHDataset](https://huggingface.co/datasets/Yanjiao-WHU/PHDataset) files.

Download the dataset from the official source provided by the original
TSONet/PHDataset authors and keep the original train/validation/test splits.

Expected usage:

```bash
bash configs/train/train_10m.sh /path/to/PHDataset
bash configs/test/test_10m.sh /path/to/PHDataset
