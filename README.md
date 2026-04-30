Wanderlust AI Trip Planner

An AI-powered Full Stack Travel Planning Web Application that helps users generate personalized trip itineraries, explore hotel options, and simulate booking with integrated payment functionality.

🚀 Live Demo
🌐 Frontend: https://your-netlify-link.netlify.app
🔗 Backend API: https://wanderlust-trip-planner.onrender.com
🧠 Features
✈️ AI-generated travel itineraries
🏨 Hotel recommendations based on budget & destination
💬 Smart chatbot for travel queries
📋 Trip management (Create, View, Delete)
💳 Razorpay payment integration (Test Mode)
🎨 Modern UI (Glassmorphism + Responsive Design)
🛠 Tech Stack
Frontend
HTML, CSS, JavaScript
Tailwind CSS
Backend
Python (Flask)
REST APIs
Database
SQLite
Payment
Razorpay (Test Mode)
Deployment
Frontend → Netlify
🔌 API Endpoints
Method	Endpoint	Description
GET	/get_trips	Fetch all trips
POST	/add_trip	Add new trip
DELETE	/delete_trip/<id>	Delete trip
POST	/generate_itinerary	Generate itinerary
POST	/get_hotels	Get hotel recommendations
POST	/chat	Chatbot response
💳 Payment Integration
Razorpay Checkout used in test mode
Supports simulated payments
No real transactions processed
🧠 Future Improvements
Real hotel API integration
Live weather data
AI-based dynamic pricing
Booking confirmation system
User authentication
Backend → Render (Gunicorn)
Version Control
Git & GitHub
