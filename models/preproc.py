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


def write_textfile(filename, tpl_list):
    """Writes a list of tuples to file. Write each tuple to file
    separated by space. Each list item is newline separated.

    Args:
        filename (str): Path of file to write.
        tpl_list (:obj:`list` of :obj:`tuple`): List of tuples to write.
    """
    with open(filename, "w") as file:
        for tpl in tpl_list:
            line_str = ""
            for obj in tpl:
                line_str += " " + str(obj)
            file.write(line_str + "\n")


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

    # Read file from either plaintext file or json file
    file_reader = read_textfile
    if (args.f_type == 'json'):
        file_reader = read_jsonfile
    elif (args.f_type == 'csv'):
        file_reader = read_csv

    all_s = []

    num_train, num_test, num_eval = 0.6, 0.25, 0.15
    train_s, test_s, eval_s = [], [], []

