from bertopic import BERTopic
from sklearn.cluster import KMeans
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import silhouette_score
import numpy as np

class BERTopicWrapper(BaseEstimator, TransformerMixin):
    def __init__(self, n_clusters=15, top_n_words=4, stop_words=None):
        self.n_clusters = n_clusters
        self.top_n_words = top_n_words
        self.stop_words = stop_words if stop_words is not None else []
        self.model = None
    
    def fit(self, X, y=None):
        vectorizer_model = CountVectorizer(stop_words=list(self.stop_words))
        cluster_model = KMeans(n_clusters=self.n_clusters)
        self.model = BERTopic(language="catalan", vectorizer_model=vectorizer_model, hdbscan_model=cluster_model, top_n_words=self.top_n_words)
        self.model.fit(X)
        return self

    def transform(self, X):
        return self.model.transform(X)
    
    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X)
    
    def get_params(self, deep=True):
        return {
            'n_clusters': self.n_clusters,
            'top_n_words': self.top_n_words,
            'stop_words': self.stop_words
        }

    def set_params(self, **params):
        for param, value in params.items():
            setattr(self, param, value)
        return self
    
    def get_topic_info(self):
        return self.model.get_topic_info()
    
    def get_document_info(self, documents):
        return self.model.get_document_info(documents)


def silhouette_scorer(estimator, X):
    topics, probs = estimator.transform(X)
    labels = estimator.hdbscan_model.labels_
    valid_points = labels != -1
    if np.sum(valid_points) > 1:
        score = silhouette_score(X[valid_points], labels[valid_points])
        return score
    else:
        return -1
