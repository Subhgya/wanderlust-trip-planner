def generate_itinerary(data):
    days = data.get("days", 3)

    itinerary = []
    for i in range(days):
        itinerary.append({
            "day": i+1,
            "morning": "Explore local attractions",
            "afternoon": "Visit famous spots",
            "evening": "Enjoy local food"
        })

    return {
        "personality": "Explorer",
        "weather": {"temperature": 25, "description": "Sunny"},
        "hotels": ["Hotel A", "Hotel B"],
        "map": "https://maps.google.com",
        "itinerary": itinerary
    }