#The script will make an HTTP GET request to api.ipstack.com and query the API key.
#For security purposes, I placed the API key into a separate file: config.py

#Run script:
./api_test.py

#script will prompt you for an IP address entry:
Enter an IP address (or leave it blank to exit) 192.124.249.29

#Address is confirmed and coordinates returned (also included a data field for City):
IP Address: 192.124.249.29
City: Menifee
Latitude: 33.65753173828125
Longitude: -117.1891098022461

#if address is left blank, program will exit:
Enter an IP address (or leave it blank to exit): 
Exiting the program.

#If address is invalid, no values are returned:
Enter an IP address: 192.168.1.254
IP Address: 192.168.1.254
City: None
Latitude: 0.0
Longitude: 0.0

#More data fields such as “country_name” or “isp” could be added and integrated into a larger project.

Cheers

Jorg
