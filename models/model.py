from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import _pickle as pickle
from sklearn.svm import SVC
import numpy as np
from scipy.sparse import csc_matrix


def get_tokens(data):
    tokens = {}
    # Accumulate all tokens
    t_itr = 0
    for com in data:
        for word in com.split(" "):
            if word not in tokens:
                tokens[word] = t_itr
                t_itr += 1
    return tokens

def vectorize(data, tokens):
    # Vectorize comments
    vecs = np.zeros((len(data), len(tokens)))
    for i, com in enumerate(data):
        for word in com.split(" "):
            if word in tokens:
                j = tokens[word]
                vecs[i, j] += 1

    return vecs

class DataParser:
    def __init__(self):
        pass

    def parse(self, data):
        pass

class JsonParser(DataParser):
    def __init__(self):
        pass
    
    def parse(self, data):
        pass

class Model:
    def __init__(self):
        pass

    def classify(self, sentence):
        pass

    def train(self, data, eval=None, d_print=False):
        pass

    def test(self, data):
        pass

    def save(self, filename):
        pass

    def load(self, filename):
        pass



class TBSentiment(Model):
    """Wrapper around the TextBlob sentiment analyzer. Can train and test a
    using the standardized data format.
    
    Args:
        Model (): Initialize the model.
    """

    def __init__(self):
        self.cl = NaiveBayesClassifier([])

    def classify(self, comment):
        prob_dist = self.cl.prob_classify(comment)
        pol_pred = prob_dist.max()
        confidence = prob_dist.prob(pol_pred)
        return pol_pred, confidence

    def train(self, data, eval=None, d_print=False):
        """Train the TextBlob object on custom data.
        
        Args:
            data (:obj:`list` of :obj:`tuple`): Take a list of tuples with
                format (comment, polarity in ["pos", "neg"]).
        """

        self.cl.update(data)

    def test(self, data):
        """Test the TextBlob object on custom data.
        
        Args:
            data (:obj:`list` of :obj:`tuple`): Take a list of tuples with
                format (comment, polarity in ["pos", "neg"]).

        Returns:
            :obj:`tuple`: Return the successes and failures in a list (:obj:`list`, :obj:`list`)
        """
        return 


class SVMSentiment(Model):
    """Wrapper around the SciKit-Learn SVM module. Can train and test a
    using the standardized data format.
    
    Args:
        Model (): Initialize the model.
    """

    def __init__(self):
        self.svm = SVC(kernel='poly', verbose=1, gamma='scale', degree=2)
        self.tokens = {}

    def classify(self, comment):
        vec = vectorize([comment], self.tokens)
        y_pred = self.svm.predict(vec)
        return y_pred[0]

    def train(self, data, eval=None, d_print=False):
        """Train the TextBlob object on custom data.
        
        Args:
            data (:obj:`list` of :obj:`tuple`): Take a list of tuples with
                format (comment, polarity in ["pos", "neg"]).
        """

        # Break up data into X and Y
        comments = [com for com, pol in data]
        labels = [pol for com, pol in data]

        # Create token lookup table. 
        # Used to get vector-index of token (word).
        self.tokens = get_tokens(comments)

        # Vectorize the comments
        # X_vec[comment_index][token_index]
        X_vec = vectorize(comments, self.tokens)

        # Feed the vectors as our training data
        self.svm.fit(X_vec, labels)

    def test(self, data):
        """Test the TextBlob object on custom data.
        
        Args:
            data (:obj:`list` of :obj:`tuple`): Take a list of tuples with
                format (comment, polarity in ["pos", "neg"]).

        Returns:
            :obj:`tuple`: Return the successes and failures in a list (:obj:`list`, :obj:`list`)
        """
        correct = 0
        for com, pol in data:
            pred = self.classify(com)
            if (pred == pol):
                correct += 1

        return float(correct/len(data))


if __name__ == "__main__":
    train = [("Hey my name is jeff", "pos"),
             ("I don't like it", "neg"),
             ("Hey don't speak to me like that it isn't nice to do that", "neg")]
    
    svm = SVMSentiment()
    svm.train(train)
    print(svm.classify("Hey my name is jeff"))