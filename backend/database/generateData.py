import csv
from datetime import date, datetime, timedelta
import random
from offer.standaloneFunctions import getTravelTimes, getTravelPrices, dateStrToDate, timeStrToHour

travel_times = getTravelTimes()
travel_price = getTravelPrices()

#very simple functions that generate data to a spesific company, and one with lines with error too at the bottom, it reads from a csv file
def generateSolRuta(destination):
    company = "SolRuta"
    #we have destination as input
    travelDate = (str(date.today()))
    departureStr = random.choice(["11:00", "12:00", "13:00", "14:00", "15:00"])
    departure = timeStrToHour(departureStr)
    duration = travel_times[destination] * random.choice([0.5,0.6,0.4])
    arrivalTime = departure + timedelta(hours=duration)
    price = travel_price[destination] * random.choice([0.5,0.8,0.9])
    if(duration > 5): 
        transfers = random.choice([2,4])
    else: 
        transfers = random.choice([1,2])
    luggage_allowance = 1
    changeability = "NONE"
    refundability = "NONE"
    available_seats = random.randint(10,40)
    customer_rating = round(random.uniform(3, 5), 1)
    environmental_measure = random.choice([5,6,7])
    return {
        "company": company,
        "destination": destination,
        "travel_date": travelDate,
        "departure_time": departureStr,
        "arrival_time": arrivalTime.strftime("%H:%M"),
        "duration": duration,
        "price": price,
        "transfers": transfers,
        "luggage_allowance": luggage_allowance,
        "changeability": changeability,
        "refundability": refundability,
        "available_seats": available_seats,
        "customer_rating": customer_rating,
        "environmental_measure": environmental_measure
    }
def generateCaminoExpress(destination):
    company = "Camino Express"
    fastPaths = ["Barcelona","Valencia","Seville","Malaga","Bilbao","Zaragoza"]
    #we have destination as input
    travelDate = (str(date.today()))
    departureStr = random.choice(["11:00", "12:00", "13:00","14:00", "15:00", "16:00","17:00", "18:00", "19:00","20:00", "21:00", "22:00"])
    departure = datetime.strptime(departureStr, "%H:%M")
    if(destination in fastPaths):
        duration = travel_times[destination] * random.choice([0.6,0.7,0.65])
    else:
        duration = travel_times[destination] * random.choice([1.1,1.9,1.2])
    arrivalTime = departure + timedelta(hours=duration)
    price = travel_price[destination] * random.choice([1.2,1.3,1.5])
    transfers = random.choice([0, 0, 0, 1])
    luggage_allowance = 1
    changeability = "LIMITED"
    refundability = "NONE"
    available_seats = random.randint(10,40)
    customer_rating = round(random.uniform(4.0, 5.0), 1)
    environmental_measure = 8
    return {
        "company": company,
        "destination": destination,
        "travel_date": travelDate,
        "departure_time": departureStr,
        "arrival_time": arrivalTime.strftime("%H:%M"),
        "duration": duration,
        "price": price,
        "transfers": transfers,
        "luggage_allowance": luggage_allowance,
        "changeability": changeability,
        "refundability": refundability,
        "available_seats": available_seats,
        "customer_rating": customer_rating,
        "environmental_measure": environmental_measure
    }
def generateCostaLink(destination):
    company = "CostaLink"
    #it is good at costal travel
    coastal_destinations = [
        "Barcelona", "Valencia", "Malaga",
        "Bilbao", "San Sebastian", "Murcia",
        "Alicante", "Cadiz"
    ]
    #we have destination as input
    travelDate = (str(date.today()))
    departureStr = random.choice(["08:00", "10:00", "12:00", "14:00", "16:00"])
    departure = datetime.strptime(departureStr, "%H:%M")

    if(destination in coastal_destinations): 
        duration = travel_times[destination] * 0.6
        transfers = 0
        price = travel_price[destination]  * random.choice([0.6,0.7,0.5])
        available_seats = random.randint(20,50)
    else:
        duration = travel_times[destination]
        transfers = random.choice([2,5])
        price = travel_price[destination] * random.choice([1.6,1.7,1.5])
        available_seats = random.randint(0,15)
    
    arrivalTime = departure + timedelta(hours=duration)
    luggage_allowance = 1
    changeability = "LIMITED"
    refundability = "NONE"
    customer_rating = round(random.uniform(3, 5))
    environmental_measure = 8
    return {
        "company": company,
        "destination": destination,
        "travel_date": travelDate,
        "departure_time": departureStr,
        "arrival_time": arrivalTime.strftime("%H:%M"),
        "duration": duration,
        "price": price,
        "transfers": transfers,
        "luggage_allowance": luggage_allowance,
        "changeability": changeability,
        "refundability": refundability,
        "available_seats": available_seats,
        "customer_rating": customer_rating,
        "environmental_measure": environmental_measure
    }
