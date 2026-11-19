/* Phone menu toggle and tap-to-open dropdowns (hover menus don't work on touch screens). */
(function () {
  // The 2022 layout spaces content with empty table cells; mark them so phones can drop them.
  var cells = document.querySelectorAll('#Wrap03 td');
  for (var c = 0; c < cells.length; c++) {
    if (!cells[c].children.length && !cells[c].textContent.replace(/ /g, '').trim()) cells[c].className += ' spacer';
  }

  var nav = document.getElementById('Wrap02');
  var menu = document.getElementById('menu');
  if (!nav || !menu) return;

  var toggle = document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'menu-toggle';
  toggle.setAttribute('aria-expanded', 'false');
  toggle.setAttribute('aria-controls', 'menu');
  toggle.innerHTML = '<span aria-hidden="true"></span>Menu';
  menu.parentNode.insertBefore(toggle, menu);
  toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('nav-open');
    toggle.setAttribute('aria-expanded', String(open));
  });

  var subs = menu.querySelectorAll('li.has-sub > a');
  for (var i = 0; i < subs.length; i++) {
    subs[i].addEventListener('click', function (e) {
      var li = this.parentNode;
      var touch = window.matchMedia('(hover: none), (max-width: 820px)').matches;
      if (!touch && this.getAttribute('href') !== '#') return; // desktop: hover opens it, the link still works
      e.preventDefault();
      var wasOpen = li.classList.contains('open');
      var open = menu.querySelectorAll('li.open');
      for (var j = 0; j < open.length; j++) open[j].classList.remove('open');
      if (!wasOpen) li.classList.add('open');
      this.setAttribute('aria-expanded', String(!wasOpen));
    });
  }
  document.addEventListener('click', function (e) {
    if (menu.contains(e.target)) return;
    var open = menu.querySelectorAll('li.open');
    for (var j = 0; j < open.length; j++) open[j].classList.remove('open');
  });
})();

/* Gallery viewer: photo centred on screen and scaled to fit, with swipe, arrow keys and Esc. */
(function () {
  var nodes = document.querySelectorAll('td.Font20, a[data-lightbox]');
  if (!document.querySelector('a[data-lightbox]')) return;
  var items = [], section = '';
  for (var i = 0; i < nodes.length; i++) {
    if (nodes[i].tagName === 'TD') { section = nodes[i].textContent.replace(/\s+/g, ' ').trim(); continue; }
    items.push({ link: nodes[i], href: nodes[i].getAttribute('href'), caption: section });
  }

  var box = document.createElement('div');
  box.className = 'pv';
  box.hidden = true;
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-modal', 'true');
  box.setAttribute('aria-label', 'Photo viewer');
  box.innerHTML = '<button type="button" class="pv-close" aria-label="Close">&times;</button>' +
    '<button type="button" class="pv-prev" aria-label="Previous photo">&lsaquo;</button>' +
    '<img alt="">' +
    '<div class="pv-cap"></div>' +
    '<button type="button" class="pv-next" aria-label="Next photo">&rsaquo;</button>';
  document.body.appendChild(box);
  var img = box.querySelector('img'), cap = box.querySelector('.pv-cap');
  var prev = box.querySelector('.pv-prev'), next = box.querySelector('.pv-next');
  var current = -1, lastFocus = null;

  function fit() {
    if (!img.naturalWidth) return;
    var maxW = window.innerWidth - 32, maxH = window.innerHeight - 150;
    // The 2022 photos are small (about 250px wide), so scale them up to a comfortable size, capped at 3x.
    var scale = Math.min(maxW / img.naturalWidth, maxH / img.naturalHeight, 3);
    img.style.width = Math.round(img.naturalWidth * scale) + 'px';
    img.style.height = Math.round(img.naturalHeight * scale) + 'px';
  }
  img.addEventListener('load', fit);
  window.addEventListener('resize', function () { if (!box.hidden) fit(); });

  function show(n) {
    current = n;
    img.src = items[n].href;
    img.alt = items[n].caption ? items[n].caption + ', photo ' + (n + 1) : 'Photo ' + (n + 1);
    cap.textContent = items[n].caption;
    var count = document.createElement('span');
    count.textContent = (n + 1) + ' of ' + items.length;
    cap.appendChild(count);
    prev.disabled = n === 0;
    next.disabled = n === items.length - 1;
  }
  function open(n) {
    lastFocus = document.activeElement;
    box.hidden = false;
    document.body.classList.add('pv-open');
    show(n);
    requestAnimationFrame(function () { box.classList.add('show'); });
    box.querySelector('.pv-close').focus();
  }
  function close() {
    box.classList.remove('show');
    document.body.classList.remove('pv-open');
    box.hidden = true;
    img.removeAttribute('src');
    if (lastFocus) lastFocus.focus();
  }
  function step(d) { var n = current + d; if (n >= 0 && n < items.length) show(n); }

  items.forEach(function (it, n) {
    it.link.addEventListener('click', function (e) { e.preventDefault(); open(n); });
  });
  box.querySelector('.pv-close').addEventListener('click', close);
  prev.addEventListener('click', function () { step(-1); });
  next.addEventListener('click', function () { step(1); });
  box.addEventListener('click', function (e) { if (e.target === box) close(); });
  document.addEventListener('keydown', function (e) {
    if (box.hidden) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') step(-1);
    else if (e.key === 'ArrowRight') step(1);
  });
  var x0 = null;
  box.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
  box.addEventListener('touchend', function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) step(dx < 0 ? 1 : -1);
    x0 = null;
  });
})();
