#!/bin/bash

if [[ $1 == 'train' ]]; then
    echo 'Run training...'
    python train.py \
        --cuda \
        --data ../data/smiles/ \
        --dataset smiles \
        --n_layer 3 \
        --d_model 256 \
        --n_head 4 \
        --d_head 64 \
        --d_inner 1024 \
        --dropout 0.0 \
        --dropatt 0.0 \
        --optim adam \
        --lr 0.00025 \
        --warmup_step 0 \
        --max_step 180000 \
        --tgt_len 125 \
        --mem_len 0 \
        --eval_tgt_len 125 \
        --ext_len 0 \
        --batch_size 100 \
        --log-interval 1800 \
        --eval-interval 18000 \
        --attn_type 0 \
        --max_eval_steps 18000 \
        ${@:2}
elif [[ $1 == 'eval' ]]; then
    echo 'Run evaluation...'
    python eval.py \
        --cuda \
        --data ../data/smiles/ \
        --dataset smiles \
        --tgt_len 125 \
        --mem_len 0 \
        --clamp_len 0 \
        --same_length \
        --split test \
        ${@:2}
else
    echo 'unknown argment 1'
fi
