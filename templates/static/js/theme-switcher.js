
document.addEventListener("DOMContentLoaded", function() {
    const themeToggleButton = document.getElementById("theme-toggle");
    const themeIcon = document.getElementById("theme-icon");
    const currentTheme = localStorage.getItem("theme");

    // Verificar o tema atual e aplicar a classe correta ao body
    if (currentTheme) {
        document.body.classList.add(currentTheme);
        themeIcon.className = currentTheme === "dark-theme" ? "fas fa-moon" : "fas fa-sun";
    } else {
        document.body.classList.add("light-theme");
        themeIcon.className = "fas fa-sun";
    }

    themeToggleButton.addEventListener("click", function() {
        if (document.body.classList.contains("light-theme")) {
            document.body.classList.remove("light-theme");
            document.body.classList.add("dark-theme");
            localStorage.setItem("theme", "dark-theme");
            themeIcon.className = "fas fa-moon"; // Ícone para o tema escuro
        } else {
            document.body.classList.remove("dark-theme");
            document.body.classList.add("light-theme");
            localStorage.setItem("theme", "light-theme");
            themeIcon.className = "fas fa-sun"; // Ícone para o tema claro
        }
    });
});