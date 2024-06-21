from tensorflow import keras
import pickle
import numpy as np

model_loaded = keras.models.load_model('summarization1.h5')
with open('ultraslovar1.pkl', 'rb') as f:
    ultraslovar = pickle.load(f)
input_data = np.loadtxt('extended_input_data1.txt')
output_data = np.loadtxt('extended_output_data1.txt')
shape = input_data.shape
start = []
ok1 = input_data[0]
clown1 = []
for i in range(0, len(ok1)):
    clown1.append(ok1[i])
print(clown1)
def func():
    global start
    for i in range(0, 10):
        clown = np.array([clown1]).reshape(1, 90, 1)
        prediction = model_loaded.predict(clown)
        max_index = np.argmax(prediction)
        prediction[0][max_index] -= 0.5
        max_index1 = np.argmax(prediction)
        prediction[0][max_index1] -= 0.5
        max_index2 = np.argmax(prediction)
        start.append(ultraslovar[int(max_index)])
        print(ultraslovar[int(max_index)])
        print(ultraslovar[int(max_index1)])
        print(ultraslovar[int(max_index2)])
        clown1[80+i] = max_index
        print(clown1)
        print(start)

func()