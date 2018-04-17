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
        print '\n\tNo connection made... handle is a dummy'

    #Initializing ADAR1000 RX_1 for signal input.
    mySdp.write_spi(0x00, 0x81)     #Reset the whole board
    mySdp.write_spi(0x00, 0x18)     #Configure board for SPI communication
    mySdp.write_spi(0x400, 0x55)    #Adjust LDOs
    mySdp.write_spi(0x38, 0x60)     #Select SPI for channel settings
    mySdp.write_spi(0x2e, 0x7f)     #Enable LNA
    mySdp.write_spi(0x34, 0x08)     #Set RX LNA bias to 8
    mySdp.write_spi(0x35, 0x16)     #Set RX VGA bias to 2
    mySdp.write_spi(0x31, 0x20)     #
    mySdp.write_spi(0x10, 0xff)     #Set VGA gain to max
    mySdp.write_spi(0x14, 0x36)     #Set CH1 Vec mod I-input to +, magnitude 16
    mySdp.write_spi(0x15, 0x36)     #Vec mod Q-input to +, magnitude ‘15’; these two together set phase to 45 deg
    mySdp.write_spi(0x28, 0x01)     #
    
        
if __name__ == '__main__':
    main()