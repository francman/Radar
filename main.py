# Author: Frank Manu
# Reference: Benjamin Sam
# Date: 04/12/2018
# Purpose: This is the main file for the system

from SDP_driver_new import *

def main():
    # List of all Hardware IDs I want to look through to see if a board matches.
    # This is helpful because you can maintain a list of all IDs you've ever wanted to connect to, and the
    
    hw_id = ['6065711100000001']
    
    # Connect to the SDP board
    mySdp = connect_sdp(hw_id, sclkFrequency=2e6)

    # Show whether the connection was successful
    if mySdp.connected: 
        print '\nWe\'re connected!'
        print '\nBoard Name =', mySdp.name
        print 'Board Description =', mySdp.description

    else:
        print '\n\tNo connection made...'

    if mySdp.connected:
        #Initializing ADAR1000 RX_1 for signal input.
        mySdp.write_spi(0x0000, 0x81)     #Reset the whole board
        mySdp.write_spi(0x0000, 0x18)     #Configure board for SPI communication
        mySdp.write_spi(0x0400, 0x55)     #Adjust LDOs
        mySdp.write_spi(0x0038, 0x60)     #Select SPI for channel settings
        mySdp.write_spi(0x002e, 0x7f)     #Enable LNA
        mySdp.write_spi(0x0034, 0x08)     #Set RX LNA bias to 8
        mySdp.write_spi(0x0035, 0x16)     #Set RX VGA bias to 2
        mySdp.write_spi(0x0031, 0x20)     
        mySdp.write_spi(0x0010, 0xff)    
        mySdp.write_spi(0x0014, 0x36)     
        mySdp.write_spi(0x0015, 0x36)     
        mySdp.write_spi(0x0028, 0x01) 
        
if __name__ == '__main__':
    main()