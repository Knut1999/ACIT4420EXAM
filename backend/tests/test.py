from Controller import Controller
controller = Controller()
offers = controller.websiteInputs("Cadiz", "Budget traveller", 42.0, "12:50")
result = []
for offer in offers:
    result.append(offer.__dict__)

for res in result:
    print(res)
