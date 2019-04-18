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
                    
                    top_pos = []
                    top_neg = []
                    avg_pol = 0
                    i = 0
                
                    for comment in data[k]:
                        pol, con = model_obj.classify(comment)
                        
                        if pol == 'pos':
                            if len(top_pos) < 5:
                                top_pos.append((comment, con))
                            elif con > top_pos[0][1]:
                                del top_pos[0]
                                top_pos.append((comment, con))
                            top_pos = sorted(top_pos, key=lambda x: x[1])

                        if pol == 'neg':
                            con = -con
                            if len(top_neg) < 5:
                                top_neg.append((comment, con))
                            elif con < top_neg[-1][1]:
                                del top_neg[-1]
                                top_neg.append((comment, con))
                            top_neg = sorted(top_neg, key=lambda x: x[1])

                        avg_pol += con
                        if i > 0:
                            avg_pol /= 2
                        else:
                            i += 1

                    overall_pol = ''
                    if 0.75 <= avg_pol <= 1:
                        overall_pol = 'very positive'
                    elif 0.25 <= avg_pol < 0.75:
                        overall_pol = 'positive'
                    elif -0.25 < avg_pol < 0.25:
                        overall_pol = 'neutral'
                    elif -0.75 < avg_pol <= -0.25:
                        overall_pol = 'negative'
                    else:
                        overall_pol = 'very negative'

                    print('overall sentiment:', overall_pol, avg_pol)

                    #print('most positive comments:', top_pos)
                    #print('most negative comments:', top_neg)

                    overall_data[k]['sentiment'] = overall_pol
                    overall_data[k]['confidence'] = avg_pol
                    overall_data[k]['top_pos'] = top_pos
                    overall_data[k]['top_neg'] = top_neg

            with open(args.save, 'w+') as file:
                json.dump(overall_data, file)
    else:
        print('needs a model')
