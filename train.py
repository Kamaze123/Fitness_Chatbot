import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras import regularizers
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import SGD
from sklearn.model_selection import train_test_split
import pickle
from utils import load_intents, prepare_data, vectorize_text, encode_labels

#Loading data
data = load_intents("data/intents.json")
patterns, tags = prepare_data(data)

#Vectorize
X, vectorizer = vectorize_text(patterns)

#Encode labels
y, label_encoder = encode_labels(tags)
y = to_categorical(y)

#Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X.toarray(), y, test_size = 0.2, random_state=42
)

#Train Neural Network
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],),  kernel_regularizer=regularizers.l2(0.001)),
    Dropout(0.4),
    Dense(32, activation='relu',  kernel_regularizer=regularizers.l2(0.001)),
    Dropout(0.3),
    Dense(y.shape[1], activation='softmax')
])


sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

model.compile(
    optimizer=sgd,
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

#fitting training data into neural network
# history = model.fit(
#     X_train,
#     y_train,
#     epochs=120,
#     batch_size=8,
#     validation_data=(X_test, y_test),
#     verbose=1
# )

#Early stopping to prevent memorization
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

history = model.fit(X_train, y_train, epochs = 100, batch_size = 8, verbose = 1)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {accuracy:.2f}")