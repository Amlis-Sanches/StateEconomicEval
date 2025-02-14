import beaapi
import configparser
import os
from IPython.display import display

'''
Throttling: The BEA api limits requests to a maximum of 100/minute and 
100MB/minute (as well as 30 errors/minute). If the user exceeds this, 
they will be denied access for 1 hour. This package will automatically 
self-throttle, so in general, the user does not have to worry about that.
'''

# Load the API key from the config file then remove config object as this is a onetime use.
config = configparser.ConfigParser()
configpath = os.path.expanduser('~/Programming/Keys/keyconfig.ini')
config.read(configpath)
beakey = config.get('economicmodle keys','beaapi')

del config

gdp_data = beaapi.get_data(
    beakey,
    datasetname="Regional",
    TableName="SQGDP2",
    GeoFips="STATE",
    Year="2023",
    LineCode="1",  # This is REQUIRED
    ResultFormat="JSON"
)

print(gdp_data)

