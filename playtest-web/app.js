// Fisher-Yates shuffle
function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

const CATEGORY_ORDER = [
  "detection",
  "prevention",
  "enforcement",
  "governance"
];

const CATEGORY_COLORS = {
  detection:   "#27ae60",
  prevention:  "#d4a017",
  enforcement: "#c0392b",
  governance:  "#16a085"
};

let state = {
  mode: null,
  deck: [],
  hand: [],
  treaty: [],
  selected: new Set(),
  failures: 0,
  safety: 0,
  turn: 0,
  currentCard: null,
  log: [],
  gameOver: false
};

// Track collapsed categories (persists across renders)
let collapsedCategories = new Set();

function newGame(mode) {
  const crisisCount = mode === '5min' ? 8 : 18;
  const safetyCount = mode === '5min' ? 2 : 3;

  // Build and shuffle crisis pool
  const allEvents = [...CARDS.threat1, ...CARDS.threat2];
  shuffle(allEvents);
  const crisisCards = allEvents.slice(0, crisisCount);

  // Pick safety cards
  const safetyPool = [...CARDS.safety];
  shuffle(safetyPool);
  const safetyCards = safetyPool.slice(0, safetyCount);

  // Combine and shuffle deck
  const deck = shuffle([...crisisCards, ...safetyCards]);

  // Hand = all treaty cards (deep copy)
  const hand = CARDS.treaty.map(c => ({...c}));

  state = {
    mode,
    deck,
    hand,
    treaty: [],
    selected: new Set(),
    failures: 0,
    safety: 0,
    turn: 0,
    currentCard: null,
    log: [],
    gameOver: false
  };

  collapsedCategories = new Set();

  // Log header
  state.log.push(`Treaty Stress Test — ${mode} mode`);
  state.log.push(`Hand: ${hand.map(c => c.name).join(', ')}`);

  render();
}

function parseLabel(label) {
  // Returns {min, max} for failure range
  // "0 failures" => {min:0, max:0}
  // "0–1 failures" => {min:0, max:1}
  // "1–2 failures" => {min:1, max:2}
  // "1+ failures" => {min:1, max:Infinity}
  // "2+ failures" => {min:2, max:Infinity}
  // "3+ failures" => {min:3, max:Infinity}
  const plusMatch = label.match(/^(\d+)\+/);
  if (plusMatch) return { min: parseInt(plusMatch[1]), max: Infinity };
  const rangeMatch = label.match(/^(\d+)[–-](\d+)/);
  if (rangeMatch) return { min: parseInt(rangeMatch[1]), max: parseInt(rangeMatch[2]) };
  const singleMatch = label.match(/^(\d+) failure/);
  if (singleMatch) return { min: parseInt(singleMatch[1]), max: parseInt(singleMatch[1]) };
  return { min: 0, max: Infinity };
}

function activeTierLabel(card, failures) {
  // Returns label1 or label2 based on current failure count
  const r1 = parseLabel(card.label1);
  if (failures >= r1.min && failures <= r1.max) return card.label1;
  return card.label2;
}

function checkGameOver() {
  // Returns 'win', 'loss', or null
  if (state.safety >= 3) return 'win';
  if (state.failures >= 4) return 'loss';
  if (state.deck.length === 0 && state.currentCard === null) return 'win';
  return null;
}

function endGame(result) {
  state.gameOver = true;
  const resultStr = result === 'win' ? 'WIN' : 'LOSS';
  state.log.push(`Result: ${resultStr} | Failures: ${state.failures}/4 | Safety: ${state.safety}/3 | Treaty size: ${state.treaty.length}`);
  state.log.push(`Active treaty: ${state.treaty.length > 0 ? state.treaty.map(c => c.name).join(', ') : '(none)'}`);
  state.log.push(`Unused hand: ${state.hand.length > 0 ? state.hand.map(c => c.name).join(', ') : '(none)'}`);
  render();
}

function drawCard() {
  if (state.deck.length === 0) return;
  const card = state.deck.pop();
  state.turn++;
  state.currentCard = card;
  state.selected = new Set();
  render();
}

