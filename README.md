# Medzilla - Risk Analysis

## Overview
Medzilla is a high-performance, AI-driven medical triage and risk escalation platform. Designed to minimize Time-to-Triage (TTT) in high-stakes emergency environments, Medzilla uses a hybrid pipeline combining Natural Language Processing (NLP) with deterministic Emergency Severity Index (ESI) protocols to instantly evaluate raw patient symptoms. 

This architecture ensures critical, life-threatening conditions (Level 1/Level 2 emergencies) bypass probabilistic machine learning models and trigger immediate escalation, while non-critical cases are safely queued for advanced risk probability analysis.

## Current Architecture
The system is built on a decoupled, micro-frontend architecture for maximum resilience and speed:

* **Frontend (The Patient Kiosk):** A frictionless, login-free web interface built with pure HTML, CSS, and Vanilla JavaScript. It features a "Clinical Stealth" monochromatic carbon-fiber design and utilizes the Comfortaa typeface for optimal readability under high cognitive load.
* **API Gateway:** A Python Flask REST API handling cross-origin (CORS) asynchronous requests from the client.
* **The NLP Bouncer (Pre-Screener):** Powered by SpaCy's `en_core_web_md` word vector embeddings. It translates raw, colloquial patient inputs into standardized medical terminology using a 0.75 semantic similarity threshold.
* **ESI Deterministic Engine:** A hardcoded, rule-based clinical engine that checks standardized symptoms against official Emergency Severity Index protocols (Trauma, Sepsis, Cardiac, Neurological, Toxicology).

## Key Features Developed
1.  **Frictionless Ingestion:** Zero authentication barriers to ensure immediate patient data entry during active emergencies.
2.  **Semantic Translation:** Automatically maps chaotic symptom descriptions (e.g., "my head is pounding") to clinical ontology.
3.  **Titanium Triage Rules:** Instantly flags critical conditions like strokes, internal hemorrhaging, and airway collapse.
4.  **Asynchronous Communication:** Uses modern JS Fetch API to interact with the Python backend without page reloads.

## Installation & Setup
To run the Medzilla ecosystem locally:

1.  **Activate the Python Virtual Environment:**
    `source venv/bin/activate` (Linux/WSL) or `venv\Scripts\activate` (Windows)
2.  **Install Backend Dependencies:**
    `pip install -r backend/requirements.txt`
3.  **Boot the Flask Server (Port 5000):**
    `python backend/app.py`
4.  **Launch the Patient Kiosk:**
    Open `frontend/public/index.html` via VS Code Live Server or a local HTTP server.

## Roadmap & Next Steps
* **Phase 1 (Complete):** NLP Vectorization & ESI-Compliant Bouncer.
* **Phase 2 (In Progress):** Tabular Data Ingestion & Feature Selection.
* **Phase 3:** Training and serializing a Scikit-Learn Random Forest Classifier to calculate exact risk probabilities for non-emergency patients.
* **Phase 4:** Development of the secure Doctor's Command Center (Admin Dashboard) with live Kanban sorting.
* **Phase 5:** Integration of real-time Computer Vision (OpenCV) for behavioral distress and facial drooping analysis.