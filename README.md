# vityarthi-project-ai-ml

Name - Saumya Dixit
Registration no.-25BAI11460

Smart food waste reduction system

OVERVIEW

The Smart Food Waste Reduction System (SFWS) is a technological innovation to reduce food wastage in domestic, hostels and food serving institutions. This system involves real-time tracking and forecasting of food intake, and fostering responsible consumption of food resources.

OBJECTIVES

The key objectives of this project are:
To observe and record eating patterns.

How to minimize food Wastage through data analysis

So as to give usup-by-mortimatoesuggestions of how to use our food in the best way.

General General/in general With the aim of increasing the awareness of consumers about sustainable use

In order to enhance interaction between food providers and consumers

KEY FEATURES

Food Tracking System: Entries for the daily preparation and consumption of foods.

Waste Monitoring-Recording of the amount of wasted food; the system should allow the quantity of wasted food to be easily identified and stored.

Predictive Analysis: Proposes the right food requirements on the base of previous data.

User Feedback Module: Gathers user feed back to reduce erroneous system readings and improve accuracy of system.

Alerts and Notifications: Inform users if they prepare too much or there is likely to be too many leftovers.

TECHNOLOGIES USED

Frontend: HTML, CSS, JavaScript

Backend: Python

Database: SQLite / MySQL

Tools & Platforms: Visual Studio Code, GitHub

PROJECT STRUCTURE

smart-food-waste-reduction/
│── static/          # CSS and JavaScript files  
│── templates/       # HTML interface files  
│── database/        # Database storage  
│── app.py           # Main application logic  
│── README.md        # Project documentation

PYTHON CODE

import pandas as pd

from sklearn.tree import DecisionTreeRegressor

# Sample dataset
data = {
    "day": [1,2,3,4,5,6,7,1,2,3],
    "prev_attendance": [100,120,110,130,140,150,90,105,125,115],
    "event": [0,0,1,0,1,0,0,0,1,0],
    "attendance": [110,130,150,140,180,160,100,115,160,120]
}

df = pd.DataFrame(data)

X = df[["day","prev_attendance","event"]]

y = df["attendance"]

model = DecisionTreeRegressor()

model.fit(X, y)

# User input
day = int(input("Enter day (1=Mon ... 7=Sun): "))

prev = int(input("Enter yesterday attendance: "))

event = int(input("Any event today? (1=yes, 0=no): "))

user = pd.DataFrame({
    "day":[day],
    "prev_attendance":[prev],
    "event":[event]
})

predicted = int(model.predict(user)[0])

print("\nExpected Students:", predicted)

# Logic-based recommendation

food_per_student = 0.5  # kg

total_food = predicted * food_per_student

print("Prepare approx food (kg):", total_food)

if predicted < prev:

    print(" Reduce food preparation (low attendance expected)")
    
else:

    print("Maintain or increase preparation")


    CONCLUSION

    The Smart Food Waste Reduction System is an innovative method in addressing food wastage through combining the knowledge of technology and user awareness. It provides a good way of overcoming wasteful overproduction of food by promoting sensible consumption.