function handleEvent() {
  const card = state.currentCard;
  const selectedCards = [...state.selected].map(i => state.hand[i]);

  // Move selected cards from hand to treaty
  const selectedIndices = new Set(state.selected);
  state.hand = state.hand.filter((_, i) => !selectedIndices.has(i));
  state.treaty.push(...selectedCards);

  // Build transcript line
  let typeInfo = card.type;
  if (card.type === 'threat-2') {
    typeInfo = `threat-2, ${activeTierLabel(card, state.failures)}`;
  }
  let logLine = `Turn ${state.turn}: [${card.name}] (${typeInfo}) → HANDLED`;
  if (selectedCards.length > 0) {
    logLine += ` with ${selectedCards.map(c => c.name).join(', ')}`;
  } else {
    logLine += ` (treaty reference)`;
  }
  state.log.push(logLine);

  state.selected = new Set();
  state.currentCard = null;

  const result = checkGameOver();
  if (result) {
    endGame(result);
  } else {
    render();
  }
}

function failEvent() {
  const card = state.currentCard;
  state.failures++;
  state.selected = new Set();

  let typeInfo = card.type;
  if (card.type === 'threat-2') {
    typeInfo = `threat-2, ${activeTierLabel(card, state.failures - 1)}`;
  }
  state.log.push(`Turn ${state.turn}: [${card.name}] (${typeInfo}) → FAILED`);

  state.currentCard = null;

  const result = checkGameOver();
  if (result) {
    endGame(result);
  } else {
    render();
  }
}

function collectSafety() {
  const card = state.currentCard;
  state.safety++;
  state.log.push(`Turn ${state.turn}: [${card.name}] → Collected (${state.safety}/3)`);
  state.currentCard = null;

  const result = checkGameOver();
  if (result) {
    endGame(result);
  } else {
    render();
  }
}

function copyTranscript() {
  const text = state.log.join('\n');
  navigator.clipboard.writeText(text).then(() => {
    const btn = document.getElementById('copy-btn');
    if (btn) {
      btn.textContent = 'Copied!';
      setTimeout(() => { btn.textContent = 'Copy Transcript'; }, 1500);
    }
  }).catch(() => {
    // Fallback: show alert with transcript
    alert(text);
  });
}

function toggleCategory(cat) {
  if (collapsedCategories.has(cat)) {
    collapsedCategories.delete(cat);
  } else {
    collapsedCategories.add(cat);
  }
  render();
}

function toggleSelected(index) {
  if (state.selected.has(index)) {
    state.selected.delete(index);
  } else {
    state.selected.add(index);
  }
  render();
}

// ---- Rendering ----

function el(tag, attrs, ...children) {
  const e = document.createElement(tag);
  if (attrs) {
    for (const [k, v] of Object.entries(attrs)) {
      if (v == null) continue;  // skip null/undefined attributes
      if (k === 'class') e.className = v;
      else if (k === 'style') Object.assign(e.style, v);
      else if (k.startsWith('on')) e.addEventListener(k.slice(2), v);
      else e.setAttribute(k, v);
    }
  }
  for (const child of children) {
    if (child == null) continue;
    if (typeof child === 'string') e.appendChild(document.createTextNode(child));
    else e.appendChild(child);
  }
  return e;
}

function renderScoreBar() {
  return el('div', {class: 'score-bar'},
    el('div', {class: 'score-item'},
      el('span', {class: 'score-label'}, 'Turn'),
      el('span', {class: 'score-value'}, `${state.turn}`)
    ),
    el('div', {class: 'score-item'},
      el('span', {class: 'score-label'}, 'Failures'),
      el('span', {class: 'score-value score-failures'}, `${state.failures}/4`)
    ),
    el('div', {class: 'score-item'},
      el('span', {class: 'score-label'}, 'Safety'),
      el('span', {class: 'score-value score-safety'}, `${state.safety}/3`)
    ),
    el('div', {class: 'score-item'},
      el('span', {class: 'score-label'}, 'Deck'),
      el('span', {class: 'score-value'}, `${state.deck.length}`)
    )
  );
}

