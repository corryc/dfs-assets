// DFS WhatsApp Click-to-Chat Loader
// Injects a floating WhatsApp button in bottom-right corner of pages
// Usage: <script src="https://corryc.github.io/dfs-assets/dfs-whatsapp-loader.js"></script>

(function() {
  'use strict';

  // Inject styles
  const styleSheet = document.createElement('style');
  styleSheet.textContent = `
    .dfs-whatsapp-fab {
      position: fixed;
      bottom: 100px;
      right: 16px;
      width: 56px;
      height: 56px;
      background-color: #25d366;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(37, 211, 102, 0.4);
      transition: all 0.3s ease;
      z-index: 9999;
      text-decoration: none;
      border: none;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    }

    .dfs-whatsapp-fab:hover {
      background-color: #20ba58;
      box-shadow: 0 6px 16px rgba(37, 211, 102, 0.5);
      transform: scale(1.1);
    }

    .dfs-whatsapp-fab:active {
      transform: scale(0.95);
    }

    .dfs-whatsapp-fab svg {
      width: 28px;
      height: 28px;
      fill: white;
    }

    .dfs-whatsapp-tooltip {
      position: absolute;
      bottom: 70px;
      right: 0;
      background-color: #0d1b2e;
      color: white;
      padding: 8px 12px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 500;
      white-space: nowrap;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }

    .dfs-whatsapp-fab:hover .dfs-whatsapp-tooltip {
      opacity: 1;
    }

    /* Mobile responsiveness */
    @media (max-width: 768px) {
      .dfs-whatsapp-fab {
        bottom: 80px;
        right: 12px;
        width: 52px;
        height: 52px;
      }

      .dfs-whatsapp-fab svg {
        width: 26px;
        height: 26px;
      }

      .dfs-whatsapp-tooltip {
        display: none;
      }
    }

    /* Very small screens only */
    @media (max-width: 320px) {
      .dfs-whatsapp-fab {
        display: none;
      }
    }
  `;
  document.head.appendChild(styleSheet);

  // WhatsApp SVG Icon
  const whatsappIcon = `
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
      <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.076 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421-7.403h-.004a9.87 9.87 0 00-5.031 1.378c-3.055 2.309-3.645 6.71-1.331 9.527.442.571.371 1.571-.823 3.102-1.088 1.454.266 2.89 1.875 3.2 1.604.301 3.225.292 5.205.6h.004c5.522 0 10-4.477 10-10s-4.478-10-10-10z"/>
    </svg>
  `;

  // Create button element
  const button = document.createElement('a');
  button.className = 'dfs-whatsapp-fab';
  button.href = 'https://wa.me/610419891983?text=Hi, I\'d like to get quick mortgage advice about my mortgage options. Can we chat?';
  button.target = '_blank';
  button.rel = 'noopener noreferrer';
  button.setAttribute('aria-label', 'Chat on WhatsApp');
  button.innerHTML = whatsappIcon + '<div class="dfs-whatsapp-tooltip">Chat on WhatsApp</div>';

  // Insert button at end of body
  if (document.body) {
    document.body.appendChild(button);
  } else {
    document.addEventListener('DOMContentLoaded', function() {
      document.body.appendChild(button);
    });
  }
})();