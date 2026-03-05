# backend/clinical_rules.py
import spacy
import sys

# Load the NLP model with word vectors (Semantic Embeddings)
try:
    print("Booting up the NLP Neural Network... (This takes a second)")
    nlp = spacy.load("en_core_web_md")
    print("System Online. The Titanium Bouncer is ready.\n")
except OSError:
    print("Warning: spaCy model not found. Run 'python -m spacy download en_core_web_md' in terminal.")
    sys.exit()

# The Ultimate ESI-Backed Standardized Medical Ontology
STANDARD_SYMPTOMS = [
    # Neurological & Cognitive
    "headache", "severe headache", "dizziness", "confusion", "slurred speech", "facial drooping", 
    "weakness on one side", "weakness", "sudden numbness", "seizures", "tremors", "stiff neck",
    "loss of consciousness", "fainting", "head injury",
    
    # Cardiac & Respiratory
    "chest pain", "shortness of breath", "difficulty breathing", "palpitations", "rapid heart rate", 
    "cough", "wheezing", "sore throat", "runny nose", "bluish lips", "choking", "severe allergic reaction",
    
    # Gastrointestinal & Abdominal
    "abdominal pain", "severe abdominal pain", "nausea", "vomiting", "diarrhea", "constipation", 
    "loss of appetite", "heartburn",
    
    # Musculoskeletal & Skin
    "muscle pain", "joint pain", "leg swelling", "back pain", "cramps", 
    "rash", "itching", "bruising", "skin lesions",
    
    # Trauma & Bleeding
    "broken bone", "severe trauma", "uncontrollable bleeding", "severe burns",
    "coughing blood", "vomiting blood",
    
    # Systemic, General & Toxicology
    "high fever", "chills", "sweating", "fatigue", "unexplained weight loss", 
    "weight gain", "swallowed poison", "suicidal",
    
    # Urological & Sensory
    "painful urination", "urinary frequency", "vision changes", "blurry vision", "earache", "hearing loss"
]

def standardize_symptoms_nlp(raw_symptoms, debug=False):
    """
    Uses NLP Word Embeddings to map raw user input to standardized medical terms.
    """
    standardized = []
    similarity_threshold = 0.75  
    
    for raw_sym in raw_symptoms:
        raw_doc = nlp(raw_sym.lower().strip())
        best_match = raw_sym 
        highest_score = 0.0
        
        if debug:
            print(f"\n[NLP ENGINE] Analyzing Input: '{raw_doc.text}'")
            print("-" * 40)
            
        for standard_sym in STANDARD_SYMPTOMS:
            standard_doc = nlp(standard_sym)
            score = raw_doc.similarity(standard_doc)
            
            if debug and score > 0.4: 
                print(f"  -> vs '{standard_sym}': Score {score:.4f}")
                
            if score > highest_score and score >= similarity_threshold:
                highest_score = score
                best_match = standard_sym
                
        if debug:
            print("-" * 40)
            if best_match != raw_doc.text:
                print(f"  [WINNER] Translated '{raw_doc.text}' to -> '{best_match}'")
            else:
                print(f"  [NO MATCH] Kept original '{raw_doc.text}' (Failed to hit {similarity_threshold} threshold)")
                
        standardized.append(best_match)
        
    return list(set(standardized))

def check_red_flags(raw_symptoms, debug=False):
    """
    The ESI-Compliant Bouncer.
    Evaluates symptoms against Level 1 and Level 2 Emergency Severity Index protocols.
    """
    symptoms = standardize_symptoms_nlp(raw_symptoms, debug)
    
    # ESI Protocol Arrays
    airway_cardiac_flags = ["chest pain", "difficulty breathing", "shortness of breath", "bluish lips", "severe allergic reaction", "choking"]
    neuro_flags = ["slurred speech", "facial drooping", "weakness on one side", "sudden numbness", "loss of consciousness", "fainting", "seizures", "head injury", "severe headache"]
    trauma_blood_flags = ["uncontrollable bleeding", "coughing blood", "vomiting blood", "severe burns", "broken bone", "severe abdominal pain"]
    tox_systemic_flags = ["swallowed poison", "suicidal"]
    
    if debug:
        print(f"\n[BOUNCER ENGINE] Final Standardized List: {symptoms}\n")

    # 1. Airway & Cardiac Protocol (Immediate Level 1)
    if any(flag in symptoms for flag in airway_cardiac_flags):
        return {
            "risk_level": "High", 
            "recommendation": "Emergency Care", 
            "reason": "Critical airway, respiratory, or cardiac compromise detected. Immediate intervention required."
        }
    
    # 2. Neurological & Stroke Protocol (Level 1/2)
    if any(flag in symptoms for flag in neuro_flags):
         return {
             "risk_level": "High", 
             "recommendation": "Emergency Care", 
             "reason": "Symptoms align with severe neurological emergencies, potential stroke, or traumatic brain injury."
         }
         
    # 3. Severe Trauma & Hemorrhage Protocol (Level 1/2)
    if any(flag in symptoms for flag in trauma_blood_flags):
         return {
             "risk_level": "High", 
             "recommendation": "Emergency Care", 
             "reason": "Signs of severe physical trauma, internal/external hemorrhage, or acute surgical abdomen."
         }
         
    # 4. Toxicology & Psychiatric Protocol (Level 1/2)
    if any(flag in symptoms for flag in tox_systemic_flags):
         return {
             "risk_level": "High", 
             "recommendation": "Emergency Care", 
             "reason": "Toxic ingestion or psychiatric emergency detected requiring immediate stabilization."
         }

    # 5. Sepsis & Meningitis Protocol (Level 2)
    if "high fever" in symptoms and ("confusion" in symptoms or "stiff neck" in symptoms):
         return {
             "risk_level": "High", 
             "recommendation": "Emergency Care", 
             "reason": "Combination of fever with altered mental status or stiff neck indicates potential sepsis or meningitis."
         }

    # 6. Cleared for ML
    return {
        "risk_level": "Pending", 
        "recommendation": "Proceed to ML Model", 
        "reason": "No immediate critical ESI Level 1 or 2 flags detected. Escalating to ML risk assessment."
    }

if __name__ == "__main__":
    print("=== Triage Bouncer NLP Lab ===")
    print("Type your symptoms separated by commas")
    print("Type 'quit' or 'exit' to shut down the lab.")
    print("==============================\n")
    
    while True:
        user_input = input("\nPatient Symptoms > ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("Shutting down the NLP lab. Stay grinding!")
            break
            
        if not user_input.strip():
            continue
            
        patient_symptoms = [sym.strip() for sym in user_input.split(',')]
        result = check_red_flags(patient_symptoms, debug=True)
        
        print("\n[FINAL DECISION]")
        print(f"Risk Level: {result['risk_level']}")
        print(f"Recommendation: {result['recommendation']}")
        print(f"Reason: {result['reason']}")
        print("==============================\n")