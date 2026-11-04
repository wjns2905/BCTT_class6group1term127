target = r"C:\Users\camka\OneDrive\Desktop\BCTT_class6group1term127\css\style.css"

profile_css = """
/* ===================================================================
   AUTHENTIC EDITORIAL PROFILES (FROM [BCTT] PROFILES.DOCX)
   =================================================================== */
.profiles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}
.profile-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline, rgba(84, 17, 30, 0.12));
  border-radius: var(--radius-lg, 12px);
  padding: 1.75rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
  transition: transform var(--duration-fast, 0.2s), box-shadow var(--duration-fast, 0.2s);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.profile-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(84, 17, 30, 0.12);
  border-color: rgba(84, 17, 30, 0.25);
}
.profile-header-wrap {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 0.85rem;
}
.profile-avatar-circle {
  width: 58px;
  height: 58px;
  border-radius: 50%;
  background: linear-gradient(135deg, #54111E 0%, #7D1728 100%);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-editorial, 'Plus Jakarta Sans');
  font-weight: 800;
  font-size: 1.25rem;
  letter-spacing: 0.02em;
  box-shadow: 0 4px 12px rgba(84, 17, 30, 0.25);
  flex-shrink: 0;
}
.profile-name-text {
  font-family: var(--font-editorial, 'Plus Jakarta Sans');
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--color-text-headline, #141011);
  margin: 0 0 0.25rem 0;
  line-height: 1.3;
}
.profile-title-pill {
  display: inline-block;
  background: var(--color-surface-blush, #FBF3F4);
  color: var(--color-brand-primary, #54111E);
  font-size: 0.725rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 0.2rem 0.65rem;
  border-radius: var(--radius-full, 9999px);
  border: 1px solid rgba(84, 17, 30, 0.12);
}
.profile-role-desc {
  font-size: 0.875rem;
  color: var(--color-text-body, #4A4036);
  line-height: 1.65;
  margin: 0.5rem 0 1.25rem 0;
  flex-grow: 1;
}
.profile-email-link {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  font-size: 0.8125rem;
  font-weight: 700;
  color: var(--color-brand-primary, #54111E);
  text-decoration: none;
  background: var(--color-surface-blush, #FBF3F4);
  padding: 0.4rem 0.85rem;
  border-radius: var(--radius-full, 9999px);
  border: 1px solid rgba(84, 17, 30, 0.1);
  transition: all var(--duration-fast, 0.2s);
  width: fit-content;
}
.profile-email-link:hover {
  background: var(--color-brand-primary, #54111E);
  color: #FFFFFF;
  box-shadow: 0 2px 8px rgba(84, 17, 30, 0.2);
}
"""

with open(target, 'r', encoding='utf-8') as f:
    cur = f.read()

if '.profiles-grid' not in cur:
    cur += '\n' + profile_css
    with open(target, 'w', encoding='utf-8') as f:
        f.write(cur)
    print("SUCCESS: Appended profile_css to style.css!")
else:
    print("profile_css already present in style.css.")
