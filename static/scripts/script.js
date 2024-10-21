// Fonction pour afficher les onglets (Login et Sign Up)
function showTab(tab) {
  const tabs = document.querySelectorAll('.tab');
  const titles = document.querySelectorAll('.tab-title');

  tabs.forEach(t => {
    t.classList.remove('active'); // Masque tous les onglets
  });

  titles.forEach(title => {
    title.style.display = 'none'; // Masque tous les titres
  });

  document.getElementById(tab).classList.add('active'); // Affiche l'onglet sélectionné

  // Affiche le titre correspondant
  if (tab === 'login') {
    document.getElementById('login-title').style.display = 'block';
  } else if (tab === 'sign-up') {
    document.getElementById('signup-title').style.display = 'block';
  }
}



// Créer une balise <script> pour le widget Calendly
var script = document.createElement('script');
script.type = 'text/javascript';
script.src = 'https://assets.calendly.com/assets/external/widget.js';
script.async = true; // Charger le script de manière asynchrone
document.body.appendChild(script); // Ajouter la balise <script> à la fin du <body>
