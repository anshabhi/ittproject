

#Product Functions

The software outside the core product provide the user with functionalities like:

	1. Storing their name and details in the database.
	2. Making their attendance in real time with timestamp.
  3. Recognising the faces with certain accuracy. 

In the core product, the user is provided with some basic functions like:
	
	1. Enrolling a student to the database.
	
	2. Removing a student from the database.

	3. If the current user is Admin, they can add or remove students from  any database. 
 
# User Classes and Characteristics


The Classes that we might find essential for this project are listed as follows(in descending priority):
	
    1. Recognition System:  This consists of the main python scripts that correctly classifies the images and maps them to their respective tuples in the DB and the camera which captures the image to be processed and cleans it of any background noise or unnecessary features.
    2. Website: All the features are accessible to the user via an interface of a website that is being implemented with the help of Javascript, HTML and CSS.

# Operating Environment

The provided software supports platform independency and can support any device capable of running on any web browser that has support for a webcam  and is able to run particular python scripts with database connectivity to MongoDB.

# Design and Implementation Constraints

Devices running a version of their OS below the versions specified might have trouble or not be able to run the specified software:-
	Windows: Windows 95 or higher
	MAC OS: OS 8.1 or higher
	Linux: Ubuntu Linux or Any Linux running Debian 

The Device running the software must have the minimum hardware requirements:
	RAM: 512 MB or higher
	GPU: Intel HD 430 or equivalent with 256MB or higher VRAM
	Directx: Not required
	Camera: Any functioning camera with a resolution > 4MP
	Storage: 24MB or higher
	
  #User Documentation

No specific documentation is required for the product as it is not proprietary and can be treated as an open source project with an MIT license. The website is quite straightforward and can be learned to operate without any prior knowledge as it contains all the instructions for operating the software.

# User Interfaces

The user interface is quite minimalistic and user friendly. The main menu for the software has options to add or remove student records from the database and a window that displays what the camera is capturing at the current time. The capture button when pressed would then display the picture taken by the camera and send it to the algorithm for further classification. The UI is pretty simple and easy to grasp, whereas there is not much focus on the UX as the website does not contain any subpages which can be optimised for user experience.

# Hardware Interfaces

Since the software is a FAS, the only hardware interface required is a working webcam that can take images in grayscale and color.
# Software Interfaces

As the user opens the website, they can clearly notice the options present on the index page there are options to register a new student in the database and to capture a new image for which the camera is activated and is displaying whatever information it is capturing. On pressing the capture button the camera sends the taken snapshot to the algorithm for further classification and processing.
 Also any crash dumps and memory dumps that might be created due to faulty execution or severe bugs will be handled by the software and the storage facility that is being used by the component device.
# Communications Interfaces

The software communicates to the user through the website to the user whereas for the backend we have implemented python scripts along with the usage of MongoDB which helps us store and classify our data. This can be useful as the changes made are highlighted everywhere in the DB and are in general real time.
   
The following have been used to provide an ease in reading this document:-

DB: Database
FAS: Facial Attendance System
Req: Requirements
RAM : Random Access Memory
CPU: Central Processing Unit
