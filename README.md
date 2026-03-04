# Smart Emergency Triage & Risk Escalation System



## Overview
The Smart Emergency Triage & Risk Escalation System is a web-based clinical decision support application designed to alleviate emergency department overcrowding. By analyzing patient symptoms, demographic data, and basic health indicators, the system provides a transparent, AI-assisted estimation of medical risk and categorizes the urgency of care required. 

This project operates on a hybrid architecture, bridging the gap between digital symptom checkers and clinical diagnosis by utilizing definitive rule-based safety checks alongside a machine learning prediction model.

## Core Features
* **Rule-Based Red Flag Detection:** Instantly identifies critical symptom combinations (e.g., chest pain and shortness of breath) to bypass standard evaluation and immediately recommend emergency care.
* **Machine Learning Risk Model:** Evaluates non-critical symptom combinations, demographics, and vitals using lightweight ML models (Random Forest / Logistic Regression) to output a calibrated risk probability score.
* **Explainable AI (XAI) Layer:** Utilizes SHAP (SHapley Additive exPlanations) to provide transparent reasoning for every triage recommendation, building clinical trust and user comprehension.
* **Actionable Urgency Mapping:** Translates technical risk scores into clear, actionable directives: Home Care, Clinic Visit, or Emergency Care.

## Technology Stack
* **Frontend:** React, HTML, CSS, JavaScript
* **Backend:** Python, Flask (or FastAPI)
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Explainability:** SHAP

## Current Project Status: Active Development (Phase 1)
The project is currently in the initial scaffolding and architecture phase. 

**Completed Milestones:**
* Repository initialized and directory structure established.
* Separation of concerns implemented (isolated frontend UI, backend API, and ML engine environments).
* High-level system architecture and clinical urgency mapping finalized.

**Immediate Next Steps (In Progress):**
* Development of the `clinical_rules.py` hardcoded triage engine.
* Training and serialization of the initial ML model using public healthcare datasets.
* Building the React functional components for the user input form.

## Local Setup & Installation (Coming Soon)
*(Instructions for `pip install -r requirements.txt` and `npm install` will be populated here once the dependency trees are finalized in the upcoming commits.)*

## Disclaimer
This system is a proof-of-concept designed for hackathon demonstration purposes. It is a decision-support tool and does not provide definitive medical diagnoses. Users experiencing severe symptoms should contact emergency services immediately.