(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.querySelector('.nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  var form = document.querySelector('form[data-contact]');
  if (form) {
    var compose = function () {
      var lines = [];
      form.querySelectorAll('[data-label]').forEach(function (el) {
        if (el.value.trim()) lines.push(el.getAttribute('data-label') + ': ' + el.value.trim());
      });
      return form.getAttribute('data-intro') + '\n\n' + lines.join('\n');
    };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var via = (e.submitter && e.submitter.value) || 'wa';
      var text = encodeURIComponent(compose());
      if (via === 'mail') {
        window.location.href = 'mailto:' + form.getAttribute('data-mail') + '?subject=' +
          encodeURIComponent(form.getAttribute('data-subject')) + '&body=' + text;
      } else {
        window.open('https://wa.me/' + form.getAttribute('data-wa') + '?text=' + text, '_blank', 'noopener');
      }
    });
  }
})();
