/**
 * Baba Bulleh Shah: Complete Works (सम्पूर्ण रचनावली)
 * Trilingual Master Edition: 160 Kafian, 12 Baranmah, 7 Athwara, 40 Gandhan, 76 Siharfian, 56 Dohre (Total 351 Masterpieces)
 */

(function () {
  'use strict';

  // Application State
  const state = {
    manifest: window.BULLEH_SHAH_MANIFEST || [],
    dataStore: window.BULLEH_SHAH_DATA || {},
    currentUid: null,
    currentFilter: 'all', // 'all', 'kafi', 'baranmah', 'athwara', 'dohre', 'gandhan', 'siharfian', 'bookmarks'
    searchQuery: '',
    viewMode: 'all', // 'all', 'verses', 'gloss', 'trans'
    fontScale: 1.0,
    theme: localStorage.getItem('bbs_theme') || 'dark',
    bookmarks: new Set(JSON.parse(localStorage.getItem('bbs_bookmarks') || '[]'))
  };

  // DOM Elements
  const el = {
    themeBtn: document.getElementById('theme-toggle-btn'),
    themeIcon: document.getElementById('theme-icon'),
    sidebarToggleBtn: document.getElementById('sidebar-toggle-btn'),
    sidebar: document.getElementById('app-sidebar'),
    sidebarBackdrop: document.getElementById('sidebar-backdrop'),
    kafiList: document.getElementById('kafi-list-container'),
    searchInput: document.getElementById('search-input'),
    sidebarSearchInput: document.getElementById('sidebar-search-input'),
    filterTabs: document.querySelectorAll('.tab-btn'),
    itemCountBadge: document.getElementById('filtered-count-badge'),
    welcomeView: document.getElementById('welcome-hero-view'),
    poemView: document.getElementById('poem-reader-view'),
    randomBtn: document.getElementById('random-kafi-btn'),
    bookmarksBtn: document.getElementById('bookmarks-view-btn'),
    toast: document.getElementById('toast-notification'),
    toastMsg: document.getElementById('toast-message'),
    viewModeTabs: document.querySelectorAll('.view-tab')
  };

  // Initialize
  function init() {
    applyTheme(state.theme);
    initViewFromHash();
    renderSidebar();
    attachEventListeners();
  }

  // Theme Management
  function applyTheme(theme) {
    state.theme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('bbs_theme', theme);

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

  // URL Hash Routing
  function initViewFromHash() {
    const hash = window.location.hash;
    if (!hash) {
      showWelcomeView();
      return;
    }

    // Match generic prefix like #kafi-21, #baranmah-1, #athwara-7, #dohre-1, #gandhan-1, #siharfi-1
    const match = hash.match(/^#([a-zA-Z]+)-(\d+)$/);
    if (match) {
      const genre = match[1];
      const id = parseInt(match[2], 10);
      const uid = `${genre}_${id}`;
      if (state.dataStore[uid] || state.dataStore[id]) {
        loadWork(uid, false);
        return;
      }
    }
    showWelcomeView();
  }

  window.addEventListener('hashchange', () => {
    const hash = window.location.hash;
    const match = hash.match(/^#([a-zA-Z]+)-(\d+)$/);
    if (match) {
      const uid = `${match[1]}_${match[2]}`;
      if (uid !== state.currentUid) {
        loadWork(uid, false);
      }
    } else if (!hash) {
      showWelcomeView();
    }
  });

  // Filter & Search Logic
  function getFilteredManifest() {
    return state.manifest.filter(item => {
      // Filter by genre
      if (state.currentFilter !== 'all') {
        if (state.currentFilter === 'bookmarks') {
          if (!state.bookmarks.has(item.uid)) return false;
        } else if (item.genre !== state.currentFilter) {
          return false;
        }
      }

      // Filter by search query
      if (state.searchQuery) {
        const q = state.searchQuery.toLowerCase().trim();
        const idMatch = String(item.id) === q;
        const titleMatch = item.title.toLowerCase().includes(q);
        const enMatch = (item.title_english || '').toLowerCase().includes(q);
        const lineMatch = (item.first_line || '').toLowerCase().includes(q);
        const genreMatch = (item.genre_label || '').toLowerCase().includes(q);
        return idMatch || titleMatch || enMatch || lineMatch || genreMatch;
      }
      return true;
    });
  }

  // Render Sidebar
  function renderSidebar() {
    if (!el.kafiList) return;
    const items = getFilteredManifest();

    if (el.itemCountBadge) {
      el.itemCountBadge.textContent = `${items.length} रचनाएं`;
    }

    if (items.length === 0) {
      el.kafiList.innerHTML = `
        <li style="padding: 2.5rem 1rem; text-align: center; color: var(--text-faint);">
          <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">🍃</div>
          <div style="font-weight: 600;">कोई रचना नहीं मिली</div>
          <div style="font-size: 0.8rem; margin-top: 0.25rem;">कृपया अन्य खोज शब्द आज़माएं</div>
        </li>
      `;
      return;
    }

    el.kafiList.innerHTML = items.map(item => {
      const isActive = item.uid === state.currentUid;
      const isStarred = state.bookmarks.has(item.uid);
      return `
        <li class="kafi-item ${isActive ? 'active' : ''}" data-uid="${item.uid}" id="sidebar-item-${item.uid}">
          <div class="kafi-num-pill">${item.id}</div>
          <div class="kafi-info">
            <div class="kafi-item-title">${escapeHtml(item.title)}</div>
            <div class="kafi-item-sub">
              <span style="font-style: normal; color: var(--gold-primary); font-weight: 600; margin-right: 4px;">[${escapeHtml(item.genre_label || 'रचना')}]</span>
              ${escapeHtml(item.title_english || item.first_line || '')}
            </div>
          </div>
          <button class="kafi-star-btn ${isStarred ? 'starred' : ''}" data-star-uid="${item.uid}" title="${isStarred ? 'पसंदीदा से हटाएं' : 'पसंदीदा में जोड़ें'}">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="${isStarred ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2">
              <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
            </svg>
          </button>
        </li>
      `;
    }).join('');

    // Attach click events on sidebar items
    el.kafiList.querySelectorAll('.kafi-item').forEach(li => {
      li.addEventListener('click', (e) => {
        if (e.target.closest('.kafi-star-btn')) return;
        const uid = li.getAttribute('data-uid');
        loadWork(uid);
        closeMobileSidebar();
      });
    });

    // Attach star button clicks
    el.kafiList.querySelectorAll('.kafi-star-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const uid = btn.getAttribute('data-star-uid');
        toggleBookmark(uid);
      });
    });
  }

  // Bookmarks Management
  function toggleBookmark(uid) {
    if (state.bookmarks.has(uid)) {
      state.bookmarks.delete(uid);
      showToast(`पसंदीदा से हटाया गया`);
    } else {
      state.bookmarks.add(uid);
      showToast(`पसंदीदा में जोड़ा गया`);
    }
    localStorage.setItem('bbs_bookmarks', JSON.stringify(Array.from(state.bookmarks)));
    renderSidebar();
    updateBookmarkBtnState();
  }

  function updateBookmarkBtnState() {
    const starBtn = document.getElementById('active-kafi-star-btn');
    if (starBtn && state.currentUid) {
      const isStarred = state.bookmarks.has(state.currentUid);
      starBtn.classList.toggle('active', isStarred);
      starBtn.title = isStarred ? 'पसंदीदा से हटाएं' : 'पसंदीदा में जोड़ें';
    }
  }

  // Load Any Work
  function loadWork(uid, updateHash = true) {
    let item = state.dataStore[uid];
    if (!item) {
      // Fallback: check if integer ID was passed for kafian
      const numMatch = uid.match(/\d+/);
      if (numMatch && state.dataStore[numMatch[0]]) {
        item = state.dataStore[numMatch[0]];
        uid = `kafi_${numMatch[0]}`;
      }
    }

    if (!item) {
      showToast(`रचना लोड करने में असमर्थ`);
      return;
    }

    state.currentUid = uid;
    if (updateHash) {
      const hashPart = uid.replace('_', '-');
      window.location.hash = `#${hashPart}`;
    }

    renderWork(item);
    renderSidebar();

    // Scroll active item into view in sidebar
    const activeItem = document.getElementById(`sidebar-item-${uid}`);
    if (activeItem) {
      activeItem.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    // Scroll reader window to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function showWelcomeView() {
    state.currentUid = null;
    if (el.welcomeView) el.welcomeView.style.display = 'block';
    if (el.poemView) el.poemView.classList.remove('active');
    renderSidebar();
  }

  // Render Work into Reader View
  function renderWork(k) {
    if (el.welcomeView) el.welcomeView.style.display = 'none';
    if (!el.poemView) return;
    el.poemView.classList.add('active');

    const uid = k.uid || `kafi_${k.id}`;
    const isStarred = state.bookmarks.has(uid);

    // Find previous and next within the same genre
    const genreItems = state.manifest.filter(m => m.genre === k.genre);
    const currIdx = genreItems.findIndex(m => m.uid === uid);
    const prevItem = currIdx > 0 ? genreItems[currIdx - 1] : null;
    const nextItem = currIdx < genreItems.length - 1 ? genreItems[currIdx + 1] : null;

    // Tags
    const tags = [];
    if (k.genre_label) tags.push(`<span class="tag-badge"><strong>विधा:</strong> ${escapeHtml(k.genre_label)}</span>`);
    if (k.raga) tags.push(`<span class="tag-badge"><strong>राग:</strong> ${escapeHtml(k.raga)}</span>`);
    if (k.meter) tags.push(`<span class="tag-badge"><strong>छंद:</strong> ${escapeHtml(k.meter)}</span>`);
    if (k.theme) tags.push(`<span class="tag-badge"><strong>विषय:</strong> ${escapeHtml(k.theme)}</span>`);
    if (k.season) tags.push(`<span class="tag-badge"><strong>ऋतु:</strong> ${escapeHtml(k.season)}</span>`);

    // Stanzas rendering
    const showVerses = state.viewMode === 'all' || state.viewMode === 'verses';
    const showGloss = state.viewMode === 'all' || state.viewMode === 'gloss';
    const showTrans = state.viewMode === 'all' || state.viewMode === 'trans';

    // Original Verses Block
    let versesHtml = '';
    if (showVerses) {
      const lines = k.original_verses || [];
      versesHtml = `
        <section class="reader-card" id="card-original-verses">
          <div class="reader-card-header">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 19l7-7 3 3-7 7-3-3z"/>
              <path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/>
              <path d="M2 2l7.586 7.586"/>
              <circle cx="11" cy="11" r="2"/>
            </svg>
            <div>
              <h3>मूल पाठ</h3>
              <span class="en-badge">Original Classical Punjabi</span>
            </div>
          </div>
          <div class="verses-container">
            ${lines.map(l => `<div class="verse-line">${escapeHtml(l)}</div>`).join('')}
          </div>
        </section>
      `;
    }

    // Word-by-Word Gloss Block
    let glossHtml = '';
    if (showGloss && k.stanzas && k.stanzas.length > 0) {
      glossHtml = `
        <section class="reader-card" id="card-glossary">
          <div class="reader-card-header">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="8"/>
              <line x1="21" y1="21" x2="16.65" y2="16.65"/>
            </svg>
            <div>
              <h3>पद-वार शब्दार्थ एवं पदच्छेद</h3>
              <span class="en-badge">Word-by-Word Hindi & English Gloss</span>
            </div>
          </div>
          <div class="gloss-container">
            ${k.stanzas.map((stanza, sIdx) => `
              <div class="stanza-gloss-group">
                ${k.stanzas.length > 1 ? `<span class="stanza-badge">छंद ${sIdx + 1} (Stanza ${sIdx + 1})</span>` : ''}
                ${stanza.lines.map(line => `
                  <div class="gloss-line-card">
                    <div class="gloss-orig-line">${escapeHtml(line.original)}</div>
                    ${line.hindi_gloss ? `
                      <div class="gloss-detail">
                        <strong>हिन्दी शब्दार्थ:</strong>
                        <span class="gloss-hi-text">${formatGlossWords(line.hindi_gloss)}</span>
                      </div>
                    ` : ''}
                    ${line.english_gloss ? `
                      <div class="gloss-detail">
                        <strong>English Gloss:</strong>
                        <span class="gloss-en-text">${formatGlossWords(line.english_gloss)}</span>
                      </div>
                    ` : ''}
                  </div>
                `).join('')}
              </div>
            `).join('')}
          </div>
        </section>
      `;
    }

    // Poetic Translations Block
    let transHtml = '';
    if (showTrans && k.stanzas && k.stanzas.length > 0) {
      transHtml = `
        <section class="reader-card" id="card-translations">
          <div class="reader-card-header">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <line x1="2" y1="12" x2="22" y2="12"/>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
            </svg>
            <div>
              <h3>काव्यात्मक अनुवाद</h3>
              <span class="en-badge">Poetic Metered Rendition</span>
            </div>
          </div>
          <div class="translations-grid">
            <div class="trans-col">
              <div class="trans-col-header">
                <span>🇮🇳 हिन्दी काव्यात्मक भावार्थ</span>
              </div>
              <div class="trans-body-hi">
                ${k.stanzas.map(s => `
                  <div class="trans-stanza">
                    ${(s.poetic_hindi || []).map(l => `<div>${escapeHtml(l)}</div>`).join('')}
                  </div>
                `).join('')}
              </div>
            </div>
            <div class="trans-col">
              <div class="trans-col-header">
                <span>🇬🇧 English Poetic Translation</span>
              </div>
              <div class="trans-body-en">
                ${k.stanzas.map(s => `
                  <div class="trans-stanza">
                    ${(s.poetic_english || []).map(l => `<div>${escapeHtml(l)}</div>`).join('')}
                  </div>
                `).join('')}
              </div>
            </div>
          </div>
        </section>
      `;
    }

    // Commentary Block
    let commentaryHtml = '';
    if (k.commentary && (state.viewMode === 'all' || state.viewMode === 'verses')) {
      const paras = k.commentary.split('\n\n').filter(Boolean);
      commentaryHtml = `
        <section class="reader-card" id="card-commentary">
          <div class="reader-card-header">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>
            </svg>
            <div>
              <h3>दार्शनिक एवं सूफी व्याख्या</h3>
              <span class="en-badge">Sufi & Philosophical Meaning</span>
            </div>
          </div>
          <div class="commentary-body">
            ${paras.map(p => `<p>${escapeHtml(p)}</p>`).join('')}
          </div>
        </section>
      `;
    }

    // Render Full Reader HTML
    el.poemView.innerHTML = `
      <div class="poem-header-card">
        <div class="poem-meta-top">
          <span class="section-tag">${escapeHtml(k.section || k.genre_label || '')}</span>
          <div class="poem-top-nav">
            <button class="icon-btn ${isStarred ? 'active' : ''}" id="active-kafi-star-btn" title="पसंदीदा">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="${isStarred ? 'currentColor' : 'none'}" stroke="currentColor" stroke-width="2">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
              </svg>
            </button>
            <button class="icon-btn" id="copy-kafi-btn" title="रचना कॉपी करें">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="9" y="9" width="13" height="13" rx="2" ry="2"/>
                <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>
              </svg>
            </button>
            <button class="icon-btn" id="share-link-btn" title="लिंक कॉपी करें">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="18" cy="5" r="3"/>
                <circle cx="6" cy="12" r="3"/>
                <circle cx="18" cy="19" r="3"/>
                <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/>
                <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/>
              </svg>
            </button>
          </div>
        </div>

        <h2 class="poem-title-dev">${escapeHtml(k.title)}</h2>
        ${k.title_english ? `<div class="poem-title-en">${escapeHtml(k.title_english)}</div>` : ''}

        ${tags.length > 0 ? `<div class="tags-row">${tags.join('')}</div>` : ''}

        ${k.refrain ? `
          <div class="context-box">
            <strong>टेक (Refrain):</strong> ${escapeHtml(k.refrain)}
          </div>
        ` : ''}

        ${k.historical_context ? `
          <div class="context-box">
            <strong>प्रसंग एवं संदर्भ:</strong> ${escapeHtml(k.historical_context)}
          </div>
        ` : ''}
      </div>

      <!-- View Selector Bar -->
      <div class="view-tabs-bar">
        <div class="view-tabs-group">
          <button class="view-tab ${state.viewMode === 'all' ? 'active' : ''}" data-mode="all">📜 समग्र अध्ययन</button>
          <button class="view-tab ${state.viewMode === 'verses' ? 'active' : ''}" data-mode="verses">🪶 मूल पाठ</button>
          <button class="view-tab ${state.viewMode === 'gloss' ? 'active' : ''}" data-mode="gloss">🔍 पद-वार शब्दार्थ</button>
          <button class="view-tab ${state.viewMode === 'trans' ? 'active' : ''}" data-mode="trans">🌐 काव्यात्मक अनुवाद</button>
        </div>
        <div class="font-controls">
          <button class="font-btn" id="btn-font-sub" title="छोटा फॉन्ट">A-</button>
          <button class="font-btn" id="btn-font-reset" title="सामान्य फॉन्ट">A</button>
          <button class="font-btn" id="btn-font-add" title="बड़ा फॉन्ट">A+</button>
        </div>
      </div>

      <!-- Content Cards -->
      ${versesHtml}
      ${glossHtml}
      ${transHtml}
      ${commentaryHtml}

      <!-- Bottom Prev / Next Nav -->
      <div class="reader-bottom-nav">
        ${prevItem ? `
          <div class="nav-card-btn" id="prev-work-card" data-nav-uid="${prevItem.uid}">
            <div class="nav-dir">← पिछली रचना (${escapeHtml(prevItem.genre_label)})</div>
            <div class="nav-poem-title">${escapeHtml(prevItem.title)}</div>
          </div>
        ` : '<div></div>'}
        ${nextItem ? `
          <div class="nav-card-btn" id="next-work-card" data-nav-uid="${nextItem.uid}" style="text-align: right;">
            <div class="nav-dir">अगली रचना (${escapeHtml(nextItem.genre_label)}) →</div>
            <div class="nav-poem-title">${escapeHtml(nextItem.title)}</div>
          </div>
        ` : '<div></div>'}
      </div>
    `;

    attachWorkActions(k);
  }

  function formatGlossWords(str) {
    if (!str) return '';
    const escaped = escapeHtml(str);
    return escaped.replace(/\(([^)]+)\)/g, '<span style="color: var(--gold-primary); font-weight: 600;">($1)</span>');
  }

  function attachWorkActions(k) {
    const starBtn = document.getElementById('active-kafi-star-btn');
    if (starBtn) {
      starBtn.addEventListener('click', () => toggleBookmark(k.uid || `kafi_${k.id}`));
    }

    const copyBtn = document.getElementById('copy-kafi-btn');
    if (copyBtn) {
      copyBtn.addEventListener('click', () => {
        const textToCopy = `${k.title}\n\n${(k.original_verses || []).join('\n')}\n\n— बाबा बुल्ले शाह`;
        navigator.clipboard.writeText(textToCopy).then(() => {
          showToast('रचना क्लिपबोर्ड में कॉपी हो गई!');
        }).catch(() => {
          showToast('कॉपी करने में असमर्थ');
        });
      });
    }

    const shareBtn = document.getElementById('share-link-btn');
    if (shareBtn) {
      shareBtn.addEventListener('click', () => {
        const url = window.location.href;
        navigator.clipboard.writeText(url).then(() => {
          showToast('लिंक कॉपी हो गया!');
        });
      });
    }

    // View Mode Switchers
    el.poemView.querySelectorAll('.view-tab').forEach(btn => {
      btn.addEventListener('click', () => {
        state.viewMode = btn.getAttribute('data-mode');
        renderWork(k);
      });
    });

    // Font Controls
    const fontSub = document.getElementById('btn-font-sub');
    const fontReset = document.getElementById('btn-font-reset');
    const fontAdd = document.getElementById('btn-font-add');

    if (fontSub) {
      fontSub.addEventListener('click', () => {
        state.fontScale = Math.max(0.8, state.fontScale - 0.1);
        document.documentElement.style.setProperty('--reader-font-scale', state.fontScale);
      });
    }
    if (fontReset) {
      fontReset.addEventListener('click', () => {
        state.fontScale = 1.0;
        document.documentElement.style.setProperty('--reader-font-scale', 1.0);
      });
    }
    if (fontAdd) {
      fontAdd.addEventListener('click', () => {
        state.fontScale = Math.min(1.4, state.fontScale + 0.1);
        document.documentElement.style.setProperty('--reader-font-scale', state.fontScale);
      });
    }

    // Bottom Navigation Cards
    const prevCard = document.getElementById('prev-work-card');
    if (prevCard) {
      prevCard.addEventListener('click', () => {
        const uid = prevCard.getAttribute('data-nav-uid');
        loadWork(uid);
      });
    }

    const nextCard = document.getElementById('next-work-card');
    if (nextCard) {
      nextCard.addEventListener('click', () => {
        const uid = nextCard.getAttribute('data-nav-uid');
        loadWork(uid);
      });
    }
  }

  // Sidebar Controls
  function toggleMobileSidebar() {
    if (el.sidebar) el.sidebar.classList.toggle('mobile-open');
    if (el.sidebarBackdrop) el.sidebarBackdrop.classList.toggle('active');
  }

  function closeMobileSidebar() {
    if (el.sidebar) el.sidebar.classList.remove('mobile-open');
    if (el.sidebarBackdrop) el.sidebarBackdrop.classList.remove('active');
  }

  // Global Event Listeners
  function attachEventListeners() {
    if (el.themeBtn) el.themeBtn.addEventListener('click', toggleTheme);
    if (el.sidebarToggleBtn) el.sidebarToggleBtn.addEventListener('click', toggleMobileSidebar);
    if (el.sidebarBackdrop) el.sidebarBackdrop.addEventListener('click', closeMobileSidebar);

    // Search input
    if (el.searchInput) {
      el.searchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value;
        renderSidebar();
      });
    }

    // Filter Tabs
    el.filterTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        el.filterTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        state.currentFilter = tab.getAttribute('data-filter');
        renderSidebar();
      });
    });

    // Random Masterpiece Button
    if (el.randomBtn) {
      el.randomBtn.addEventListener('click', () => {
        const randomItem = state.manifest[Math.floor(Math.random() * state.manifest.length)];
        if (randomItem) {
          loadWork(randomItem.uid);
          showToast(`${randomItem.title} खोला गया`);
        }
      });
    }

    // Bookmarks View Button
    if (el.bookmarksBtn) {
      el.bookmarksBtn.addEventListener('click', () => {
        el.filterTabs.forEach(t => {
          if (t.getAttribute('data-filter') === 'bookmarks') t.click();
        });
        if (window.innerWidth <= 850) toggleMobileSidebar();
      });
    }

    // Brand Header Link
    const brand = document.getElementById('brand-header-link');
    if (brand) {
      brand.addEventListener('click', () => {
        window.location.hash = '';
        showWelcomeView();
      });
    }

    // Feature pill cards on hero welcome page (6 classical genres)
    document.querySelectorAll('.feature-pill').forEach(pill => {
      const activateGenre = () => {
        const genre = pill.getAttribute('data-genre');
        const firstUid = pill.getAttribute('data-first-uid');

        // 1. Activate the corresponding sidebar tab
        if (genre && el.filterTabs) {
          el.filterTabs.forEach(t => {
            if (t.getAttribute('data-filter') === genre) {
              el.filterTabs.forEach(tab => tab.classList.remove('active'));
              t.classList.add('active');
              state.currentFilter = genre;
              renderSidebar();
            }
          });
        }

        // 2. Load the first work of that genre directly into reader
        if (firstUid) {
          loadWork(firstUid);
          const heading = pill.querySelector('h3');
          const title = heading ? heading.textContent.trim() : '';
          if (title) showToast(`${title} खोला गया`);
        }
      };

      pill.addEventListener('click', activateGenre);
      pill.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          activateGenre();
        }
      });
    });

    // Quick pick chips on hero welcome page
    document.querySelectorAll('.pick-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        const targetUid = chip.getAttribute('data-uid');
        if (targetUid) loadWork(targetUid);
      });
    });

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
        if (e.key === 'Escape') document.activeElement.blur();
        return;
      }
      if (e.key === '/' && el.searchInput) {
        e.preventDefault();
        el.searchInput.focus();
        return;
      }
      if (e.key === 't' || e.key === 'T') {
        toggleTheme();
        return;
      }
      if (e.key === 'Escape') closeMobileSidebar();
    });
  }

  function escapeHtml(text) {
    if (!text) return '';
    return String(text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
