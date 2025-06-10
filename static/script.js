const steps = document.querySelectorAll(".form-step");
const nextBtns = document.querySelectorAll(".next");
const prevBtns = document.querySelectorAll(".prev");
const form = document.getElementById("careerForm");
const result = document.getElementById("result");
const submitBtn = document.getElementById("submit-btn");

let currentStep = 0;


// Form step navigation
nextBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    steps[currentStep].classList.remove("active");
    currentStep++;
    steps[currentStep].classList.add("active");
  });
});


prevBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    steps[currentStep].classList.remove("active");
    currentStep--;
    steps[currentStep].classList.add("active");
  });
});


form.addEventListener("submit", async (e) => {
  e.preventDefault();

  // Disable the submit button to prevent multiple clicks
  submitBtn.disabled = true;
  submitBtn.textContent = "Submitting...";

  const formData = new FormData(form);
  const data = Object.fromEntries(formData.entries());

  result.innerHTML = `<p>Loading career suggestions...</p>`;

  try {
    const response = await fetch("/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const resultData = await response.json();

    // Advance to result step
    steps[currentStep].classList.remove("active");
    currentStep++;
    steps[currentStep].classList.add("active");

    result.innerHTML = `
      <h3>Career Suggestions:</h3>
      <pre style="white-space: pre-wrap; font-family: inherit; line-height: 1.5;">
${resultData.reply}
      </pre>
    `;
  } catch (error) {
    result.innerHTML = `<p style="color: red;">Error fetching career suggestions. Please try again later.</p>`;
    console.error("Error:", error);
  } finally {
    // Re-enable the submit button in case of retry or reload
    submitBtn.disabled = false;
    submitBtn.textContent = "Submit";
  }
});


// Restart form
document.querySelector(".restart")?.addEventListener("click", () => {
  steps[currentStep].classList.remove("active");
  currentStep = 0;
  steps[currentStep].classList.add("active");
  form.reset();
  result.innerHTML = "";
});
