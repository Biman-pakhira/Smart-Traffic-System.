# Smart Traffic System

This project aims to create a smart traffic system using IoT sensors, AI models, and a web dashboard to monitor and manage traffic data.

## Components

1. **Backend**: Flask application to manage traffic data.
2. **IoT**: Script to send traffic data from sensors.
3. **Web Dashboard**: HTML, CSS, and JavaScript to display live traffic data.
4. **AI Model**: YOLOv5 model to detect vehicles in a video.

## Setup

1. Install dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```

2. Run the Flask application:
    ```bash
    python backend/app.py
    ```

3. Open [index.html](http://_vscodecontentref_/9) in a browser to view live traffic data.

4. Run the IoT sensor script:
    ```bash
    python iot/sensor_data.py
    ```

5. Run the traffic signal adjustment script:
    ```bash
    python backend/traffic_signal.py
    ```

6. Run the vehicle detection script:
    ```bash
    python ai_model/vehicle_detection.py
    ```