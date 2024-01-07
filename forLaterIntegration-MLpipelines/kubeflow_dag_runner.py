import os
from absl import logging
from tfx.orchestration.kubeflow import kubeflow_dag_runner
from pipeline import create_pipeline
import time

suffix = int(time.time())


PIPELINE_NAME = f'grapes_leaf_prediction_{suffix}'
PIPELINE_ROOT = 'gs://grapes-tf-model/metadata'
DATA_PATH= 'gs://grapes-tf-model/data'
SERVING_DIR = 'gs://grapes-tf-model/models'
#temp = 'gs://grapes-tf-model/temp'


"""  
beam_pipeline_args = [ 
    "--runner=Dataflowrunner",
    "--experiments=shuffel_mode=auto",
    "--project=grapes-diseases-project",
    f"--temp_location={temp}",
    "--region=europe-west12",
    "disk_size_gb=50"
]
"""


def run():
    metadata_config = kubeflow_dag_runner.get_default_kubeflow_metadata_config()
    tfx_image = 'gcr.io/grapes-desease-project/predict_image'
    runner_config = kubeflow_dag_runner.KubeflowDagRunnerConfig(
        kubeflow_metadata_config = metadata_config,
        tfx_image = tfx_image
    )

    kubeflow_dag_runner.KubeflowDagRunnerConfig(config = runner_config).run(
        create_pipeline(
            pipeline_name=PIPELINE_NAME,
            pipeline_root=PIPELINE_ROOT,
            serving_dir=SERVING_DIR,
            data_path=DATA_PATH,
            #beam_pipeline_args=beam_pipeline_args
        )
    )


if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)
    run()

#remember that we need to create through IAM an access token. To do that we goo to:
    #IAM & Admin > Service Account > on 3 dots click on "manage keys" > Add key

#after setting the token, run the following command:
    # $tfx pipeline create --pipeline-path=kubeflow_dag_runner.py --endpoint=<uri of your kubeflow dashboard>

#then you can check on CS bucket /metadata your metadata

#remember to put your json credentials on .gitignore 