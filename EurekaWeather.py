import datetime
import ffxivweather
import time
from playsound import playsound

# CONST
FORCAST_COUNT = 31

# def
def getRemainTime(start_time):
    if type(start_time) != type(datetime.datetime.utcnow()):
        return ' | '
    return str(round((start_time - datetime.datetime.utcnow()).total_seconds() / 60))

def printTable(pazuzu, crab, cassie, skoll, pen):
    
    print("+-----------------------+---------------+")
    print('No.', end='\t')
    print('pazuzu', end='\t')
    print('crab', end='\t')
    print('cassie', end='\t')
    print('skoll', end='\t')
    print('pen', end='\n')
    print("+-----------------------+---------------+")
    for n in range(2, FORCAST_COUNT+2, 1):
        #print (str(n-2) + '\t' + remainingTime + '\t' + name)
        print(str(n-2), end='\t')
        print(getRemainTime(pazuzu[n]), end='\t')
        print(getRemainTime(crab[n]), end='\t')
        print(getRemainTime(cassie[n]), end='\t')
        print(getRemainTime(skoll[n]), end='\t')
        print(getRemainTime(pen[n]), end='\n')

def timer():
    minute = int(input("\nTime: "))
    eurekaWeather()
    print('\n--------------- ' + str(minute) + " Minute Left!" + ' --------------- ' + str(datetime.datetime.now())+ '\n')
    for i in range(0,minute,1):
        if minute-i<10:
            playsound("E:\Arrist\Sound\Meme\Cant Killean The Zilean (Meme).mp3")
            time.sleep(40)
        else:
            time.sleep(60)
        eurekaWeather()
        print('\n--------------- ' + str(minute-i) + " Minute Left!" + ' --------------- ' + str(datetime.datetime.now()))
        
    print('\n------------------- THE END ------------------- ' + str(datetime.datetime.now()))
    playsound("D:\sound.mp3")
def eurekaWeather():
    
    # var
    pazuzu = ['Pazuzu','Pazuzu']
    crab = ['King Arthro', 'Crab']
    cassie = ['Copycat Cassie','Cassie']
    skoll = ['Skoll','Skoll']
    pen = ['Penthesilea','Pen']

    # get weather
    Anemos = ffxivweather.forecaster.get_forecast(place_name="Eureka Anemos", count=FORCAST_COUNT)
    Pagos = ffxivweather.forecaster.get_forecast(place_name="Eureka Pagos", count=FORCAST_COUNT)
    Pyros = ffxivweather.forecaster.get_forecast(place_name="Eureka Pyros", count=FORCAST_COUNT)

    for i in range(0, FORCAST_COUNT, 1):
        # pazuzu
        if Anemos[i][0]['id'] == 6:
            pazuzu.append(Anemos[i][1])
        else:
            pazuzu.append(False)
        # Crab
        if Pagos[i][0]['id'] == 4:
            crab.append(Pagos[i][1])
        else:
            crab.append(False)
        # Cassie
        if Pagos[i][0]['id'] == 16:
            cassie.append(Pagos[i][1])
        else:
            cassie.append(False)
        # Skoll
        if Pyros[i][0]['id'] == 16:
            skoll.append(Pyros[i][1])
        else:
            skoll.append(False)
        # Pen
        if Pyros[i][0]['id'] == 14:
            pen.append(Pyros[i][1])
        else:
            pen.append(False)
        continue;

    printTable(pazuzu, crab, cassie, skoll, pen)

eurekaWeather()
timer()
