import time
import requests

def adjust_signal_timing():
    response = requests.get('http://127.0.0.1:5000/get_traffic')
    traffic_data = response.json()

    # Example logic to adjust signal timing
    for lane, count in traffic_data.items():
        if count > 50:
            print(f"Increase green light duration for {lane}")
        else:
            print(f"Decrease green light duration for {lane}")

if __name__ == '__main__':
    while True:
        adjust_signal_timing()
        time.sleep(60)  # Adjust signal timing every minute