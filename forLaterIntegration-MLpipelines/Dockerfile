
FROM python:3.10.13-slim-bullseye

COPY requirements.txt .

RUN pip install  -r requirements.txt

RUN mkdir -p project

COPY . ./project

EXPOSE 8080

CMD [ "unicorn", "grapes-leage-disease.main:app", "--host", "0.0.0.0", "--port", "8080"]

#On our GCP VM instance after installing docker and biuld the yaml file through the comand: gcloud biulds summit --config cloudbiuld.yaml . 
#we run the image with the command: sudo docker run -p 8080 gcr.io/grapes-desease-project/predict_image
#after that on gcp through vm instance on external IP /predic you can access the FasApi app after that you can delete your instance.