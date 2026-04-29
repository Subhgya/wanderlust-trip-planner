def get_hotels(destination, budget):
    hotels = {
        "Budget": [
            f"Budget Inn - {destination}",
            f"Hostel Stay - {destination}"
        ],
        "Mid-range": [
            f"3 Star Hotel - {destination}",
            f"Comfort Suites - {destination}"
        ],
        "Luxury": [
            f"5 Star Resort - {destination}",
            f"Luxury Villa - {destination}"
        ]
    }

    return hotels.get(budget, ["Standard Hotel"])


def get_hotels(destination, budget):
    hotels = []

    if budget == "Budget":
        hotels = [
            {"name": "Budget Stay Inn", "price": 2000},
            {"name": "Backpackers Hub", "price": 1500}
        ]

    elif budget == "Mid-range":
        hotels = [
            {"name": "Comfort Suites", "price": 5000},
            {"name": "City View Hotel", "price": 6000}
        ]

    else:
        hotels = [
            {"name": "Grand Palace Hotel", "price": 12000},
            {"name": "Luxury Resort & Spa", "price": 15000}
        ]

    return hotels