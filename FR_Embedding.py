#calculate a face embedding for each face in the dataset using facenet
#this eliminates the need to retrain the model with the entire 3*xx pixel array images

from numpy import load
from numpy import expand_dims
from numpy import asarray
from numpy import savez_compressed
from keras.models import load_model

#get the face embedding for one face
def get_embedding(model, face_pixels):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    #make face into one sample
    samples = expand_dims(face_pixels, axis=0)
    #make a prediction to get embedding
    yhat = model.predict(samples)
    return yhat[0]

#load the face dataset
#this can only work with detected faces-->bounding box is important
data = load('5-celebrity-faces-dataset.npz')
trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
print('Loaded: ', trainX.shape, trainy.shape, testX.shape, testy.shape)#test statements
#loading facenet
model = load_model('facenet_keras.h5')
print('Loaded Model')
#convert each face in the train to an embedding
newTrainX = list()
for face_pixels in trainX:
    embedding = get_embedding(model, face_pixels)
    newTrainX.append(embedding)
newTrainX = asarray(newTrainX)
print(newTrainX.shape)
#convert each face in the test to an embedding
newTestX = list()
for face_pixels in testX:
    embedding = get_embedding(model, face_pixels)
    newTestX.append(embedding)
newTestX = asarray(newTestX)
print(newTestX.shape)
savez_compressed('5-celebrity-faces-embeddings.npz', newTrainX, trainy, newTestX, testy)
#now this compressed file needs to be passed onto the third program to classify
#only embeddings are classified
#triplet loss not taken into consideration-->difficult to implement
#check Notebook from 15/09/2019
