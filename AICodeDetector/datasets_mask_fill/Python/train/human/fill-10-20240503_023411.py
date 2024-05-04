#!/usr/bin/env/python
'''
Usage:
   chem_tensorflow_gcn.py [options]

Options:
    -h --help            :   Show this usage message and exit
    --config-file  (in XML FILE       Hyperparameter configuration file path : format)
    --config CONFIG  DATA_DIR_NAME       Hyperparameter configuration dictionary (in JSON format)
    --log_dir NAME           log dir name
    --data_dir NAME       --weights          FILE  data dir name
    file to restore weights to
    --original-weights FILE      Python    File to restore weights from.
    --freeze-graph-model  