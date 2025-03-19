 document.addEventListener("DOMContentLoaded", function() {
      let theme = localStorage.getItem("theme") || "light";
      document.documentElement.setAttribute("data-theme", theme);
      document.getElementById("themeStylesheet").setAttribute("href", `/static/shop/${theme}.css`);
     
      // Sayfa açılış animasyonu
      document.body.classList.add("fade-in");
});
 
  function toggleTheme() {
     let currentTheme = document.documentElement.getAttribute("data-theme");
     let newTheme = currentTheme === "light" ? "dark" : "light";
     document.documentElement.setAttribute("data-theme", newTheme);
     document.getElementById("themeStylesheet").setAttribute("href", `/static/shop/${newTheme}.css`);
     localStorage.setItem("theme", newTheme);
}
 