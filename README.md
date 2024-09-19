
# Traffic Signal Violation Detection System

A Computer Vision-based Traffic Signal Violation Detection System developed using **YOLOv3** and **Tkinter** for detecting violations from video footage. This system provides a user-friendly graphical interface for easy interaction.

## Table of Contents
- [Introduction](#introduction)
- [Objectives](#objectives)
- [System Overview](#system-overview)
- [Methodology](#methodology)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Libraries Used](#libraries-used)
- [Output](#output)
- [Contributors](#contributors)
- [License](#license)

## Introduction
----------------
The growing number of vehicles on roads has resulted in an increase in traffic violations, which in turn leads to accidents and property damage. To address this problem, this project aims to automate traffic signal violation detection in real-time. The system enforces traffic regulations, helping traffic authorities monitor roads more efficiently.

The system can:
- Detect traffic signal violations in real-time.
- Provide a simple and user-friendly graphical interface.
- Enable authorities to monitor traffic and take action swiftly.

## Objectives
------------
The goal of this project is to automate the detection of traffic signal violations, making it easier for authorities to monitor roads and take action against violators efficiently.

Key objectives:
1. **Real-time Detection**: Detect vehicles crossing traffic signals in real time.
2. **User-friendly Interface**: Provide an easy-to-use graphical interface to operate the system.
3. **Automated Monitoring**: Allow authorities to automate traffic monitoring and rule enforcement.

## System Overview
-----------------
![System Overview](https://user-images.githubusercontent.com/72919682/235343349-02b93190-fcc9-44ca-9f43-d3e81c6aa95f.png)

The system captures video footage, processes each frame using YOLOv3 object detection, and detects if any vehicle crosses a defined traffic signal line.

## Methodology
------------
### Vehicle Classification:
The system uses the YOLOv3 model to classify and detect vehicles in the video footage. Once a vehicle is detected, the system checks whether it crosses a predefined line, which serves as the traffic signal boundary.

### Steps:
1. **Open Video Footage**: The user can load video footage from the storage using the "Open" option in the File menu.
2. **Set Region of Interest (ROI)**: The user selects two points to define the traffic signal line.
3. **Detection Process**: The system detects vehicles that cross the signal line and highlights violations in real-time.
4. **Output**: Violations are logged, and an output video (`output.mp4`) is generated showing the violations.

## Requirements
---------------
Before running the system, ensure the following dependencies are installed:

- Python 3.7+
- Keras
- TensorFlow
- OpenCV
- Tkinter
- PIL (Pillow)

## Installation
---------------
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Traffic-Signal-Violation-Detection-System.git
    cd Traffic-Signal-Violation-Detection-System
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. (Optional) Download the YOLOv3 pre-trained weights and place them in the appropriate directory:
    ```bash
    wget https://pjreddie.com/media/files/yolov3.weights
    ```

4. Run the application:
    ```bash
    python Project-GUI.py
    ```

## Usage
--------
### Running the System:
1. Open the application by running `Project-GUI.py`.
2. Load a video file by selecting **File > Open**.
3. Define the **Region of Interest (ROI)** by selecting **Analyze > Region of Interest** and clicking on two points to draw the line.
4. The system will process the video and display detected violations. It will generate an output file (`output.mp4`) with the violations highlighted.

### Example:
```bash
python Project-GUI.py
```
Follow the GUI prompts to load video footage and detect violations.

## Libraries Used
----------------
*   **Tkinter**: Used for creating the graphical user interface.
*   **OpenCV**: Used for processing video footage and images.
*   **Keras**: Used for building and running the YOLOv3 object detection model.
*   **PIL (Pillow)**: For image handling in the GUI.
*   **NumPy**: For numerical computations.

## Output
--------
The system generates an output video (`output.mp4`) in the `output` folder, which highlights traffic violations detected in the input footage.

## Contributors
------------
*   **Your Name** - [@yourusername](https://github.com/alihadimoghadam)
*   **Other Contributors**

## License
-------
This project is licensed under the MIT License - see the LICENSE file for details.