function renderEventCard(card) {
  const typeLabel = 'Threat';
  const parts = [
    el('div', {class: 'threat-type-badge'}, typeLabel),
    el('div', {class: 'threat-name'}, card.name)
  ];

  if (card.type === 'threat-1') {
    parts.push(el('p', {class: 'threat-text'}, card.text));
  } else {
    // threat-2: show both tiers
    const active1 = parseLabel(card.label1);
    const isActive1 = state.failures >= active1.min && state.failures <= active1.max;

    parts.push(
      el('div', {class: `tier-block${isActive1 ? ' tier-active' : ' tier-inactive'}`},
        el('div', {class: 'tier-label'}, card.label1),
        el('p', {class: 'threat-text'}, card.text1)
      ),
      el('div', {class: `tier-block${!isActive1 ? ' tier-active' : ' tier-inactive'}`},
        el('div', {class: 'tier-label'}, card.label2),
        el('p', {class: 'threat-text'}, card.text2)
      )
    );
  }

  return el('div', {class: 'threat-card'}, ...parts);
}

function renderTreatyPicker() {
  // Group hand cards by category
  const byCategory = {};
  state.hand.forEach((card, i) => {
    if (!byCategory[card.category]) byCategory[card.category] = [];
    byCategory[card.category].push({card, index: i});
  });

  // Count treaty cards by category
  const treatyByCategory = {};
  state.treaty.forEach(card => {
    treatyByCategory[card.category] = (treatyByCategory[card.category] || 0) + 1;
  });

  const sections = [];

  for (const cat of CATEGORY_ORDER) {
    const handItems = byCategory[cat] || [];
    const treatyCount = treatyByCategory[cat] || 0;
    if (handItems.length === 0 && treatyCount === 0) continue;

    const color = CATEGORY_COLORS[cat];
    const isCollapsed = collapsedCategories.has(cat);
    const catLabel = cat.charAt(0).toUpperCase() + cat.slice(1);

    const header = el('div', {
      class: 'category-header',
      style: { backgroundColor: hexToRgba(color, 0.2), borderLeft: `4px solid ${color}` },
      onclick: () => toggleCategory(cat)
    },
      el('span', {class: 'category-name'}, catLabel),
      el('span', {class: 'category-count'}, `${handItems.length} in hand, ${treatyCount} in treaty`),
      el('span', {class: 'category-chevron'}, isCollapsed ? '▶' : '▼')
    );

    const rows = handItems.map(({card, index}) => {
      const isSelected = state.selected.has(index);
      const rowStyle = isSelected
        ? { borderLeft: `4px solid ${color}`, backgroundColor: hexToRgba(color, 0.12) }
        : {};
      return el('div', {
        class: `hand-card-row${isSelected ? ' selected' : ''}`,
        style: rowStyle,
        onclick: () => toggleSelected(index)
      },
        el('div', {class: 'hand-card-name'}, card.name),
        el('div', {class: 'hand-card-desc'}, card.description)
      );
    });

    const body = el('div', {class: `category-body${isCollapsed ? ' collapsed' : ''}`}, ...rows);

    sections.push(el('div', {class: 'category-section'}, header, body));
  }

  return el('div', {class: 'treaty-picker'},
    el('h3', {class: 'picker-heading'}, 'Select treaty cards to play'),
    ...sections
  );
}

function renderActiveTreaty() {
  if (state.treaty.length === 0) return null;

  const byCategory = {};
  state.treaty.forEach(card => {
    if (!byCategory[card.category]) byCategory[card.category] = [];
    byCategory[card.category].push(card);
  });

  const sections = [];
  for (const cat of CATEGORY_ORDER) {
    const items = byCategory[cat];
    if (!items) continue;
    const color = CATEGORY_COLORS[cat];
    const catLabel = cat.charAt(0).toUpperCase() + cat.slice(1);

    const rows = items.map(card =>
      el('div', {class: 'treaty-card-row'},
        el('span', {class: 'treaty-check'}, '✓ '),
        el('span', {class: 'treaty-card-name'}, card.name)
      )
    );

    sections.push(el('div', {class: 'treaty-category'},
      el('div', {class: 'treaty-category-label', style: {color}}, catLabel),
      ...rows
    ));
  }

  return el('div', {class: 'active-treaty'},
    el('h3', {class: 'treaty-heading'}, `Active Treaty (${state.treaty.length} cards)`),
    ...sections
  );
}

