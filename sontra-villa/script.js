function toggleView(view) {
  const mainView = document.getElementById('main-view');
  const supportView = document.getElementById('support-view');
  const recommendationsView = document.getElementById('recommendations-view');
  const tourView = document.getElementById('tour-view');
  const servicesView = document.getElementById('services-view');
  const supportBtn = document.getElementById('support-link-btn');
  const langToggle = document.querySelector('.lang-toggle');

  // Hide all first
  mainView.style.display = 'none';
  supportView.style.display = 'none';
  
  if (recommendationsView) {
      recommendationsView.style.display = 'none';
  }
  
  if (tourView) {
      tourView.style.display = 'none';
  }

  if (servicesView) {
      servicesView.style.display = 'none';
  }

  if (view === 'support') {
    supportBtn.style.display = 'none';
    if (langToggle) langToggle.style.display = 'none';
    supportView.style.display = 'block';
  } else if (view === 'recommendations') {
    supportBtn.style.display = 'none';
    if (langToggle) langToggle.style.display = 'none';
    if (recommendationsView) recommendationsView.style.display = 'block';
  } else if (view === 'tour') {
    supportBtn.style.display = 'none';
    if (langToggle) langToggle.style.display = 'none';
    if (tourView) {
      tourView.style.display = 'block';
      // Re-verify auto-slides when opening tour view
      if (typeof initAutoSlides === 'function') initAutoSlides();
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  } else if (view === 'services') {
    supportBtn.style.display = 'none';
    if (langToggle) langToggle.style.display = 'none';
    if (servicesView) servicesView.style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  } else {
    mainView.style.display = 'block';
    supportBtn.style.display = 'flex';
    if (langToggle) langToggle.style.display = 'flex';
  }
}

// ===== BACK TO TOP FUNCTIONALITY =====
function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

let lastScrollTop = 0;
window.addEventListener('scroll', function() {
  const btn = document.getElementById('back-to-top');
  if (btn) {
    const st = window.pageYOffset || document.documentElement.scrollTop;
    
    // Scrolling UP and depth > 300
    if (st < lastScrollTop && st > 300) {
      btn.classList.add('visible');
    } else {
      // Scrolling DOWN or at top
      btn.classList.remove('visible');
    }
    
    lastScrollTop = st <= 0 ? 0 : st; // For Mobile or negative scrolling
  }
});

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
    local_rec_link: 'Local Recommendations',
    // support view
    back_btn: 'Go Back',
    support_title: 'Quick Support',
    support_subtitle: 'Select a contact method below for assistance',
    support_call: 'Direct Call (+84 862 852 258)',
    support_zalo: 'Zalo (+84862852258)',
    support_whatsapp: 'WhatsApp Chat',
    // recommendations view
    rec_title: '🌟 Local Highlights',
    rec_subtitle: '80+ hand-picked spots for food, drinks & vibes in Hoi An',
    rec_tab_all: 'All',
    rec_tab_bar: '🍺 Bars',
    rec_tab_cocktail: '🍸 Cocktails',
    rec_tab_hotfood: '🍜 Hot Food',
    rec_tab_snack: '🥨 Snacks',
    rec_tab_cafe: '☕ Cafés',
    rec_tab_shop: '🛍️ Shops',
    rec_badge_bar: 'Bar',
    rec_badge_cocktail: 'Cocktail',
    rec_badge_hotfood: 'Hot Food',
    rec_badge_snack: 'Snacks',
    rec_badge_cafe: 'Café',
    rec_badge_shop: 'Shop',
    // tour list view
    tour_title: '🗺️ Discovery Tours 2026',
    tour_subtitle: 'Hand-picked authentic experiences in & around Hoi An',
    tour_tab_all: '🌏 ALL',
    tour_tab_hoian: '🏮 Hoi An',
    tour_tab_hue: '🏯 Hue',
    tour_tab_danang: '🌉 Da Nang',
    tour_card_hint: 'Tap to see details →',
    // tour modal labels
    modal_highlights_title: '✨ Highlights',
    modal_itinerary_title: '🗓️ Itinerary',
    modal_included_title: "✅ What's Included",
    modal_notes_title: '📋 Important Notes',
    modal_book_zalo: '📲 Book via Zalo — +84 862 852 258',
    modal_book_whatsapp: '💬 Chat via WhatsApp',
    // services view
    services_link: '🛵 Villa Services & Rentals',
    services_title: '🛵 Villa Services & Rentals',
    services_subtitle: 'On-site vehicle rentals — please ask reception to book for you',
    // motorbike
    services_moto_name: 'Motorbike',
    services_moto_subtitle: 'Manual / Semi-automatic',
    services_moto_price_unit: 'per day (24 hours)',
    services_moto_tag: "⚠️ Driver's license required",
    services_moto_feat_1: '✅ Best for longer coastal rides',
    services_moto_feat_2: '✅ Fast & flexible',
    services_moto_feat_3: '✅ Great for exploring the beach road',
    // 49cc scooter
    services_49cc_name: '49cc Scooter',
    services_49cc_subtitle: 'Beginner friendly',
    services_49cc_price_unit: 'per day (24 hours)',
    services_49cc_tag: '✅ No license required',
    services_49cc_feat_1: '✅ Easy to ride for first-timers',
    services_49cc_feat_2: '✅ Moderate, comfortable speed',
    services_49cc_feat_3: '✅ Safe & convenient around town',
    // electric bike
    services_electric_name: 'Electric Bike',
    services_electric_subtitle: 'Eco-friendly',
    services_electric_price_unit: 'per day (24 hours)',
    services_electric_tag: '✅ No license required',
    services_electric_feat_1: '✅ Eco-friendly & quiet',
    services_electric_feat_2: '✅ Smooth, silent ride',
    services_electric_feat_3: '✅ Perfect inside the Old Town',
    // bicycle
    services_bike_name: 'Bicycle',
    services_bike_subtitle: 'For villa guests',
    services_bike_price_unit: 'Free for guests',
    services_bike_tag: '🎁 Complimentary service',
    services_bike_feat_1: '✅ Leisurely rides around Old Town',
    services_bike_feat_2: '✅ Healthy & relaxing',
    services_bike_feat_3: '✅ Priority for villa guests',
    // services contact
    services_contact_title: 'Book a vehicle now',
    services_contact_desc: 'Contact reception or message us on Zalo / WhatsApp to reserve in advance',
    services_contact_btn_zalo: 'Zalo',
    services_contact_btn_whatsapp: 'WhatsApp'
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
    local_rec_link: 'Gợi Ý Địa Phương',
    // support view
    back_btn: 'Quay Lại',
    support_title: 'Hỗ Trợ Nhanh',
    support_subtitle: 'Chọn cách liên hệ bên dưới để được hỗ trợ',
    support_call: 'Gọi Trực Tiếp (+84 862 852 258)',
    support_zalo: 'Zalo (+84862852258)',
    support_whatsapp: 'Chat WhatsApp',
    // recommendations view
    rec_title: '🌟 Gợi Ý Địa Phương',
    rec_subtitle: 'Hơn 80 địa điểm ăn uống, vui chơi được chọn lọc tại Hội An',
    rec_tab_all: 'Tất Cả',
    rec_tab_bar: '🍺 Quán Bar',
    rec_tab_cocktail: '🍸 Cocktail',
    rec_tab_hotfood: '🍜 Món Nóng',
    rec_tab_snack: '🥨 Ăn Vặt',
    rec_tab_cafe: '☕ Quán Cà Phê',
    rec_tab_shop: '🛍️ Cửa Hàng',
    rec_badge_bar: 'Quán Bar',
    rec_badge_cocktail: 'Cocktail',
    rec_badge_hotfood: 'Đồ Ăn Nóng',
    rec_badge_snack: 'Đồ Ăn Vặt',
    rec_badge_cafe: 'Cà Phê',
    rec_badge_shop: 'Cửa Hàng',
    // tour list view
    tour_title: '🗺️ Discovery Tours 2026',
    tour_subtitle: 'Các trải nghiệm chân thật được chọn lọc tại & quanh Hội An',
    tour_tab_all: '🌏 Tất Cả',
    tour_tab_hoian: '🏮 Hội An',
    tour_tab_hue: '🏯 Huế',
    tour_tab_danang: '🌉 Đà Nẵng',
    tour_card_hint: 'Nhấn để xem chi tiết →',
    // tour modal labels
    modal_highlights_title: '✨ Điểm nổi bật',
    modal_itinerary_title: '🗓️ Lịch trình chi tiết',
    modal_included_title: '✅ Dịch vụ bao gồm',
    modal_notes_title: '📋 Lưu ý quan trọng',
    modal_book_zalo: '📲 Đặt tour qua Zalo — +84 862 852 258',
    modal_book_whatsapp: '💬 Chat qua WhatsApp',
    // services view
    services_link: '🛵 Dịch Vụ & Thuê Xe Villa',
    services_title: '🛵 Dịch Vụ & Thuê Xe Villa',
    services_subtitle: 'Dịch vụ cho thuê xe từ villa — liên hệ lễ tân để đặt',
    // motorbike
    services_moto_name: 'Xe Máy',
    services_moto_subtitle: 'Số / tay ga',
    services_moto_price_unit: '/ 24 giờ',
    services_moto_tag: '⚠️ Cần bằng lái',
    services_moto_feat_1: '✅ Phù hợp chạy đường biển dài',
    services_moto_feat_2: '✅ Nhanh & linh hoạt',
    services_moto_feat_3: '✅ Khám phá bờ biển Đà Nẵng',
    // 49cc scooter
    services_49cc_name: 'Xe 49cc',
    services_49cc_subtitle: 'Dễ lái cho người mới',
    services_49cc_price_unit: '/ 24 giờ',
    services_49cc_tag: '✅ Không cần bằng lái',
    services_49cc_feat_1: '✅ Phù hợp cho người mới tập lái',
    services_49cc_feat_2: '✅ Tốc độ vừa phải, an toàn',
    services_49cc_feat_3: '✅ Tiện di chuyển quanh Hội An',
    // electric bike
    services_electric_name: 'Xe Điện',
    services_electric_subtitle: 'Thân thiện môi trường',
    services_electric_price_unit: '/ 24 giờ',
    services_electric_tag: '✅ Không cần bằng lái',
    services_electric_feat_1: '✅ Thân thiện môi trường',
    services_electric_feat_2: '✅ Êm ái, không tiếng ồn',
    services_electric_feat_3: '✅ Rất hợp đi trong phố cổ',
    // bicycle
    services_bike_name: 'Xe Đạp',
    services_bike_subtitle: 'Ưu tiên khách villa',
    services_bike_price_unit: 'Miễn phí',
    services_bike_tag: '🎁 Dịch vụ miễn phí',
    services_bike_feat_1: '✅ Thoải mái dạo phố cổ',
    services_bike_feat_2: '✅ Tốt cho sức khỏe',
    services_bike_feat_3: '✅ Ưu tiên cho khách Villa',
    // services contact
    services_contact_title: 'Đặt xe ngay',
    services_contact_desc: 'Liên hệ lễ tân hoặc nhắn Zalo / WhatsApp để đặt trước',
    services_contact_btn_zalo: 'Zalo',
    services_contact_btn_whatsapp: 'WhatsApp'
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

  // cache bilingual content for tour cards
  const tourCardState = [];
  const tourCardStateById = {};
  const tourCards = document.querySelectorAll('#tour-list-container .tour-card');
  tourCards.forEach((card) => {
    const onclick = card.getAttribute('onclick') || '';
    const match = onclick.match(/openTourModal\('([^']+)'\)/);
    if (!match) return;
    const tourId = match[1];
    const tour = (typeof TOUR_DATA !== 'undefined') ? TOUR_DATA[tourId] : null;
    if (!tour) return;

    const titleEl = card.querySelector('.tour-info h3');
    const descEl = card.querySelector('.tour-info p');
    const metaEls = card.querySelectorAll('.tour-meta-item');
    const badgeEl = card.querySelector('.tour-badge');

    const viTitle = titleEl ? titleEl.textContent.trim() : '';
    const viDesc = descEl ? descEl.textContent.trim() : '';
    const viMeta = Array.from(metaEls).map(el => el.textContent.trim());
    const viBadge = badgeEl ? badgeEl.textContent.trim() : '';

    const enTitle = tour.title || viTitle;
    const enDesc = tour.desc_card || tour.description || viDesc;
    const enMeta = (tour.meta || []).map(pair => Array.isArray(pair) ? (pair[0] + ' ' + pair[1]) : String(pair));
    const enBadge = tour.badge || viBadge;

    const state = { titleEl, descEl, metaEls, badgeEl, viTitle, viDesc, viMeta, viBadge, enTitle, enDesc, enMeta, enBadge };
    tourCardState.push(state);
    tourCardStateById[tourId] = {
      viTitle,
      viDesc,
      viMeta,
      viBadge,
      enTitle,
      enDesc,
      enMeta,
      enBadge
    };
  });

  // expose for modal usage
  window.TOUR_CARD_STATE_BY_ID = tourCardStateById;

  function setTourCardsLang(lang) {
    tourCardState.forEach((state) => {
      if (!state.titleEl || !state.descEl) return;
      if (lang === 'vi') {
        state.titleEl.textContent = state.viTitle;
        state.descEl.textContent = state.viDesc;
        state.metaEls.forEach((el, idx) => {
          if (state.viMeta[idx]) el.textContent = state.viMeta[idx];
        });
        if (state.badgeEl) {
          state.badgeEl.textContent = state.viBadge || state.enBadge || state.badgeEl.textContent;
        }
      } else {
        state.titleEl.textContent = state.enTitle;
        state.descEl.textContent = state.enDesc;
        state.metaEls.forEach((el, idx) => {
          if (state.enMeta[idx]) el.textContent = state.enMeta[idx];
        });
        if (state.badgeEl) {
          state.badgeEl.textContent = state.enBadge || state.viBadge || state.badgeEl.textContent;
        }
      }
    });
  }

  function setLang(lang) {
    currentLang = lang;
    document.documentElement.setAttribute('data-lang', lang);
    document.documentElement.setAttribute('lang', lang === 'vi' ? 'vi' : 'en');
    pills.forEach((btn) => {
      btn.classList.toggle('lang-active', btn.dataset.lang === lang);
    });
    applyLanguage(lang);
    setTourCardsLang(lang);
  }

  pills.forEach((btn) => {
    btn.addEventListener('click', function () {
      const lang = btn.dataset.lang || 'en';
      if (lang !== currentLang) {
        setLang(lang);
      }
    });
  });

  // initial render: default English (also for tour cards)
  setLang('en');
});

