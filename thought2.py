import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

with open("TEXT.txt", encoding='utf-8') as f:
    s = f.read()

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
            'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю',
            'я', ' ', '.', ',', '"', '!', '?', '(', ')', '-']

symbols = list(s)

# Преобразовать все символы в нижний регистр
lowercase_symbols = [symbol.lower() for symbol in symbols]

transformation_text = []
transformation_text_numbers = []


def transformation():
    global transformation_text, transformation_text_numbers
    if lowercase_symbols[0] in alphabet:
        transformation_text.append(lowercase_symbols[0])
    for i in range(1, len(lowercase_symbols)):
        if lowercase_symbols[i] in alphabet and not (lowercase_symbols[i] == " " and lowercase_symbols[i - 1] == " "):
            transformation_text.append(lowercase_symbols[i])
    for i in range(0, len(transformation_text)):
        transformation_text_numbers.append(alphabet.index(transformation_text[i]))


transformation()
print(transformation_text_numbers)

input_data = []
output_data = []


def division_into_arrays():
    global input_data, output_data
    for i in range(0, len(transformation_text_numbers) - 10):
        input_data.append(transformation_text_numbers[i: i + 10])
        output_data.append(transformation_text_numbers[i + 10])


division_into_arrays()
input_data = np.array(input_data)
output_data = np.array(output_data)

model = Sequential()
model.add(LSTM(256, input_shape=(10, 1), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(Dense(len(alphabet), activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
model.fit(input_data, output_data, batch_size=20, epochs=5, validation_split=0.2)
model.save('my_model.h5')