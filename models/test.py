import json
import _pickle as pickle
from model import TBSentiment
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="reddit data go here please")
    parser.add_argument('--data', type=str, nargs='?')
    parser.add_argument('--model', type=str, nargs='?')
    parser.add_argument('--save', type=str, nargs='?')
    args = parser.parse_args()

    if args.model is not None:
        print("loading model")
        loader = open(args.model, 'rb')
        model_obj = pickle.load(loader)

        if args.data is not None:
            overall_data = {}

            with open(args.data, 'r') as file:
                data = json.load(file)
                print('loaded json file')
                for k, _ in data.items():
                    print(k)
                    overall_data[k] = {}
                    
                    neg_c = []
                    pos_c = []
                    sum_conf = 0

                    # Classify and store comments in list
                    for comment in data[k]:
                        pol, con = model_obj.classify(comment)

                        sum_conf += con
                        
                        if pol == 'pos':
                            pos_c.append((pol, con, comment))
                        elif pol == 'neg':
                            neg_c.append((pol, con, comment))
                    
                    avg_conf = sum_conf / (len(pos_c) + len(neg_c))

                    # Sort list by confidence
                    pos_c = sorted(pos_c, key=lambda x: x[1])
                    neg_c = sorted(neg_c, key=lambda x: x[1])

                    sent_score = len(pos_c)/(len(pos_c) + len(neg_c))

                    overall_pol = ''
                    if 0.80 <= sent_score <= 1:
                        overall_pol = 'very positive'
                    elif 0.60 <= sent_score < 0.80:
                        overall_pol = 'positive'
                    elif 0.40 < sent_score < 0.60:
                        overall_pol = 'neutral'
                    elif 0.20 < sent_score <= 0.40:
                        overall_pol = 'negative'
                    else:
                        overall_pol = 'very negative'

                    print('overall sentiment:', overall_pol, sent_score)
                    print("average confidence:", avg_conf)

                    #print('most positive comments:', top_pos)
                    #print('most negative comments:', top_neg)

                    overall_data[k]['sentiment'] = overall_pol
                    overall_data[k]['confidence'] = avg_conf
                    overall_data[k]['top_pos'] = pos_c[:10]
                    overall_data[k]['top_neg'] = neg_c[:10]

                    with open(args.save, 'w') as file:
                        json.dump(overall_data, file)
    else:
        print('needs a model')
