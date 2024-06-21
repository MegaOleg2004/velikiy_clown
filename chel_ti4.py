from tensorflow import keras
import pickle
import numpy as np

model_loaded = keras.models.load_model('ultraoleg.h5')
clown = np.array([12, 12, 555, 44, 233]).reshape(1, 5, 1)
prediction = model_loaded.predict(clown)
max_index = np.argmax(prediction)
print(prediction, max_index)
with open('ultraslovar.pkl', 'rb') as f:
    ultraslovar = pickle.load(f)
start = ['почему', 'ты', 'пришел', 'сюда', 'воин']
clown1 = []
for i in range(0, len(start)):
    clown1.append(ultraslovar.index(start[i]))
def func():
    global start
    for i in range(0, 15):
        clown = np.array([clown1]).reshape(1, 5, 1)
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
        clown2 = clown1.copy()
        clown1.clear()
        clown1.extend(clown2[1:5])
        clown1.append(max_index)
        print(clown1)
        print(start)

func()