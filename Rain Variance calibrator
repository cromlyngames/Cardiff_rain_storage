#! /usr/bin/env python3

## example_function_name
## ExampleVariableName


import random

## targets based on met office monthly data
## Row Labels	  Average of rain	StdDev of rain	StdDevp of rain
## 1	             127.425	      60.61179013	  59.84934732
## 2	             89.0475	      49.09225218	  48.47471499
## 3	              88.52564103	  44.66502646	  44.08867939
## 4	              65.86666667	  38.2410384	  37.74758497
## 5	              75.72307692	  40.7776736	  40.25148802
## 6	              69.77435897	  41.79887758	  41.25951463
## 7	              76.62564103	  44.51739883	  43.94295672
## 8	              95.01282051	  58.55597942	  57.80038674
## 9	              87.6225	      49.43868768	  48.81679264
## 10	            124.3675	    57.02466128	  56.30734138
## 11	            125.6875  	  50.63449816	  49.99756088
## 12	            131.4	        57.07990351	  56.36188872

## decision. use stdev, not stdevp. Data was last twenty years, but results outside of the sample are very possible .

## 
##  hypothesis. the rainfall on two days in the same month is largely indepentdent
## therefore The variance of rainfall between two januaries will be smaller than 
## the variance in rainfall between two rainy days in january.

## the vairance of the two would be related.

## Method - generate probailty tables for simple, round, rainfalls. 
## Run for 50 years.
## Test against average and stdev against met office values
## If much better than previous option, keep it. If much worse, revert. If mixed, mix the probality tables (genetic alog whoo!)

TargetAverage=[
0,
127.4250, 89.0475, 88.5256, 65.8666,
75.7230, 69.7744, 76.6256, 95.0128,
87,6225, 124.3675, 125.6875, 131.4000
]

## initalise table of probabilities of rain amounts

StartMonthDict={
## rain in mm : probability of it happening
0.1   : 0.09,
0.5   : 0.11,
1.0   : 0.08,
2.0   : 0.12,
4.0   : 0.07,
8.0   : 0.13,
16.0  : 0.06,
32.0  : 0.14,
64.0  : 0.05,
128.0 : 0.15
}

JanDict={}
FebDict={}
MarDict={}
AprDict={}
MayDict={}
JunDict={}
JulDict={}
AugDict={}
SepDict={}
OctDict={}
NovDict={}
DecDict={}


MonthDictLookupDict = {
1: JanDict,
2: FebDict,
3: MarDict,
4: AprDict,
5: MayDict,
6: JunDict,
7: JulDict,
8: AugDict,
9: SepDict,
10:OctDict,
11:NovDict,
12:DecDict
}

def day_of_rainfall(MonthX, YearsRain):
    Target = random.random()
    diff = float('inf')
    MonthDict = MonthDictLookupDict[MonthX]
    
    for key,value in MonthDict.items():
        if diff > abs(Target-value):
            diff = abs(Target-value)
            RainInMM = key
            print(Target, key, value, diff, RainInMM)
    YearsRain[MonthX]=round(YearsRain[MonthX] + RainInMM, 4)
    return(YearsRain)




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


    


## Program Start

## Properly intialise the monthly dicts:
## this is used to allow the start shape of the different rain slots to be easily modified.
for MonthDicts in MonthDictLookupDict:
    for RainKeys in StartMonthDict:
        #print(RainKeys, StartMonthDict[RainKeys])
        ThisMonthDict = MonthDictLookupDict[MonthDicts]
        ThisMonthDict[RainKeys] = StartMonthDict[RainKeys]
        
ErasRain = [[0, 0,0,0,0,0,0, 0,0,0,0,0,0]]

for year in range (1,5):
    DayCounter= 1
    MonthX =1
    YearsRain = [0, 0,0,0,0,0,0, 0,0,0,0,0,0]
    while DayCounter < 365:
        DayCounterCheck = DayCounter + get_block_of_days(MonthX)
        if DayCounterCheck > 365:
            ## unlike the watering program, only need to see if rain at end of this block is outside the year of record. 
            break
        ## no watering functions needed
        DayCounter = DayCounterCheck+1
        MonthX= update_month(DayCounter)
        YearsRain = day_of_rainfall(MonthX, YearsRain)
        #print(YearsRain)
    ErasRain.append(YearsRain)
print(ErasRain)        
        
        


    


