import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find tabs / navigation on about.html
print("About.html search for tabs / nav:")
for line in html.splitlines():
    if 'Editorial Profiles' in line or 'Photojournalism' in line or 'Mission' in line or 'about-tab' in line or 'about_tab' in line:
        print(line)

print("\n" + "="*50 + "\nSections in about.html:")
sections = re.findall(r'<section[^>]+id=["\']([^"\']+)["\']', html)
print(sections)
