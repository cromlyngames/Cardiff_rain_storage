# Cardiff_rain_storage

## Purpose

The purpose of this repo is to provide estimation tools for people to estimate the size of water storage and collection area needed to water their garden with a set probability of not running out of water in the summer. It will be initalised for Cardiff, UK weather.
Cardiff is the wettest city in the UK, with an annual tempreture range between -3 deg C and 25 deg C.  


## Method

Initally, it will use number of rainy days ber month and the rain days 'clumpiness' distribtion based on a public weather station at Stolford. It will use publicly available UK Meterological data for Cardiff Bute Park for monthly rainfall in mm.
The two data sets will be kludged together to provide a rough average of rainfall for each rainy day for each month. 
A future improvement would be to include a distrobution for the rain per rainy day (some are heavier than others). This will capture rarer but important stress scenarios like three weeks with 10 days of very little rain. http://www.environmentdata.org/archive/ealit:3902/OBJ/20002503.pdf might be a good place to start

No estimate or forecast ability regarding climate change will be included. Modelling that is hard.

The simualtion will be run for a certain sized collector and a certain sized storage unit. Water usage in the garden is modelled at 40 liter per week. It is conservativley assumed the garden  will be watered every non-rainy day. A future improvement to the model would be a soil resivioir, with the gardener only watering if the soil is dry (below plastic atterberg limit for example). Water usage should be increased to match this: http://cardiffallotments.uk/2015/05/water-data-and-analysis/

The simulation will be run repeatedly to allow the different random factors to play out. The user must decide what the longest time without water they would accept and what probability for that they would allow. Ie is a 1% chance of 3 days drought acceptable?


## Verification
Verification checks have been carried out on the Verification Branch.
Output is collected at the monthly level of rainfall, and the simualtion run for 10000 years.
At version 1, overestimation for rain in January is persistant. Needs to be resolved.
At version 2, overflow into january was resolved, but consistent errors were found against met office average. 'fixed' by applying a multiplier to the monthly median rain on rainy days. 
At version 3 errors trace around 1-2% variance against the met office average
