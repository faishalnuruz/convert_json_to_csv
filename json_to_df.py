# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 12:01:01 2018

@author: Faishal
"""

import urllib.parse as urlparse
from urllib.request import urlopen as req
import pandas as pd
from pandas.io.json import json_normalize
import json

df = pd.DataFrame()

data = {}
data['location'] = '-6.2211226,106.8202995'
data['radius'] = '100' # Put the channelId of channel you want to Sync to.
data['type'] = 'restaurants'
data['key'] =   'AIzaSyAR4hnZheCz1aOjguBIWuVBcOfKHN59m44'

requestValues = urlparse.urlencode(data)
request = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?' + requestValues
string = req(request).read().decode('utf8')
item = json.loads(string)['results']

df = pd.DataFrame.from_dict(json_normalize(item), orient='columns')