def computepay(hr,rt):  
    hour=float(hr)
    rate=float(rt)
    if hour <= 40 :
        Cpay=hour*rate
    else:
        extra_hr=hour-40
        Cpay=(40*rate)+(extra_hr*(1.5*rate))        
    
    return(Cpay)
    
hr=input('Enter hours')
rt=input('Enter rate')
p=computepay(hr,rt)
print('Pay',p)
    
