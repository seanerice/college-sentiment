import argparse
import json


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


def read_jsonfile(pathname):
    """Read the word list (json) from file and return the list of words.
    Args:
        filename (str): Path of file to read.
    Returns:
        :obj:`list` of :obj:`tuple`: List of lines, with each word on the line
            in a tuple.
    """

    with open(pathname, 'r') as infile:
        data = json.load(infile)
        return data
    return None


if __name__ == "__main__":
    # parse command-line arguments
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--all', type=str, nargs='?')
    parser.add_argument('--train', type=str, nargs='?')
    parser.add_argument('--test', type=str, nargs='?')
    parser.add_argument('--eval', type=str, nargs='?')
    parser.add_argument('--blob', type=str, action='store_true')
    parser.add_argument('--ngram', type=str, action='store_true')
    parser.add_argument('')
    args = parser.parse_args()
    print(args)

    # load data from file
    train_s, test_s, eval_s = None, None, None
    if (args.train is not None):
        train_s = 


    # create new model or load existing model


    # train model on train-data


    # test model on test-data


    pass