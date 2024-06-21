import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

input_data = np.loadtxt("extended_input_data.txt")
output_data = np.loadtxt("extended_output_data.txt")

model = Sequential()
model.add(LSTM(512, input_shape=(5, 1), return_sequences=True))
model.add(Dropout(0.1))
model.add(LSTM(256))
model.add(Dense(30000, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
model.fit(input_data, output_data, batch_size=32, epochs=3, validation_split=0.2)
model.save(filepath = 'summarization1.h5')

