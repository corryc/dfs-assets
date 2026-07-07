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
      bottom: 90px;
      right: 20px;
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
      z-index: 999;
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
    @media (max-width: 640px) {
      .dfs-whatsapp-fab {
        bottom: 80px;
        right: 16px;
        width: 48px;
        height: 48px;
      }

      .dfs-whatsapp-fab svg {
        width: 24px;
        height: 24px;
      }

      .dfs-whatsapp-tooltip {
        display: none;
      }
    }

    /* Hide on very small screens to avoid overlapping with nav */
    @media (max-width: 360px) {
      .dfs-whatsapp-fab {
        display: none;
      }
    }
  `;
  document.head.appendChild(styleSheet);

  // WhatsApp SVG Icon - Modern design
  const whatsappIcon = `
    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
      <path fill="white" d="M12 2C6.48 2 2 6.48 2 12c0 1.54.36 3 .97 4.3L2.5 22l6.3-1.29c1.26.6 2.64.98 4.2.98 5.52 0 10-4.48 10-10S17.52 2 12 2zm0 18c-1.41 0-2.73-.36-3.88-.99l-.28-.15-2.89.59.61-2.89-.15-.29C4.5 14.76 4 13.45 4 12c0-4.41 3.59-8 8-8s8 3.59 8 8-3.59 8-8 8zm4.64-12.67c-.15-.25-.46-.4-.92-.4-.25 0-.92.1-1.31.68-.32.51-.63 1.29-.63 2.65 0 1.44 1.01 3.05 1.15 3.3.03.05.1.15.26.27 1.27 1.27 3.02 1.85 4.73 1.85.37 0 .72-.02 1.05-.07 1.14-.18 1.72-1.43 1.9-2.26.1-.47.1-.77.1-.77s-.08-1.33-.5-1.92c-.33-.47-.75-.73-1.24-.73z"/>
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