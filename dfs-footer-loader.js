/**
 * DFS Footer Loader v1.0
 * Fetches and injects the shared DFS footer into any page.
 * Hosted at: https://corryc.github.io/dfs-assets/dfs-footer-loader.js
 *
 * Usage — add this ONE line to any page before closing </body>:
 * <script src="https://corryc.github.io/dfs-assets/dfs-footer-loader.js"></script>
 *
 * To update footer across ALL pages: edit dfs-footer.html on GitHub. Done.
 */

(function() {
  fetch('https://corryc.github.io/dfs-assets/dfs-footer.html')
    .then(function(r) { return r.text(); })
    .then(function(html) {
      // Create a temp container to parse the HTML
      var temp = document.createElement('div');
      temp.innerHTML = html;

      // Extract footer and styles
      var footer = temp.querySelector('footer.footer');
      var styles = temp.querySelector('style');

      if (footer && document.body) {
        // Remove any existing footer
        var existing = document.querySelector('footer.footer');
        if (existing) {
          existing.remove();
        }

        // Add styles
        if (styles) {
          var styleEl = document.createElement('style');
          styleEl.textContent = styles.textContent;
          document.head.appendChild(styleEl);
        }

        // Append footer at end of body
        document.body.appendChild(footer);

        // Load WhatsApp button after footer is injected
        var whatsappScript = document.createElement('script');
        whatsappScript.src = 'https://corryc.github.io/dfs-assets/dfs-whatsapp-loader.js';
        whatsappScript.async = true;
        document.body.appendChild(whatsappScript);
      }
    })
    .catch(function(e) {
      console.warn('DFS footer loader: could not load footer', e);
    });
})();