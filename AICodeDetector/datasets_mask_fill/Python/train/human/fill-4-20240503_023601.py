#!/usr/bin/env/python
"""
Usage:
    chem_tensorflow_sparse.py [options]

Options:
    -h --help                Show this screen.
 -d  --config-file FILE       Hyperparameter configuration file path (in JSON format).
    --config-dict DICTIONARY          Hyperparameter configuration dictionary (in JSON format).
    --log_dir DIR    DIR        DIR  Log dir name.
    --data_dir DIR   DIR  FILE    Data dir name.
    --restore FILE  File to restore weights to.
    --weights-file FILE  FILE  File to save weights in   .  DIR File to restore weights from.
    --freeze-graph-model