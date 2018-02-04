import requests

print("This line will be printed.")
# https://developers.google.com/maps/documentation/distance-matrix/start
# https://developers.google.com/maps/documentation/distance-matrix/get-api-key
# my API key is AIzaSyBC-G5dFJp8O6g6r0dqK_oXOEG4zBv0GHI
# http://docs.python-requests.org/en/latest/user/install/ dunno where the library is physically installed though

url="https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=Washington,DC&destinations=New+York+City,NY&key=AIzaSyBC-G5dFJp8O6g6r0dqK_oXOEG4zBv0GHI"

# print(url)

response=requests.get(url,verify=False) # currently doing an unverified request
print(response.json())