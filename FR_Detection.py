# from keras.models import load_model
#
# model = load_model('facenet_keras.h5')-->embeddings are passed through this
# can I try running the one shot learning part through this?
# then it has to be trianed for at least all the group members


# print(model.inputs)
# print(model.outputs)
#
# #pip install mtcnn
# import mtcnn
# # print version
#print(mtcnn.__version__)
#
#
##the above statements are check statements
##run before executing this and the next two Python scripts

#face detection for the 5 celebrity faces dataset
from os import listdir
from os.path import isdir
from PIL import Image
from matplotlib import pyplot
from numpy import savez_compressed
from numpy import asarray
from mtcnn.mtcnn import MTCNN

#extract a single face from a given photo
def extract_face(filename, required_size=(160, 160)):
    image = Image.open(filename)
    image = image.convert('RGB') #would only need it if the images are in B/W
    pixels = asarray(image)
    detector = MTCNN()
    results = detector.detect_faces(pixels)
    x1, y1, width, height = results[0]['box']
    x1, y1 = abs(x1), abs(y1)#correction 
    x2, y2 = x1 + width, y1 + height
    face = pixels[y1:y2, x1:x2]
    image = Image.fromarray(face)
    image = image.resize(required_size)
    face_array = asarray(image)
    return face_array

#load images and extract faces for all images in a directory
def load_faces(directory):
    faces = list()
    #list of files
    for filename in listdir(directory):
        #get path
        path = directory + filename
        #get face
        face = extract_face(path)
        #store
        faces.append(face)
    return faces


#load a dataset that contains one subdir for each class
#each class has images
#the number of subdirs would be 2*(the numnber of people in class)-->train+test
def load_dataset(directory):
    X, y = list(), list()
    for subdir in listdir(directory):
        path = directory + subdir + '/'
        if not isdir(path):#skip if not a directory, error case, improbable
            #could happen if the registration process for new ID has begun, but not properly initialised, etc
            continue
        faces = load_faces(path)
        labels = [subdir for _ in range(len(faces))]
        print('>loaded %d examples for class: %s' % (len(faces), subdir))
        X.extend(faces)
        y.extend(labels)
    return asarray(X), asarray(y)


#load train dataset
trainX, trainy = load_dataset('5-celebrity-faces-dataset/train/')
print(trainX.shape, trainy.shape)
#load test dataset
testX, testy = load_dataset('5-celebrity-faces-dataset/val/')
#save arrays to one file in compressed format
savez_compressed('5-celebrity-faces-dataset.npz', trainX, trainy, testX, testy)
#check to see if this is the best format to store such a file
