from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import requests



app = FastAPI()
#here apply tensorflowserving in order to enhance versioning of models
endpoint = "http://localhost:8501/v1/models/1:predict"


#MODEL= tf.keras.models.load_model("/home/alvaro/Documents/JupyterLab1/DeepLearningProject/modelsdeepl/1")
CLASS_NAMES= ['black rot',
 'esca (black measles)',
 'healthy',
 'leaf blight (isariopsis leaf spot)']

@app.get("/ping")
async def ping():
    return "Hello, I'm alive "

def read_file_as_tf(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))

    return image

@app.post("/predict")
async def predict(

    file: UploadFile = File(...)
):
    
    image = read_file_as_tf(await file.read())
    image_batch = np.expand_dims(image, 0)
    json_data = {
        "instances": image_batch.tolist()
    }
    response = requests.post(endpoint, json=json_data)
    prediction = np.array(response.json()["predictions"][0])
    
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


if __name__=="__main__":
    uvicorn.run(app,host = 'localhost', port=8000)




