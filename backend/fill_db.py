from datetime import date, datetime, timedelta
import random
import sqlite3
#existing sql, we delete existing data here, and generate new below
conn = sqlite3.connect("backend\dataset.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM routInfo")
conn.commit()


today = date.today()
def fill_db():
    departureHub = "Madrid"
    destinations = ["Barcelona", "Valencia", "Seville", "Malaga", "Granada", "Cordoba", "Bilbao", "San Sebastian", "Zaragoza", "Alicante", "Murcia", "Salamanca", "Toledo", "Santiago de Compostela", "Cadiz"]
    for i in range(len(destinations)):
        solRutaDict = generateSolRuta(destinations[i])
        caminoExpress = generateCaminoExpress(destinations[i])
        costaLink = generateCostaLink(destinations[i])
        verdeBus = generateVerdeBus(destinations[i])
        nocheVia = generateNocheVia(destinations[i])
        sqlInsertion(solRutaDict)
        sqlInsertion(caminoExpress)
        sqlInsertion(costaLink)
        sqlInsertion(verdeBus)
        sqlInsertion(nocheVia)
        

travel_times = {
    "Barcelona": 7.0,
    "Cordoba": 4.5,
    "Murcia": 4.5,
    "Valencia": 4.0,
    "Bilbao": 5.0,
    "Salamanca": 2.5,
    "Seville": 6.0,
    "San Sebastian": 6.0,
    "Toledo": 1.5,
    "Malaga": 6.0,
    "Zaragoza": 4.0,
    "Santiago de Compostela": 7.0,
    "Granada": 5.0,
    "Alicante": 5.0,
    "Cadiz": 7.0
}
travel_price = {
    "Barcelona": 35.0,
    "Cordoba": 22.5,
    "Murcia": 22.5,
    "Valencia": 20.0,
    "Bilbao": 25.0,
    "Salamanca": 12.5,
    "Seville": 30.0,
    "San Sebastian": 30.0,
    "Toledo": 7.5,
    "Malaga": 30.0,
    "Zaragoza": 20.0,
    "Santiago de Compostela": 35.0,
    "Granada": 25.0,
    "Alicante": 25.0,
    "Cadiz": 35.0
}
def generateSolRuta(destination):
    company = "SolRuta"
    #we have destination as input
    travelDate = (str(date.today()))
    departureStr = random.choice(["11:00", "12:00", "13:00"])
    departure = datetime.strptime(departureStr, "%H:%M")
    duration = travel_times[destination]
    arrivalTime = departure + timedelta(hours=duration)
    price = travel_price[destination]
    if(duration > 5): 
        transfers = random.choice([2,4])
    else: 
        transfers = random.choice([1,2])
    luggage_allowance = 1
    changeability = "NONE"
    refundability = "NONE"
    available_seats = random.randint(10,40)
    customer_rating = round(random.uniform(3, 5), 1)
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
def generateCaminoExpress(destination):
    company = "Camino Express"
    #we have destination as input
    travelDate = (str(date.today()))
    departureStr = random.choice(["11:00", "12:00", "13:00","14:00", "15:00", "16:00","17:00", "18:00", "19:00","20:00", "21:00", "22:00"])
    departure = datetime.strptime(departureStr, "%H:%M")
    duration = travel_times[destination] * 0.8
    arrivalTime = departure + timedelta(hours=duration)
    price = travel_price[destination] * 1.2
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
        price = travel_price[destination] * 0.6
        available_seats = random.randint(20,50)
    else:
        duration = travel_times[destination]
        transfers = random.choice([2,5])
        price = travel_price[destination] * 1.6
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
    duration = travel_times[destination] * 0.7
    arrivalTime = departure + timedelta(hours=duration)
    price = travel_price[destination] * 1.10
    if(duration > 5): 
        transfers = 0
    else: 
        transfers = random.choice([0, 0, 0, 1])
    luggage_allowance = 1
    changeability = "LIMITED"
    refundability = "LIMITED"
    available_seats = random.randint(10, 35)
    customer_rating = round(random.uniform(2.0, 4.0), 1)
    environmental_measure = 3
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
    duration = travel_times[destination] * 1.1
    arrivalTime = departure + timedelta(hours=duration) 
    price = travel_price[destination] * 1.3
    if(duration > 5): 
        transfers = random.choice([2,4])
    else: 
        transfers = random.choice([1,2])
    luggage_allowance = 2
    changeability = "LIMITED"
    refundability = "NONE"
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


def sqlInsertion(dict):
    cursor.execute(
        """INSERT INTO routInfo (
            company, destination, travel_date, departure, duration,
            arrival_time, price, transfers, luggage_allowance,
            changeability, refundability, available_seats,
            customer_rating, environmental_measure
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (dict["company"], dict["destination"], dict["travel_date"],
        dict["departure_time"], dict["duration"], dict["arrival_time"],
        dict["price"], dict["transfers"], dict["luggage_allowance"],
        dict["changeability"], dict["refundability"], dict["available_seats"],
        dict["customer_rating"], dict["environmental_measure"])
    )
    conn.commit()

fill_csv()
conn.close()
