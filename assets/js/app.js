/**
 * Mystic Poetry Heritage Hub (रहस्यवादी काव्य महाकोश)
 * Multi-Poet Trilingual Master Edition:
 * - Baba Bulleh Shah (351 Masterpieces)
 * - Sant Ravidas Ji (208 Masterpieces)
 * Total: 559 Classical Masterpieces
 */

(function () {
  'use strict';

  // Application State
  const state = {
    currentPoet: null, // null (Hub), 'bulleh-shah', 'sant-ravidas'
    currentUid: null,
    currentFilter: 'all',
    searchQuery: '',
    viewMode: 'all', // 'all', 'verses', 'gloss', 'trans'
    fontScale: 1.0,
    theme: localStorage.getItem('mystic_theme') || 'dark',
    bookmarks: new Set(JSON.parse(localStorage.getItem('mystic_bookmarks') || '[]')),
    
    // Data stores
    poets: {
      'bulleh-shah': {
        id: 'bulleh-shah',
        name: 'बाबा बुल्ले शाह',
        name_en: 'Baba Bulleh Shah',
        emblem: 'ब',
        total: 351,
        color: 'var(--gold-primary)',
        manifest: window.BULLEH_SHAH_MANIFEST || [],
        data: window.BULLEH_SHAH_DATA || {},
        tabs: [
          { id: 'all', label: 'सभी (351)' },
          { id: 'kafi', label: 'काफ़ियां (160)' },
          { id: 'dohre', label: 'दोहरे (56)' },
          { id: 'baranmah', label: 'बारहमाह (12)' },
          { id: 'athwara', label: 'अठवारा (7)' },
          { id: 'gandhan', label: 'गन्धां (40)' },
          { id: 'siharfian', label: 'सीहरफ़ियां (76)' },
          { id: 'bookmarks', label: '★ पसंदीदा' }
        ]
      },
      'sant-ravidas': {
        id: 'sant-ravidas',
        name: 'संत शिरोमणि रविदास जी',
        name_en: 'Sant Ravidas Ji',
        emblem: 'र',
        total: 208,
        color: 'var(--ravidas-text)',
        manifest: window.RAVIDAS_MANIFEST || [],
        data: window.RAVIDAS_DATA || {},
        tabs: [
          { id: 'all', label: 'सभी (208)' },
          { id: 'shabad', label: 'आदि ग्रंथ शब्द (40)' },
          { id: 'padaavali', label: 'अमर पद (117)' },
          { id: 'dohe', label: 'साखी दोहे (51)' },
          { id: 'bookmarks', label: '★ पसंदीदा' }
        ]
      },
      'sheikh-farid': {
        id: 'sheikh-farid',
        name: 'बाबा शेख फरीद',
        name_en: 'Baba Sheikh Farid',
        emblem: 'फ',
        total: 134,
        color: 'hsl(165, 80%, 42%)',
        manifest: window.FARID_MANIFEST || [],
        data: window.FARID_DATA || {},
        tabs: [
          { id: 'all', label: 'सभी (134)' },
          { id: 'salok', label: 'सलोक (130)' },
          { id: 'shabad', label: 'शब्द (4)' },
          { id: 'bookmarks', label: '★ पसंदीदा' }
        ]
      },
      'meerabai': {
        id: 'meerabai',
        name: 'संत शिरोमणि मीराबाई',
        name_en: 'Sant Mirabai',
        emblem: 'मी',
        total: 418,
        color: 'hsl(330, 85%, 60%)',
        manifest: window.MEERABAI_MANIFEST || [],
        data: window.MEERABAI_DATA || {},
        tabs: [
          { id: 'all', label: 'सभी (418)' },
          { id: 'padaavali', label: 'अमर पद (418)' },
          { id: 'bookmarks', label: '★ पसंदीदा' }
        ]
      },
      'sant-kabir': {
        id: 'sant-kabir',
        name: 'संत कबीर दास',
        name_en: 'Sant Kabir Das',
        emblem: 'क',
        total: 562,
        color: 'hsl(215, 90%, 55%)',
        manifest: window.KABIR_MANIFEST || [],
        data: window.KABIR_DATA || {},
        tabs: [
          { id: 'all', label: 'सभी (562)' },
          { id: 'shabad', label: 'शब्द (149)' },
          { id: 'salok', label: 'सलोक (245)' },
          { id: 'doha', label: 'दोहे (84)' },
          { id: 'ramaini', label: 'रमैणी (8)' },
          { id: 'sakhi', label: 'साखी अंग (59)' },
          { id: 'pad', label: 'पद राग (17)' },
          { id: 'bookmarks', label: '★ पसंदीदा' }
        ]
      }
    }
  };


  // DOM Elements
  const el = {
    // Views
    hubView: document.getElementById('hub-view'),
    poetWorkspace: document.getElementById('poet-workspace-view'),
    welcomeView: document.getElementById('welcome-hero-view'),
    poemView: document.getElementById('poem-reader-view'),
    
    // Header
    brandHeader: document.getElementById('brand-header-link'),
    headerEmblem: document.getElementById('header-emblem'),
    headerMainTitle: document.getElementById('header-main-title'),
    headerSubTitle: document.getElementById('header-sub-title'),
    navHubBtn: document.getElementById('nav-hub-btn'),
    poetSwitcherBtn: document.getElementById('poet-switcher-btn'),
    poetSwitcherLabel: document.getElementById('poet-switcher-label'),
    searchInput: document.getElementById('search-input'),
    randomBtn: document.getElementById('random-kafi-btn'),
    bookmarksBtn: document.getElementById('bookmarks-view-btn'),
    themeBtn: document.getElementById('theme-toggle-btn'),
    themeIcon: document.getElementById('theme-icon'),
    sidebarToggleBtn: document.getElementById('sidebar-toggle-btn'),
    sidebar: document.getElementById('app-sidebar'),
    sidebarBackdrop: document.getElementById('sidebar-backdrop'),
    
    // Hub specific
    hubSearchInput: document.getElementById('hub-search-input'),
    hubSearchResults: document.getElementById('hub-search-results'),
    
    // Sidebar inside poet workspace
    sidebarPoetEmblem: document.getElementById('sidebar-poet-emblem'),
    sidebarPoetName: document.getElementById('sidebar-poet-name'),
    sidebarBackToHub: document.getElementById('sidebar-back-to-hub'),
    sidebarTabsContainer: document.getElementById('sidebar-tabs-container'),
    sidebarSearchInput: document.getElementById('sidebar-search-input'),
    filteredCountBadge: document.getElementById('filtered-count-badge'),
    kafiList: document.getElementById('kafi-list-container'),
    
    // Poem Reader
    poemGenreBadge: document.getElementById('poem-genre-badge'),
    poemRagaBadge: document.getElementById('poem-raga-badge'),
    poemIndexBadge: document.getElementById('poem-index-badge'),
    poemTitleDev: document.getElementById('poem-title-dev'),
    poemTitleEn: document.getElementById('poem-title-en'),
    poemVersesContainer: document.getElementById('poem-verses-container'),
    poemTransHindi: document.getElementById('poem-trans-hindi'),
    poemTransEnglish: document.getElementById('poem-trans-english'),
    poemCommentary: document.getElementById('poem-commentary-content'),
    prevPoemBtn: document.getElementById('nav-prev-poem-btn'),
    nextPoemBtn: document.getElementById('nav-next-poem-btn'),
    returnHubBtn: document.getElementById('nav-return-hub-btn'),
    copyPoemBtn: document.getElementById('copy-poem-btn'),
    bookmarkToggleBtn: document.getElementById('bookmark-toggle-btn'),
    fontDecBtn: document.getElementById('font-decrease'),
    fontIncBtn: document.getElementById('font-increase'),
    
    // Toast
    toast: document.getElementById('toast-notification'),
    toastMsg: document.getElementById('toast-message'),
    viewModeTabs: document.querySelectorAll('.view-tab')
  };

  // Initialize Application
  function init() {
    applyTheme(state.theme);
    attachEventListeners();
    window.addEventListener('hashchange', handleRoute);
    handleRoute();
  }

  // Theme Management
  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('mystic_theme', theme);

    if (el.themeIcon) {
      el.themeIcon.innerHTML = theme === 'dark'
        ? '<path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'
        : '<path d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" fill="currentColor"/>';
    }
  }

  function toggleTheme() {
    applyTheme(state.theme === 'dark' ? 'light' : 'dark');
  }

  // Toast Notification
  let toastTimer = null;
  function showToast(message) {
    if (el.toast && el.toastMsg) {
      el.toastMsg.textContent = message;
      el.toast.classList.add('show');
      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => {
        el.toast.classList.remove('show');
      }, 2600);
    }
  }

  // Routing Management
  function handleRoute() {
    const hash = window.location.hash || '';

    // Hub Route: #, #/, or empty
    if (!hash || hash === '#' || hash === '#/') {
      showHubView();
      return;
    }

    // Match /bulleh-shah/ or /sant-ravidas/ routes
    if (hash.startsWith('#/bulleh-shah')) {
      state.currentPoet = 'bulleh-shah';
      const sub = hash.replace('#/bulleh-shah', '').replace(/^\//, '');
      showPoetWorkspace('bulleh-shah');
      if (!sub) {
        showPoetWelcome();
      } else {
        resolveWorkRoute('bulleh-shah', sub);
      }
      return;
    }

    if (hash.startsWith('#/sant-ravidas')) {
      state.currentPoet = 'sant-ravidas';
      const sub = hash.replace('#/sant-ravidas', '').replace(/^\//, '');
      showPoetWorkspace('sant-ravidas');
      if (!sub) {
        showPoetWelcome();
      } else {
        resolveWorkRoute('sant-ravidas', sub);
      }
      return;
    }

    if (hash.startsWith('#/sheikh-farid')) {
      state.currentPoet = 'sheikh-farid';
      const sub = hash.replace('#/sheikh-farid', '').replace(/^\//, '');
      showPoetWorkspace('sheikh-farid');
      if (!sub) {
        showPoetWelcome();
      } else {
        resolveWorkRoute('sheikh-farid', sub);
      }
      return;
    }

    if (hash.startsWith('#/meerabai')) {
      state.currentPoet = 'meerabai';
      const sub = hash.replace('#/meerabai', '').replace(/^\//, '');
      showPoetWorkspace('meerabai');
      if (!sub) {
        showPoetWelcome();
      } else {
        resolveWorkRoute('meerabai', sub);
      }
      return;
    }

    if (hash.startsWith('#/sant-kabir')) {
      state.currentPoet = 'sant-kabir';
      const sub = hash.replace('#/sant-kabir', '').replace(/^\//, '');
      showPoetWorkspace('sant-kabir');
      if (!sub) {
        showPoetWelcome();
      } else {
        resolveWorkRoute('sant-kabir', sub);
      }
      return;
    }

    // Legacy fallback for old Bulleh Shah hashes like #kafi-21, #dohre-5
    const legacyMatch = hash.match(/^#([a-zA-Z]+)-(\d+)$/);
    if (legacyMatch) {
      const g = legacyMatch[1];
      const id = legacyMatch[2];
      if (['kafi', 'dohre', 'baranmah', 'athwara', 'gandhan', 'siharfi', 'siharfian'].includes(g)) {
        window.location.hash = `#/bulleh-shah/${g}-${id}`;
        return;
      }
      if (['shabad', 'pada', 'padaavali', 'doha', 'dohe'].includes(g)) {
        window.location.hash = `#/sant-ravidas/${g}-${id}`;
        return;
      }
      if (['salok'].includes(g)) {
        window.location.hash = `#/sheikh-farid/${g}-${id}`;
        return;
      }
    }

    // Default to Hub
    showHubView();
  }

  function resolveWorkRoute(poetId, sub) {
    const poetObj = state.poets[poetId];
    if (!poetObj) return;

    // e.g. 'shabad-1', 'pada-3', 'doha-1', 'kafi-21'
    const match = sub.match(/^([a-zA-Z]+)-(\d+)$/);
    if (!match) {
      showPoetWelcome();
      return;
    }

    let genre = match[1].toLowerCase();
    const id = parseInt(match[2], 10);

    // Normalize genre alias
    if (genre === 'pada') genre = 'padaavali';
    if (genre === 'doha') genre = 'dohe';
    if (genre === 'siharfian') genre = 'siharfi';

    // Try finding matching item in manifest
    const manifestItem = (poetObj.manifest || []).find(m => {
      if (m.id !== id) return false;
      const mg = (m.genre || '').toLowerCase();
      return mg === genre || mg.startsWith(genre.slice(0, 4)) || (genre === 'siharfi' && mg === 'siharfian');
    });

    if (manifestItem && poetObj.data[manifestItem.uid]) {
      loadWork(manifestItem.uid, false);
      return;
    }

    // Direct lookup fallbacks
    const candidateUids = [
      `${genre}_${id}`,
      `kabir_${genre}_${id}`,
      `kabir_shabad_${id}`,
      `kabir_salok_${id}`,
      `kabir_doha_${id}`,
      `kabir_ramaini_${id}`,
      `kabir_sakhi_${id}`,
      `kabir_pad_${id}`,
      `farid_${genre}_${id}`,
      `farid_salok_${id}`,
      `farid_shabad_${id}`,
      `meerabai_${genre}_${id}`,
      `meerabai_pada_${id}`,
      `ravidas_${genre}_${id}`,
      `siharfi_${id}`,
      `siharfian_${id}`,
      `kafi_${id}`,
      String(id)
    ];

    for (const uid of candidateUids) {
      if (poetObj.data[uid]) {
        loadWork(uid, false);
        return;
      }
    }

    showPoetWelcome();
  }

  // View Display Functions
  function showHubView() {
    state.currentPoet = null;
    state.currentUid = null;
    document.body.removeAttribute('data-poet');
    
    el.hubView.style.display = 'flex';
    el.poetWorkspace.style.display = 'none';
    
    // Header adjustments
    el.headerEmblem.textContent = '✨';
    el.headerMainTitle.textContent = 'रहस्यवादी काव्य महाकोश';
    el.headerSubTitle.textContent = 'Mystic Poetry Archive • 1,673 Masterpieces';
    el.navHubBtn.style.display = 'none';
    el.poetSwitcherBtn.style.display = 'none';
    el.sidebarToggleBtn.style.display = 'none';
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function showPoetWorkspace(poetId) {
    const poet = state.poets[poetId];
    if (!poet) return;

    document.body.setAttribute('data-poet', poetId);

    el.hubView.style.display = 'none';
    el.poetWorkspace.style.display = 'flex';
    
    // Header adjustments
    el.headerEmblem.textContent = poet.emblem;
    el.headerMainTitle.textContent = poet.name;
    el.headerSubTitle.textContent = `${poet.name_en} • ${poet.total} Masterpieces`;
    el.navHubBtn.style.display = 'inline-flex';
    el.sidebarToggleBtn.style.display = 'inline-flex';

    // Switcher button cycles to next poet
    const poetList = ['bulleh-shah', 'sant-ravidas', 'sheikh-farid', 'meerabai', 'sant-kabir'];
    const currIdx = poetList.indexOf(poetId);
    const nextPoetId = poetList[(currIdx + 1) % poetList.length];
    const nextPoet = state.poets[nextPoetId];
    el.poetSwitcherBtn.style.display = 'inline-flex';
    el.poetSwitcherLabel.textContent = nextPoet.name;
    el.poetSwitcherBtn.onclick = () => {
      window.location.hash = `#/${nextPoetId}/`;
    };

    // Sidebar poet banner
    el.sidebarPoetEmblem.textContent = poet.emblem;
    el.sidebarPoetName.textContent = poet.name;

    renderSidebarTabs(poet);
    renderSidebarList();
  }

  function showPoetWelcome() {
    state.currentUid = null;
    el.poemView.style.display = 'none';
    el.welcomeView.style.display = 'block';

    const poet = state.poets[state.currentPoet];
    if (!poet) return;

    const titleEl = document.getElementById('poet-welcome-title');
    const subEl = document.getElementById('poet-welcome-sub');
    const descEl = document.getElementById('poet-welcome-desc');
    const gridEl = document.getElementById('welcome-genres-grid');

    titleEl.textContent = `${poet.name} : सम्पूर्ण रचनावली`;
    subEl.textContent = `${poet.name_en} : Complete Trilingual Edition (${poet.total} Works)`;
    
    if (state.currentPoet === 'bulleh-shah') {
      descEl.innerHTML = `सूफी दर्शन के अमर प्रतीक <strong>हज़रत बाबा बुल्ले शाह (1680–1757)</strong> की समस्त 351 कालजयी रचनाओं का प्रामाणिक त्रिभाषी शोध संस्करण। इसमें 160 काफ़ियां, बारहमाह, अठवारा, 40 गन्धां, सीहरफ़ियां और 56 दोहरे सम्मिलित हैं।`;
    } else if (state.currentPoet === 'sant-ravidas') {
      descEl.innerHTML = `भक्ति आंदोलन के युगदृष्टा <strong>संत शिरोमणि रविदास जी (1377–1528)</strong> की समस्त 208 कालजयी रचनाओं का प्रामाणिक त्रिभाषी शोध संस्करण। इसमें श्री गुरु ग्रंथ साहिब जी के 40 शब्द, 117 अमर पद और 51 साखी दोहे सम्मिलित हैं।`;
    } else if (state.currentPoet === 'sheikh-farid') {
      descEl.innerHTML = `चिश्ती सूफी परंपरा के प्रकाश-स्तंभ और पंजाबी के आदि-कवि <strong>बाबा शेख फरीद (1173–1266)</strong> की समस्त 134 कालजयी रचनाओं का प्रामाणिक त्रिभाषी शोध संस्करण। इसमें श्री गुरु ग्रंथ साहिब जी के 130 सलोक और 4 पावन शब्द सम्मिलित हैं।`;
    } else if (state.currentPoet === 'meerabai') {
      descEl.innerHTML = `भक्ति आंदोलन की अमर प्रेमावतार <strong>संत शिरोमणि मीराबाई (1498–1547)</strong> की समस्त 418 कालजयी रचनाओं का प्रामाणिक त्रिभाषी शोध संस्करण। इसमें राजस्थानी, डिंगल और ब्रजभाषा के 418 अमर भक्ति पद सम्मिलित हैं।`;
    } else if (state.currentPoet === 'sant-kabir') {
      descEl.innerHTML = `15वीं सदी के महानतम निर्गुण संत और समाज-सुधारक <strong>संत कबीर दास (1398–1518)</strong> की समस्त 562 कालजयी रचनाओं का प्रामाणिक त्रिभाषी शोध संस्करण। इसमें श्री गुरु ग्रंथ साहिब जी के 149 शब्द व 245 सलोक, 84 अमर दोहे, 8 रमैणी, ग्रंथावली के 59 साखी अंग (935 साखियाँ) और 17 पद राग (407 पद) सम्मिलित हैं।`;
    }

    // Render genre highlights
    gridEl.innerHTML = poet.tabs
      .filter(t => t.id !== 'all' && t.id !== 'bookmarks')
      .map(t => `
        <div class="genre-highlight-card" onclick="window.appAPI.setGenreFilter('${t.id}')">
          <div class="genre-card-title">${t.label}</div>
          <p style="font-size: 0.82rem; color: var(--text-faint); margin-top: 0.25rem;">संग्रह देखने हेतु क्लिक करें</p>
        </div>
      `).join('');

    // Highlight active in sidebar
    document.querySelectorAll('.kafi-item').forEach(i => i.classList.remove('active'));
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Sidebar Tabs & List Rendering
  function renderSidebarTabs(poet) {
    el.sidebarTabsContainer.innerHTML = poet.tabs.map(t => `
      <button class="tab-btn ${state.currentFilter === t.id ? 'active' : ''}" data-filter="${t.id}">
        ${t.label}
      </button>
    `).join('');

    el.sidebarTabsContainer.querySelectorAll('.tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        el.sidebarTabsContainer.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.currentFilter = btn.dataset.filter;
        renderSidebarList();
      });
    });
  }

  function getFilteredManifest() {
    const poet = state.poets[state.currentPoet];
    if (!poet) return [];

    let list = poet.manifest;

    // Filter by genre
    if (state.currentFilter === 'bookmarks') {
      list = list.filter(item => state.bookmarks.has(item.uid));
    } else if (state.currentFilter !== 'all') {
      list = list.filter(item => item.genre === state.currentFilter);
    }

    // Filter by search query
    const q = state.searchQuery.trim().toLowerCase();
    if (q) {
      list = list.filter(item => {
        const titleMatch = (item.title || '').toLowerCase().includes(q);
        const lineMatch = (item.first_line || '').toLowerCase().includes(q);
        const idMatch = String(item.id) === q;
        const themeMatch = (item.theme || '').toLowerCase().includes(q);
        return titleMatch || lineMatch || idMatch || themeMatch;
      });
    }

    return list;
  }

  function renderSidebarList() {
    const list = getFilteredManifest();
    el.filteredCountBadge.textContent = `${list.length} रचनाएं`;

    if (list.length === 0) {
      el.kafiList.innerHTML = `
        <li style="padding: 2.5rem 1rem; text-align: center; color: var(--text-faint); font-size: 0.9rem;">
          कोई रचना नहीं मिली।
        </li>
      `;
      return;
    }

    el.kafiList.innerHTML = list.map(item => {
      const isActive = item.uid === state.currentUid ? 'active' : '';
      const isBookmarked = state.bookmarks.has(item.uid);
      const genreLabel = item.genre_label || item.genre;
      
      return `
        <li class="kafi-item ${isActive}" data-uid="${item.uid}" id="item-${item.uid}">
          <div class="kafi-item-header">
            <span class="kafi-index"># ${item.id}</span>
            <span class="kafi-genre-pill">${genreLabel}</span>
          </div>
          <div class="kafi-item-title">${escapeHTML(item.title)}</div>
          <div class="kafi-item-firstline">${escapeHTML(item.first_line || '')}</div>
          ${isBookmarked ? '<span style="font-size:0.75rem; color:var(--gold-primary); margin-top:0.25rem;">★ पसंदीदा</span>' : ''}
        </li>
      `;
    }).join('');

    el.kafiList.querySelectorAll('.kafi-item').forEach(itemEl => {
      itemEl.addEventListener('click', () => {
        const uid = itemEl.dataset.uid;
        loadWork(uid, true);
        closeMobileSidebar();
      });
    });
  }

  // Work Loading & Reading
  function loadWork(uid, updateHash = true) {
    const poetObj = state.poets[state.currentPoet];
    if (!poetObj) return;

    const data = poetObj.data[uid];
    if (!data) return;

    state.currentUid = uid;

    // Update active highlight in sidebar
    el.kafiList.querySelectorAll('.kafi-item').forEach(item => {
      item.classList.toggle('active', item.dataset.uid === uid);
    });

    const activeItem = document.getElementById(`item-${uid}`);
    if (activeItem) {
      activeItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    // Populate poem view
    renderPoemReader(data);

    el.welcomeView.style.display = 'none';
    el.poemView.style.display = 'block';

    if (updateHash) {
      const g = data.genre;
      window.location.hash = `#/${state.currentPoet}/${g}-${data.id}`;
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function renderPoemReader(data) {
    el.poemGenreBadge.textContent = data.genre_label || data.genre;
    el.poemIndexBadge.textContent = `# ${data.id}`;

    if (data.raga) {
      el.poemRagaBadge.style.display = 'inline-flex';
      el.poemRagaBadge.textContent = data.raga;
    } else {
      el.poemRagaBadge.style.display = 'none';
    }

    el.poemTitleDev.textContent = data.title;
    el.poemTitleEn.textContent = data.theme || data.title_english || '';

    // Verses & Glosses normalization across both Bulleh Shah and Ravidas schemas
    let lines = [];
    let hiGlosses = [];
    let enGlosses = [];

    if (Array.isArray(data.lines) && data.lines.length > 0) {
      lines = data.lines;
      hiGlosses = data.hindi_gloss || [];
      enGlosses = data.english_gloss || [];
    } else if (Array.isArray(data.stanzas) && data.stanzas.length > 0) {
      data.stanzas.forEach(s => {
        (s.lines || []).forEach(l => {
          lines.push(l.original || '');
          hiGlosses.push(l.hindi_gloss || '');
          enGlosses.push(l.english_gloss || '');
        });
      });
    } else if (Array.isArray(data.original_verses)) {
      lines = data.original_verses;
    }

    el.poemVersesContainer.innerHTML = lines.map((line, idx) => {
      const hi = hiGlosses[idx] || '';
      const en = enGlosses[idx] || '';

      return `
        <div class="verse-group-card">
          <div class="verse-devanagari">${escapeHTML(line)}</div>
          ${hi ? `
            <div class="gloss-block hindi-gloss">
              <span class="gloss-lang-badge">🇮🇳 हिन्दी पदच्छेद</span>
              <div class="gloss-text">${escapeHTML(hi)}</div>
            </div>
          ` : ''}
          ${en ? `
            <div class="gloss-block english-gloss">
              <span class="gloss-lang-badge">🇬🇧 English Gloss</span>
              <div class="gloss-text">${escapeHTML(en)}</div>
            </div>
          ` : ''}
        </div>
      `;
    }).join('');

    // Translations
    let hiTrans = data.hindi_translation || '';
    if (!hiTrans && Array.isArray(data.stanzas)) {
      hiTrans = data.stanzas.map(s => Array.isArray(s.poetic_hindi) ? s.poetic_hindi.join('\n') : (s.poetic_hindi || '')).filter(Boolean).join('\n\n');
    }
    el.poemTransHindi.innerHTML = (hiTrans || 'काव्यानुवाद उपलब्ध नहीं है।').replace(/\n/g, '<br>');

    let enTrans = data.english_translation || '';
    if (!enTrans && Array.isArray(data.stanzas)) {
      enTrans = data.stanzas.map(s => Array.isArray(s.poetic_english) ? s.poetic_english.join('\n') : (s.poetic_english || '')).filter(Boolean).join('\n\n');
    }
    el.poemTransEnglish.innerHTML = (enTrans || 'English verse translation unavailable.').replace(/\n/g, '<br>');

    // Commentary
    el.poemCommentary.innerHTML = formatCommentaryMarkdown(data.commentary || 'दार्शनिक भावार्थ उपलब्ध नहीं है।');

    // Update Bookmark Button
    const isBookmarked = state.bookmarks.has(data.uid);
    el.bookmarkToggleBtn.textContent = isBookmarked ? '★' : '☆';
    el.bookmarkToggleBtn.style.color = isBookmarked ? 'var(--gold-primary)' : 'inherit';

    // Update Next/Prev buttons
    updateNavigationControls(data.uid);
  }

  function updateNavigationControls(currentUid) {
    const list = getFilteredManifest();
    const currIdx = list.findIndex(i => i.uid === currentUid);

    el.prevPoemBtn.disabled = currIdx <= 0;
    el.nextPoemBtn.disabled = currIdx < 0 || currIdx >= list.length - 1;

    el.prevPoemBtn.onclick = () => {
      if (currIdx > 0) {
        loadWork(list[currIdx - 1].uid, true);
      }
    };

    el.nextPoemBtn.onclick = () => {
      if (currIdx >= 0 && currIdx < list.length - 1) {
        loadWork(list[currIdx + 1].uid, true);
      }
    };

    el.returnHubBtn.onclick = () => {
      window.location.hash = '#/';
    };
  }

  // Global Cross-Poet Search (for Hub)
  function handleGlobalSearch(query) {
    const q = query.trim().toLowerCase();
    if (!q) {
      el.hubSearchResults.style.display = 'none';
      el.hubSearchResults.innerHTML = '';
      return;
    }

    const allMatches = {};
    let totalMatches = 0;

    for (const [pId, pObj] of Object.entries(state.poets)) {
      const matches = (pObj.manifest || []).filter(i => {
        return (i.title || '').toLowerCase().includes(q) ||
               (i.first_line || '').toLowerCase().includes(q) ||
               (i.theme || '').toLowerCase().includes(q);
      });
      if (matches.length > 0) {
        allMatches[pId] = matches;
        totalMatches += matches.length;
      }
    }

    if (totalMatches === 0) {
      el.hubSearchResults.innerHTML = `
        <div style="text-align: center; color: var(--text-faint); padding: 1.5rem;">
          '${escapeHTML(query)}' के लिए 1,111 रचनाओं में कोई परिणाम नहीं मिला।
        </div>
      `;
      el.hubSearchResults.style.display = 'block';
      return;
    }

    let html = `<div style="margin-bottom: 0.75rem; font-weight: 600; font-size: 0.85rem; color: var(--text-muted);">${totalMatches} रचनाएं मिलीं:</div>`;

    for (const [pId, matches] of Object.entries(allMatches)) {
      const poet = state.poets[pId];
      html += `
        <div class="search-results-group">
          <h4 style="color: ${poet.color};">${poet.name} (${matches.length} परिणाम)</h4>
          ${matches.slice(0, 10).map(m => `
            <div class="search-result-item" onclick="window.location.hash='#/${pId}/${m.genre}-${m.id}'">
              <div>
                <div class="search-result-title">${escapeHTML(m.title)}</div>
                <div style="font-size: 0.78rem; color: var(--text-faint);">${escapeHTML(m.first_line || m.theme || '')}</div>
              </div>
              <span class="search-result-badge" style="border: 1px solid ${poet.color}; color: ${poet.color};">${m.genre_label || m.genre}</span>
            </div>
          `).join('')}
        </div>
      `;
    }

    el.hubSearchResults.innerHTML = html;
    el.hubSearchResults.style.display = 'block';
  }


  // Utilities
  function escapeHTML(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function formatCommentaryMarkdown(md) {
    let out = escapeHTML(md);
    out = out.replace(/^### (.*$)/gim, '<h4 style="font-size: 1.15rem; color: var(--gold-primary); margin: 1.25rem 0 0.5rem;">$1</h4>');
    out = out.replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>');
    out = out.replace(/\n\n/g, '<br><br>');
    return out;
  }

  function closeMobileSidebar() {
    el.sidebar.classList.remove('mobile-open');
    el.sidebarBackdrop.classList.remove('active');
  }

  function toggleBookmark(uid) {
    if (state.bookmarks.has(uid)) {
      state.bookmarks.delete(uid);
      showToast('पसंदीदा सूची से हटाया गया');
    } else {
      state.bookmarks.add(uid);
      showToast('★ पसंदीदा सूची में जोड़ा गया!');
    }
    localStorage.setItem('mystic_bookmarks', JSON.stringify(Array.from(state.bookmarks)));

    if (state.currentUid === uid) {
      const isBookmarked = state.bookmarks.has(uid);
      el.bookmarkToggleBtn.textContent = isBookmarked ? '★' : '☆';
      el.bookmarkToggleBtn.style.color = isBookmarked ? 'var(--gold-primary)' : 'inherit';
    }

    if (state.currentFilter === 'bookmarks') {
      renderSidebarList();
    }
  }

  // Event Listeners
  function attachEventListeners() {
    // Brand header click
    el.brandHeader.addEventListener('click', () => {
      window.location.hash = '#/';
    });

    // Nav Hub Button
    el.navHubBtn.addEventListener('click', () => {
      window.location.hash = '#/';
    });

    // Poet Switcher Button
    el.poetSwitcherBtn.addEventListener('click', () => {
      if (state.currentPoet === 'bulleh-shah') {
        window.location.hash = '#/sant-ravidas/';
      } else {
        window.location.hash = '#/bulleh-shah/';
      }
    });

    // Sidebar back to hub button
    el.sidebarBackToHub.addEventListener('click', () => {
      window.location.hash = '#/';
    });

    // Theme Toggle
    el.themeBtn.addEventListener('click', toggleTheme);

    // Sidebar Mobile Toggle
    el.sidebarToggleBtn.addEventListener('click', () => {
      el.sidebar.classList.toggle('mobile-open');
      el.sidebarBackdrop.classList.toggle('active');
    });

    el.sidebarBackdrop.addEventListener('click', closeMobileSidebar);

    // Hub Search Input
    el.hubSearchInput.addEventListener('input', (e) => {
      handleGlobalSearch(e.target.value);
    });

    // Desktop Header Search
    el.searchInput.addEventListener('input', (e) => {
      const q = e.target.value;
      if (!state.currentPoet) {
        el.hubSearchInput.value = q;
        handleGlobalSearch(q);
      } else {
        state.searchQuery = q;
        renderSidebarList();
      }
    });

    // Sidebar Search
    el.sidebarSearchInput.addEventListener('input', (e) => {
      state.searchQuery = e.target.value;
      renderSidebarList();
    });

    // Keyboard shortcut / for search
    window.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== el.searchInput && document.activeElement !== el.hubSearchInput) {
        e.preventDefault();
        if (!state.currentPoet) {
          el.hubSearchInput.focus();
        } else {
          el.searchInput.focus();
        }
      }
    });

    // Random Work Button
    el.randomBtn.addEventListener('click', () => {
      if (!state.currentPoet) {
        // Pick random poet
        const pIds = ['bulleh-shah', 'sant-ravidas'];
        const chosenPoet = pIds[Math.floor(Math.random() * pIds.length)];
        const m = state.poets[chosenPoet].manifest;
        const randomItem = m[Math.floor(Math.random() * m.length)];
        window.location.hash = `#/${chosenPoet}/${randomItem.genre}-${randomItem.id}`;
      } else {
        const list = getFilteredManifest();
        if (list.length > 0) {
          const randomItem = list[Math.floor(Math.random() * list.length)];
          loadWork(randomItem.uid, true);
        }
      }
    });

    // Welcome Random Button
    const welcomeRand = document.getElementById('welcome-random-btn');
    if (welcomeRand) {
      welcomeRand.addEventListener('click', () => {
        el.randomBtn.click();
      });
    }

    // Bookmark Toggle Button
    el.bookmarkToggleBtn.addEventListener('click', () => {
      if (state.currentUid) {
        toggleBookmark(state.currentUid);
      }
    });

    // Bookmarks View Button
    el.bookmarksBtn.addEventListener('click', () => {
      if (!state.currentPoet) {
        window.location.hash = '#/bulleh-shah/';
      }
      state.currentFilter = 'bookmarks';
      const bTab = el.sidebarTabsContainer.querySelector('[data-filter="bookmarks"]');
      if (bTab) {
        el.sidebarTabsContainer.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        bTab.classList.add('active');
      }
      renderSidebarList();
    });

    // Copy Poem Button
    el.copyPoemBtn.addEventListener('click', () => {
      if (!state.currentUid) return;
      const poetObj = state.poets[state.currentPoet];
      const data = poetObj.data[state.currentUid];
      if (!data) return;

      const textToCopy = `【${data.title}】\nरचयिता: ${data.poet_name || 'महाकवि'}\n\n[मूल रचना]\n${(data.lines || []).join('\n')}\n\n[काव्यानुवाद]\n${data.hindi_translation || ''}\n\n[English Translation]\n${data.english_translation || ''}\n\nस्रोत: रहस्यवादी काव्य महाकोश (https://dg-code-source.github.io/mystic-poetry/)`;

      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast('सम्पूर्ण रचना क्लिपबोर्ड पर कॉपी हो गई!');
      }).catch(() => {
        showToast('कॉपी करने में त्रुटि हुई');
      });
    });

    // Font Scaling
    el.fontIncBtn.addEventListener('click', () => {
      if (state.fontScale < 1.35) {
        state.fontScale += 0.08;
        document.documentElement.style.setProperty('--reader-font-scale', state.fontScale);
      }
    });

    el.fontDecBtn.addEventListener('click', () => {
      if (state.fontScale > 0.8) {
        state.fontScale -= 0.08;
        document.documentElement.style.setProperty('--reader-font-scale', state.fontScale);
      }
    });

    // View Mode Tabs (All / Verses / Gloss / Trans)
    el.viewModeTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        el.viewModeTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        const mode = tab.dataset.mode;
        
        const secText = document.getElementById('section-original-text');
        const secTrans = document.getElementById('section-translations');
        const glossBlocks = document.querySelectorAll('.gloss-block');

        if (mode === 'all') {
          secText.style.display = 'block';
          secTrans.style.display = 'block';
          glossBlocks.forEach(b => b.style.display = 'block');
        } else if (mode === 'verses') {
          secText.style.display = 'block';
          secTrans.style.display = 'none';
          glossBlocks.forEach(b => b.style.display = 'none');
        } else if (mode === 'gloss') {
          secText.style.display = 'block';
          secTrans.style.display = 'none';
          glossBlocks.forEach(b => b.style.display = 'block');
        } else if (mode === 'trans') {
          secText.style.display = 'none';
          secTrans.style.display = 'block';
        }
      });
    });
  }

  // Public API for inline onclick handlers
  window.appAPI = {
    setGenreFilter: function (genreId) {
      state.currentFilter = genreId;
      const targetBtn = el.sidebarTabsContainer.querySelector(`[data-filter="${genreId}"]`);
      if (targetBtn) {
        el.sidebarTabsContainer.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        targetBtn.classList.add('active');
      }
      renderSidebarList();
      const list = getFilteredManifest();
      if (list.length > 0) {
        loadWork(list[0].uid, true);
      }
    }
  };

  // Start
  document.addEventListener('DOMContentLoaded', init);

})();
