from backend.offer.OfferController import OfferController
controller = OfferController()
weights = [0.1667,0.1667,0.1667,0.1667,0.1667,0.1667,0.342]
offers = controller.websiteInputs("Cadiz", "Budget traveller", 42.0, "12:50", weights)
result = []
for offer in offers:
    result.append(offer.__dict__)

for res in result:
    print(res)
