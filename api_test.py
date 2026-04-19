#!/usr/bin/env python3

# imports API from config file
from config import API_KEY
# this imports the requests module for making HTTP requests
import requests

# this defines the base URL for the ipstack api
ABSTRACT_API_URL = 'https://ip-intelligence.abstractapi.com/v1/?'

# this function takes the ip address and queries the ipstack api to retrieve the ip
def query_ipstack(ip_address):
    url = f"{ABSTRACT_API_URL}api_key={API_KEY}&ip_address={ip_address}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# the main section asks to input an ip address
if __name__ == '__main__':
    ip_address = input("Enter an IP address (or leave it blank to exit): ")

# this calls the  function with the user provided ip address    
    if ip_address:
        data = query_ip_intelligence(ip_address)

        if data:
            print(f"IP Address: {data['ip_address']}")
            print(f"City: {data['city']['name']}")
            print(f"Latitude: {data['location']['latitude']}")
            print(f"Longitude: {data['location']['longitude']}")
            # Add more data fields as needed
        else:
            print("Failed to obtain location data for the provided IP address.")
# if the ip_address was left blank, the program terminates
    else:
        print("Exiting the program.")
