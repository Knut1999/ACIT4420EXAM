from datetime import date, datetime

from offer.classes import Offer
from offer.standaloneFunctions import getDestinations

#all the functions return the error type and the specific error
def validateDestination(offer):
    errorType = []
    error = []
    if offer.destination not in getDestinations():
        errorType.append("Invalid destination")
        error.append(offer.destination)
    return errorType, error

def validateDate(offer):
    errorType = []
    error = []
    try:
        dateString = offer.travelDate
        parsedDate = datetime.strptime(dateString, "%Y-%m-%d")
        travelDate = parsedDate.date()
        # print(type(travelDate), travelDate)
        if travelDate < date.today():
            errorType.append("Travel date is in the past")
            error.append(offer.travelDate)
    except ValueError:
        errorType.append("Invalid travel date type")
        error.append(offer.travelDate)
    return errorType, error

def validateDepartureAndArrival(offer: Offer):
    errorType = []
    error = []
    for stringType, time in [("Departure",offer.departureTime), ("Arrival", offer.arrivalTime)]:
        try:
            departureString = time
            parsedTime = datetime.strptime(departureString, "%H:%M")
            departureTime = parsedTime.time()
        except ValueError:
            errorType.append(f"Invalid {stringType} time")
            error.append(time)
    return errorType, error

def validateNonNegativeFloat(offer:Offer):
    errorType = []
    error = []
    #both duration and price uses same function due to both beeing float above 0   
    for stringType, value in [("Duration",offer.duration), ("Price",offer.price)]:
        try:
            duration = float(value)
            if duration <= 0:
                errorType.append(f"Invalid {stringType}")
                error.append(value)
                return errorType, error
        except ValueError:
            errorType.append(f"Invalid {stringType}")
            error.append(value)
            return errorType, error
    return errorType, error

def validateNonNegativeInteger(offer: Offer):
    errorType = []
    error = [] 
    try:
        for stringType, value in [("Luggage allowance",offer.luggageAllowance), ("Available seats",offer.availableSeats), ("Environmental measure", offer.environmentalMeasure)]:
            integer = int(value)
            if integer < 0:
                errorType.append(f"Invalid number of {stringType}")
                error.append(value)
                return errorType, error
    except ValueError:
        errorType.append(f"Invalid type of {stringType}")
        error.append(value)
        return errorType, error 
    return errorType, error

def validateCustomerRating(offer: Offer):
    errorType = []
    error = [] 
    try:
        rating = float(offer.customerRating)
        if rating < 0 or rating > 5:
            errorType.append("Invalid customer rating")
            error.append(offer.customerRating)
        return errorType, error
    except ValueError:
        errorType.append("Invalid customer rating type")
        error.append(offer.customerRating)
        return errorType, error