// Obtiene el interruptor de modo oscuro
var darkModeSwitch = document.getElementById('darkModeSwitch');

// Al cargar la página, verifica si hay una preferencia almacenada en localStorage
document.addEventListener('DOMContentLoaded', function () {
  if (localStorage.getItem('darkMode') === 'enabled') {
    enableDarkMode();
  }
});

// Añade un evento 'change' al interruptor
darkModeSwitch.addEventListener('change', function () {
  // Obtiene la etiqueta asociada al interruptor
  var switchLabel = this.nextElementSibling;

  // Comprueba si el interruptor está activado
  if (this.checked) {
    // Si el interruptor está activado, aplica estilos para modo oscuro
    enableDarkMode();
    // Cambia el color de fondo y de texto de la etiqueta
    switchLabel.style.backgroundColor = 'var(--primary-color)';
    switchLabel.style.color = 'var(--text-color)';
    // Almacena la preferencia en localStorage
    localStorage.setItem('darkMode', 'enabled');
  } else {
    // Si el interruptor está desactivado, elimina los estilos de modo oscuro
    disableDarkMode();
    // Restaura el color de fondo y de texto de la etiqueta a los valores por defecto
    switchLabel.style.backgroundColor = '';
    switchLabel.style.color = '';
    // Almacena la preferencia en localStorage
    localStorage.setItem('darkMode', 'disabled');
  }
});

function enableDarkMode() {
  document.body.classList.add('dark-mode');
}

function disableDarkMode() {
  document.body.classList.remove('dark-mode');
}
// scripts.js
function toggleDetails(section) {
  var details = document.getElementById('details-' + section);
  details.style.display = (details.style.display === 'none' || details.style.display === '') ? 'block' : 'none';
}

var headers = document.getElementsByClassName('details-header');
for (var i = 0; i < headers.length; i++) {
  headers[i].addEventListener('mouseover', function() {
    this.style.backgroundColor = "#f2f2f2";
  });
  headers[i].addEventListener('mouseout', function() {
    this.style.backgroundColor = "";
  });
}
