document.addEventListener("DOMContentLoaded", function() {
    const themeToggleButton = document.getElementById("theme-toggle");
    const currentTheme = localStorage.getItem("theme");

    // Verificar o tema atual e aplicar a classe correta ao body
    if (currentTheme) {
        document.body.classList.add(currentTheme);
    } else {
        document.body.classList.add("light-theme");
    }

    themeToggleButton.addEventListener("click", function() {
        if (document.body.classList.contains("light-theme")) {
            document.body.classList.remove("light-theme");
            document.body.classList.add("dark-theme");
            localStorage.setItem("theme", "dark-theme");
        } else {
            document.body.classList.remove("dark-theme");
            document.body.classList.add("light-theme");
            localStorage.setItem("theme", "light-theme");
        }
    });
});