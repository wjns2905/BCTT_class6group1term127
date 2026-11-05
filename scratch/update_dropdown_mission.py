import glob, os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

root = r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127'

old_dropdown_pattern = re.compile(
    r'<div class="about-dropdown-menu">\s*'
    r'<a href="about\.html#profiles"[^>]*>.*?</a>\s*'
    r'<a href="about\.html#photo"[^>]*>.*?</a>\s*'
    r'<a href="about\.html#subscribe"[^>]*>.*?</a>\s*'
    r'<a href="about\.html#mission"[^>]*>.*?</a>\s*'
    r'</div>',
    re.DOTALL
)

new_dropdown = """<div class="about-dropdown-menu">
            <a href="about.html#mission" class="about-dropdown-item"><i class="fas fa-bullseye"></i> <span data-i18n="about_opt_mission">Mission</span></a>
            <a href="about.html#profiles" class="about-dropdown-item"><i class="fas fa-users"></i> <span data-i18n="about_opt_profiles">Profiles</span></a>
            <a href="about.html#photo" class="about-dropdown-item"><i class="fas fa-camera"></i> <span data-i18n="about_opt_photo">Photo</span></a>
            <a href="about.html#subscribe" class="about-dropdown-item"><i class="fas fa-paper-plane"></i> <span data-i18n="about_opt_subscribe">Subscribe</span></a>
          </div>"""

for fpath in glob.glob(os.path.join(root, '*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if old_dropdown_pattern.search(html):
        new_html = old_dropdown_pattern.sub(new_dropdown, html)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Updated dropdown in:", os.path.basename(fpath))
    else:
        print("Pattern not matched in:", os.path.basename(fpath))
