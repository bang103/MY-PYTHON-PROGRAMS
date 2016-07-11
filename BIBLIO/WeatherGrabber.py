#Weather Grabber
#Description
#The National Weather Service is a part of the National Oceanic and Atmospheric Administration and is charge of providing
#weather forecasts and warnings all around the U.S. You can find all sorts of great weather maps, weather data,
#climate news, and information on natural disasters on their Web pages.

#One of the services provided by the National Weather Service is their Internet Weather Source,
#an online source for weather maps, current conditions, and weather forecasts.
#The NWS maintains a network of automated weather monitoring stations all around the country, most operating from airports.
#The purpose of these weather stations is to provide current weather information for aviation.

#The stations make their data available over the Internet in a special format called METAR.
#The METAR codes form a very abbreviated summary of the weather conditions at the various reporting stations.
#The NWS provides a detailed description of the METAR system and codes. A METAR report is in the form:

#2001/11/17 15:38
#KSGS 171538Z AUTO 19005KT 7SM CLR M01/M05 A3021 RMK AO2

#A fresh copy of this report can be obtained by pointing your Web browser (or Python program)
#to ftp://weather.noaa.gov/data/observations/metar/stations/KSGS.TXT.
#You can probably already guess about some the features of the METAR code.
#The following table summarizes some of the important features of this particular METAR report:

#2001/11/17	The date of the last observation.
#15:38	The time of the last observation. (Note: This time is in 24-hour format and is expressed in GMT (Greenwich Mean Time) or Zulu in aviation-speak.)
#KSGS	The four-letter station code. KSGS is the station at the South St. Paul Municipal-Richard E. Fleming Field Airport. Other station codes
#can be found by searching by state and airport at the Internet Weather Source page (use the United States Weather search).

#71538Z	This is a further abbreviated field indicating the date and time (Z for Zulu)
#AUTO	The KSGS station reports its data automatically.

#19005KT	Wind direction and velocity. This indicates a direction of 190 and a velocity of 05 knots. This field can be more complicated
#if there are wind gusts. You might see something like 19010G25KT which means that winds are at 10 gusting to 25 knots.

#7SM	The visibility is 7 statute miles.
#CLR	The sky is clear
#M01/M05	The current temperature is -1 C and the dew point is -5 C. (Negative (minus) numbers are indicated by the M in front of the numbers.)
#A3021	The atmospheric pressure is 30.21" of mercury.

#The NWS also provides a short guide that lists more of the common METAR codes.
#Input
#Your program should prompt the user for a four-letter METAR station code.
#Output
#Your program will take the METAR station code, retrieve the relevant weather data, and print a summary of the current
#conditions. You must print at least the current time, date, temperature, wind speed and direction.
#If you finish your program before the due date, begin added the other fields.

#Sample run
#The following is the minimum you are expected to complete. Add more features as time allows.
#Current weather conditions
# This program retrieves the current weather conditions from the National
#Weather Service. Enter a four-letter station ID (e.g., 'KSGS')
##
#Get weather from what station? KSGS
#Current conditions for KSGS
#Last observation: 2001/11/17 at 15:38 GMT
#Temperature: -1 C (30 F)
#Wind: S at 6 mph (5 knots)
#Going further
#There are many ways to extend this program:
#Include more METAR data in your report.
#Calculate the wind chill. The National Weather Service has published a new wind chill formula that you should use as a
#reference.
#Investigate using regular expressions to pull out the weather information.
#Regular expressions are a very powerful tool that are defintely worth learning.
