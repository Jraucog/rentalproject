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
