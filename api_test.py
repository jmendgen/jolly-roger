#!/usr/bin/env python3
# tells the OS to run this file using Python.

# pulls the secret API key from a separate file called config.py. Keeping it separate is good practice to avoid accidentally exposing credentials.
from config import API_KEY

# loads the requests library, which simplifies making HTTP calls.
import requests

# stores the base URL of the Abstract API as a constant. The ? signals the start of query parameters that will be appended later.
ABSTRACT_API_URL = 'https://ip-intelligence.abstractapi.com/v1/?'

# this function takes the ip address and queries the ipstack api to retrieve the ip
def query_ip_intelligence(ip_address):
# builds the full request URL by combining the base URL, your API key, and the target IP. The & separates query parameters.
    url = f"{ABSTRACT_API_URL}api_key={API_KEY}&ip_address={ip_address}"
# sends an HTTP GET request to the API and stores the response. Wrapped in a try block to handle potential errors gracefully.
    try:       
        response = requests.get(url)
# checks the HTTP status code. If the API returns an error (e.g. 404, 500), this line raises an exception immediately rather than silently continuing with bad data.
        response.raise_for_status()
        data = response.json()
        return data
# parses the API's JSON response into a Python dictionary and returns it to the caller.
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
# catches any network or HTTP error (connection issues, timeouts, bad status codes) and prints it. Returns None so the rest of the program knows the request failed.

# the main section asks to input an ip address. The code inside only runs when this file is executed directly, not when it's imported by another script.
if __name__ == '__main__':
# prompt to type an IP address into the terminal and stores whatever is entered.       
    ip_address = input("Enter an IP address (or leave it blank to exit): ")
# calls the function above and stores the result.
    if ip_address:
        data = query_ip_intelligence(ip_address)
 # if the API returned valid data, it extracts and prints specific fields from the nested dictionary.     
        if data:
            print(f"IP Address: {data['ip_address']}")
            print(f"Postal Code: {data['location']['postal_code']}")
            print(f"Timezone: {data['timezone']['name']}")
            print(f"ISP: {data['asn']['name']}")
            print(f"City: {data['location']['city']}")
            print(f"Region: {data['location']['region']}")
            print(f"Country: {data['location']['country']}")
            print(f"Latitude: {data['location']['latitude']}")
            print(f"Longitude: {data['location']['longitude']}")
# if data is None (the request failed).      
        else:
            print("Failed to obtain location data for the provided IP address.")
# if the user pressed Enter without typing anything, the script exits cleanly.   
    else:
        print("Exiting the program.")
