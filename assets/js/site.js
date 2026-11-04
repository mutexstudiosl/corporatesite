(function () {
  var GA_ID = 'G-R9QSEZ3HMM';
  var KEY = 'ms_cookie_consent';

  document.addEventListener('click', function (event) {
    if (event.target.closest('#mobile-menu-btn')) {
      var menu = document.getElementById('mobile-menu');
      if (menu) menu.classList.toggle('is-open');
    }
    var settings = event.target.closest('[data-cookie-settings]');
    if (settings) {
      event.preventDefault();
      showBanner();
    }
    var pp = event.target.closest('[data-paypal-load]');
    if (pp) {
      event.preventDefault();
      loadPayPal(pp);
    }
  });

  function getConsent() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function setConsent(value) {
    try { localStorage.setItem(KEY, value); } catch (e) {}
  }

  function loadAnalytics() {
    if (window.__gaLoaded) return;
    window.__gaLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_ID, { anonymize_ip: true });
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
  }

  function removeAnalyticsCookies() {
    var names = document.cookie.split(';').map(function (c) { return c.split('=')[0].trim(); });
    var host = location.hostname;
    var domains = [host, '.' + host, '.' + host.replace(/^www\./, '')];
    names.forEach(function (n) {
      if (n === '_ga' || n.indexOf('_ga_') === 0 || n === '_gid' || n.indexOf('_gat') === 0) {
        domains.forEach(function (d) {
          document.cookie = n + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; domain=' + d;
        });
        document.cookie = n + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
      }
    });
  }

  function loadPayPal(btn) {
    var holder = btn.parentNode;
    btn.disabled = true;
    btn.textContent = 'Loading PayPal…';
    var s = document.createElement('script');
    s.src = 'https://www.paypal.com/sdk/js?client-id=BAAWrTHlRByFj4h9ML7M7JASrE-JZIH0MYmMZeUEhREdtGr39JyShmv8cSKjnKyKBwaHtdLWuKUdUxxnBE&components=hosted-buttons&disable-funding=venmo&currency=EUR';
    s.onload = function () {
      btn.remove();
      window.paypal.HostedButtons({ hostedButtonId: 'L8PPM27WKB8SJ' }).render('#paypal-container-L8PPM27WKB8SJ');
    };
    s.onerror = function () {
      btn.disabled = false;
      btn.textContent = 'Could not load PayPal. Try again';
    };
    holder.appendChild(s);
  }

  function showBanner() {
    var old = document.querySelector('.cookie-banner');
    if (old) old.remove();
    var banner = document.createElement('div');
    banner.className = 'cookie-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Cookie preferences');
    banner.innerHTML =
      '<div class="cookie-banner-inner">' +
        '<p>We use Google Analytics cookies to understand how the site is used, only if you accept. ' +
        'Without your consent we set no analytics cookies. ' +
        '<a href="/cookies/">Cookie policy</a> · <a href="/privacy/">Privacy</a></p>' +
        '<div class="cookie-actions">' +
          '<button type="button" class="btn btn-secondary cookie-reject">Reject</button>' +
          '<button type="button" class="btn btn-secondary cookie-accept">Accept</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(banner);
    banner.querySelector('.cookie-accept').addEventListener('click', function () {
      setConsent('granted');
      loadAnalytics();
      banner.remove();
    });
    banner.querySelector('.cookie-reject').addEventListener('click', function () {
      setConsent('denied');
      removeAnalyticsCookies();
      banner.remove();
    });
  }

  var consent = getConsent();
  if (consent === 'granted') loadAnalytics();
  else if (consent !== 'denied') showBanner();
})();
