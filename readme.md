#The script will make an HTTP GET request to api.ipstack.com and query the API key.
#For security purposes, I placed the API key into a separate file: config.py

#Run script:
./api_test.py

#script will prompt you for an IP address entry:
Enter an IP address (or leave it blank to exit) 81.154.70.150

#Address is confirmed and coordinates returned (also included a data field for City):
IP Address: 81.154.70.150
Postal Code: NP9 4UR
Timezone: Europe/London
ISP: British Telecommunications PLC
City: Newport
Region: Wales
Country: United Kingdom
Latitude: 52.490132
Longitude: -1.366964

#if address is left blank, program will exit:
Enter an IP address (or leave it blank to exit): 
Exiting the program.

#If address is invalid, no values are returned:

#More data fields such as “country_name” or “isp” could be added and integrated into a larger project.

Cheers

Jorg
