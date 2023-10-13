#!/usr/bin/env python3

# imports API from config file
from config import API_KEY
# this imports the requests module for making HTTP requests
import requests

# this defines the base URL for the ipstack api
IPSTACK_API_URL = 'http://api.ipstack.com/'

# this function takes the ip address and queries the ipstack api to retrieve the ip
def query_ipstack(ip_address):
    url = f"{IPSTACK_API_URL}{ip_address}?access_key={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error: Request to IPStack API failed")
        return None

# the main section asks to input an ip address
if __name__ == '__main__':
    ip_address = input("Enter an IP address (or leave it blank to exit): ")

# this calls the  function with the user provided ip address    
    if ip_address:
        data = query_ipstack(ip_address)

        if data:
            print(f"IP Address: {data['ip']}")
            print(f"City: {data['city']}")
            print(f"Latitude: {data['latitude']}")
            print(f"Longitude: {data['longitude']}")
            # Add more data fields as needed
        else:
            print("Failed to obtain location data for the provided IP address.")
# if the ip_address was left blank, the program terminates
    else:
        print("Exiting the program.")
