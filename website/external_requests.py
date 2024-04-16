import requests

# Make external API request to website to gather IP
# geolocation info
def lookup_geoip(ip):
    url = "http://ip-api.com/json/" + str(ip)
    try:
        r = requests.get(url)
        result_dict = {
            "isp": [],
            "city": [],
            "country": []
        }

        # If request did not return valid data, write "N/A" to the db entry
        # Else write the real data from the API request
        if "isp" not in r.json():
            result_dict["isp"] = "N/A"
            result_dict["city"] = "N/A"
            result_dict["country"] = "N/A"
        else:
            result_dict["isp"] = r.json()["isp"]
            result_dict["city"] = r.json()["city"]
            result_dict["country"] = r.json()["countryCode"]
        return result_dict
    except:
        # In case of failure, write "N/A" to the db entry
        result_dict = {
            "isp": [],
            "city": [],
            "country": []
        }
        result_dict["isp"] = "N/A"
        result_dict["city"] = "N/A"
        result_dict["country"] = "N/A"
        return result_dict