function renderCopyButton() {
  return el('button', {
    id: 'copy-btn',
    class: 'btn btn-copy',
    onclick: copyTranscript
  }, 'Copy Transcript');
}

function renderPlayingScreen() {
  const app = document.getElementById('app');
  app.innerHTML = '';

  app.appendChild(renderScoreBar());

  const main = el('div', {class: 'main-content'});

  if (!state.currentCard) {
    // No card drawn yet, or waiting for next draw
    main.appendChild(
      el('button', {
        class: 'btn btn-draw',
        onclick: drawCard,
        disabled: state.deck.length === 0 ? 'true' : null
      }, state.deck.length === 0 ? 'Deck Empty' : 'Draw')
    );
    main.appendChild(renderCopyButton());

    // Show treaty picker collapsed for reference
    if (state.hand.length > 0 || state.treaty.length > 0) {
      main.appendChild(renderTreatyPicker());
    }
    const at = renderActiveTreaty();
    if (at) main.appendChild(at);

  } else if (state.currentCard.type === 'safety') {
    // Safety card
    main.appendChild(
      el('div', {class: 'threat-card safety-card'},
        el('div', {class: 'threat-type-badge safety-badge'}, 'Safety Breakthrough'),
        el('div', {class: 'threat-name'}, state.currentCard.name),
        el('p', {class: 'threat-text'}, state.currentCard.description)
      )
    );
    main.appendChild(
      el('button', {class: 'btn btn-collect', onclick: collectSafety}, 'Collect')
    );

  } else {
    // Event card
    main.appendChild(renderEventCard(state.currentCard));

    // Action buttons
    main.appendChild(
      el('div', {class: 'action-buttons'},
        el('button', {class: 'btn btn-handled', onclick: handleEvent}, 'Handled'),
        el('button', {class: 'btn btn-failed', onclick: failEvent}, 'Failed')
      )
    );

    // Treaty picker
    main.appendChild(renderTreatyPicker());

    const at = renderActiveTreaty();
    if (at) main.appendChild(at);

    main.appendChild(renderCopyButton());
  }

  app.appendChild(main);
}

function renderStartScreen() {
  const app = document.getElementById('app');
  app.innerHTML = '';

  app.appendChild(
    el('div', {class: 'start-screen'},
      el('h1', {class: 'start-title'}, 'Treaty Stress Test'),
      el('p', {class: 'start-subtitle'}, 'Solo Playtest'),
      el('div', {class: 'start-buttons'},
        el('button', {class: 'btn btn-draw', onclick: () => newGame('5min')}, '5-min game'),
        el('button', {class: 'btn btn-draw', onclick: () => newGame('15min')}, '15-min game')
      )
    )
  );
}

function renderGameOverScreen() {
  const app = document.getElementById('app');
  app.innerHTML = '';

  // Determine result from log
  const resultLine = state.log.find(l => l.startsWith('Result:')) || '';
  const isWin = resultLine.includes('WIN');

  const main = el('div', {class: 'main-content'});

  main.appendChild(
    el('div', {class: 'game-over-header'},
      el('div', {class: `game-over-result ${isWin ? 'result-win' : 'result-loss'}`}, isWin ? 'YOU WIN' : 'YOU LOSE'),
      el('div', {class: 'game-over-stats'}, resultLine.replace('Result: ', ''))
    )
  );

  main.appendChild(
    el('div', {class: 'transcript-box'},
      el('pre', {class: 'transcript-text'}, state.log.join('\n'))
    )
  );

  main.appendChild(
    el('div', {class: 'game-over-buttons'},
      renderCopyButton(),
      el('button', {class: 'btn btn-new-game', onclick: () => { state.mode = null; render(); }}, 'New Game')
    )
  );

  app.appendChild(main);
}

function render() {
  if (!state.mode) {
    renderStartScreen();
  } else if (state.gameOver) {
    renderGameOverScreen();
  } else {
    renderPlayingScreen();
  }
}

function hexToRgba(hex, alpha) {
  const r = parseInt(hex.slice(1,3), 16);
  const g = parseInt(hex.slice(3,5), 16);
  const b = parseInt(hex.slice(5,7), 16);
  return `rgba(${r},${g},${b},${alpha})`;
}

// Boot
render();
