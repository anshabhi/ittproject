#developing a classifier for 5 celeb faces data
from random import choice#for final test
from numpy import load
from numpy import expand_dims
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
from matplotlib import pyplot

#load faces
data = load('5-celebrity-faces-dataset.npz')
testX_faces = data['arr_2']
#load face embeddings
data = load('5-celebrity-faces-embeddings.npz')
trainX, trainy, testX, testy = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
#normalize input vectors
in_encoder = Normalizer(norm='l2')
#check with the second, notebook at 5/10/19
trainX = in_encoder.transform(trainX)
testX = in_encoder.transform(testX)
#label encode targets
out_encoder = LabelEncoder()
out_encoder.fit(trainy)
trainy = out_encoder.transform(trainy)
testy = out_encoder.transform(testy)
#fit model
model = SVC(kernel='linear', probability=True)
model.fit(trainX, trainy)
#check notebook at 6/10/19

#test model on a random example from the test dataset
####IMPLEMENTING ON ATTENDANCE SYSTEM--add the corresponding new photo to file
####add new image each time to an empty folder, run through classifier, and then clear the folder again

selection = choice([i for i in range(testX.shape[0])])
random_face_pixels = testX_faces[selection]
random_face_emb = testX[selection]
random_face_class = testy[selection]
random_face_name = out_encoder.inverse_transform([random_face_class])
#prediction for the face
samples = expand_dims(random_face_emb, axis=0)
yhat_class = model.predict(samples)
yhat_prob = model.predict_proba(samples)
#get name
class_index = yhat_class[0]
class_probability = yhat_prob[0,class_index] * 100
predict_names = out_encoder.inverse_transform(yhat_class)
print('Predicted: %s (%.3f)' % (predict_names[0], class_probability))
print('Expected: %s' % random_face_name[0])
#plot for checking output
pyplot.imshow(random_face_pixels)
title = '%s (%.3f)' % (predict_names[0], class_probability)
pyplot.title(title)
pyplot.show()
