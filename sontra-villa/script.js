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

// ===== LANGUAGE SWITCH (EN / VI) =====
const I18N_MAP = {
  en: {
    support_link: 'Quick Support',
    home_title: 'Son Tra Villa Hoi An',
    home_subtitle: 'Quiet Pool Villa Near Old Town',
    gallery_title: 'Villa Gallery',
    gallery_tag_1: 'Relaxing Vibe',
    gallery_tag_2: 'Tropical Summer',
    wifi_link: 'Villa WiFi',
    wifi_network_label: '📶 Network',
    wifi_password_label: '🔑 Password',
    maps_link: 'Google Maps Location',
    hoian_tour_link: 'Hoi An Tour List',
    local_rec_link: 'Local Recommendations'
  },
  vi: {
    support_link: 'Hỗ Trợ Nhanh',
    home_title: 'Sơn Trà Villa Hội An',
    home_subtitle: 'Biệt Thự Hồ Bơi Yên Tĩnh Gần Phố Cổ',
    gallery_title: 'Bộ Sưu Tập Biệt Thự',
    gallery_tag_1: 'Không Gian Thư Giãn',
    gallery_tag_2: 'Mùa Hè Nhiệt Đới',
    wifi_link: 'WiFi Biệt Thự',
    wifi_network_label: '📶 Mạng',
    wifi_password_label: '🔑 Mật khẩu',
    maps_link: 'Vị Trí Google Maps',
    hoian_tour_link: 'Danh Sách Tour Hội An',
    local_rec_link: 'Gợi Ý Địa Phương'
  }
};

function applyLanguage(lang) {
  const dict = I18N_MAP[lang] || I18N_MAP.en;
  Object.keys(dict).forEach((key) => {
    const nodes = document.querySelectorAll('[data-i18n="' + key + '"]');
    nodes.forEach((el) => {
      el.textContent = dict[key];
    });
  });
}

document.addEventListener('DOMContentLoaded', function () {
  const pills = document.querySelectorAll('.lang-pill');
  let currentLang = 'en';

  function setLang(lang) {
    currentLang = lang;
    document.documentElement.setAttribute('data-lang', lang);
    pills.forEach((btn) => {
      btn.classList.toggle('lang-active', btn.dataset.lang === lang);
    });
    applyLanguage(lang);
  }

  pills.forEach((btn) => {
    btn.addEventListener('click', function () {
      const lang = btn.dataset.lang || 'en';
      if (lang !== currentLang) {
        setLang(lang);
      }
    });
  });

  // initial render: default English
  setLang('en');
});