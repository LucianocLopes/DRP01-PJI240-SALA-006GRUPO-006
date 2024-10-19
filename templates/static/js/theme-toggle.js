document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';

    // Define o tema atual no body
    document.body.setAttribute('data-bs-theme', currentTheme);
    
    // Cria um novo elemento de ícone no botão
    const themeIcon = document.createElement('img');
    themeIcon.alt = "Tema escuro";
    themeIcon.width = 25;
    themeIcon.height = 25;
    themeToggle.appendChild(themeIcon);
    updateIcon(currentTheme); // Atualiza o ícone de acordo com o tema atual

    themeToggle.addEventListener('click', function() {
        const newTheme = document.body.getAttribute('data-bs-theme') === 'light' ? 'dark' : 'light';
        document.body.setAttribute('data-bs-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateIcon(newTheme);
    });

    function updateIcon(theme) {
        if (theme === 'dark') {
            themeIcon.src = "{% static 'img/icon-sun.svg' %}"; // Ícone para tema escuro
        } else {
            themeIcon.src = "{% static 'img/icon-moon.svg' %}"; // Ícone para tema claro
        }
    }
});
