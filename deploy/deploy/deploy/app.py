from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

services = [
    {
        "id": 1,
        "name": "Basic Bath & Dry",
        "price": 799,
        "duration": "1 hr",
        "description": "Full shampoo, conditioner rinse, blow dry & brush out.",
        "icon": "🛁",
        "pets": ["Dogs", "Cats"]
    },
    {
        "id": 2,
        "name": "Deluxe Spa Package",
        "price": 1499,
        "duration": "2 hrs",
        "description": "Bath, deep conditioning, ear cleaning, nail trim & spritz.",
        "icon": "✨",
        "pets": ["Dogs", "Cats"]
    },
    {
        "id": 3,
        "name": "Puppy First Bath",
        "price": 599,
        "duration": "45 min",
        "description": "Gentle, stress-free first experience for puppies under 6 months.",
        "icon": "🐾",
        "pets": ["Puppies"]
    },
    {
        "id": 4,
        "name": "Nail Trim & Paw Care",
        "price": 299,
        "duration": "20 min",
        "description": "Nail clipping, filing and moisturising paw pad treatment.",
        "icon": "💅",
        "pets": ["Dogs", "Cats", "Rabbits"]
    },
    {
        "id": 5,
        "name": "De-Shedding Treatment",
        "price": 999,
        "duration": "90 min",
        "description": "Deep bath + specialized de-shedding shampoo & blow out.",
        "icon": "🌬️",
        "pets": ["Dogs"]
    },
    {
        "id": 6,
        "name": "Teeth Brushing",
        "price": 249,
        "duration": "15 min",
        "description": "Pet-safe toothpaste brush to keep that smile fresh & healthy.",
        "icon": "🦷",
        "pets": ["Dogs", "Cats"]
    },
]

testimonials = [
    {"name": "Priya S.", "pet": "Golden Retriever", "text": "Max comes out smelling like a dream! The staff are so gentle and loving with him.", "stars": 5},
    {"name": "Rahul M.", "pet": "Persian Cat", "text": "My cat Mochi actually enjoys bath time now. That says everything!", "stars": 5},
    {"name": "Anita K.", "pet": "Labrador", "text": "Best grooming service in Chandigarh. Affordable and the results are amazing.", "stars": 5},
]

bookings = []

@app.route("/")
def home():
    return render_template("index.html", services=services, testimonials=testimonials)

@app.route("/book", methods=["POST"])
def book():
    data = request.json
    bookings.append(data)
    return jsonify({"success": True, "message": f"Booking confirmed for {data.get('pet_name', 'your pet')}! We'll see you soon 🐾"})

if __name__ == "__main__":
    app.run(debug=True, port=5050)
