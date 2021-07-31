hr=input('Enter hours')
hour=float(hr)
rt=input('Enter rate')
rate=float(rt)
if hour <= 40 :
    pay=hour*rate
    print(pay)
else:
    extra_hr=hour-40
    pay=(40*rate)+(extra_hr*(1.5*rate))
    print(pay)
    
