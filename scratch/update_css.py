import os, sys

sys.stdout.reconfigure(encoding='utf-8')
css_path = r"c:\Users\camka\OneDrive\Desktop\BCTT\css\style.css"

with open(css_path, 'r', encoding='utf-8') as f:
    current_css = f.read()

# Add @import "tokens.css"; at the top if not present
if '@import "tokens.css";' not in current_css:
    current_css = '@import "tokens.css";\n\n' + current_css

# Additional Impeccable CSS enhancements
additional_css = """
/* ===================================================================
   IMPECCABLE CRAFT ENHANCEMENTS: TYPOGRAPHY, MOTION, ACCESSIBILITY
   =================================================================== */

/* Custom Text Selection */
::selection {
  background-color: var(--color-brand-primary);
  color: var(--color-text-inverse);
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 9px;
  height: 9px;
}
::-webkit-scrollbar-track {
  background: var(--color-canvas);
}
::-webkit-scrollbar-thumb {
  background: #C7BCA9;
  border-radius: var(--radius-full);
  border: 2px solid var(--color-canvas);
}
::-webkit-scrollbar-thumb:hover {
  background: var(--color-brand-primary);
}

/* Focus Visible Accessible Rings (No unstyled defaults) */
:focus-visible {
  outline: 2px solid var(--color-brand-primary);
  outline-offset: 3px;
  border-radius: var(--radius-sm);
}

/* Authentic Newspaper Drop Cap for Longform Reading */
.article-body-text > p:first-of-type::first-letter {
  float: left;
  font-family: var(--font-serif);
  font-size: 3.6rem;
  line-height: 0.82;
  padding-top: 4px;
  padding-right: 12px;
  padding-bottom: 2px;
  font-weight: 700;
  color: var(--color-brand-primary);
}

/* Pullquote Styling */
.article-pullquote {
  font-family: var(--font-serif);
  font-size: 1.35rem;
  font-style: italic;
  line-height: 1.5;
  color: var(--color-brand-dark);
  border-left: 3px solid var(--color-brand-primary);
  padding: 1rem 0 1rem 1.5rem;
  margin: 1.5rem 0;
  background-color: rgba(139, 30, 45, 0.03);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
}

/* Reading Progress Bar (Fixed Top) */
.reading-progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 0%;
  height: 3px;
  background: linear-gradient(90deg, var(--color-brand-primary), var(--color-status-live));
  z-index: 9999;
  transition: width 0.1s ease-out;
}

/* Ambient Heartbeat Canvas (60fps Non-blocking Hero Atmosphere) */
.ambient-canvas-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
  opacity: 0.45;
}
.ambient-canvas {
  width: 100%;
  height: 100%;
  display: block;
}

/* Offline Network Status Banner */
.offline-indicator-banner {
  display: none;
  background-color: #2D2723;
  color: #F8E7D8;
  text-align: center;
  padding: 0.45rem 1rem;
  font-size: 0.8125rem;
  font-weight: 600;
  border-bottom: 2px solid var(--color-status-accent);
  position: sticky;
  top: 0;
  z-index: 10000;
}
.offline-indicator-banner.active {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

/* Toast Notifications Container */
.toast-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 9000;
  display: flex;
  flex-direction: column;
  gap: 10px;
  pointer-events: none;
}
.toast-message {
  pointer-events: auto;
  background-color: #1A1715;
  color: #FDFBF8;
  padding: 0.75rem 1.25rem;
  border-radius: var(--radius-sm);
  border-left: 4px solid var(--color-brand-primary);
  box-shadow: var(--shadow-lg);
  font-size: 0.875rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  animation: toast-slide-up 0.28s var(--ease-spring);
  max-width: 380px;
}
@keyframes toast-slide-up {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

/* Like Button Heart Micro-interaction */
.btn-article-like {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 0.85rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-full);
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--color-text-body);
  transition: all var(--duration-fast);
}
.btn-article-like:hover {
  border-color: var(--color-brand-primary);
  color: var(--color-brand-primary);
  transform: scale(1.05);
}
.btn-article-like.liked {
  background: var(--primitive-burgundy-100);
  border-color: var(--color-brand-primary);
  color: var(--color-brand-primary);
}
.btn-article-like.liked i {
  animation: heart-burst 0.35s var(--ease-spring);
  color: var(--color-brand-primary);
}
@keyframes heart-burst {
  0% { transform: scale(1); }
  50% { transform: scale(1.4); }
  100% { transform: scale(1); }
}

/* Onboarding Welcome Modal */
.onboard-modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(18, 14, 12, 0.75);
  backdrop-filter: blur(6px);
  z-index: 5000;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}
.onboard-modal-backdrop.active {
  display: flex;
}
.onboard-card {
  background: var(--color-canvas);
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  max-width: 580px;
  width: 100%;
  padding: 2.25rem;
  box-shadow: var(--shadow-modal);
  position: relative;
  text-align: center;
}
.onboard-badge {
  font-size: 0.75rem;
  font-weight: 800;
  text-transform: uppercase;
  color: var(--color-brand-primary);
  letter-spacing: 0.08em;
  margin-bottom: 0.5rem;
}
.onboard-title {
  font-family: var(--font-serif);
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--color-brand-dark);
  margin-bottom: 0.75rem;
}
.onboard-desc {
  font-size: 0.9375rem;
  color: var(--color-text-body);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}
.onboard-steps-progress {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-bottom: 1.5rem;
}
.onboard-step-dot {
  width: 24px;
  height: 4px;
  border-radius: 2px;
  background: #D8CFBF;
  transition: background var(--duration-fast);
}
.onboard-step-dot.active {
  background: var(--color-brand-primary);
  width: 36px;
}
.onboard-feature-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  text-align: left;
  margin-bottom: 1.75rem;
}
.onboard-feature-item {
  background: var(--color-surface);
  border: 1px solid var(--color-border-subtle);
  border-radius: var(--radius-sm);
  padding: 0.85rem;
}
.onboard-feature-item h4 {
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--color-text-headline);
  margin-bottom: 0.2rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.onboard-feature-item p {
  font-size: 0.75rem;
  color: var(--color-text-muted);
  line-height: 1.4;
}
.onboard-action-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.btn-onboard-next {
  background: var(--color-brand-primary);
  color: white;
  font-weight: 600;
  padding: 0.55rem 1.5rem;
  border-radius: var(--radius-sm);
  font-size: 0.875rem;
}
.btn-onboard-next:hover {
  background: var(--color-brand-hover);
}

/* Empty State Cards */
.empty-state-card {
  text-align: center;
  padding: 3rem 1.5rem;
  color: var(--color-text-muted);
}
.empty-state-icon {
  font-size: 2.5rem;
  color: var(--color-brand-primary);
  margin-bottom: 1rem;
  opacity: 0.7;
}
.empty-state-title {
  font-family: var(--font-serif);
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--color-text-headline);
  margin-bottom: 0.4rem;
}
.empty-state-text {
  font-size: 0.875rem;
  max-width: 420px;
  margin: 0 auto 1.25rem auto;
  line-height: 1.5;
}
.empty-tag-list {
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.empty-tag-pill {
  padding: 0.3rem 0.75rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--color-text-body);
  cursor: pointer;
}
.empty-tag-pill:hover {
  border-color: var(--color-brand-primary);
  color: var(--color-brand-primary);
}

/* Mobile Bottom Navigation Dock (< 768px) */
.mobile-bottom-dock {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 56px;
  background: rgba(250, 247, 242, 0.95);
  backdrop-filter: blur(10px);
  border-top: 1px solid var(--color-border-hairline);
  z-index: 1000;
  justify-content: space-around;
  align-items: center;
}
@media (max-width: 768px) {
  .mobile-bottom-dock {
    display: flex;
  }
  body {
    padding-bottom: 60px;
  }
}
.mobile-dock-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  color: var(--color-text-muted);
  font-size: 0.6875rem;
  font-weight: 600;
  min-width: 48px;
  min-height: 48px;
}
.mobile-dock-btn i {
  font-size: 1.15rem;
}
.mobile-dock-btn.active, .mobile-dock-btn:hover {
  color: var(--color-brand-primary);
}

/* Keyboard Shortcuts Dialog */
.shortcuts-modal {
  position: fixed;
  inset: 0;
  background: rgba(18, 14, 12, 0.75);
  backdrop-filter: blur(4px);
  z-index: 6000;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}
.shortcuts-modal.active {
  display: flex;
}
.shortcuts-card {
  background: var(--color-surface);
  border-radius: var(--radius-md);
  max-width: 480px;
  width: 100%;
  padding: 1.75rem;
  box-shadow: var(--shadow-modal);
  border: 1px solid var(--color-border-hairline);
}
.shortcut-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.6rem 0;
  border-bottom: 1px solid var(--color-border-subtle);
  font-size: 0.875rem;
}
.shortcut-row:last-child {
  border-bottom: none;
}
.shortcut-key {
  display: inline-block;
  padding: 0.2rem 0.5rem;
  background: var(--color-canvas);
  border: 1px solid var(--color-border-hairline);
  border-radius: 4px;
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  box-shadow: 0 1px 1px rgba(0,0,0,0.08);
}
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(current_css + '\n' + additional_css)

print("css/style.css updated successfully with Impeccable enhancements.")
