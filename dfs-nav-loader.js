/**
 * DFS Nav Loader v1.1
 * Fetches and injects the shared DFS nav (including mobile hamburger panel)
 * into any page.
 * Hosted at: https://corryc.github.io/dfs-assets/dfs-nav-loader.js
 *
 * Usage — add this ONE line to any page:
 * <script src="https://corryc.github.io/dfs-assets/dfs-nav-loader.js"></script>
 *
 * To update nav across ALL pages: edit dfs-nav.html on GitHub. Done.
 *
 * v1.1 fix (2026-07-09): v1.0 only injected the <nav> element itself,
 * never the sibling .mobile-nav hamburger panel, and never re-executed
 * the toggle <script> (scripts inserted via innerHTML do not run
 * automatically). Result: hamburger button appeared but did nothing.
 * v1.1 injects the mobile-nav panel and re-creates+appends the script
 * so it actually executes.
 */

(function() {
  fetch('https://corryc.github.io/dfs-assets/dfs-nav.html')
    .then(function(r) { return r.text(); })
    .then(function(html) {
      // Create a temp container to parse the HTML
      var temp = document.createElement('div');
      temp.innerHTML = html;

      var nav = temp.querySelector('nav.nav');
      var navStyles = temp.querySelector('style');
      var mobileNav = temp.querySelector('.mobile-nav');
      var scripts = temp.querySelectorAll('script');

      if (nav && document.body) {
        // Remove any existing nav / mobile panel already on the page
        var existingNav = document.querySelector('nav.nav');
        if (existingNav) existingNav.remove();
        var existingMobileNav = document.querySelector('.mobile-nav');
        if (existingMobileNav) existingMobileNav.remove();

        // Add styles first
        if (navStyles) {
          var styleEl = document.createElement('style');
          styleEl.textContent = navStyles.textContent;
          document.head.appendChild(styleEl);
        }

        // Prepend nav
        document.body.insertBefore(nav, document.body.firstChild);

        // Insert the mobile hamburger panel right after the nav
        if (mobileNav) {
          nav.insertAdjacentElement('afterend', mobileNav);
        }

        // Re-create and append any <script> tags so they actually execute
        // (scripts set via innerHTML are inert — this is required for the
        // hamburger open/close toggle to work)
        scripts.forEach(function(oldScript) {
          var newScript = document.createElement('script');
          if (oldScript.src) {
            newScript.src = oldScript.src;
          } else {
            newScript.textContent = oldScript.textContent;
          }
          document.body.appendChild(newScript);
        });
      }
    })
    .catch(function(e) {
      console.warn('DFS nav loader: could not load nav', e);
    });
})();
