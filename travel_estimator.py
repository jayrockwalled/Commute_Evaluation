import requests
import json
print("This line will be printed.")
# https://developers.google.com/maps/documentation/distance-matrix/start
# https://developers.google.com/maps/documentation/distance-matrix/get-api-key
# my API key is AIzaSyBC-G5dFJp8O6g6r0dqK_oXOEG4zBv0GHI
# http://docs.python-requests.org/en/latest/user/install/ dunno where the library is physically installed though

url="https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=Washington,DC&destinations=New+York+City,NY&key=AIzaSyBC-G5dFJp8O6g6r0dqK_oXOEG4zBv0GHI"

# print(url)

# InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
# http://docs.python-requests.org/en/master/user/advanced/
response=requests.get(url,verify=False) # currently doing an unverified request
print(response)
print("Here we print response.json().")
print(response.json())
print("\n")
#print("Here we print response.headers.")
#print(response.headers)
#print("\n")
#print("Here we print response.headers['Content-Type'].")
#print(response.headers['Content-Type'])
#print("\n")

# https://stackoverflow.com/questions/42899389/typeerror-the-json-object-must-be-str-not-dict
print("Here we print json.dumps(data['rows'])")
data=response.json()
""" 
Here's an example of the response.
{'destination_addresses': ['New York, NY, USA'], 'status': 'OK', 'origin_addresses': ['Washington, DC, USA'], 
'rows': [{'elements': [{'duration': {'value': 13816, 'text': '3 hours 50 mins'}, 
'distance': {'value': 361940, 'text': '225 mi'}, 'status': 'OK'}]}]}
""" 
#

# print(json.dumps(data['rows']))
print("Here we print data['rows']")
print(data['rows'])
print("Here we print data['rows'][0]")
print(data['rows'][0])
print("Here we print data['rows'][0]['elements'][0]")
print(data['rows'][0]['elements'][0])
print("Here we print data['rows'][0]['elements'][0]['duration']")
print(data['rows'][0]['elements'][0]['duration'])
print("Here we print data['rows'][0]['elements'][0]['duration']['text']")
print(data['rows'][0]['elements'][0]['duration']['text'])
print(data['rows'][0]['elements'][0]['duration']['value'])

