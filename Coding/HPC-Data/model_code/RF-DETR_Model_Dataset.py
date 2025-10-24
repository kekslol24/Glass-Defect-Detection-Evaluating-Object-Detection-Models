import os
from zipfile import ZipFile
from rfdetr import RFDETRNano

model = RFDETRNano()


DATA_YAML = "data/config.yaml"
data_set_dir = "data"

path = os.getcwd()
print(path)

# Create the directory if it doesn't exist
extract_dir = "data"
os.makedirs(extract_dir, exist_ok=True)

with ZipFile("kaggle_glass_defect_COCO.zip", "r") as data_set:
    data_set.extractall(extract_dir)

model.train(dataset_dir=data_set_dir, epochs=100, batch_size=8, grad_accum_steps=2)

