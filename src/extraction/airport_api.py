import requests

def find_airport_info(airport_code: str) -> dict:
    headers = {
        'authority': 'openflights.org',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://openflights.org',
        'referer': 'https://openflights.org/html/apsearch?apid=3670',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    data = {
        'name': '',
        'iata': 'LAS',
        'icao': '',
        'city': '',
        'country': 'United States',
        'code': 'US',
        'x': '',
        'y': '',
        'elevation': '',
        'timezone': '',
        'dst': 'U',
        'db': 'airports',
        'iatafilter': 'true',
        'apid': '',
        'action': 'SEARCH',
        'offset': '0',
    }

    response = requests.post('https://openflights.org/php/apsearch.php', headers=headers, data=data)

    data = response.json()
    airport = data.get('airports', [])[0]
    
    return {
        "name": airport.get('name'),
        "city": airport.get('city'),
        "code": airport.get("iata"),
        "lat": airport.get("y"),
        "lon": airport.get("x")
    }