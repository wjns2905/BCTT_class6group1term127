import sys
sys.stdout.reconfigure(encoding='utf-8')

css_path = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add styles for social-pill-btn if not present
social_css = """
/* ===================================================================
   SLEEK SOCIAL PILL BUTTONS (FOOTER & DRAWER)
   =================================================================== */
.social-pill-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.38rem 0.95rem;
  border-radius: 9999px;
  font-size: 0.8125rem;
  font-weight: 700;
  text-decoration: none;
  background: #F8F5F2;
  color: #54111E;
  border: 1px solid rgba(84, 17, 30, 0.18);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

.social-pill-btn:hover {
  background: #54111E;
  color: #FFFFFF !important;
  border-color: #54111E;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(84, 17, 30, 0.25);
}

.social-pill-btn.fb:hover {
  background: #1877F2;
  border-color: #1877F2;
  box-shadow: 0 4px 12px rgba(24, 119, 242, 0.35);
}

.social-pill-btn.ig:hover {
  background: radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%, #d6249f 60%, #285AEB 90%);
  border-color: #d6249f;
  box-shadow: 0 4px 12px rgba(214, 36, 159, 0.35);
}

.social-pill-btn.tw:hover {
  background: #000000;
  border-color: #000000;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
}

.social-pill-btn i {
  font-size: 0.95rem;
}

.drawer-social-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.08);
  color: #FFFFFF;
  text-decoration: none;
  font-size: 1.1rem;
  transition: all 0.2s ease;
  border: 1px solid rgba(255, 255, 255, 0.15);
}

.drawer-social-link:hover {
  background: #54111E;
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
}
"""

if ".social-pill-btn" not in css:
    css += social_css
    print("Added social pill CSS")

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css successfully!")
