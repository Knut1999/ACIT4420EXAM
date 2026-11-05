from offer.standaloneFunctions import findMinOrMaxRating, findMinOrMaxTransfers, timeStrToHour, timeDelta, findMinOrMaxWait,findMinOrMaxDuration,findMinOrMaxPrice,findMinOrMaxEnvironment
from offer.classes import Company, Offer

class OfferRanker:
    def __init__(self, companies:list[Company], destination:str, preferredDepartureTime:str, budget:float, weights:list[float]):
        self.companies = companies
        self.destination = destination
        self.preferredDepartureTime = timeStrToHour(preferredDepartureTime)
        self.budget = budget
        #we could filter by budget in fillAllOffers(), but for readability, we dont
        self.rankedOffersList:list[Offer] = self.fillAllOffers()
        #filtered by budget, so the list below does not have offer above budget
        self.validRankedOffersList = self.filterByBudget(self.rankedOffersList)
        # we need to find min and max values for later
        self.maxPrice = findMinOrMaxPrice(self.validRankedOffersList, True)
        self.maxDuration = findMinOrMaxDuration(self.validRankedOffersList, True)        
        self.minPrice = findMinOrMaxPrice(self.validRankedOffersList, False)
        self.minDuration = findMinOrMaxDuration(self.validRankedOffersList, False)
        self.maxWait = findMinOrMaxWait(self.validRankedOffersList, self.preferredDepartureTime, True)
        self.minWait = findMinOrMaxWait(self.validRankedOffersList, self.preferredDepartureTime, False)
        self.maxRating = findMinOrMaxRating(self.validRankedOffersList, True)
        self.minRating = findMinOrMaxRating(self.validRankedOffersList, False)
        self.maxTransfers = findMinOrMaxTransfers(self.validRankedOffersList, True)
        self.minTransfers = findMinOrMaxTransfers(self.validRankedOffersList, False)
        self.maxEnvironment = findMinOrMaxEnvironment(self.validRankedOffersList, True)
        self.minEnvironment = findMinOrMaxEnvironment(self.validRankedOffersList, False)

        self.minWait
        #defult values
        self.w_price = weights[0]
        self.w_duration = weights[1]
        self.w_time = weights[2]
        self.w_flexibility = weights[3]
        self.w_customerRating = weights[4]
        self.w_transfers = weights[5]
        self.w_environment = weights[6]
        self.calculateScores()
        self.sortOffers()

    def filterByBudget(self, rankedOffersList):
        updatetList = []
        for offer in rankedOffersList:
            if offer.price <= self.budget:
                updatetList.append(offer)
        return updatetList

    def sortOffers(self):
        #used example: sorted(student_tuples, key=lambda student: student[2])   # sort by age
        #from this link: https://docs.python.org/3/howto/sorting.html
        self.validRankedOffersList = sorted(self.validRankedOffersList, key=lambda offer: offer.score, reverse=True)

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
        for offer in self.validRankedOffersList:
            #find the score
            offerScore = self.score(offer)
            #put the score in the offer object
            offer.setScore(offerScore)

    def score(self, offer:Offer) -> float: 
        # Score(j) = w_price P(j) + w_duration D(j) + w_time T(j) + w_flexibility F(j) + w_customerRating R(j) 
        # + w_transfers * TR(j)
        return (self.w_price * self.P(offer) + 
                self.w_duration * self.D(offer) + 
                self.w_time * self.T(offer) + 
                self.w_flexibility * self.F(offer) +
                self.w_customerRating * self.R(offer) +
                self.w_transfers * self.TR(offer) +
                self.w_environment * self.E(offer))

    def P(self, offer:Offer):
        if (self.maxPrice == self.minPrice):
            return 1.0
        return ((self.maxPrice - offer.price) / (self.maxPrice - self.minPrice))
    def D(self, offer:Offer):
        if(self.maxDuration == self.minDuration):
            return 1.0
        return ((self.maxDuration - offer.duration) / (self.maxDuration - self.minDuration)) 
    def T(self, offer:Offer):
        offerDepartureTime = timeStrToHour(offer.departureTime)
        delta = timeDelta(offerDepartureTime, self.preferredDepartureTime)
        if(self.maxWait == self.minWait):
            return 1
        return ((self.maxWait - delta) / (self.maxWait - self.minWait))
    def F(self, offer:Offer):
        sum = 0
        if(offer.refundability == "LIMITED"): sum += 0.25
        elif(offer.refundability == "FULL"): sum += 0.5
        if(offer.changeability == "LIMITED"): sum += 0.25
        elif(offer.changeability == "FULL"): sum += 0.5
        return sum
    def R(self, offer:Offer):
        if (self.maxRating == self.minRating):
            return 1.0
        return (offer.customerRating - self.minRating) / (self.maxRating - self.minRating)
    def TR(self, offer:Offer):
        if (self.maxTransfers == self.minTransfers):
            return 1.0
        return (self.maxTransfers - offer.transfers) / (self.maxTransfers - self.minTransfers)
    def E(self, offer:Offer):
        if (self.maxEnvironment == self.minEnvironment):
            return 1.0
        return (offer.environmentalMeasure - self.minEnvironment) / (self.maxEnvironment - self.minEnvironment)

