from standaloneFunctions import getTravelPrice, getTravelTime, timeStrToHour, dateStrToDate, timeDelta
from classes import Company, Offer

class OfferRanker:
    def __init__(self, companies:list[Company], destination:str, preferredDepartureTime:str, budget:float):
        self.companies = companies
        self.destination = destination
        self.preferredDepartureTime = timeStrToHour(preferredDepartureTime)
        self.budget = budget
        #we could filter by budget in fillAllOffers(), but for readability, we dont
        self.rankedOffersList:list[Offer] = self.fillAllOffers()
        #filtered by budget, so the list below does not have offer above budget
        self.validRankedOffersList = self.filterByBudget(self.rankedOffersList)
        # we need to find min and max values for later
        self.maxPrice = self.findMinOrMaxPrice(self.validRankedOffersList, True)
        self.maxDuration = self.findMinOrMaxDuration(self.validRankedOffersList, True)        
        self.minPrice = self.findMinOrMaxPrice(self.validRankedOffersList, False)
        self.minDuration = self.findMinOrMaxDuration(self.validRankedOffersList, False)
        #defult values
        self.w_price = 0.25
        self.w_duration = 0.25
        self.w_time = 0.25
        self.w_flexibility = 0.25
        self.calculateScores()
        self.sortOffers()

    def findMinOrMaxPrice(self, validRankedOffersList:list[Offer], Max:bool):
        allPrices = []
        for offer in validRankedOffersList:
            allPrices.append(offer.price)
        if(Max == True):
            return max(allPrices)
        if(Max == False):
            return min(allPrices)
        return
    def findMinOrMaxDuration(self, validRankedOffersList:list[Offer], Max:bool):
        allDurations = []
        for offer in validRankedOffersList:
            allDurations.append(offer.duration)
        if(Max == True):
            return max(allDurations)
        if(Max == False):
            return min(allDurations)
        return

    def filterByBudget(self, rankedOffersList):
        updatetList = []
        for offer in rankedOffersList:
            if offer.price <= self.budget:
                updatetList.append(offer)
        return updatetList

    def sortOffers(self):
        #used example: sorted(student_tuples, key=lambda student: student[2])   # sort by age
        #from this link: https://docs.python.org/3/howto/sorting.html
        self.rankedOffersList = sorted(self.rankedOffersList, key=lambda offer: offer.score, reverse=True)

    def changeWeights(self, price, duration, time, flexibility):
        self.w_price = price
        self.w_duration = duration
        self.w_time = time
        self.w_flexibility = flexibility
        self.calculateScores()

    def fillAllOffers(self):
        allOffers = []
        for company in self.companies:
            allOffers.extend(company.getOffers())
        return allOffers

    def getRankedOffers(self):
        return self.validRankedOffersList


    def calculateScores(self):
        for offer in self.rankedOffersList:
            #find the score
            offerScore = self.score(offer)
            #put the score in the offer object
            offer.setScore(offerScore)

    def score(self, offer:Offer) -> float: 
        # Score(j) = w_price P(j) + w_duration D(j) + w_time T(j) + w_flexibility F(j)
        return (self.w_price * self.P(offer) + 
                self.w_duration * self.D(offer) + 
                self.w_time * self.T(offer) + 
                self.w_flexibility * self.F(offer))

    def P(self, offer:Offer):
        if self.maxPrice == self.minPrice:
            return 1.0
        return ((self.maxPrice - offer.price) / (self.maxPrice - self.minPrice))
    def D(self, offer:Offer):
        return 1 - (offer.duration / self.maxDuration) 
    def T(self, offer:Offer):
        offerDepartureTime = timeStrToHour(offer.departureTime)
        delta = timeDelta(offerDepartureTime, self.preferredDepartureTime)
        for i in range(10):
            if delta < i + 1: #need +1 because it is always bigger than 0
                return (10 - i)/10 #return 1 if travel within 1 ohur, 0.9 for two .... and so on
        return 0
    def F(self, offer:Offer):
        sum = 0
        if(offer.refundability == "LIMITED"): sum += 0.25
        elif(offer.refundability == "FULL"): sum += 0.5
        if(offer.changeability == "LIMITED"): sum += 0.25
        elif(offer.changeability == "FULL"): sum += 0.5
        return sum

