import requests


# get distance
def distance(From, To):
    URL = "http://dev.virtualearth.net/REST/V1/Routes/Driving?o=json&wp.0={}&wp.1={}&avoid=minimizeTolls&key=AvkRKWKi5NvNhi2uyQERoMXAE_5cOnM9GROxIbGpjKE3GxULTS-B5kG2HBst08qw".format(
        From, To)
    r = requests.get(url=URL, params=None)
    try:
        data = r.json()['resourceSets'][0]['resources'][0]['travelDistance']
    except:
        data = None
    return (data)


def premium(dist, rate, carValue):
    # distance factor
    dist_f = dist * 10
    # rate factor
    rate_f = (rate / 100) / 365 * int(carValue)
    premium = round(int(dist_f) + rate_f, 2)
    return premium

def path_to_map(From,To):
    path = 'https://www.google.com/maps/dir/{}+Kenya/{}+Kenya/data=!4m2!4m1!3e0'.format(From,To)
    return path
