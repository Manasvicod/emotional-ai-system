Error Analysis

Failure Cases

1. Short text input → wrong emotion
2. Mixed emotions → model predicts dominant only
3. Sarcasm not detected
4. Low-quality reflection → poor prediction
5. Noisy categorical inputs
6. Extreme stress + happy text mismatch
7. Ambiguous mood words
8. Missing values
9. Similar classes (sad vs tired)
10. Imbalanced dataset bias

Insights
* Model struggles with:

  * Ambiguity
  * Multi-emotion context
  * Sparse text

* Numeric features (stress, energy) strongly influence prediction

* Confidence score helps identify unreliable predictions

 Improvements
* Use NLP embeddings (BERT)
* Handle multi-label emotions
* Add more training data
* Improve feature scaling
