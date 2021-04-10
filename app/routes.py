from app import app, db
from flask import render_template, request, jsonify
from app.models import Trip
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['GET']
def calculate(starttime, stoptime):
    trip = Trip.query.all()
    trip_mean = sum(trip) / len(trip)
   
    return jsonify(trip_mean)

    