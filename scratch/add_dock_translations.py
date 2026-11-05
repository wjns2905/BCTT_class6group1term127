import re

path = 'C:/Users/camka/OneDrive/Desktop/BCTT_class6group1term127/js/translations.js'
with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# Add to vi
vi_dock = '''    dock_search: "Tìm kiếm",
    dock_menu: "Menu",
'''

# Add to en
en_dock = '''    dock_search: "Search",
    dock_menu: "Menu",
'''

if 'dock_search:' not in code:
    code = code.replace('breadcrumb_home: "Trang chủ",', 'breadcrumb_home: "Trang chủ",\n' + vi_dock, 1)
    code = code.replace('breadcrumb_home: "Home",', 'breadcrumb_home: "Home",\n' + en_dock, 1)
    print("Added dock translations")
else:
    print("Dock translations already exist")

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("translations.js updated successfully")
