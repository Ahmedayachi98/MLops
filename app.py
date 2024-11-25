from flask import Flask, request, render_template
import pickle

# Load the model and vectorizer
with open('sentiment_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get text input from user
    text = request.form['text']
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]

    # Convert numeric prediction to sentiment label
    sentiment_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
    sentiment = sentiment_map.get(prediction, "Unknown")

    return render_template('index.html', prediction_text=f'Sentiment: {sentiment}')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)

#netstat -ano | findstr :5000
#taskkill /PID 32128 /F