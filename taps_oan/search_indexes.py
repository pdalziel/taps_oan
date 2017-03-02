from haystack import indexes
from taps_oan.models import Beer, Pub


class BeerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')

    def get_model(self):
        return Beer


class PubIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    #beers = indexes.MultiValueField(model_attr='beers')

    def get_model(self):
        return Pub
