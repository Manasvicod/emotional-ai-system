Emotion AI System

 Overview

This project predicts a user's emotional state using behavioral and contextual features, and provides actionable recommendations along with supportive messages.

Setup Instructions

bash
 Create environment (optional)
conda create -n emotion python=3.9 -y
conda activate emotion

Install dependencies
pip install flask pandas numpy scikit-learn joblib


  Approach

1. Data preprocessing and feature engineering
2. Train ML models for:

   * Emotional State (classification)
   * Intensity (optional)
3. Add decision logic (rule-based)
4. Add uncertainty handling using prediction probability
5. Deploy via Flask API



 Feature Engineering

* Text feature: `journal_text`
* Numeric features:

  * sleep_hours
  * energy_level
  * stress_level
  * duration_min
* Categorical:

  * ambience_type
  * time_of_day
  * previous_day_mood
  * face_emotion_hint
  * reflection_quality

Encoding:

Label Encoding / One-Hot Encoding



Model Choice

* RandomForestClassifier
* Reason:

  * Handles mixed data types
  * Robust to noise
  * Provides probability (for confidence)

How to Run

bash
python app.py


Open in browser:


http://127.0.0.1:5000/predict


 API Output json
{
  "predicted_state": "anxious",
  "confidence": 0.82,
  "uncertain_flag": 0,
  "what_to_do": "grounding",
  "when_to_do": "now",
  "support_message": "Take a deep breath."
}

Bonus Features

* Decision Engine (rule-based)
* Confidence-based uncertainty handling
* Supportive conversational layer
* Flask API deployment

  
