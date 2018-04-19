# Author: Frank Manu
# Reference: Benjamin Sam
# Date: 04/12/2018
# Purpose: This is the main file for the system

import config 
from SDP_driver_new import *

global mySdp

def starter():

    hw_id = ['6065711100000001']
    mySdp = connect_sdp(hw_id, sclkFrequency=2e6)

    # Show whether the connection was successful
    if mySdp.connected: 
        print '\n\tConnection Successful!'
        print '\n\t%s', mySdp.name
        print '\t%s', mySdp.description
        config.ADAR1000A_init(mySdp)
        config.ADAR1000B_init(mySdp)

    else:
        print '\n\tNo connection made...'
    

if __name__ == '__main__':
    starter()