 document.addEventListener("DOMContentLoaded", () => {
     const themeToggle = document.getElementById("theme-toggle");
     const htmlElement = document.documentElement;
 
      // Önceden kaydedilmiş tema varsa uygula
     const savedTheme = localStorage.getItem("theme") || "light";
     htmlElement.setAttribute("data-theme", savedTheme);
 
      // Tema butonu tıklandığında değiştir
     themeToggle.addEventListener("click", () => {
          let currentTheme = htmlElement.getAttribute("data-theme");
          let newTheme = currentTheme === "light" ? "dark" : "light";
          htmlElement.setAttribute("data-theme", newTheme);          
          localStorage.setItem("theme", newTheme);      
     });
});       
 