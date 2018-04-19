"""
def Beamsteer(mySdp):
    #default to 45 degrees
        mySdp.write_spi(0x2000, 0x81)     #Reset the whole board
        mySdp.write_spi(0x2000, 0x18)     #Configure board for SPI communication
        mySdp.write_spi(0x2400, 0x55)     #Adjust LDOs
        mySdp.write_spi(0x2038, 0x60)     #Select SPI for channel settings
        mySdp.write_spi(0x202e, 0x7f)     #Enable LNA
        mySdp.write_spi(0x2034, 0x08)     #Set RX LNA bias to 8
        mySdp.write_spi(0x2035, 0x16)     #Set RX VGA bias to 2
        mySdp.write_spi(0x2031, 0x20)    

    #Set the phase and amplitude for channel 1
        mySdp.write_spi(0x2010, 0xff)   #Set the gain 
        mySdp.write_spi(0x2014, 0x3F)   #Set the I phase
        mySdp.write_spi(0x2015, 0x01)   #Set the Q phase
        mySdp.write_spi(0x2028, 0x01)   #Load the new settings    

    #Set the phase and amplitude for channel 2 
        mySdp.write_spi(0x0011, 0xff)    
        mySdp.write_spi(0x0014, 0x36)     
        mySdp.write_spi(0x0015, 0x36)     
        mySdp.write_spi(0x0028, 0x01)   #Load the new settings 

    #Set the phase and amplitude for channel 2
        mySdp.write_spi(0x0012, 0xff)    
        mySdp.write_spi(0x0014, 0x36)     
        mySdp.write_spi(0x0015, 0x36)     
        mySdp.write_spi(0x0028, 0x01)   #Load the new settings 

    #Set the phase and amplitude for channel 2 
        mySdp.write_spi(0x0014, 0xff)    
        mySdp.write_spi(0x0014, 0x36)     
        mySdp.write_spi(0x0015, 0x36)     
        mySdp.write_spi(0x0028, 0x01)   #Load the new settings 
"""
