import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Check renderAboutUsSection tail
pos_start = js.find('function renderAboutUsSection()')
pos_end = js.find('/* ===================================================================\n   ARTICLE DETAIL MODAL', pos_start)

about_body = js[pos_start:pos_end]

# Enhance tab click / hash listener at the end of renderAboutUsSection
old_tail = """        <div style="padding-top:1.25rem; border-top:1px dashed var(--color-border-hairline); display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:0.75rem; font-size:0.875rem; color:var(--color-text-muted);">
          <span>
            <i class="fas fa-shield-alt" style="color:var(--color-brand-primary); margin-right:0.35rem;"></i>
            ${isEn ? 'Academic Multimedia Journalism Project • ULIS - VNU • Class 6 - Group 1 - Term 127' : 'Đề án Báo chí Đa phương tiện Học thuật • ULIS - VNU • Lớp 6 - Nhóm 1 - Khóa 127'}
          </span>
          <span>
            <i class="fas fa-check-circle" style="color:#2E7D32; margin-right:0.35rem;"></i>
            ${isEn ? 'Multi-Source Fact-Checking & Journalistic Ethics Compliance' : 'Kiểm chứng đa nguồn & Tuân thủ Chuẩn mực Đạo đức Báo chí'}
          </span>
        </div>
      </div>
    </section>
  `;
}"""

new_tail = """        <div style="padding-top:1.25rem; border-top:1px dashed var(--color-border-hairline); display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:0.75rem; font-size:0.875rem; color:var(--color-text-muted);">
          <span>
            <i class="fas fa-shield-alt" style="color:var(--color-brand-primary); margin-right:0.35rem;"></i>
            ${isEn ? 'Academic Multimedia Journalism Project • ULIS - VNU • Class 6 - Group 1 - Term 127' : 'Đề án Báo chí Đa phương tiện Học thuật • ULIS - VNU • Lớp 6 - Nhóm 1 - Khóa 127'}
          </span>
          <span>
            <i class="fas fa-check-circle" style="color:#2E7D32; margin-right:0.35rem;"></i>
            ${isEn ? 'Multi-Source Fact-Checking & Journalistic Ethics Compliance' : 'Kiểm chứng đa nguồn & Tuân thủ Chuẩn mực Đạo đức Báo chí'}
          </span>
        </div>
      </div>
    </section>
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

if old_tail in js:
    js = js.replace(old_tail, new_tail)
    with open(r'C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\js\app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Enhanced tab active listener added successfully!")
else:
    print("old_tail not matched directly")
