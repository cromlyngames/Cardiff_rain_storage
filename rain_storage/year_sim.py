#!/usr/bin/env python3

## example_function_name
## ExampleVariableName

import random

def get_block_of_days(MonthX):
    
## generates a block of days until it rains again
## current iteration ignores the month and returns average iteration for watering months
## this underestimates frequency of rain in winter
    BlockFreqLookupTable={
    0 : 0.684449093444909,
    1 : 0.118200836820084,
    2 : 0.0753138075313808,
    3 : 0.0352161785216179,
    4 : 0.0209205020920502,
    5 : 0.0135983263598326,
    6 : 0.0125523012552301,
    7 : 0.00906555090655509,
    8 : 0.00488145048814505,
    9 : 0.00488145048814505,
    10 : 0.00627615062761506,
    11 : 0.00453277545327755,
    12 : 0.00278940027894003,
    13 : 0.00209205020920502,
    14 : 0.00139470013947001,
    15 : 0.000697350069735007,
    16 : 0.000697350069735007,
    17 : 0.00104602510460251,
    18 : 0.000348675034867503,
    19 : 0.000348675034867503,
    20 : 0.000697350069735007,
    21 : 0,
    }

    Target = random.random()
    diff = float('inf')
    for key,value in BlockFreqLookupTable.items():
        if diff > abs(Target-value):
            diff = abs(Target-value)
            BlockOfDays = key
    


    
    return(BlockOfDays)
    ## 0 means it rains the next day as well as today.
    ## yes, in my 20 year data set, cardiff has NEVER had 3 weeks or more without rain.


def water_the_garden(StoredVol):
    StoredVol = StoredVol-GardenAllowance/7
    ## assumes 40 Liters a week watering. BIG assumption
    return(StoredVol)

def water_the_greenhouse(StoredVol):
    StoredVol = StoredVol-GreenhouseAllowance/7
    ## assumes 10 liters a week for greenhouses, seedlings, leaks, evaporation ect.
    return(StoredVol)

def record_shortage(MonthX, StoredVol, RecordThis):
    ## records total number of dry days by month
    ## records total missing volume too
    ## further accuracy likely to be misleading
    if RecordThis == True:
        OutputLine= "dry day in Month "+ str(MonthX) +"  needs  "+ str(StoredVol) +"  for  " +str(CollectorArea)+" "+ str(StorageVolume)+"\n"
        f.write(OutputLine)

    
def add_rain_to_storage(MonthX, StoredVol, YearsRain):
    MedianRainByMonth =[ ## Cardiff Bute Park, Met office data
        0,
        137.25,
        74.95,
        79.2,
        70.2,
        75.2,
        64.9,
        69.7,
        74.2,
        81.2,
        124.5,
        113.25,
        128,
        137.25 ## jan again
        ]
    
    AverageRainyDaysByMonth=[ ## Stolford, 2 decades
         0,
         19.9,
         16.5,
         13.9,
         14.9,
         17.7,
         14.9,
         17.3,
         16.6,
         14.9,
         20.2,
         20.4,
         19.3,
         19.9 ## jan again
         ]

    ForcedCorrelationFactor=[
        0,
        0.91606,
        1.11788,
        0.84749,
        0.80381,
        0.91915,
        0.85132,
        1.05532,
        1.14787,
        0.92629,
        1.20239,
        1.19714,
        1.02959,
        1.00157,
        0.91606 # jan again
        ]
        
    
    RainInMM = MedianRainByMonth[MonthX]/AverageRainyDaysByMonth[MonthX] *ForcedCorrelationFactor[MonthX]
    RainVol = RainInMM*CollectorArea ## mm*m2 = liters
    #print("rained liters", RainVol)
    StoredVol = StoredVol + RainVol
    if StoredVol > StorageVolume: ## lose what you can't store
        StoredVol = StorageVolume
   # print("new stored Vol = ",StoredVol, "StorageVolume is ", StorageVolume)
    YearsRain[MonthX] = YearsRain[MonthX] + RainInMM
    return(StoredVol, YearsRain)        

def update_month(DayCount):
    x= 0
    DaysPerMonth = [
        0,
        31, 28, 31,
        30, 31, 30,
        31, 30, 31,
        30, 31, 30,
        25
        ]
    while DayCount >0:
        x=x+1
        if x==13:
            x = 1
       # print(x, DayCount)
        DayCount = DayCount - DaysPerMonth[x]
    MonthX = x
    return(MonthX)


