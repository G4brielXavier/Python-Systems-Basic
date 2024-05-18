import time

mins = 1
secs = 0

def time_start(m, s):    
    def ver(m, s):
        if s < 10 and m < 10:
            print(f'0{str(m)}m 0{str(s)}s')
        elif s >= 10 and m < 10:
            print(f'0{str(m)}m {str(s)}s')
            pass
        elif s >= 10 and m >= 10:
            print(f'{str(m)}m {str(s)}s')  
            pass 
        pass 
    
    ver(m, s)

    if s == 0:
        time.sleep(1)
        m -= 1
        s = 59
        ver(m, s)

    if s > 0:
        time.sleep(1)
        s -= 1
        ver(m, s)

    
    
    time_start(m, s)
    
time_start(mins, secs)