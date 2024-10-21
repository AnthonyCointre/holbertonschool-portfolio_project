function showTab(tab) {
  const tabs = document.querySelectorAll('.tab');
  const titles = document.querySelectorAll('.tab-title');
  tabs.forEach(t => {
    t.classList.remove('active');
  });
  titles.forEach(title => {
    title.style.display = 'none';
  });
  document.getElementById(tab).classList.add('active');
  if (tab === 'login') {
    document.getElementById('login-title').style.display = 'block';
  } else if (tab === 'sign-up') {
    document.getElementById('signup-title').style.display = 'block';
  }
}

var script = document.createElement('script');
script.type = 'text/javascript';
script.src = 'https://assets.calendly.com/assets/external/widget.js';
script.async = true;
document.body.appendChild(script);
