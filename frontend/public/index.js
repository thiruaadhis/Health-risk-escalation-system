// frontend/public/index.js

async function sendToAI() {
    const rawSymptoms = document.getElementById('symptomsInput').value;
    const resultBox = document.getElementById('resultBox');
    
    if (!rawSymptoms) {
        alert("System Error: No symptoms provided. Please enter patient data.");
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/api/triage', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ symptoms: rawSymptoms })
        });
        
        const data = await response.json();
        
        if (data.error) {
            alert(data.message);
            return;
        }

        document.getElementById('uiRisk').innerText = data.risk_level;
        document.getElementById('uiRec').innerText = data.recommendation;
        document.getElementById('uiReason').innerText = data.reason;
        
        if (data.risk_level === "High") {
            resultBox.classList.add('high-risk');
        } else {
            resultBox.classList.remove('high-risk');
        }

        resultBox.style.display = 'block';

    } catch (error) {
        console.error(error);
        alert("Connection Failed: Backend server is offline. Verify Flask is running.");
    }
}