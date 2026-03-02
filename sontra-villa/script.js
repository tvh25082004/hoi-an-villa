function toggleView(view) {
  const mainView = document.getElementById('main-view');
  const supportView = document.getElementById('support-view');
  const recommendationsView = document.getElementById('recommendations-view');
  const tourView = document.getElementById('tour-view');
  const supportBtn = document.getElementById('support-link-btn');

  // Hide all first
  mainView.style.display = 'none';
  supportView.style.display = 'none';
  
  if (recommendationsView) {
      recommendationsView.style.display = 'none';
  }
  
  if (tourView) {
      tourView.style.display = 'none';
  }

  if (view === 'support') {
    supportBtn.style.display = 'none';
    supportView.style.display = 'block';
  } else if (view === 'recommendations') {
    supportBtn.style.display = 'none';
    if (recommendationsView) recommendationsView.style.display = 'block';
  } else if (view === 'tour') {
    supportBtn.style.display = 'none';
    if (tourView) tourView.style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  } else {
    mainView.style.display = 'block';
    supportBtn.style.display = 'flex';
  }
}

function toggleWifi() {
  const panel = document.getElementById('wifi-details');
  if (panel.style.display === 'none') {
    panel.style.display = 'block';
    panel.style.opacity = '0';
    panel.style.transform = 'translateY(-10px)';
    setTimeout(() => {
      panel.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
      panel.style.opacity = '1';
      panel.style.transform = 'translateY(0)';
    }, 10);
  } else {
    panel.style.opacity = '0';
    panel.style.transform = 'translateY(-10px)';
    setTimeout(() => {
      panel.style.display = 'none';
    }, 300);
  }
}

// Safety: prevent clicking the "Get Directions" button from also triggering the parent card's onclick
document.addEventListener('click', function (e) {
  const target = e.target;
  const mapBtn = target && target.closest ? target.closest('a.rec-map-btn') : null;
  if (mapBtn) e.stopPropagation();
});