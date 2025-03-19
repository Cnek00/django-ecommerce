document.addEventListener("DOMContentLoaded", function () {
     const showMoreBtn = document.getElementById("show-more-reviews");
     const hiddenReviews = document.getElementById("hidden-reviews");
 
     if (showMoreBtn) {
         showMoreBtn.addEventListener("click", function () {
             if (hiddenReviews.style.display === "none") {
                 hiddenReviews.style.display = "block";
                 showMoreBtn.textContent = "Daha Az Yorum Göster";
             } else {
                 hiddenReviews.style.display = "none";
                 showMoreBtn.textContent = "Daha Fazla Yorum Göster";
             }
         });
     }
 });
 