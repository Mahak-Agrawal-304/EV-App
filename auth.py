from flask import Flask, request, jsonify, render_template, session, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
app.secret_key = "e9f1a3b7c2e84d1d86e7df0c4a6789f120cbb89e5f843f3c74a8a776bc9ff2a5"  # Required for Flask sessions


# Initialize Firebase
cred = credentials.Certificate("ev-navigation-app-firebase-adminsdk-fbsvc-77344df7be.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/", methods=["GET", "POST"])
def login_register():
    if request.method == "GET":
        return render_template("login.html")  # Ensure login.html is inside "templates" folder

    data = request.json
    print(f"Received Data: {data}")  # Debugging

    action = data.get("action")  # Determines if it's login or register
    station_id = data.get("station_id")
    access_key = data.get("access_key")

    if not station_id or not access_key:
        return jsonify({"error": "Missing credentials!"}), 400

    doc_ref = db.collection("charging_stations").document(station_id)

    if action == "login":
        doc = doc_ref.get()
        if doc.exists:
            station_data = doc.to_dict()
            if station_data["access_key"] == access_key:
                session["station_id"] = station_id  # Store station_id in the session
                return jsonify({
                    "message": "Login successful!", 
                    "station_data": station_data,
                    "redirect": "/dashboard"  # Optional: instruct the frontend to redirect
                }), 200
            return jsonify({"error": "Invalid access key!"}), 401
        return jsonify({"error": "Station ID not found!"}), 404

    elif action == "register":
        name = data.get("name")
        if not name:
            return jsonify({"error": "Missing station name!"}), 400

        if doc_ref.get().exists:
            return jsonify({"error": "Station ID already exists!"}), 400

        doc_ref.set({
            "station_id": station_id,
            "access_key": access_key,
            "name": name
        })
        return jsonify({"message": "Registration successful!"}), 201

    return jsonify({"error": "Invalid action!"}), 400

@app.route("/dashboard")
def dashboard():
    if "station_id" not in session:
        print("No station_id found in session!")  # Debugging
        return redirect(url_for("login_register"))  # Redirect to login if session is missing

    station_id = session["station_id"]
    print(f"Station ID from session: {station_id}")  # Debugging

    doc_ref = db.collection("charging_stations").document(station_id)
    doc = doc_ref.get()

    if doc.exists:
        station_data = doc.to_dict()
        return render_template("dashboard.html", station=station_data)  # ✅ Pass station data
    else:
        return "Error: Station not found", 404


@app.route("/update_station", methods=["POST"])
def update_station():
    if "station_id" not in session:
        return jsonify({"error": "Not logged in!"}), 403

    data = request.json
    station_id = session["station_id"]

    # Prepare update data from the form (ensure keys match what your JS sends)
    update_data = {
        "name": data.get("stationName"),
        "operator": data.get("operatorName"),
        "charging_type": data.get("chargingType"),
        "location": data.get("location"),
        "total_slots": int(data.get("totalSlots")),
        "available_slots": int(data.get("availableSlots")),
        "charging_rate": int(data.get("chargingRate"))
    }

    try:
        doc_ref = db.collection("charging_stations").document(station_id)
        doc_ref.update(update_data)
        return jsonify({"message": "Station details updated successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
if __name__ == "__main__":
    app.run(debug=True)
