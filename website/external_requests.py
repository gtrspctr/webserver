import requests

def lookup_geoip(ip):
    url = "https://api.geoiplookup.net/?query=" + str(ip) + "&json=true"
    try:
        r = requests.get(url)
        result_dict = {
            "isp": [],
            "city": [],
            "country": []
        }
        if "isp" not in r.json():
            result_dict["isp"] = "N/A"
            result_dict["city"] = "N/A"
            result_dict["country"] = "N/A"
        else:
            result_dict["isp"] = r.json()["isp"]
            result_dict["city"] = r.json()["city"]
            result_dict["country"] = r.json()["countrycode"]
        return result_dict
    except:
        result_dict = {
            "isp": [],
            "city": [],
            "country": []
        }
        result_dict["isp"] = "N/A"
        result_dict["city"] = "N/A"
        result_dict["country"] = "N/A"
        return result_dict
