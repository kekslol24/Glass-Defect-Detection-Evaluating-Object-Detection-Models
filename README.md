## Glass Defect Detection: Model Evaluation for Industrial Efficiency
This repository documents a Bachelor's project at ZHAW focused on evaluating advanced deep learning models for quality control in glass manufacturing.

The primary objective is to quantify the necessary trade-off between detection reliability and industrial efficiency for defect recognition.

Core Methodology
The project applies Transfer Learning to fine-tune two fundamentally different object detection architectures on a custom dataset of glass defects.

1. YOLOv11 Nano (Efficiency Baseline)
Architecture: A one-stage, anchor-free detector, chosen for its minimal memory footprint and highest potential CPU inference speed.


2. RF-DETR (Accuracy Baseline)
Architecture: A Transformer-based detector (Reduced Flops DETR). These models excel in global context understanding, often leading to high detection accuracy.

Evaluation Focus
The research centers on a direct, quantitative comparison of both models. Benchmarking involves measuring Accuracy (mAP) to establish which architecture delivers the most practical solution for real-time industrial requirements.

## Installation & Setup

It is recommended to use a virtual environment to manage dependencies. Please follow the steps below to set up your environment.

### 1. Create a Virtual Environment

Run the following command in the root directory of the project:

```bash
python -m venv venv
```

2. Activate the Environment
Windows:

```Bash

.\venv\Scripts\activate
```
macOS / Linux:

```Bash

source venv/bin/activate
```

3. Install Dependencies
Install the required Python packages using the provided requirements.txt:

```Bash

pip install -r requirements.txt
```