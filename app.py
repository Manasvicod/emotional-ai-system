from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# ----------------------------
# LOAD MODEL
# ----------------------------
model = joblib.load("model_state.pkl")

# ----------------------------
# DECISION FUNCTION
# ----------------------------
def decide_action(state, stress, energy):
    
    if stress >= 8:
        return "box_breathing", "now"
    
    if state in ["sad","lonely"]:
        return "journaling", "now"
    
    if state == "anxious":
        return "grounding", "now"
    
    if energy >= 7:
        return "deep_work", "now"
    
    if energy <= 3:
        return "rest", "later_today"
    
    return "light_planning", "within_15_min"

# ----------------------------
# SUPPORT MESSAGE
# ----------------------------
def generate_message(state):
    
    if state == "sad":
        return "It's okay to feel low. Try writing your thoughts."
    
    if state == "anxious":
        return "Take a deep breath. Focus on the present moment."
    
    if state == "happy":
        return "Great to hear! Keep it up."
    
    if state == "angry":
        return "Pause and take a few slow breaths."
    
    return "You're doing your best. Keep going."

# ----------------------------
# HOME ROUTE
# ----------------------------
@app.route("/")
def home():
    return "Emotion AI API Running 🚀"

# ----------------------------
# PREDICT ROUTE (GET for demo)
# ----------------------------
@app.route("/predict", methods=["GET"])
def predict():
    
    # Demo input (browser friendly)
    data = {
        "journal_text": "I feel stressed and tired today",
        "sleep_hours": 5,
        "energy_level": 3,
        "stress_level": 8,
        "duration_min": 10,
        "ambience_type": "home",
        "time_of_day": "morning",
        "previous_day_mood": "neutral",
        "face_emotion_hint": "tired",
        "reflection_quality": "low"
    }
    
    df = pd.DataFrame([data])
    
    # Prediction
    pred = model.predict(df)[0]
    
    # Confidence
    probs = model.predict_proba(df)
    confidence = float(np.max(probs))
    uncertain_flag = int(confidence < 0.6)
    
    # Decision
    action, when = decide_action(pred, data["stress_level"], data["energy_level"])
    
    # Message
    message = generate_message(pred)
    
    return jsonify({
        "predicted_state": pred,
        "confidence": round(confidence, 2),
        "uncertain_flag": uncertain_flag,
        "what_to_do": action,
        "when_to_do": when,
        "support_message": message
    })

# ----------------------------
# RUN APP
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)