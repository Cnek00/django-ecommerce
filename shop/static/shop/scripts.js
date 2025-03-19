document.addEventListener("DOMContentLoaded", function () {
     console.log("Neon tema aktif!");
 
     // Smooth Scrolling
     document.querySelectorAll('a[href^="#"]').forEach(anchor => {
         anchor.addEventListener("click", function (e) {
             e.preventDefault();
             document.querySelector(this.getAttribute("href")).scrollIntoView({
                 behavior: "smooth"
             });
         });
     });
 
     // Neon Glow Efekti
     const neonTexts = document.querySelectorAll(".neon-text");
     neonTexts.forEach(text => {
         text.addEventListener("mouseover", () => {
             text.style.color = "#ff0099";
         });
         text.addEventListener("mouseleave", () => {
             text.style.color = "#9d00ff";
         });
     });
 
     // Kart Hover Efekti
     const neonCards = document.querySelectorAll(".neon-card");
     neonCards.forEach(card => {
         card.addEventListener("mouseover", () => {
             card.style.transform = "scale(1.05)";
         });
         card.addEventListener("mouseleave", () => {
             card.style.transform = "scale(1)";
         });
     });
 
     // Buton Animasyonları
     const neonButtons = document.querySelectorAll(".neon-btn");
     neonButtons.forEach(button => {
         button.addEventListener("mouseover", () => {
             button.style.boxShadow = "0px 0px 15px #ff0099";
         });
         button.addEventListener("mouseleave", () => {
             button.style.boxShadow = "0px 0px 10px #9d00ff";
         });
     });
 
     // Favori Buton Efekti
     const favButtons = document.querySelectorAll(".fav-btn");
     favButtons.forEach(btn => {
         btn.addEventListener("mouseover", () => {
             btn.style.textShadow = "0px 0px 10px #ff0099";
         });
         btn.addEventListener("mouseleave", () => {
             btn.style.textShadow = "none";
         });
     });
     const showMoreBtn = document.getElementById("show-more-reviews");
     if (showMoreBtn) {
         showMoreBtn.addEventListener("click", function () {
             fetch(window.location.href + "?show_all_reviews=true")
                 .then(response => response.text())
                 .then(data => {
                     const parser = new DOMParser();
                     const doc = parser.parseFromString(data, "text/html");
                     const newReviews = doc.querySelector("#review-container").innerHTML;
                     document.getElementById("review-container").innerHTML = newReviews;
                     showMoreBtn.style.display = "none";
                 });
         });
     }

 });
 
 document.addEventListener("DOMContentLoaded", function () {
     const showMoreBtn = document.getElementById("show-more-reviews");
     if (showMoreBtn) {
         showMoreBtn.addEventListener("click", function () {
             fetch(window.location.href + "?show_all_reviews=true")
                 .then(response => response.text())
                 .then(data => {
                     const parser = new DOMParser();
                     const doc = parser.parseFromString(data, "text/html");
                     const newReviews = doc.querySelector("#review-container").innerHTML;
                     document.getElementById("review-container").innerHTML = newReviews;
                     showMoreBtn.style.display = "none";  // Butonu gizle
                 });
         });
     }
 });
 