def generateVerdeBus(destination):
    company = "VerdeBus"
    #we have destination as input
    travelDate = str(date.today())
    departureStr = random.choice(["07:00", "09:00", "11:00", "13:00", "15:00"])
    departure = datetime.strptime(departureStr, "%H:%M")
    duration = travel_times[destination] * random.choice([0.7,0.8,0.9])
    arrivalTime = departure + timedelta(hours=duration)
    price = travel_price[destination] * random.choice([1.10,1.2,1.4,2])
    if(duration > 5): 
        transfers = 0
    else: 
        transfers = random.choice([0, 0, 0, 1])
    luggage_allowance = 1
    changeability = "LIMITED"
    refundability = "LIMITED"
    available_seats = random.randint(10, 35)
    customer_rating = round(random.uniform(2.0, 4.0), 1)
    environmental_measure = random.choice([8,9,10])
    return {
        "company": company,
        "destination": destination,
        "travel_date": travelDate,
        "departure_time": departureStr,
        "arrival_time": arrivalTime.strftime("%H:%M"),
        "duration": duration,
        "price": price,
        "transfers": transfers,
        "luggage_allowance": luggage_allowance,
        "changeability": changeability,
        "refundability": refundability,
        "available_seats": available_seats,
        "customer_rating": customer_rating,
        "environmental_measure": environmental_measure
    }
def generateNocheVia(destination):
    company = "NocheVia"
    #we have destination as input
    travelDate = (str(date.today()))
    departureStr = random.choice(["20:00", "22:00", "00:00","02:00", "04:00", "06:00"])
    departure = datetime.strptime(departureStr, "%H:%M")
    duration = travel_times[destination] * random.choice([1.1,1.2,1.3])
    arrivalTime = departure + timedelta(hours=duration) 
    price = travel_price[destination] * random.choice([1.4,1.5,1.6])
    if(duration > 5): 
        transfers = random.choice([2,4])
    else: 
        transfers = random.choice([1,2])
    luggage_allowance = 2
    changeability = "FULL"
    refundability = "FULL"
    available_seats = random.randint(10, 35)
    customer_rating = round(random.uniform(2, 5.0), 1)
    environmental_measure = 6
    return {
        "company": company,
        "destination": destination,
        "travel_date": travelDate,
        "departure_time": departureStr,
        "arrival_time": arrivalTime.strftime("%H:%M"),
        "duration": duration,
        "price": price,
        "transfers": transfers,
        "luggage_allowance": luggage_allowance,
        "changeability": changeability,
        "refundability": refundability,
        "available_seats": available_seats,
        "customer_rating": customer_rating,
        "environmental_measure": environmental_measure
    }
def transferErrorRecordsToDatabase():
    with open('database/errorValues.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)
        dictList = []
        for row in reader:
            dict = {}
            try:
                dict["company"] = row[1]
                dict["destination"] = row[2]
                dict["travel_date"] = row[3]
                dict["departure_time"] = row[4]
                dict["duration"] = float(row[5])
                dict["arrival_time"] = row[6]
                dict["price"] = float(row[7])
                dict["transfers"] = int(row[8])
                dict["luggage_allowance"] = int(row[9])
                dict["changeability"] = row[10]
                dict["refundability"] = row[11]
                dict["available_seats"] = int(row[12])
                dict["customer_rating"] = float(row[13])
                dict["environmental_measure"] = int(row[14])
            except (ValueError, IndexError) as e:
                print(f"Skipping line: {e}")
                continue
            dictList.append(dict)
    return dictList