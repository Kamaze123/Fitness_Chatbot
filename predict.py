import numpy as np
import tensorflow as tf
import pickle
import re

# Load trained model
model = tf.keras.models.load_model("model/chatbot_model.keras")

# Load vectorizer and label encoder
with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

conversation_state= None
user_data={}

#Intent prediction
def predict_intent(text):
    X = vectorizer.transform([text]).toarray()
    prediction = model.predict(X)
    tag_index = np.argmax(prediction)
    tag = label_encoder.inverse_transform([tag_index])[0]
    confidence = np.max(prediction)
    return tag, confidence

#BMI function
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

#Chat loop
print("Fitness Bot Ready! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    # ---- If waiting for height ----
    if conversation_state == "bmi_height":
        try:
            user_data["height"] = float(user_input)
            conversation_state = "bmi_weight"
            print("Bot: Enter your weight in kg:")
        except:
            print("Bot: Please enter a valid number for height.")
        continue

    # ---- If waiting for weight ----
    if conversation_state == "bmi_weight":
        try:
            user_data["weight"] = float(user_input)
            bmi = calculate_bmi(user_data["height"], user_data["weight"])

            print(f"Bot: Your BMI is {bmi}")

            if bmi < 18.5:
                print("Bot: You are underweight.")
            elif 18.5 <= bmi < 24.9:
                print("Bot: You are in the healthy range.")
            elif 25 <= bmi < 29.9:
                print("Bot: You are overweight.")
            else:
                print("Bot: You are obese.")

            conversation_state = None
            user_data = {}
        except:
            print("Bot: Please enter a valid number for weight.")
        continue

    # ---- Normal Intent Prediction ----
    tag, confidence = predict_intent(user_input)

    if confidence < 0.6:
        print("Bot: I'm not sure I understood that.")
        continue

    if tag == "bmi_calculation":
        print("Bot: Sure! What is your height in cm?")
        conversation_state = "bmi_height"
        continue

    # Default response
    print(f"Bot: Intent detected → {tag}")