// ===== Tour Gallery Slider =====
(function() {
  function getState(gallery) {
    var track = gallery.querySelector('.tg-track');
    var slides = track.querySelectorAll('.tg-slide');
    var dots = gallery.querySelectorAll('.tg-dot');
    var idx = parseInt(gallery.getAttribute('data-idx') || '0');
    return { track, slides, dots, idx };
  }
  function goTo(gallery, newIdx) {
    var s = getState(gallery);
    var total = s.slides.length;
    newIdx = ((newIdx % total) + total) % total;
    s.track.style.transform = 'translateX(-' + (newIdx * 100) + '%)';
    s.dots.forEach(function(d, i) {
      d.classList.toggle('tg-active', i === newIdx);
    });
    gallery.setAttribute('data-idx', newIdx);
  }
  // Auto-slide functionality
  var autoSlideInterval = 3000; // 3 seconds
  var galleryIntervals = {};

  function startAutoSlide(gallery) {
    var id = gallery.id;
    if (!id) return;
    if (galleryIntervals[id]) clearInterval(galleryIntervals[id]);
    
    galleryIntervals[id] = setInterval(function() {
      var s = getState(gallery);
      if (s.slides.length > 1) {
        goTo(gallery, s.idx + 1);
      }
    }, autoSlideInterval);
  }

  function stopAutoSlide(gallery) {
    var id = gallery.id;
    if (id && galleryIntervals[id]) {
        clearInterval(galleryIntervals[id]);
        delete galleryIntervals[id];
    }
  }

  // Initial start for all galleries
  window.initAutoSlides = function() {
    var galleries = document.querySelectorAll('.tour-gallery');
    if (galleries.length === 0) return;
    
    galleries.forEach(function(g) {
      if (!g.id) {
          g.id = 'tg-' + Math.random().toString(36).substr(2, 9);
      }
      // Only start if not already running
      if (!galleryIntervals[g.id]) {
        startAutoSlide(g);
      }
    });
  };

  window.tgPrev = function(e, btn) {
    e.stopPropagation();
    var gallery = btn.closest('.tour-gallery');
    var s = getState(gallery);
    goTo(gallery, s.idx - 1);
    // Restart timer on manual interaction
    startAutoSlide(gallery);
  };
  window.tgNext = function(e, btn) {
    e.stopPropagation();
    var gallery = btn.closest('.tour-gallery');
    var s = getState(gallery);
    goTo(gallery, s.idx + 1);
    // Restart timer on manual interaction
    startAutoSlide(gallery);
  };

  // Touch/swipe support
  document.addEventListener('touchstart', function(e) {
    var gallery = e.target.closest('.tour-gallery');
    if (!gallery) return;
    stopAutoSlide(gallery); // Stop auto-slide while swiping
    gallery._touchStartX = e.touches[0].clientX;
    gallery._touchStartY = e.touches[0].clientY;
    gallery._swiping = false;
  }, { passive: true });

  document.addEventListener('touchmove', function(e) {
    var gallery = e.target.closest('.tour-gallery');
    if (!gallery || gallery._touchStartX == null) return;
    var dx = e.touches[0].clientX - gallery._touchStartX;
    var dy = e.touches[0].clientY - gallery._touchStartY;
    if (!gallery._swiping && Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 8) {
      gallery._swiping = true;
    }
    if (gallery._swiping) {
      e.preventDefault();
    }
  }, { passive: false });

  document.addEventListener('touchend', function(e) {
    var gallery = e.target.closest('.tour-gallery');
    if (!gallery || gallery._touchStartX == null) return;
    var dx = e.changedTouches[0].clientX - gallery._touchStartX;
    if (gallery._swiping && Math.abs(dx) > 40) {
      var s = getState(gallery);
      goTo(gallery, dx < 0 ? s.idx + 1 : s.idx - 1);
    }
    gallery._touchStartX = null;
    gallery._swiping = false;
    startAutoSlide(gallery); // Resume auto-slide after swipe
  }, { passive: true });

  // Start automation
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAutoSlides);
  } else {
    initAutoSlides();
  }
})();
