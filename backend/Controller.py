from OfferRanker import OfferRanker
from standaloneFunctions import getOffers, createCompanyObjects, create_empty_invalid_records
from validation.validation import validateCompany, validateOffers
from classes import User
from database.database import Database

class Controller:
    def __init__(self):
        #list of strings of the company names from static Database function
        self.companies_set = Database.getCompanies()
        # create company objects
        self.companies = createCompanyObjects(self.companies_set)
        #first create emty invalid csv, then remove companies with faulty names(put them in the invalid csv), update list with valid companies
        create_empty_invalid_records()
        self.companies = validateCompany(self.companies)
        self.user = None
        self.offerRanker = None
        self.destination = None
        self.preferredDepartureTime = None
        self.budget = None
        

    def websiteInputs(self, destination, budgetType, budget, preferredDepartureTime):
        self.destination = destination
        self.preferredDepartureTime = preferredDepartureTime
        self.budget = budget
        self.user = User(destination, budgetType, budget)
        self.generateOffers()
        return self.offerRanker.getRankedOffers()


    def generateOffers(self):
        for company in self.companies:
            company.generateOffers(self.user.getUserDestination())
            validateOffers(company) #removes invalid offers, puts them in invalid_records.csv
        self.rankOffers()

    def rankOffers(self):
        self.offerRanker = OfferRanker(self.companies, self.destination, self.preferredDepartureTime, self.budget)

    
        

    
            

if __name__ == "__main__":
    getOffers()