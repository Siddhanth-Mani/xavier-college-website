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
