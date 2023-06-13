
def add_time(start, duration, day=None):
  
    days = ['Monday', 'Tuesday' , 'Wednesday', 'Thrusday' , 'Friday' , 'Saturday', 'Sunday','Monday', 'Tuesday' , 'Wednesday', 'Thrusday' , 'Friday' , 'Saturday', 'Sunday']
       
    lower_days =[]
    ## SEPARATE TIMESTAMP AND THE TIME
    start = start.split()
   
    time  = start[0]
    time_stamp = start[1]
    total_day = None
    total_halfday = None


    #SEPARATE THE HOUR AND MINUTE
    time = time.split(":")
    hour = int(time[0])
    min = int(time [1])
    
   
    #SEPERATE THE ADDED_HOUR AND ADDED MINUTE
    duration = duration.split(":")
    add_hour = int(duration[0])
    add_min = int(duration[1])
    

   
    #OPERATION

    total_hour = 0
    while True:
        added_min =  min + add_min
        if added_min > 60 :
            
            added_min -= 60
            total_hour += 1
            break 
        else : break


    total_halfday = 0
    added_hour = hour + add_hour + total_hour
    try :
        while True:
            if int(added_hour) - 12 >= 1 :
                added_hour = added_hour - 12
                total_halfday += 1
            else : break
    except: pass
    total_day = total_halfday  / 2
    


    #set timestamp to change every odd number
    
    if total_halfday % 2:
        if time_stamp == "AM":
                time_stamp = "PM"
        else:
            time_stamp = "AM" 
            total_day += 1

    if added_hour == 12:
        if time_stamp =="AM":
            time_stamp = "PM"
        else:
            time_stamp = "AM" 
            total_day += 1
        
    
    
    #Day 
    try :
        day_index = 0
        [lower_days.append(x.lower()) for x in days]
        day_index = lower_days.index(day.lower())
        indexes = total_day
        while True:
            
            if indexes > 7 :
                indexes -= 7
            else:
                break    
    
        new_day = days[day_index + int(indexes)]
    except :  
        pass
    
    #additional 
    if int(total_day) == 1:
        add_inf = "(next day)"
    if total_day >= 2 :
        add_inf = f"({int(total_day)} days later)"
    


    try:
        new_time = f'{added_hour}:{added_min:02d} {time_stamp} {add_inf}'
        pass
    except:
         new_time = f'{added_hour}:{added_min:02d} {time_stamp}'
    

    try:
        try:
            new_time = f'{added_hour}:{added_min:02d} {time_stamp}, {new_day} {add_inf}'
            pass
        except: 
            new_time = f'{added_hour}:{added_min:02d} {time_stamp}, {new_day}'
    except: pass

    return  new_time




    return new_time
