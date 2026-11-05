import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = """    </section>

      `;
}"""

replacement = """    </section>
  `;

  // Highlight active tab based on hash or default to #mission
  const currentHash = window.location.hash || '#mission';
  const tabs = container.querySelectorAll('.about-tab-btn');
  tabs.forEach(tab => {
    if (tab.getAttribute('href') === currentHash) {
      tab.classList.add('active');
    } else {
      tab.classList.remove('active');
    }
    tab.addEventListener('click', function() {
      tabs.forEach(t => t.classList.remove('active'));
      this.classList.add('active');
    });
  });
}"""

if target in js:
    js = js.replace(target, replacement)
    with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Added tab listener successfully!")
else:
    print("Target not found")
