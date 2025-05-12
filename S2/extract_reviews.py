from serpapi import GoogleSearch
from serpapi_key import *

params= {
    "engine" : "google_maps_reviews",
    "hl" : "fr",
    "api_key" : SERPAPI_KEY, 
    "data_id" : "0x47e6723acd3b913f:0x597fb78edf2d647e"
}

search = GoogleSearch(params)
results = search.get_dict()
reviews = results["reviews"]



for r in results["reviews"]:
    print("----------------------------REVIEW----------------------------")
    print(r["snippet"])