# Programmers: Nicol Gutierrez
# Course: CS151, Dr. Rajeev
# Programming Assignment: 5
# Program Inputs: [file name, longitude and latitude, day, date]
# Program Outputs: [avg cost for cash and credit card, count of all trips,
# all trips with a pickup or dropoff location that is within a given distance of a given location.]


#this function returns a list of all the information retained from this file

import math
import csv
def read_file(file_name):
    all_data = []

    #open file named filename for reading

    try:
        file = open(file_name, "r")

        for line in file:
            #it loops through all the lines and the files that we just opened
            temp=line.split(",")
            #temp is now a list separated
            all_data.append(temp)
            #add a list to the overall list




        file.close()
    except:
        print("File not found")

    return all_data

#each line contains this information in this order
#Taxi's id number 0
# Date and time of the start of the trip in month/day/year hour:minute format 1
# Date and time of the end of the trip in month/day/year hour:minute format 2
# Duration of trip in seconds 3
# Distance of the trip in miles 4
# Cost of the trip 5
# Payment type ("Cash" or "Credit Card") 6
# Taxi company 7
# Pickup location latitude (-90 to 90) 8
# Pickup location longitude (-180 to 180) 9
# Dropoff location latitude (-90 to 90) 10
# Dropoff location longitude (-180 to 180) 11

# Output the average cost for cash and (separately) credit card payments
# Output the count of all trips that started or ended on a user-given date.

#Output to a file (name provided by the user)
# the information for all trips with a pickup or dropoff location that is within a given distance of a given location.
#formula distance = arccos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)) * 3,959 miles

def distance(lat2, long2, lat1, long1):
    distance = (math.arccos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2)) * 3,959)
    return distance

def location(output_file, given_distance,long,lat, all_data):
    file = open(output_file, "w")
      # opens a new file file name comes from the variable output_file
    for trip in all_data:

    #it goes through all data variables one by one, trip represents an individual line
        pickup_distance=distance(lat,long,float(trip[8]), float(trip[9]))
        #calls the distance function using outside information and it casts trips 8 and 9 as floats
        dropoff_location=distance(lat, long, float(trip[10]),float(trip[11]))
        if(pickup_distance<given_distance or dropoff_location<given_distance):
            file.write(trip)
            #
def avg_cost(all_data, payment_type):
    x=0
    y=0

    for trip in all_data:
        if trip[6]==payment_type:
            x+=(float(trip[5]))
            y+=1
    x/=y
    return x

def trip_count (all_data):
    count=0

    # asking the user for the input
    month = input("Please enter the month you are searching for in MM form. eg. Jan would be 01, Dec would be 12: ")

    day = input("Please enter the day you are searching for in DD form. eg. the first day of the month would be 01: ")

    year = input("Please enter the year you are searching for in YYYY form. eg. 2021 not 21: ")


    # checking the year
    while not year.isdigit() or len(year) != 4:
        print("Please enter a valid year option.")
        year = input("Please enter what year you would like to look at: ")
        year=str(year)
    while not month.isdigit():
        print("Please enter a valid month option.")
        month = input("Please enter what month you would like to look at: ")
    # checking the month
    month = int(month)
    while month > 12 or month < 1:
        print("Please enter a valid month option.")
    month = input("Please enter what month you would like to look at: ")
    month = str(month)
   # convertin to string

    # checking the day
    while day > 31 or day < 1:
        print("Please enter a valid day option.")
        day = input("Please enter what day you would like to look at: ")
    day = str(day)


    # converting the date to match the file
    date=month+"/"+day+"/"+year

    # going through each line of the file
    for line in all_data:
        line_date= line[1]
        # taking the second element of the lines in the file
        if line_date==date:
            # doing the comparison
            count=count+1
            # updating the counter

    #printing the counter
    print("The number of trips on that date is"+count)


def output (file,all_data):
    # option d
    print("hello")






def main():
    # user_file = input("PLease enter the name of the file: ")
    # while not csv.path.exists(user_file):
        # print("sorry that file does not exist")

    user_file = input("PLease enter the name of the file: ")

    all_data = read_file(user_file)
    while all_data == []:
        user_file = input("PLease enter the name of the file: ")

        all_data = read_file(user_file)

    print("PLease pick one from the following options")
    # Output the average cost for cash
    print("Option a: output the average cost for cash")
    # and (separately) credit card payments.
    print("Option b: output e average cost of credit card")
    # Output the count of all trips that started or ended on a user-given date.
    print("Option c: count ot trips")
    # Output to a file (name provided by the user)
    # the information for all trips with a pickup or dropoff location that is within a given distance of a given location.
    print("Option d: output to a file of your choice")
    # end the program is the user wants to
    print("Option e: I'm done")
    option = input("Please enter which option you want: ")
    option.strip().lower()
    while option != "a" and option != "b" and option != "c" and option != "d" and option != "e":
        print("Please enter a valid option, try again")
        print("PLease pick one from the following options")
        # Output the average cost for cash
        print("Option a: output the average cost for cash")
        # and (separately) credit card payments.
        print("Option b: output e average cost of credit card")
        # Output the count of all trips that started or ended on a user-given date.
        print("Option c: count ot trips")
        # Output to a file (name provided by the user)
        # the information for all trips with a pickup or dropoff location that is within a given distance of a given location.
        print("Option d: output to a file of your choice")
        # end the program is the user wants to
        print("Option e: I'm done")
        option = input("Please enter which option you want: ")
        option.strip().lower()
    if option=="a":
         avg_cost(all_data, "cash")




    elif option=="b":
        avg_cost(all_data, "Credit Card")
        # couting the credit card transaction


    elif option=="c":
        trip_count(all_data)




    elif option=="d ":
        output(file,all_data)

      

    else:
        print("Thank you for using the program")









    # Each outputted line should be in the same format as the input file.
    # The distance is inputted by the user in miles.
    # The location is inputted by the user as a latitude and longitude.
    # The distance between two locations (lat1, lon1) and (lat2, lon2)
    # can be calculated using the formula distance = arccos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)) * 3,959 miles.
    # Input Validation: Your program must work for any file with the above format without any modification.
    # If an unavailable file is given as input, your program should print an error message and end normally.
    # Your program must work for any file of specified format without modification to your code (not just the two files provided).
    # Your program should also ensure user-inputted latitude and longitude (floats) are in their respective valid intervals.
    # Lastly, you should ensure user-inputted distance (float) is a positive value.


main()







