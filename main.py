# This function will return the IP address for egress
import requests
import json

def test_ip(request):
    result = requests.get("https://api.ipify.org?format=json")
    return json.dumps(result.json())