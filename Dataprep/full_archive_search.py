# Get data from twitter api
import requests
import os
import pandas as pd
import json
from tabulate import tabulate

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/all"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {
    'query': '(place_country:US OR place_country:AU OR place_country:CA OR place_country:NZ  OR place_country:GB) lang:en',
    'start_time': '2021-07-30T00:00:00Z',
    'end_time': '2021-07-30T00:01:00Z',
    'expansions': 'author_id,geo.place_id',
    'place.fields': 'country,country_code,full_name,geo,id,name,place_type',
    'user.fields': 'created_at,description,id,location,name,username',
    # 'max_results': 500
}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def query_to_csv(url, params, filename):
    json_response = connect_to_endpoint(url, params)
    # print(json.dumps(json_response, indent=4, sort_keys=True))

    tweets_id = []
    text = []
    author_id = []
    username = []
    user_created_time = []
    user_location = []
    user_name = []
    user_description = []
    geo_place_id = []
    geo_country_code = []
    geo_place_type = []
    geo_full_name = []
    geo_bbox = []
    geo_country = []
    geo_name = []
    data = json_response['data']
    users = json_response['includes']['users']
    places = json_response['includes']['places']
    time_list = params['start_time'].split('T')
    date = time_list[0]
    user_list = {}
    place_list = {}
    for i in range(0, len(users)):
        user_list[users[i].get('id', None)] = users[i]
    for i in range(0, len(places)):
        place_list[places[i].get('id', None)] = places[i]
    for i in range(0, len(data)):
        bbox = None
        cur_user = user_list.get(data[i].get('author_id', None))
        cur_place = None
        if data[i].get('geo', None) is not None:
            cur_place = place_list.get(data[i].get('geo', None).get('place_id', None))
        if cur_place is not None and cur_place.get('geo', None) is not None:
            bbox = cur_place.get('geo', None).get('bbox', None)

        tweets_id.append(data[i].get('id', None))
        text.append(data[i].get('text', None))
        author_id.append(data[i].get('author_id', None))
        if cur_user is not None:
            username.append(cur_user.get('username', None))
            user_created_time.append(cur_user.get('created_at', None))
            user_location.append(cur_user.get('location', None))
            user_name.append(cur_user.get('name', None))
            user_description.append(cur_user.get('description', None))
        else:
            username.append(None)
            user_created_time.append(None)
            user_location.append(None)
            user_name.append(None)
            user_description.append(None)

        if cur_place is not None:
            geo_place_id.append(cur_place.get('id', None))
            geo_country_code.append(cur_place.get('country_code', None))
            geo_place_type.append(cur_place.get('place_type', None))
            geo_full_name.append(cur_place.get('full_name', None))
            geo_bbox.append(bbox)
            geo_country.append(cur_place.get('country', None))
            geo_name.append(cur_place.get('name', None))
        else:
            geo_place_id.append(None)
            geo_country_code.append(None)
            geo_place_type.append(None)
            geo_full_name.append(None)
            geo_bbox.append(None)
            geo_country.append(None)
            geo_name.append(None)

    dataframe = pd.DataFrame({
        'tweets_id': tweets_id,
        'text': text,
        'author_id': author_id,
        'username': username,
        'user_created_time': user_created_time,
        'user_location': user_location,
        'user_name': user_name,
        'user_description': user_description,
        'geo_place_id': geo_place_id,
        'geo_country_code': geo_country_code,
        'geo_place_type': geo_place_type,
        'geo_full_name': geo_full_name,
        'geo_bbox': geo_bbox,
        'geo_country': geo_country,
        'geo_name': geo_name,
        'date': date
    })
    print(params['start_time'] + ' ~ ' + params['end_time'] + ':    ' + str(json_response['meta']['result_count']))
    dataframe.to_csv(filename, mode='a', index=False)
    # print(tabulate(dataframe, headers='keys', tablefmt='psql'))
    return json_response['meta']['result_count']


def main():
    filename = 'test.csv'
    query_to_csv(search_url, query_params, filename)


if __name__ == "__main__":
    # main()
    df = pd.read_csv('../Dataset/2021_07.csv')
    print(tabulate(df, headers='keys', tablefmt='psql'))
"""
    Raw Response Example:
    {
        "data": [
            {
                "geo": {
                    "place_id": "319ee7b36c9149da"
                },
                "text": "“I think we have to become comfortable with coronavirus not going away.” https://t.co/n55Ly1n45z",
                "author_id": "138460164",
                "id": "1420898180254814209"
            },
            {
                "geo": {
                    "place_id": "08fae956cd183254"
                },
                "text": "Closure on #US202 NB from North of North Maple Ave to CR 650/West Hanover Av https://t.co/ftaSPFurot",
                "author_id": "50706690",
                "id": "1420898179982282754"
            }
        ],
        "includes": {
            "users": [
                {
                    "username": "richardmskinner",
                    "created_at": "2010-04-29T16:12:05.000Z",
                    "location": "Washington, DC",
                    "name": "Richard Skinner",
                    "description": "Census decennial veteran.  @misoffact, @BrookingsInst, @legbranch. Many hats, @arlingtondems. Opinions my own. Hire me: https://t.co/oWTArkF2m2.",
                    "id": "138460164"
                },
                {
                    "username": "511NY",
                    "created_at": "2009-06-25T17:22:38.000Z",
                    "location": "New York State",
                    "name": "511 New York",
                    "description": "Traffic & transit updates for all of New York State provided by New York State 511. Visit the website for more feeds.",
                    "id": "50706690"
                },
                {
                    "username": "RatcalledAJ",
                    "created_at": "2015-05-24T05:29:43.000Z",
                    "location": "Columbus, OH",
                    "name": "Andrew Johnson",
                    "description": "Writer, drinker, and twisted thinker. \nI don't know what I want to be when I grow up.\n🎮 RatcalledAJ\n#Crew96\n#SavedTheCrew #CBJ",
                    "id": "3296109765"
                }
            ],
            "places": [
                {
                    "country_code": "US",
                    "place_type": "city",
                    "full_name": "Arlington, VA",
                    "geo": {
                        "type": "Feature",
                        "bbox": [
                            -77.172219,
                            38.827378,
                            -77.031779,
                            38.934311
                        ],
                        "properties": {}
                    },
                    "id": "319ee7b36c9149da",
                    "country": "Etats-Unis",
                    "name": "Arlington"
                },
                {
                    "country_code": "US",
                    "place_type": "city",
                    "full_name": "Bernardsville, NJ",
                    "geo": {
                        "type": "Feature",
                        "bbox": [
                            -74.618358,
                            40.684692,
                            -74.537321,
                            40.745832
                        ],
                        "properties": {}
                    },
                    "id": "08fae956cd183254",
                    "country": "Etats-Unis",
                    "name": "Bernardsville"
                }
            ]
        },
        "meta": {
            "newest_id": "1420898180254814209",
            "oldest_id": "1420898177180332033",
            "result_count": 10,
            "next_token": "b26v89c19zqg8o3fpdm6h2xa29p80wx062t0l00cx12f1"
        }
    }
"""
