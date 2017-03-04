import numpy as np
import matplotlib.pyplot as plt



def station_code_location(stationcode,date,day):
    locationsfilename='/home/carlocafaro/Downloads/midas_tempdrnl_201601-201612.txt'
    data=[]
    date=str(date)
    date=date[0:4]+'-'+date[4:6]+'-'+str(day).zfill(2)+' '+'09:00'
    print date,'ciao'
    with open(locationsfilename) as inputfile:
      for line in inputfile:
        currentline=line.split(',')
        
        if currentline[6].strip()==str(stationcode):
         if currentline[0]==date:
        
           data.append([currentline[0],currentline[8],currentline[9]])
     
    return np.reshape(data,(-1,3))


    


