import requests
import time

URL = "http://35.237.73.96:5000"

test = {
    "Make": "NISSAN",
    "Model": "Sentra",
    "Model Year": 2026}

def measure_latency(end_point, data=None, method="POST"):
    times = []
    for i in range(50):
        start = time.time()
        
        if method == "POST":
            requests.post(f"{URL}{end_point}", json=data)
        else:
            requests.get(f"{URL}{end_point}")
        
        end = time.time()
        time_taken = 1000 * (end - start)
        times.append(time_taken)

    avg_latency = sum(times) / len(times)
    return avg_latency


fast_avg = measure_latency("/insert-fast", data=test, method="POST")
safe_avg = measure_latency("/insert-safe", data=test, method="POST")
print(f"Average /insert-fast latency: {fast_avg} ms")
print(f"Average /insert-safe latency: {safe_avg} ms")
