import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

input_data = np.loadtxt("input_data.txt")
output_data = np.loadtxt("output_data.txt")

model = Sequential()
model.add(LSTM(256, input_shape=(4, 1), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(Dense(30000, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
model.fit(input_data, output_data, batch_size=20, epochs=5, validation_split=0.2)
model.save(filepath = 'oleg.h5')
