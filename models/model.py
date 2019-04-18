from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import _pickle as pickle

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
        return self.cl.accuracy(data)
