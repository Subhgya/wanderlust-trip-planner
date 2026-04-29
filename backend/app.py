from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from database import get_db, init_db
from itinerary_ai import generate_itinerary
from chatbot import travel_chatbot
from api.weather_api import get_weather
from api.hotel_api import get_hotels
from api.map_api import get_map_link
import os

# Configure Flask to serve frontend
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

init_db()

# Serve the frontend
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

# ---------------- TRIPS ----------------

@app.route('/get_trips')
def get_trips():
    conn = get_db()
    trips = conn.execute("SELECT * FROM trips").fetchall()
    return jsonify([dict(t) for t in trips])

@app.route('/add_trip', methods=['POST'])
def add_trip():
    data = request.json
    conn = get_db()
    conn.execute("""
        INSERT INTO trips (trip_name,destination,start_date,end_date,budget,travelers,travel_style,notes)
        VALUES (?,?,?,?,?,?,?,?)
    """, (
        data["trip_name"],
        data["destination"],
        data["start_date"],
        data["end_date"],
        data["budget"],
        data["travelers"],
        data["travel_style"],
        data["notes"]
    ))
    conn.commit()
    return jsonify({"msg": "added"})

@app.route('/delete_trip/<int:id>', methods=['DELETE'])
def delete_trip(id):
    conn = get_db()
    conn.execute("DELETE FROM trips WHERE id=?", (id,))
    conn.commit()
    return jsonify({"msg": "deleted"})

# ---------------- AI ----------------

@app.route('/generate_itinerary', methods=['POST'])
def ai():
    data = request.json

    itinerary_data = generate_itinerary(data)

    destination = data.get("destination", "Unknown")
    budget = data.get("budget", "Mid-range")

    return jsonify({
        "personality": itinerary_data["personality"],
        "itinerary": itinerary_data["itinerary"],
        "weather": get_weather(destination),
        "hotels": get_hotels(destination, budget),
        "map": get_map_link(destination)
    })

# ---------------- CHATBOT ----------------

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    reply = travel_chatbot(data['message'])
    return jsonify({"reply": reply})


@app.route('/get_hotels', methods=['POST'])
def hotels():
    data = request.json
    destination = data['destination']
    budget = data['budget']

    hotels = get_hotels(destination, budget)

    return jsonify(hotels)

# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)