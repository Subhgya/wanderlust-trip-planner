def travel_chatbot(query):
    q = query.lower()

    # 🌦 WEATHER
    if "weather" in q:
        return "Weather varies by location 🌤️. You can check real-time weather in your itinerary!"

    # 💰 BUDGET
    if "budget" in q or "cheap" in q or "cost" in q:
        return "For budget trips 💰, use public transport, book early, and stay in budget hotels."

    # 🏨 HOTELS
    if "hotel" in q or "stay" in q:
        return "I suggest hotels based on your budget 🏨: budget, mid-range, or luxury."

    # 📍 DESTINATIONS
    if "goa" in q:
        return "Goa 🏖️ is perfect for beaches, nightlife, and water sports!"

    if "paris" in q:
        return "Paris 🗼 is famous for romance, cafes, and the Eiffel Tower!"

    if "tokyo" in q or "japan" in q:
        return "Japan 🇯🇵 offers a mix of tradition and technology — Tokyo for city life, Kyoto for temples!"

    if "kyoto" in q:
        return "Kyoto ⛩️ is known for temples, cherry blossoms 🌸, and peaceful culture."

    if "chennai" in q:
        return "Chennai 🌴 is known for beaches, temples, and delicious South Indian food 🍛."

    if "delhi" in q:
        return "Delhi 🇮🇳 offers rich history, street food, and landmarks like Red Fort and India Gate."

    if "kerala" in q:
        return "Kerala 🌿 is famous for backwaters, houseboats, and greenery."

    if "bali" in q:
        return "Bali 🌺 is perfect for beaches, temples, and tropical vibes."

    if "dubai" in q:
        return "Dubai 🏙️ offers luxury shopping, skyscrapers, and desert safaris."

    # 🧳 PACKING
    if "pack" in q or "luggage" in q:
        return "Pack smart 🧳: clothes based on weather, documents, chargers, and essentials."

    # ✈️ FLIGHTS / TRANSPORT
    if "flight" in q or "transport" in q or "travel" in q:
        return "Book flights early ✈️ and use local transport to save money."

    # 🗺 ITINERARY
    if "plan" in q or "itinerary" in q:
        return "I generate personalized itineraries 🗺 based on your destination, budget, and travel style."

    # 🍜 FOOD
    if "food" in q or "restaurant" in q:
        return "Try local food 🍜 — it’s the best way to experience a place!"

    # ⚠️ SAFETY
    if "safe" in q or "safety" in q:
        return "Travel is generally safe 👍, but always stay alert and avoid risky areas."

    # 💳 PAYMENT
    if "pay" in q or "payment" in q or "price" in q:
        return "You can securely book your trip using our integrated payment system 💳."

    # 👥 GROUP TRAVEL
    if "group" in q or "friends" in q:
        return "Group travel is fun 🎉 — split costs and plan activities together!"

    # 🧘 TRAVEL STYLE
    if "relax" in q:
        return "Relaxation trips 😌 include beaches, resorts, and peaceful destinations."

    if "adventure" in q:
        return "Adventure trips 🏔️ include trekking, rafting, and outdoor activities!"

    if "cultural" in q:
        return "Cultural trips 🏛️ include heritage sites, museums, and traditions."

    # ⏱ DURATION
    if "days" in q or "duration" in q:
        return "3–5 days ⏳ is ideal for most trips, longer for international travel."

    # 📅 BEST TIME
    if "best time" in q or "when to visit" in q:
        return "Best time depends on the destination 📅 — usually avoid extreme weather seasons."

    # 🧾 DOCUMENTS
    if "passport" in q or "visa" in q:
        return "Carry passport, visa (if required), and valid ID documents 📄."

    # 💡 TIPS
    if "tips" in q or "suggest" in q:
        return "Travel tips ✨: plan ahead, keep backup money, and explore local experiences."

    # 👋 GREETING
    if "hi" in q or "hello" in q or "hey" in q:
        return "Hey there! 👋 I'm your travel assistant. Ask me anything about trips!"

    # 🤖 DEFAULT
    return "I can help with destinations 🌍, hotels 🏨, budgets 💰, itineraries 🗺, food 🍜, and travel tips ✨. Ask me anything!"