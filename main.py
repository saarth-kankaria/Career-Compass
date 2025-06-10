from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get("OPENROUTER_API_KEY")

# OpenRouter endpoint and headers
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "http://localhost:5000",  # Optional
    "X-Title": "CareerFinderApp"
}

def query_openrouter(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful and realistic career advisor. Suggest exactly 3 career options in raw plain text."},
        {"role": "user", "content": prompt}
    ]

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 1000
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

@app.route("/")
def landing_page():
    return render_template("home.html")

@app.route("/career")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    # Format user input as a prompt
    prompt = (
        f"Favourite Subject: {data.get('favSubject', '')}\n"
        f"Strongest Subject: {data.get('strongSubject', '')}\n"
        f"Hobbies: {data.get('hobbies', '')}\n"
        f"Preferred industries: {data.get('industries', '')}\n"
        f"Target Salary Range: {data.get('salary', '')}\n"
        f"Preferred Weekly Hours: {data.get('hours', '')}\n"
        f"Skills: {data.get('skills', '')}\n"
        f"Remote or In-Person: {data.get('remote', '')}\n"
        f"Current Education Level: {data.get('curEdu', '')}\n"
        f"Max Education Willing to Complete: {data.get('finalEdu', '')}\n"
        f"Preferred Work Environment: {data.get('environment', '')}\n"
        f"Team or Solo Preference: {data.get('team', '')}\n"
        f"Other Notes: {data.get('extraInfo', '')}"
    )

    try:
        reply = query_openrouter(prompt)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT
    app.run(host="0.0.0.0", port=port, debug=True)
