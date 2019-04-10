"""train.py

Use this script to train, test, and save a model.

Train and test sentiment analyzer on pre-processed data. Data should be stored
in a plaintext file, and each line should have a sentence ("...") and a
polarity (in ["pos", "neg", "neu"]).

usage: train.py [-h] [--all [ALL]] [--train [TRAIN]] [--test [TEST]]
                [--eval [EVAL]] [--f-type [F_TYPE]] [--blob] [--ngram]
"""

import argparse
import json
import csv
from model import TBSentiment


def read_textfile(pathname):
    """Textfile from file and return the list of words.
    Args:
        filename (str): Path of file to read.
    Returns:
        :obj:`list` of :obj:`tuple`: List of lines, with each word on the line
            in a tuple.
    """
    with open(pathname) as file:
        tuple_list = []
        for line in file:
            tpl = tuple(line.replace("\n", "").split())
            tuple_list.append(tpl)
        return tuple_list


if __name__ == "__main__":
    # parse command-line arguments
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--all', type=str, nargs='?')   # File for all data
    parser.add_argument('--train', type=str, nargs='?') # File for train data
    parser.add_argument('--test', type=str, nargs='?')  # File for test data
    parser.add_argument('--eval', type=str, nargs='?')  # File for eval data
    # Model types
    parser.add_argument('--blob', action='store_true')
    parser.add_argument('--ngram', action='store_true')
    args = parser.parse_args()

    # plaintext file-reader
    file_reader = read_textfile

    # load data from file
    train_s, test_s, eval_s = None, None, None
    if (args.train is not None):
        train_s = file_reader(args.train)
    if (args.test is not None):
        test_s = file_reader(args.train)
    if (args.eval is not None):
        eval_s = file_reader(args.eval)
    print(train_s, test_s, eval_s)

    # Pick model type
    model_type = TBSentiment

    # create new model or load existing model
    model_obj = model_type()

    # train model on train-data
    if (train_s is not None):
        model_obj.train(train_s, eval=eval_s, d_print=True)
    
    if (test_s is not None):
        succ, fail = model_obj.test(test_s)
        print(succ, fail)

    model_obj.save("")