def one_block_of_days(DayCounterLocal, MonthX, StoredVol, YearsRain, YearSummary, RecordThis):
        ## carries out a block of days between rainy days, then does the final accounting for that rainy day                
    DayCounterCheck = DayCounterLocal +get_block_of_days(MonthX)
   # print('one block', DayCounter, DayCounterCheck, DayCounterCheck-DayCounter)
    for x in range(DayCounterLocal, DayCounterCheck):
        if x >365:
            return(DayCounterLocal, MonthX, StoredVol, YearsRain, YearSummary)  ## cuts off the year to stop overspill into Jan        
     #   print("dry day", x, StoredVol)
        if 3 <= MonthX <= 11:
            StoredVol = water_the_garden(StoredVol)
        StoredVol = water_the_greenhouse(StoredVol)  ## happens all year around
        if StoredVol<0.0:
            record_shortage(MonthX, StoredVol, RecordThis)
            YearSummary[MonthX] = YearSummary[MonthX] +StoredVol
            StoredVol=0.0
    ## after the dry days we have the rainy day at the end of the block
         
    DayCounterLocal = DayCounterCheck +1
    MonthX = update_month(DayCounterLocal)
    StoredVol, YearsRain = add_rain_to_storage(MonthX, StoredVol, YearsRain)
    #print("rain day", DayCounterLocal, StoredVol)
    StoredVol = water_the_greenhouse(StoredVol)  ## order here allows the rain to maybe refill the water storage enough before you need to water
    if StoredVol<0:
            record_shortage(MonthX, StoredVol, RecordThis)
            YearSummary[MonthX] = YearSummary[MonthX] +StoredVol
            StoredVol=0.0
    return(DayCounterLocal, MonthX, StoredVol, YearsRain, YearSummary)

def initalise_year(MonthX, StoredVol):
    InitialYearDay=1
    RecordThis = False
    while InitialYearDay <365:
        YearsRain = [0, 0,0,0,0,0,0, 0,0,0,0,0,0]
        YearSummary = [0, 0,0,0,0,0,0, 0,0,0,0,0,0]
        InitialYearDay, MonthX, StoredVol, YearsRain, YearSummary = one_block_of_days(InitialYearDay, MonthX, StoredVol, YearsRain, YearSummary, RecordThis)
    if MonthX != 1:
        print("ERROR: MonthX not jan after inital year.")
        quit()
    print("inital year complete. Start stored vol for model is ", StoredVol)
    return(StoredVol)
        

## start main
DayCounter = 1
MonthX = 1  ## start on First of Jan for obviousness. Uses an intialiser year to balance this out for actual data years. Gives rain storage all winter to build up before watering starts in March
StorageVolume = 1000.0 ## in liters
CollectorArea = 2.0 ## in m2
GardenAllowance = 40.0 ## liters per week
GreenhouseAllowance = 10.0 ## liters per week




RunRainVerification = True
RunCollectionCheck = True

#for CollectorArea in range (1, 25):
#   for StorageVolume in range(100, 3000, 100):
#        print("starting ", CollectorArea, "m2 and ", StorageVolume,"liters")
if RunRainVerification == True:
    g=open('WaterVerficationResults', 'w')
    for years in range (1,300):
        print("RunRain Verification year:", years)
        DayCounter=1
        YearSummary = [0, 0,0,0,0,0,0, 0,0,0,0,0,0]
        YearsRain = [0, 0,0,0,0,0,0, 0,0,0,0,0,0]
        StoredVol = 350.0
        RecordThis = True
        #print(years)
        while DayCounter < 365:
            DayCounter, MonthX, StoredVol, YearsRain, YearSummary = one_block_of_days(DayCounter, MonthX, StoredVol, YearsRain, YearSummary, RecordThis)       
        OutputLine = str(YearsRain) +"  \n"
        g.write(OutputLine)


if RunCollectionCheck == True:
    h= open('ResultsSummary','w')
    for CollectorArea in range (1, 5):    ## one perch is ~ 25.29 m2
        for StorageVolume in range(100, 1500, 100):
            print("starting ", CollectorArea, "m2 and ", StorageVolume,"liters")
            OutputFilename = str(CollectorArea) +"m2-"+str(StorageVolume)+"liter"
            f=open(OutputFilename, 'w')
            StoredVol = 350.0 ## start with some water to cover the fixed 10liter a week, even in winter
            YearsRain = [0, 0,0,0,0,0,0, 0,0,0,0,0,0]
            YearSummary = [0, 0,0,0,0,0,0, 0,0,0,0,0,0]
            StoredVol = initalise_year(MonthX, StoredVol)
            for years in range (0,1000):
                print(years)
                DayCounter =1
                YearSummary[0] = StoredVol 
                while DayCounter < 365:
                    RecordThis = True
                    DayCounter, MonthX, StoredVol, YearsRain, YearSummary = one_block_of_days(DayCounter, MonthX, StoredVol, YearsRain, YearSummary, RecordThis)
                SummaryOutput = OutputFilename + str(YearSummary) +"  \n"
                h.write(SummaryOutput)
