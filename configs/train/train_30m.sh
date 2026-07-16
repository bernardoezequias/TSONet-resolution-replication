#!/usr/bin/env bash
set -e

python train.py \
  --name tsonet_30m \
  --data_dir /path/to/PHDataset \
  --result_dir ./results \
  --gpu_ids 0 \
  --model tsonet \
  --mode multi \
  --in_channels 7 \
  --out_channels 1 \
  --dim 32 \
  --hidden_dim 256 \
  --query_mode febr \
  --mem_levels 5 4 3 \
  --num_height_bins 64 \
  --h_min 0 \
  --h_max 145 \
  --use_task_exchange \
  --exchange_levels 1 \
  --batch_size 10 \
  --n_workers 4 \
  --n_epochs 30 \
  --lr 1e-4 \
  --lr_policy warmcos \
  --grad_clip 10 \
  --loss l1+tver+bce \
  --lambda_seg 1.0 \
  --fp_thresh 2.0 \
  --use_fp_weight \
  --inner_w 1.0 \
  --boundary_w 0.1 \
  --background_w 0.1 \
  --source_gsd 4.75 \
  --target_gsd 30
