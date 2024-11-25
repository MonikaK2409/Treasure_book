import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# API endpoint (replace with your actual endpoint)
API_URL = "http://localhost:5000/node"  # Change this URL to your Flask API's URL

# Function to simulate traffic (send requests to API)
def simulate_traffic():
    try:
        # Sending a POST request to create a node
        response = requests.post(API_URL, json={"type": "Treasure", "name": "Golden Crown"})
        
        # Print status code and the response to monitor
        print(f"Response: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        # Handle network or connection errors
        print(f"Error: {e}")

# Number of concurrent users (threads)
NUM_THREADS = 100

# Use ThreadPoolExecutor to manage threads efficiently
with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    # Submit tasks (simulate traffic)
    for _ in range(NUM_THREADS):
        executor.submit(simulate_traffic)
    
    # Optionally wait for all threads to complete (blocking)
    executor.shutdown(wait=True)

print("Traffic simulation completed.")
