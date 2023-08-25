import requests
geocoding_routing_api= "3ixGKeXBm2wnRw75MDUjRbLW3dDIeGN6"

'''
start_point = input("Starting point: ")
destination = input("Destination: ")
'''

start_point = "Eiffel Tower, Paris, France"
destination = "Times Square, New York, USA"

#api url for origin and destination
geocoding_start_url = f"https://api.tomtom.com/search/2/geocode/{start_point}.json?key={geocoding_routing_api}"
geocoding_destination_url = f"https://api.tomtom.com/search/2/geocode/{destination}.json?key={geocoding_routing_api}"

#api requests
start_response = requests.get(geocoding_start_url)
destination_response = requests.get(geocoding_destination_url)

#status code of 200 = successful response from geocoding api
#if both responses are successful, they are converted to json, coordinates of origin and destination are extracted from json dta
if start_response.status_code==200 and destination_response.status_code==200:
  start_data = start_response.json()
  destination_data = destination_response.json()
  start_coords = start_data["results"][0]["position"]
  destination_coords = destination_data["results"][0]["position"]

#moving on to routing
routing_baseurl = "https://api.tomtom.com/routing/1/calculateRoute/"
routing_url = f"{routing_baseurl}{start_coords['lat']},{start_coords['lon']}:{destination_coords['lat']},{destination_coords['lon']}/json?key={geocoding_routing_api}"

routing_resp = requests.get(routing_url)

if routing_resp.status_code ==200:
  routing_data = routing_resp.json()
  print(routing_data)
  instructions = routing_data["routes"][0]["guidance"]["instructions"]
  for index, step in enumerate(instructions, start=1):
    print(f"Step {index}: {step['instruction']}")
else: 
  print("geocoding API error: ", start_response.status_code, destination_response.status_code)
  print("Routing API error: ", routing_resp.status_code)
