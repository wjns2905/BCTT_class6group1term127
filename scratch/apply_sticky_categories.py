# -*- coding: utf-8 -*-
"""
Script to apply persistent sticky categories navigation bar across all device breakpoints.
Ensures:
1. `html, body` uses `overflow-x: clip;` instead of `overflow-x: hidden !important;`, fixing sticky positioning.
2. `.fashion-header` has persistent sticky position `position: -webkit-sticky !important; position: sticky !important; top: 0 !important; z-index: 1000 !important;`.
3. Elevation on scroll `.fashion-header.is-scrolled`.
4. On <= 991px and <= 768px, `.fashion-nav` is NEVER hidden; it displays as a smooth horizontal-scrolling category strip.
5. In `js/app.js`, `setupStickyHeader()` is initialized.
"""

import os
import re

BASE_DIR = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127"
CSS_PATH = os.path.join(BASE_DIR, "css", "style.css")
JS_PATH = os.path.join(BASE_DIR, "js", "app.js")

# --- 1. UPDATE CSS ---
with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

# Fix 1: html, body overflow-x: hidden -> overflow-x: clip
target_overflow = """html, body {
  overflow-x: hidden !important;
  max-width: 100vw;
  -webkit-text-size-adjust: 100%;
}"""

replacement_overflow = """html {
  overflow-x: clip !important;
  max-width: 100% !important;
  -webkit-text-size-adjust: 100%;
}

body {
  overflow-x: clip !important;
  max-width: 100% !important;
  -webkit-text-size-adjust: 100%;
  position: relative;
}"""

if target_overflow in css:
    css = css.replace(target_overflow, replacement_overflow)
    print("SUCCESS: Replaced global overflow-x: hidden with overflow-x: clip on html and body.")
else:
    print("WARNING: target_overflow not found verbatim. Looking with regex...")
    css = re.sub(
        r"html,\s*body\s*\{\s*overflow-x:\s*hidden\s*!important;\s*max-width:\s*100vw;\s*-webkit-text-size-adjust:\s*100%;\s*\}",
        replacement_overflow,
        css
    )
    print("SUCCESS (via regex): Replaced global overflow-x.")

# Fix 2: Reinforce .fashion-header base sticky definition
target_header_base = """.fashion-header {
  background: #FFFFFF;
  border-bottom: 1px solid var(--color-border-hairline);
  position: sticky;
  top: 0;
  z-index: 900;
  backdrop-filter: blur(8px);
}"""

replacement_header_base = """.fashion-header {
  background: #FFFFFF !important;
  border-bottom: 1px solid var(--color-border-hairline);
  position: -webkit-sticky !important;
  position: sticky !important;
  top: 0 !important;
  z-index: 1000 !important;
  backdrop-filter: blur(8px);
  transition: box-shadow 0.25s ease, border-color 0.25s ease;
}

.fashion-header.is-scrolled {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
  border-bottom-color: rgba(84, 17, 30, 0.12) !important;
}

/* On desktop, reveal compact brand mark when scrolled down past large masthead */
@media (min-width: 992px) {
  .fashion-mobile-brand {
    display: none;
    transition: opacity 0.2s ease;
  }
  .fashion-header.is-scrolled .fashion-mobile-brand {
    display: inline-flex !important;
    font-size: 1.35rem !important;
    font-weight: 900 !important;
    letter-spacing: -0.03em !important;
    margin-right: 1.5rem !important;
    color: var(--color-brand-primary, #54111E) !important;
  }
}"""

if target_header_base in css:
    css = css.replace(target_header_base, replacement_header_base)
    print("SUCCESS: Reinforced .fashion-header base stickiness and scroll elevation.")
else:
    print("WARNING: target_header_base not found verbatim, checking regex...")
    css = re.sub(
        r"\.fashion-header\s*\{\s*background:\s*#FFFFFF;\s*border-bottom:\s*1px solid var\(--color-border-hairline\);\s*position:\s*sticky;\s*top:\s*0;\s*z-index:\s*900;\s*backdrop-filter:\s*blur\(8px\);\s*\}",
        replacement_header_base,
        css
    )
    print("SUCCESS (via regex): Reinforced .fashion-header.")

# Fix 3: Remove legacy 768px .fashion-nav { display: none; }
target_legacy_768 = """@media (max-width: 768px) {
  .fashion-nav {
    display: none;
  }
  .fashion-hamburger-btn {"""

replacement_legacy_768 = """@media (max-width: 768px) {
  .fashion-hamburger-btn {"""

if target_legacy_768 in css:
    css = css.replace(target_legacy_768, replacement_legacy_768)
    print("SUCCESS: Removed legacy 768px .fashion-nav display:none.")
