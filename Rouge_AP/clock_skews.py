import time
import statistics
import json
import pywifi
import random
from pywifi import const

def get_connected_wifi_info():
    """Retrieve the currently connected Wi-Fi SSID, signal strength, and BSSID."""
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Use the first wireless interface

    iface.scan()  # Start scanning
    time.sleep(2)  # Wait for scan to complete
    scan_results = iface.scan_results()

    for network in scan_results:
        if iface.status() == const.IFACE_CONNECTED:
            return {
                "SSID": network.ssid,
                "Signal Strength": network.signal,
                "BSSID": network.bssid
            }
    return None

def measure_clock_skew(bssid, num_requests=5, delay_between_requests=0.5):
    """
    Calculate the average clock skew for the connected network.
    
    Parameters:
        bssid (str): The BSSID of the network to measure.
        num_requests (int): Number of requests to send for clock skew measurement.
        delay_between_requests (float): Time in seconds to wait between requests.
        
    Returns:
        float: The average clock skew for the given BSSID.
    """
    clock_skews = []

    for _ in range(num_requests):
        start_time = time.time()
        # Simulate sending a ping and receiving a response (placeholder)
        time.sleep(random.uniform(0.001, 0.005))  # Simulated network delay
        end_time = time.time()
        
        skew = end_time - start_time
        clock_skews.append(skew)
        time.sleep(delay_between_requests)

    average_skew = statistics.mean(clock_skews)
    print(f"Average clock skew for {bssid}: {average_skew:.6f} seconds")
    return average_skew

def store_data_in_json(data, filename='C:/_Vignesh_N/Saveetha_event/dashboard/flask-adminkit/Rouge_AP/wifi_info.json'):
    """Store the provided data in a JSON file."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    wifi_info = get_connected_wifi_info()
    
    if wifi_info:
        print(f"Connected to SSID: {wifi_info['SSID']}")
        print(f"Signal Strength: {wifi_info['Signal Strength']} dBm")
        print(f"BSSID: {wifi_info['BSSID']}")
        
        # Measure clock skew for the connected BSSID
        average_skew = measure_clock_skew(wifi_info['BSSID'])
        
        # Combine the data to store
        data_to_store = {
            "WiFi Info": wifi_info,
            "Clock Skew": average_skew
        }

        # Save the data to a JSON file
        store_data_in_json(data_to_store)
        print("Data saved to wifi_info.json.")
    else:
        print("No Wi-Fi connection found.")