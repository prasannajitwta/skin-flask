from flask import Flask
from flask_ngrok import run_with_ngrok
import pandas
import tensorflow as tf
import numpy as np
from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


import numpy as np

#model_name='classify.h5'
model=tf.keras.models.load_model('Flask-app/Rolex/classify.h5') 
def model_predict(imgPath,model):
    test_image1 = image.load_img(imgPath, target_size = (64, 64))
    test_image1 = image.img_to_array(test_image1)
    test_image1 = np.expand_dims(test_image1, axis = 0)
    result = model.predict(test_image1)
    if result[0][0] == 1:
        return('TYPE:-\n Actinic keratoses')
    elif result[0][1] == 1:
        return('TYPE:-\n Basal cell carcinoma')
    elif result[0][2] == 1:
        return('TYPE:-\n Benign keratosis-like lesions')
    elif result[0][3] == 1:
        return('TYPE:-\n Dermatofibroma')
    elif result[0][4] ==1 :
        return('TYPE:-\n Melanoma')
    elif result[0][5] == 1:
        return('TYPE:-\n Melanocytic nevi')
    elif result[0][6] == 1:
        return('TYPE:-\n Vascular lesions')
	
	

# a name for our web app
app=Flask(__name__)
run_with_ngrok(app) 

@app.route('/')
def index():
 return (render_template('index.html'))

@app.route('/predict',methods=['GET','POST'])
def upload():
	if request.method=='POST':
		f=request.files['file']

		basepath=os.path.dirname(__file__)
		file_path=os.path.join(basepath,'uploads',secure_filename(f.filename))
		f.save(file_path)

		preds=model_predict(file_path,model)
		result=preds
		return result
	return None


# run the web server
if __name__=='__main__':
	app.run()
