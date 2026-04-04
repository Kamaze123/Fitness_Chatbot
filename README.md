# FitBuddy

A deep learning trained model that helps users with workout plans, nutrition advice, BMI calculation and calorie estimation. Built with a React frontend and a Flask backend using a trained machine learning model for intent classification.

---

## Live Demo

- **Website:** [https://fitbuddy-snowy.vercel.app]

---

## Features

- **Intent classification** using a TF-IDF + Naive Bayes ML model trained on custom fitness data
- **Weight loss & muscle gain** advice with workout plans
- **BMI calculator** - conversational multi-step flow
- **Calorie calculator** - estimates daily calorie needs based on weight, height, and age
- **Protein sources** - animal-based and plant-based options
- **Gym & home workout plans** - beginner-friendly routines
- **Supplement advice** 
- **Motivation**

---

## Tech Stack

**Frontend**
- React
- Tailwind CSS
- Deployed on Vercel

**Backend**
- Python + Flask
- scikit-learn (TF-IDF vectorizer + Multinomial Naive Bayes)
- Deployed on Render

---

## Project Structure

```
Fitness_Chatbot/
├── chatbot-backend/
│   ├── data/
│   │   └── intents.json        # Training data
│   ├── model/
│   │   ├── chatbot_model.pkl   # Trained sklearn pipeline
│   │   └── label_encoder.pkl  # Label encoder
│   ├── app.py                  # Flask API
│   ├── predict.py              # Inference logic
│   ├── train.py                # Model training script
│   ├── utils.py                # Helper functions
│   └── requirements.txt
├── chatbot-frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatBox.jsx
│   │   │   ├── ChatInput.jsx
│   │   │   └── MessageBubble.jsx
│   │   └── App.jsx
│   └── package.json
└── README.md
```

---

## Getting Started

### Backend

```bash
cd chatbot-backend
pip install -r requirements.txt
python train.py        # Train the model
python app.py          # Run the Flask server
```

### Frontend

```bash
cd chatbot-frontend
npm install
npm run dev
```

Make sure the backend URL in `ChatBox.jsx` points to your Flask server.

---

## API

### POST `/chat`

**Request:**
```json
{
  "message": "How do I lose weight?"
}
```

**Response:**
```json
{
  "response": "To lose weight effectively: ..."
}
```

---

## Model

The intent classifier is a scikit-learn pipeline consisting of a TF-IDF vectorizer (bigrams, 500 features) and a Multinomial Naive Bayes classifier. It is trained on a custom dataset of ~470 fitness-related patterns across 11 intents.

| Intent | Examples |
|---|---|
| greeting | Hi, Hello, Hey |
| goodbye | Bye, See you, Take care |
| weight_loss | How do I lose weight?, Burn fat tips |
| muscle_gain | How to build muscle?, I want to bulk up |
| bmi_calculation | Calculate my BMI, Is my BMI healthy? |
| calorie_calculation | How many calories should I eat? |
| protein_sources | Best protein foods, Vegetarian protein |
| home_workout | Workout at home, No equipment exercises |
| gym_workout | Gym split routine, PPL workout plan |
| supplements | Should I take creatine?, Whey protein advice |
| motivation | I feel lazy, I want to quit gym |

---

## Acknowledgements

Built as a personal project to learn ML model deployment with a full-stack web application. Initially done using neural networks with tensorflow, test accuracy upto 85 percent. But render didn't support tensorflow deployment, hence I switched to a different learning model. This model has test accuracy of 75-80 percent. I was disappointed that I wasn't able to use my initial model but I guess that's part of life. 
