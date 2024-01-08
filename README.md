
# Project: Grapes Leaf Disease Classification

![banner](./banner/rdtron_a_minimalist_black_and_white_image_for_CNN_project_focus_670f9dce-1199-49bb-82bf-2f3e37ca4c00.png)

### some technologies used


<div style="display: inline_block"><en>

<a href="https://www.tensorflow.org/api_docs" target="_blank">
    <img align="center" alt="Alvaro-tf" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg">
</a>
<a href="https://fastapi.tiangolo.com/reference/" target="_blank">
    <img align="center" alt="Alvaro-fastapi" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original-wordmark.svg">
</a>
<a href="https://pandas.pydata.org/" target="_blank">
    <img align="center" alt="Alvaro-Pandas" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg">
</a>
<a href="https://jupyter.org/" target="_blank">
    <img align="center" alt="Alvaro-Jup" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg">
</a>
<a href="https://docs.docker.com/" target="_blank">
    <img align="center" alt="Alvaro-docker" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-plain.svg">
</a>
<a href="https://www.linux.org/" target="_blank">
    <img align="center" alt="Alvaro-Linux" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg">
</a>
<a href="https://cloud.google.com/docs/" target="_blank">
    <img align="center" alt="Alvaro-Cloud" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg">
</a>


</div>
  


## Overview
This Convolutional Neural Network (CNN) project, dedicated to the detection of grape leaf diseases through image classification, integrates a comprehensive set of technologies and tools like:

- TensorFlow and TensorFlow Serving
- FastAPI
- Uvicorn
- Wandb

  
The project includes a directory named "forLaterIntegration-MLpipelines." However, it is currently under development and is not considered in this overview due to its work-in-progress status and still pretty unorganized and unfinished.

An essential part of the project involves the utilization of the Weights & Biases platform for reporting. This tool proves highly beneficial, offering insightful visualizations and comprehensive reporting capabilities that enhance the overall project understanding.

It's important to note that the primary file governing the project is "grapes-tf-tfx-kfp.ipynb." This Jupyter Notebook serves as the main hub for executing and documenting the project's workflow, making it a crucial component of the overall implementation.

As an ongoing effort, the "forLaterIntegration-MLpipelines" directory is acknowledged as a work in progress, particularly focusing on the development of a Kubeflow ML pipeline for integration on the Google Cloud Platform (GCP). Despite its current state, this directory represents a crucial aspect of the project's evolution.


## Configuration
The model's architecture and training settings are configured using wandb. Key parameters include:

- Layers: Six convolutional layers with specified filters and activation functions.
- Pooling: Max pooling with a defined pool size.
- Dense Layers: Two dense layers with specified units and activation functions.
- Image Size: Input image size set to 256x256 pixels.
- Optimizer: Adam optimizer.
- Loss Function: Sparse categorical crossentropy.
- Metrics: Accuracy.
- Training: 36 epochs, batch size of 32, and specified steps for training and validation.
- Data Preparation
- Data augmentation is applied using ImageDataGenerator for the training, validation, and test datasets. Horizontal flipping and rotation are incorporated to enhance dataset diversity.

## Model Architecture
The CNN architecture follows the configuration specified in wandb. The layers include convolutional and max-pooling layers, followed by flattening and dense layers for classification.

## Training
The model is trained using the specified configuration and wandb callbacks for logging. Experiment results, including metrics and model checkpoints, are tracked for collaborative purposes.

# Project: Grapes Leaf Disease Classification

### some technologies used


<div style="display: inline_block"><en>

<a href="https://www.tensorflow.org/api_docs" target="_blank">
    <img align="center" alt="Alvaro-tf" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg">
</a>
<a href="https://fastapi.tiangolo.com/reference/" target="_blank">
    <img align="center" alt="Alvaro-fastapi" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original-wordmark.svg">
</a>
<a href="https://pandas.pydata.org/" target="_blank">
    <img align="center" alt="Alvaro-Pandas" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg">
</a>
<a href="https://jupyter.org/" target="_blank">
    <img align="center" alt="Alvaro-Jup" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg">
</a>
<a href="https://docs.docker.com/" target="_blank">
    <img align="center" alt="Alvaro-docker" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-plain.svg">
</a>
<a href="https://www.linux.org/" target="_blank">
    <img align="center" alt="Alvaro-Linux" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg">
</a>
<a href="https://cloud.google.com/docs/" target="_blank">
    <img align="center" alt="Alvaro-Cloud" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg">
</a>


</div>
  


## Overview
This Convolutional Neural Network (CNN) project, dedicated to the detection of grape leaf diseases through image classification, integrates a comprehensive set of technologies and tools like:

- TensorFlow and TensorFlow Serving
- FastAPI
- Uvicorn
- Wandb

  
The project includes a directory named "forLaterIntegration-MLpipelines." However, it is currently under development and is not considered in this overview due to its work-in-progress status and still pretty unorganized and unfinished.

An essential part of the project involves the utilization of the Weights & Biases platform for reporting. This tool proves highly beneficial, offering insightful visualizations and comprehensive reporting capabilities that enhance the overall project understanding.

It's important to note that the primary file governing the project is "grapes-tf-tfx-kfp.ipynb." This Jupyter Notebook serves as the main hub for executing and documenting the project's workflow, making it a crucial component of the overall implementation.

As an ongoing effort, the "forLaterIntegration-MLpipelines" directory is acknowledged as a work in progress, particularly focusing on the development of a Kubeflow ML pipeline for integration on the Google Cloud Platform (GCP). Despite its current state, this directory represents a crucial aspect of the project's evolution.


## Configuration
The model's architecture and training settings are configured using wandb. Key parameters include:

- Layers: Six convolutional layers with specified filters and activation functions.
- Pooling: Max pooling with a defined pool size.
- Dense Layers: Two dense layers with specified units and activation functions.
- Image Size: Input image size set to 256x256 pixels.
- Optimizer: Adam optimizer.
- Loss Function: Sparse categorical crossentropy.
- Metrics: Accuracy.
- Training: 36 epochs, batch size of 32, and specified steps for training and validation.
- Data Preparation
- Data augmentation is applied using ImageDataGenerator for the training, validation, and test datasets. Horizontal flipping and rotation are incorporated to enhance dataset diversity.

## Model Architecture
The CNN architecture follows the configuration specified in wandb. The layers include convolutional and max-pooling layers, followed by flattening and dense layers for classification.

## Training
The model is trained using the specified configuration and wandb callbacks for logging. Experiment results, including metrics and model checkpoints, are tracked for collaborative purposes.