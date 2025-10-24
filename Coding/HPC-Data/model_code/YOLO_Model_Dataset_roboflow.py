import os
from zipfile import ZipFile
import ultralytics
from ultralytics import YOLO

path = os.getcwd()
print(path)

# Create the directory if it doesn't exist
extract_dir = "data"
os.makedirs(extract_dir, exist_ok=True)

with ZipFile("Glass Defect Detection.v3i.yolov11.zip", "r") as data_set:
    data_set.extractall(extract_dir)


# Load a model
model = YOLO("yolo11n.pt")
model.to("cuda")

#DEFINE PATHS
DATA_YAML = "data/data.yaml"
MODEL_PATH = "yolo11n.pt"
data_set_dir = "data"


# Train the model
results = model.train(
    data = DATA_YAML,
    epochs = 100,
    batch = 16,
    lrf = 0.01,
    val = True
)