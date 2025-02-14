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

# Create the connection object
list_of_sets = beaapi.get_data_set_list(beakey)
display(list_of_sets)