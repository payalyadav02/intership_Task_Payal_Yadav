document.addEventListener("DOMContentLoaded", () => {
    let time = 15;
    const timerElement = document.getElementById("time");
  
    const interval = setInterval(() => {
      time--;
      timerElement.textContent = time;
      if (time <= 0) {
        clearInterval(interval);
        alert("Time's up! Moving to the next question.");
        window.location.href = "question2.html"; 
      }
    }, 1000);
  });
  