# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from clinical_rules import check_red_flags, standardize_symptoms_nlp

app = Flask(__name__)
# CORS allows our frontend React/HTML files to talk to this backend safely
CORS(app)

@app.route('/api/triage', methods=['POST'])
def run_triage_engine():
    """
    The main API endpoint. Receives raw symptoms from the web, 
    runs the NLP bouncer, and sends the decision back.
    """
    # 1. Grab the JSON data sent from the HTML page
    data = request.json
    raw_symptoms_string = data.get('symptoms', '')
    
    if not raw_symptoms_string.strip():
        return jsonify({
            "error": True,
            "message": "No symptoms provided. The bouncer needs data!"
        }), 400
        
    # 2. Convert the comma-separated string into a clean list
    patient_symptoms = [sym.strip() for sym in raw_symptoms_string.split(',')]
    
    # 3. Run the ML NLP Bouncer
    decision = check_red_flags(patient_symptoms, debug=False)
    
    # 4. Get the standardized terms so we can show the user what the AI understood
    standardized = standardize_symptoms_nlp(patient_symptoms, debug=False)
    decision['standardized_symptoms'] = standardized
    decision['error'] = False
    
    # 5. Blast the result back to the frontend
    return jsonify(decision)

if __name__ == '__main__':
    print("🚀 Firing up the Smart Triage Web Server on Port 5000...")
    app.run(debug=True, port=5000)