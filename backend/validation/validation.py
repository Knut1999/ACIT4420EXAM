from datetime import date, datetime

from validation.standaloneFunctionsValidation import validateCustomerRating, validateDate, validateDepartureAndArrival, validateDestination, validateNonNegativeFloat, validateNonNegativeInteger
from offer.classes import Company, Offer
from database.database import Database
from offer.standaloneFunctions import errorMessageToCSV, getCompanies

def validateCompany(companyList: list[Company]) -> list[Company]:
    validCompaniesStr = getCompanies()
    validCompanies = []
    inValidCompanies = []
    for company in companyList:
        if company.name not in validCompaniesStr:
            inValidCompanies.append(company)
            continue
        validCompanies.append(company)

    for errCompany in inValidCompanies:
        errorType = "Invalid company name"
        error = errCompany.name
        ids = Database.getIdFromCompanyName(errCompany.name)
        errorMessageToCSV(ids, errorType,error)
            
    return validCompanies

def validateOffers(company:Company):
    for offer in company.offers:
        errorType = []
        error = []
        #companyName is already validated in controller __init__
        result = (validateDestination(offer))
        errorType.extend(result[0])
        error.extend(result[1])
        #checking if traveldate is in future and that type is correct
        result = (validateDate(offer))
        errorType.extend(result[0])
        error.extend(result[1])
        #checking departure time
        result = (validateDepartureAndArrival(offer))
        errorType.extend(result[0])
        error.extend(result[1])
        #check duration
        result = (validateNonNegativeFloat(offer))
        errorType.extend(result[0])
        error.extend(result[1])
        #check transfers for int and above 0
        result = (validateNonNegativeInteger(offer))
        errorType.extend(result[0])
        error.extend(result[1])
        #customer rating between 1 and 5
        result = (validateCustomerRating(offer))
        errorType.extend(result[0])
        error.extend(result[1])

        if(errorType):
            errorMessageToCSV(offer.id, errorType,error)
            company.offers.remove(offer)

