/**
 * DFS Nav Loader v1.0
 * Fetches and injects the shared DFS nav and footer into any blog post page.
 * Hosted at: https://corryc.github.io/dfs-assets/dfs-nav-loader.js
 *
 * Usage — add this ONE line to any blog post Code Embed:
 * <script src="https://corryc.github.io/dfs-assets/dfs-nav-loader.js"></script>
 *
 * To update nav/footer across ALL posts: edit dfs-nav.html on GitHub. Done.
 */

(function() {
  fetch('https://corryc.github.io/dfs-assets/dfs-nav.html')
    .then(function(r) { return r.text(); })
    .then(function(html) {
      // Create a temp container to parse the HTML
      var temp = document.createElement('div');
      temp.innerHTML = html;

      // Inject nav at the very top of the body
      var nav = temp.querySelector('nav.nav');
      var navStyles = temp.querySelector('style');
      if (nav && document.body) {
        // Remove any existing nav
        var existing = document.querySelector('nav.nav');
        if (existing) {
          existing.remove();
        }
        // Add styles first
        if (navStyles) {
          var styleEl = document.createElement('style');
          styleEl.textContent = navStyles.textContent;
          document.head.appendChild(styleEl);
        }
        // Prepend nav
        document.body.insertBefore(nav, document.body.firstChild);
      }
    })
    .catch(function(e) {
      console.warn('DFS nav loader: could not load nav', e);
    });
})();
