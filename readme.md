set GOOGLE_APPLICATION_CREDENTIALS = path to json


dvc setup commands

dvc init 
dvc add artifacts/raw
dvc add artifacts/processed
dvc add artifacts/weights
dvc add artifacts/model_checkpoint


GCP

dvc remote add -d myremote gs://bucket-name/ 

dvc push

