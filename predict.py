import numpy as np
import tensorflow as tf
import pickle
import json
import random
import re

# Load trained model
model = tf.keras.models.load_model("model/chatbot_model.keras")

# Load vectorizer and label encoder
with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

#Load intents
with open("data/intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

user_states = {}
user_data = {}

#Intent prediction
def predict_intent(text):
    X = vectorizer.transform([text]).toarray()
    prediction = model.predict(X, verbose = 0)
    tag_index = np.argmax(prediction)
    tag = label_encoder.inverse_transform([tag_index])[0]
    confidence = np.max(prediction)
    return tag, confidence

#Response from intent prediction
def get_response(tag):
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "Sorry, I don't understand."

#BMI function
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

#Calorie function
def calculate_calories(weight, height, age, gender):
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return round(bmr)

def get_bot_response(user_input, user_id="default"):

    state = user_states.get(user_id)

    #BMI flow
    if state == "bmi_height":

        user_data[user_id] = {"height": float(user_input)}
        user_states[user_id] = "bmi_weight"
        return "Enter your weight in kg"

    if state == "bmi_weight":

        user_data[user_id]["weight"] = float(user_input)

        height = user_data[user_id]["height"]
        weight = user_data[user_id]["weight"]

        bmi = calculate_bmi(height, weight)

        user_states[user_id] = None

        return f"Your BMI is {bmi}"


    #Calorie flow
    if state == "calorie_weight":

        user_data[user_id] = {"weight": float(user_input)}
        user_states[user_id] = "calorie_height"

        return "Enter your height in cm"

    if state == "calorie_height":

        user_data[user_id]["height"] = float(user_input)
        user_states[user_id] = "calorie_age"

        return "Enter your age"

    if state == "calorie_age":

        user_data[user_id]["age"] = int(user_input)
        user_states[user_id] = "calorie_gender"

        return "Enter your gender (male/female)"

    if state == "calorie_gender":

        user_data[user_id]["gender"] = user_input

        data = user_data[user_id]

        calories = calculate_calories(
            data["weight"],
            data["height"],
            data["age"],
            data["gender"]
        )

        user_states[user_id] = None

        return f"Your estimated daily calorie requirement is {calories} kcal"


    #Normal intent
    tag, confidence = predict_intent(user_input)

    if confidence < 0.5:
        return "I'm not sure I understand that. Here's what I can help you with:\n\n**Fitness Goals**\n- Weight loss tips and fat burning\n- Muscle gain and bulking advice\n\n**Workouts**\n- Home workouts (no equipment)\n- Gym workout plans and splits\n\n**Nutrition**\n- Calorie calculation and daily intake\n- Protein sources and high-protein foods\n- Supplement advice (whey, creatine, etc.)\n\n**Calculators**\n- BMI calculation\n- Daily calorie and protein needs\n\n**Motivation**\n- Staying consistent and disciplined\n- Getting back on track\n\nTry asking something like \"How do I lose weight?\" or \"Give me a gym workout plan\"!"

    if tag == "bmi_calculation":
        user_states[user_id] = "bmi_height"
        return "Sure! What is your height in cm?"

    if tag == "calorie_calculation":
        user_states[user_id] = "calorie_weight"
        return "Let's calculate your calories. Enter your weight in kg"

    return get_response(tag)

