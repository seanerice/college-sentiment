import json
import csv
import argparse

def read_jsonfile(rmp_path, unigo_path):
    """Read the word list (json) from file and return the list of words.
    Args:
        filename (str): Path of file to read.
    Returns:
        :obj:`list` of :obj:`tuple`: List of lines, with each word on the line
            in a tuple.
    """

    rmp_comment_data = []
    unigo_comment_data = []

    with open(rmp_path, 'r') as rmp_file:
        rmp_data = json.load(rmp_file)
        unusable_comments = ['not specified', 'no comment', 'no comments']
        for k, v in rmp_data.items():
            check_comment = v['comment'].lower()
            if check_comment[-1] == '.':
                check_comment = check_comment[:-1]
            if check_comment not in unusable_comments and v['score'] != 3:
                polarity = ''
                if int(v['score']) < 3:
                    polarity = 'neg'
                else:
                    polarity = 'pos'
                comment_ = (v['comment'], polarity)
                rmp_comment_data.append(comment_)

    with open(unigo_path, 'r') as unigo_file:
        unigo_data = json.load(unigo_file)
        for k, v in unigo_data.items():
            for comment in v:
                if comment['rating'] != 3:
                    polarity = ''
                    if int(comment['rating']) < 3:
                        polarity = 'neg'
                    else:
                        polarity = 'pos'
                    stripped_body = comment['body'].strip()
                    comment_ = (stripped_body, polarity)
                    unigo_comment_data.append(comment_)

    return rmp_comment_data, unigo_comment_data

def preprocess_data(data, prefix):
    train_data_size = int(len(data) * 0.8)
    test_data_size = int(len(data) * 0.15)

    train_data = data[:train_data_size]
    test_data = data[train_data_size:train_data_size+test_data_size]
    eval_data = data[train_data_size+test_data_size:]

    print(prefix, len(train_data))
    print(prefix, len(test_data))
    print(prefix, len(eval_data))

    train_data_path = '../preprocess_data/' + prefix + '_train_data.csv'
    test_data_path = '../preprocess_data/' + prefix + '_test_data.csv'
    eval_data_path = '../preprocess_data/' + prefix + '_eval_data.csv'

    with open(train_data_path, 'w', newline='') as train_data_file:
        writer = csv.writer(train_data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for d in train_data:
            writer.writerow([d[0], d[1]])

    with open(test_data_path, 'w', newline='') as test_data_file:
        writer = csv.writer(test_data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for d in test_data:
            writer.writerow([d[0], d[1]])

    with open(eval_data_path, 'w', newline='') as eval_data_file:
        writer = csv.writer(eval_data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for d in eval_data:
            writer.writerow([d[0], d[1]])

def read_csv(pathname):
    """Textfile from csv file and return the list of words.

    Args:
        filename (str): Path of file to read.

    Returns:
        :obj:`list` of :obj:`tuple`: List of lines, with each word on the line
            in a tuple.
    """

    with open(pathname) as file:
        csv_reader = csv.DictReader(file)
        line_count = 0
        header = None
        rows = []
        for row in csv_reader:
            if (line_count == 0):
                header = row
            else:
                r_tpl = []
                for col_name in header:
                    r_tpl.append(row[col_name])
                rows.append(tuple(r_tpl))  
            line_count += 1
        return rows 

if __name__ == "__main__":
    # parse command-line arguments
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--all', type=str, nargs='?')   # File for all data
    parser.add_argument('--train', type=str, nargs='?') # File for train data
    parser.add_argument('--test', type=str, nargs='?')  # File for test data
    parser.add_argument('--eval', type=str, nargs='?')  # File for eval data
    # File type
    parser.add_argument('--f-type', type=str, nargs='?', default='json')
    # Model types
    parser.add_argument('--blob', action='store_true')
    parser.add_argument('--ngram', action='store_true')
    args = parser.parse_args()
    print(args)

    rmp_file = '../rmp_data.json'
    unigo_file = '../unigo_data.json'

    # all_s = []

    # num_train, num_test, num_eval = 0.6, 0.25, 0.15
    # train_s, test_s, eval_s = [], [], []

    rmp_data, unigo_data = read_jsonfile(rmp_file, unigo_file)

    preprocess_data(rmp_data, 'RMP')
    preprocess_data(unigo_data, 'UNIGO')
