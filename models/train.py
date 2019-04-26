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
from model import TBSentiment, SVMSentiment
import random
import _pickle as pickle

def read_csv(path):
    """Read from file and return the list of words.
    Args:
        filename (str): Path of file to read.
    Returns:
        :obj:`list` of :obj:`tuple`: List of lines, with each word on the line
            in a tuple.
    """
    with open(path, newline='') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        tuple_list = []
        for line in reader:
            tpl = line[0].replace("\n", "")
            tuple_list.append((tpl, line[1]))
        return tuple_list


if __name__ == "__main__":
    # parse command-line arguments
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--all', type=str, nargs='?')   # File for all data
    parser.add_argument('--train', type=str, nargs='?') # File for train data
    parser.add_argument('--test', type=str, nargs='?')  # File for test data
    parser.add_argument('--eval', type=str, nargs='?')  # File for eval data
    parser.add_argument('--model', type=str, nargs='?') # Previous model file
    parser.add_argument('--model-type', type=str, default="TBSentiment")
    parser.add_argument('--save', type=str, nargs='?')  # path to save model to
    # Model types
    parser.add_argument('--blob', action='store_true')
    parser.add_argument('--ngram', action='store_true')
    args = parser.parse_args()
    print(args)

    # plaintext file-reader
    file_reader = read_csv

    # load data from file
    train_s, test_s, eval_s = None, None, None
    if (args.train is not None):
        print("Reading train data.")
        train_s = file_reader(args.train)
        random.shuffle(train_s)
    if (args.test is not None):
        print("Reading test data.")
        test_s = file_reader(args.test)
        random.shuffle(test_s)
    if (args.eval is not None):
        print("Reading eval data.")
        eval_s = file_reader(args.eval)
        random.shuffle(eval_s)
    #print(train_s, test_s, eval_s)

    # Pick model type
    print("Using model TBSentiment.")
    model_type = SVMSentiment
    if (args.model_type == "TBSentiment"):
        model_type = TBSentiment
    elif (args.model_type == "SVMSentiment"):
        model_type == SVMSentiment

    # create new model or load existing model
    if args.model is not None:
        loader = open(args.model, 'rb')
        model_obj = pickle.load(loader)
    else:
        model_obj = model_type()

        # train model on train-data
        print("Training...")
        model_obj.train(train_s[:1000], eval=eval_s)

        print('done training')

        print('writing to file')
        file = open(args.save, 'wb')
        pickle.dump(model_obj, file)
    
    if (test_s is not None):
        accuracy = model_obj.test(test_s)
        print(accuracy)
