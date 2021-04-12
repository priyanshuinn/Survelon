import os,urllib.request
import numpy as np
from django.conf import settings
from cv2 import cv2
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import datetime 
# import pyttsx3


class mask_detect(object):
	def __init__(self):
		self.video = cv2.VideoCapture(1)
		self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		self.model = load_model("mask.h5")
		self.i = 0

	def __del__(self):
		self.video.release()

	def get_frame(self):
		ret, frame = self.video.read()
		if frame is None:
			pass
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = self.faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(60, 60),flags=cv2.CASCADE_SCALE_IMAGE)
		faces_list=[]
		preds=[]
		for (x, y, w, h) in faces:
			face_frame = frame[y:y+h,x:x+w]
			face_frame = cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB)
			face_frame = cv2.resize(face_frame, (224, 224))
			face_frame = img_to_array(face_frame)
			face_frame = np.expand_dims(face_frame, axis=0)
			face_frame =  preprocess_input(face_frame)
			faces_list.append(face_frame)
			if len(faces_list)>0:
				print('This is the ', np.stack( faces_list, axis=0 )[0].shape)
				preds = self.model.predict(np.stack( faces_list, axis=0 )[0])
			for pred in preds:
				(mask, withoutMask) = pred
			label = "Mask" if mask > withoutMask else "No Mask" 
			if label == "No Mask":
				cv2.imwrite(os.getcwd()+'\\course\\mask_data\\{index}.jpg'.format(index=self.i),frame)
				self.i+=1
			color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
			label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

			cv2.putText(frame, label, (x, y- 10),
						cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
			cv2.rectangle(frame, (x, y), (x + w, y + h),color, 2)
		# frame_flip = cv2.flip(frame,1)
		jpeg = cv2.imencode('.jpg', frame)[1]
		return jpeg.tobytes()
		
	