else:
    print("NOTE: target_legacy_768 was already updated or not present.")

# Fix 4: Update 991px tablet navigation: categories must be ALWAYS visible and sticky
target_991 = """@media (max-width: 991px) {
  /* Header navigation collapses to drawer */
  .fashion-nav {
    display: none !important;
  }
  .fashion-hamburger-btn {
    display: inline-flex !important;
    align-items: center;
    justify-content: center;
  }
  .fashion-mobile-brand {
    display: flex !important;
  }"""

replacement_991 = """@media (max-width: 991px) {
  /* Sticky Categories Header: 2-row layout with touch horizontal scrolling categories */
  .fashion-header-container {
    height: auto !important;
    display: flex !important;
    flex-wrap: wrap !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding-top: 0.35rem !important;
    padding-bottom: 0.25rem !important;
  }
  .fashion-mobile-brand {
    display: flex !important;
    order: 1 !important;
    font-size: 1.25rem !important;
    font-weight: 900 !important;
    letter-spacing: -0.03em !important;
  }
  .fashion-header-actions {
    display: flex !important;
    order: 2 !important;
    align-items: center !important;
    gap: 0.45rem !important;
  }
  .fashion-nav {
    display: flex !important;
    order: 3 !important;
    width: 100% !important;
    overflow-x: auto !important;
    white-space: nowrap !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: none !important;
    -ms-overflow-style: none !important;
    border-top: 1px solid rgba(84, 17, 30, 0.08) !important;
    padding: 0.4rem 0.2rem 0.35rem !important;
    margin-top: 0.3rem !important;
    gap: 1.25rem !important;
  }
  .fashion-nav::-webkit-scrollbar {
    display: none !important;
  }
  .fashion-nav .nav-item {
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    padding: 0.2rem 0.25rem !important;
    flex-shrink: 0 !important;
    white-space: nowrap !important;
    color: var(--color-text-headline) !important;
  }
  .fashion-nav .nav-item.active {
    color: var(--color-brand-primary) !important;
    font-weight: 700 !important;
  }
  .fashion-hamburger-btn {
    display: inline-flex !important;
    align-items: center;
    justify-content: center;
  }"""

if target_991 in css:
    css = css.replace(target_991, replacement_991)
    print("SUCCESS: Updated 991px responsive rules for sticky categories bar.")
else:
    print("WARNING: target_991 not found verbatim, checking regex...")
    css = re.sub(
        r"@media \(max-width: 991px\) \{\s*/\* Header navigation collapses to drawer \*/\s*\.fashion-nav \{\s*display: none !important;\s*\}\s*\.fashion-hamburger-btn \{\s*display: inline-flex !important;\s*align-items: center;\s*justify-content: center;\s*\}\s*\.fashion-mobile-brand \{\s*display: flex !important;\s*\}",
        replacement_991,
        css
    )
    print("SUCCESS (via regex): Updated 991px rules.")

# Fix 5: Ensure 768px does not constrain container height to 50px
target_768_height = """  /* Sticky header on mobile */
  .fashion-header-container {
    height: 50px !important;
  }"""

replacement_768_height = """  /* Sticky header on mobile (auto height to accommodate categories strip) */
  .fashion-header-container {
    height: auto !important;
    min-height: 48px !important;
  }"""

if target_768_height in css:
    css = css.replace(target_768_height, replacement_768_height)
    print("SUCCESS: Updated 768px header height.")
else:
    print("NOTE: target_768_height was already updated or not present.")

with open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(css)
print("Finished updating css/style.css.")


# --- 2. UPDATE JS/APP.JS ---
with open(JS_PATH, "r", encoding="utf-8") as f:
    js = f.read()

# Add setupStickyHeader function if not present
if "function setupStickyHeader()" not in js:
    sticky_header_func = """
/* ===================================================================
   STICKY HEADER SCROLL ELEVATION LISTENER
   =================================================================== */
function setupStickyHeader() {
  const header = document.querySelector('.fashion-header');
  if (!header) return;
  const onScroll = () => {
    if (window.scrollY > 15) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}
"""
    # Append right before setupReadingProgressBar
    if "function setupReadingProgressBar()" in js:
        js = js.replace("function setupReadingProgressBar()", sticky_header_func + "\nfunction setupReadingProgressBar()")
    else:
        js += "\n" + sticky_header_func

    # Call inside initApp
    if "setupStickyHeader();" not in js:
        js = js.replace("setupReadingProgressBar();", "setupStickyHeader();\n  setupReadingProgressBar();")

    with open(JS_PATH, "w", encoding="utf-8") as f:
        f.write(js)
    print("SUCCESS: Added setupStickyHeader() to js/app.js.")
else:
    print("NOTE: setupStickyHeader() already present in js/app.js.")
