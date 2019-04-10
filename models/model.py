from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

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
        self.data_parser
        pass

    def train(self, data):
        pass

    def test(self, data):
        pass


class TBSentiment(Model):
    """Wrapper around the TextBlob sentiment analyzer. Can train and test a
    using the standardized data format.
    
    Args:
        Model (): Initialize the model.
    """


    def __init__(self):
        self.data_parser
        pass

    def train(self, data):
        """Train the TextBlob object on custom data.
        
        Args:
            data (:obj:`list` of :obj:`tuple`): Take a list of tuples with
                format (comment, polarity in ["pos", "neg"]).
        """
        pass

    def test(self, data):
        """Test the TextBlob object on custom data.
        
        Args:
            data (:obj:`list` of :obj:`tuple`): Take a list of tuples with
                format (comment, polarity in ["pos", "neg"]).

        Returns:
            :obj:`tuple`: Return the successes and failures in a list (:obj:`list`, :obj:`list`)
        """
        pass