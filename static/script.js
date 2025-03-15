document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const age = document.getElementById('age').value;
    const sex = document.getElementById('sex').value;
    const bmi = document.getElementById('bmi').value;
    const children = document.getElementById('children').value;
    const smoker = document.getElementById('smoker').value === 'yes' ? 1 : 0;
    const region = document.getElementById('region').value;

    const data = {
        age: parseInt(age),
        sex: sex,
        bmi: parseFloat(bmi),
        children: parseInt(children),
        smoker: smoker,
        region: region
    };

    try {
        console.log('Sending request:', data);
        const response = await fetch('https://insurance-cost-prediction-app.nn.r.appspot.com/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        console.log('Response status:', response.status);
        const result = await response.json();
        console.log('Response data:', result);

        if (response.ok) {
            document.getElementById('result').innerText = `Predicted Cost: $${result.predicted_cost || 'No data'}`;
        } else {
            document.getElementById('result').innerText = `Error: ${result.error || 'Unknown error'}`;
        }
    } catch (error) {
        console.error('Fetch error:', error);
        document.getElementById('result').innerText = `Error: ${error.message}`;
    }
});