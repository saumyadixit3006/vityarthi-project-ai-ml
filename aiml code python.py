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
    print("⚠️ Reduce food preparation (low attendance expected)")
else:
    print("✅ Maintain or increase preparation")