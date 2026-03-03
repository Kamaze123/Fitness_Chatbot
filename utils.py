import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder


def load_intents(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def prepare_data(intents_data):
    patterns = []
    tags = []

    for intent in intents_data["intents"]:
        for pattern in intent["patterns"]:
            patterns.append(pattern.lower())
            tags.append(intent["tag"])

    return patterns, tags


def vectorize_text(patterns):
    vectorizer = TfidfVectorizer()    
    X = vectorizer.fit_transform(patterns)
    return X, vectorizer


def encode_labels(tags):
    encoder = LabelEncoder()
    y = encoder.fit_transform(tags)
    return y, encoder