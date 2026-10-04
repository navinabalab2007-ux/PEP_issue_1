const form = document.getElementById("resumeForm");
const result = document.getElementById("result");
const prediction = document.getElementById("prediction");
const fitScore = document.getElementById("fitScore");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const resumeFile = document.getElementById("resume").files[0];
    const jobDescription = document.getElementById("jobDescription").value;

    const formData = new FormData();

    if (resumeFile) {
        formData.append("resume", resumeFile);
    }

    formData.append("job_description", jobDescription);

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/analyze-resume",
            {
                method: "POST",
                body: formData
            }
        );

        if (!response.ok) {
            throw new Error("Analysis request failed");
        }

        const data = await response.json();

        prediction.textContent = `Prediction: ${data.prediction}`;
        fitScore.textContent = `Fit Score: ${data.fit_score}%`;

        result.style.display = "block";

    } catch (error) {
        prediction.textContent = "Error connecting to the backend.";
        fitScore.textContent = "";
        result.style.display = "block";

        console.error(error);
    }
});