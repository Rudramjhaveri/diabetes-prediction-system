document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    const resultDiv = document.getElementById('result');
    const predictionText = document.getElementById('predictionText');

    // Add smooth animations for input focus
    const formControls = document.querySelectorAll('.form-control, .form-select');
    formControls.forEach(control => {
        control.addEventListener('focus', function() {
            this.closest('.mb-3').style.transform = 'translateX(5px)';
            this.style.transition = 'all 0.3s ease';
        });

        control.addEventListener('blur', function() {
            this.closest('.mb-3').style.transform = 'translateX(0)';
        });
    });

    // Add input validation for numeric fields
    const numericInputs = {
        'age': { min: 0, max: 120 },
        'bmi': { min: 10, max: 100 },
        'HbA1c_level': { min: 3, max: 15 },
        'blood_glucose_level': { min: 50, max: 500 }
    };

    Object.entries(numericInputs).forEach(([inputId, limits]) => {
        const input = document.getElementById(inputId);
        if (input) {
            input.addEventListener('input', function() {
                let value = parseFloat(this.value);
                if (value < limits.min) this.value = limits.min;
                if (value > limits.max) this.value = limits.max;
            });
        }
    });

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Show loading state with animation
        const submitButton = form.querySelector('button[type="submit"]');
        const originalButtonText = submitButton.innerHTML;
        submitButton.innerHTML = `
            <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
            Analyzing...
        `;
        submitButton.disabled = true;

        try {
            const formData = new FormData(form);
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (response.ok) {
                resultDiv.style.display = 'block';
                const prediction = data.prediction === 1 ? 'High Risk' : 'Low Risk';
                const probability = data.probability;
                
                let resultMessage = `
                    <div class="prediction-result">
                        <p class="mb-3">Based on the provided information, the analysis indicates a 
                            <strong class="${data.prediction === 1 ? 'text-warning' : 'text-success'}">${prediction}</strong> 
                            of diabetes with a probability of <strong>${probability}%</strong>.
                        </p>
                `;

                if (data.prediction === 1) {
                    resultMessage += `
                        <div class="alert alert-warning mt-3">
                            <h5 class="alert-heading"><i class="bi bi-exclamation-triangle me-2"></i>Important Notice</h5>
                            <ul class="mb-0">
                                <li>This is a screening tool and not a medical diagnosis.</li>
                                <li>Please consult with a healthcare professional for proper medical advice.</li>
                                <li>Regular check-ups and lifestyle management are important for diabetes prevention.</li>
                            </ul>
                        </div>
                    `;
                } else {
                    resultMessage += `
                        <div class="alert alert-success mt-3">
                            <h5 class="alert-heading"><i class="bi bi-check-circle me-2"></i>Healthy Lifestyle Tips</h5>
                            <ul class="mb-0">
                                <li>Maintain regular physical activity (150+ minutes per week)</li>
                                <li>Follow a balanced, nutritious diet</li>
                                <li>Schedule regular health check-ups</li>
                                <li>Monitor your blood sugar levels periodically</li>
                            </ul>
                        </div>
                    `;
                }

                resultMessage += '</div>';
                predictionText.innerHTML = resultMessage;
                
                // Smooth scroll to results with highlight animation
                resultDiv.scrollIntoView({ behavior: 'smooth' });
                resultDiv.style.animation = 'slideIn 0.5s ease';
            } else {
                throw new Error(data.error || 'Prediction failed');
            }
        } catch (error) {
            resultDiv.style.display = 'block';
            predictionText.innerHTML = `
                <div class="alert alert-danger">
                    <h5 class="alert-heading"><i class="bi bi-x-circle me-2"></i>Error</h5>
                    <p class="mb-0">${error.message}</p>
                    <hr>
                    <p class="mb-0">Please try again or contact support if the problem persists.</p>
                </div>
            `;
        } finally {
            // Restore button state with smooth transition
            setTimeout(() => {
                submitButton.innerHTML = originalButtonText;
                submitButton.disabled = false;
            }, 500);
        }
    });
}); 