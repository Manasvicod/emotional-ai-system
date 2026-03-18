# Edge Deployment Plan

Deployment Approach

* Backend: Flask API
* Hosting options:
* Render / Railway / AWS
* Endpoint:
* /predict

Optimizations

* Use lightweight model (RandomForest / Logistic)
* Reduce feature size
* Cache predictions if needed

 UI Integration

* Simple frontend:
* Streamlit / HTML form
* User inputs → API → Output display

 Future Improvements

* Real-time emotion tracking
* Mobile app integration
* Voice + facial input
* Personalization

 Edge Cases Handling

* Missing inputs → default values
* Low confidence → fallback suggestion
* Invalid input → validation layer


