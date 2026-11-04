nhandan_css = """
/* ===================================================================
   BÁO NHÂN DÂN ĐIỆN TỬ (NHANDAN.VN) ASYMMETRIC LAYOUT SUITE
   Anti-Repetitive, Dynamic Modular Editorial Architecture
   =================================================================== */

/* 1. Top Focal Cluster (3 Columns: 50% Lead | 26% Sub-Lead | 24% Timeline) */
.nhandan-top-cluster {
  display: grid;
  grid-template-columns: 1.9fr 1.15fr 0.95fr;
  gap: 1.5rem;
  margin-top: 1.75rem;
  margin-bottom: 3rem;
  align-items: stretch;
}

/* Col 1: Lead Hero Card */
.focal-lead-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  box-shadow: var(--shadow-sm);
  transition: transform var(--duration-normal) var(--ease-spring), box-shadow var(--duration-normal) var(--ease-spring);
}
.focal-lead-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}
.lead-media-wrap {
  position: relative;
  border-radius: var(--radius-md);
  overflow: hidden;
  height: 280px;
  margin-bottom: 1.25rem;
}
.lead-hero-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s var(--ease-spring);
}
.focal-lead-card:hover .lead-hero-img {
  transform: scale(1.03);
}
.nhandan-flag-badge {
  position: absolute;
  top: 1rem;
  left: 1rem;
  background: var(--color-brand-primary);
  color: #FFFFFF;
  font-family: var(--font-sans);
  font-size: 0.725rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-full);
  box-shadow: 0 2px 8px rgba(84, 17, 30, 0.3);
}
.lead-card-body {
  margin-bottom: 1.25rem;
}
.lead-main-headline {
  font-family: var(--font-editorial);
  font-size: 1.85rem;
  font-weight: 800;
  line-height: 1.25;
  color: var(--color-text-headline);
  margin-bottom: 0.75rem;
}
.lead-sapo-text {
  font-family: var(--font-serif);
  font-size: 1.05rem;
  line-height: 1.6;
  color: var(--color-text-body);
  margin-bottom: 1rem;
}
.lead-meta-row {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  font-weight: 600;
}
.lead-author-tag {
  color: var(--color-brand-primary);
}
.lead-related-strip {
  border-top: 1px solid var(--color-border-hairline);
  padding-top: 1rem;
  margin-top: auto;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.related-news-item {
  display: flex;
  align-items: baseline;
  gap: 0.65rem;
  cursor: pointer;
}
.bullet-red-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background-color: var(--color-brand-primary);
  flex-shrink: 0;
}
.related-news-title {
  font-size: 0.925rem;
  font-weight: 600;
  line-height: 1.45;
  color: var(--color-text-headline);
  transition: color var(--duration-fast);
}
.related-news-item:hover .related-news-title {
  color: var(--color-brand-primary);
  text-decoration: underline;
}

/* Col 2: Sub-Lead Stories */
.focal-sublead-col {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.sublead-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  padding: 1.25rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  box-shadow: var(--shadow-sm);
  transition: transform var(--duration-normal) var(--ease-spring), box-shadow var(--duration-normal) var(--ease-spring);
}
.sublead-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}
.sublead-thumb-wrap {
  height: 145px;
  border-radius: var(--radius-md);
  overflow: hidden;
  position: relative;
  margin-bottom: 0.85rem;
}
.sublead-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.sublead-cat-tag {
  position: absolute;
  top: 0.5rem;
  left: 0.5rem;
  background: rgba(84, 17, 30, 0.88);
  color: #FFFFFF;
  font-size: 0.65rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  padding: 0.2rem 0.55rem;
  border-radius: 3px;
}
.sublead-body {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.sublead-title {
  font-family: var(--font-serif);
  font-size: 1.05rem;
  font-weight: 700;
  line-height: 1.35;
  color: var(--color-text-headline);
  margin-bottom: 0.4rem;
}
.sublead-excerpt {
  font-size: 0.85rem;
  color: var(--color-text-body);
  line-height: 1.5;
  margin-bottom: 0.75rem;
  flex-grow: 1;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.sublead-meta {
  font-size: 0.775rem;
  color: var(--color-text-muted);
  font-weight: 600;
}

/* Col 3: Dòng Thời Sự 24/7 (Timeline Live Feed) */
.focal-timeline-col {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  padding: 1.25rem 1.25rem 1rem 1.25rem;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
}
.timeline-widget-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 2px solid var(--color-brand-primary);
  padding-bottom: 0.75rem;
  margin-bottom: 1rem;
}
.timeline-title-wrap {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.pulse-live-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #D92338;
  box-shadow: 0 0 0 3px rgba(217, 35, 56, 0.25);
  animation: pulse-ring 2s infinite;
}
@keyframes pulse-ring {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(217, 35, 56, 0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(217, 35, 56, 0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(217, 35, 56, 0); }
}
.timeline-widget-title {
  font-family: var(--font-sans);
  font-size: 0.925rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  color: var(--color-brand-primary);
}
.timeline-date-label {
  font-size: 0.75rem;
  color: var(--color-text-muted);
  font-weight: 600;
}
.timeline-items-list {
  display: flex;
  flex-direction: column;
  gap: 0.9rem;
  flex-grow: 1;
}
.timeline-item {
  position: relative;
  padding-left: 0.75rem;
  border-left: 2px solid var(--color-border-hairline);
  cursor: pointer;
  transition: all var(--duration-fast);
}
.timeline-item:hover {
  border-left-color: var(--color-brand-primary);
  transform: translateX(2px);
}
.timeline-stamp {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.25rem;
}
.timeline-time {
  font-variant-numeric: tabular-nums;
  font-size: 0.75rem;
  font-weight: 800;
  color: var(--color-brand-primary);
}
.timeline-badge-cat {
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--color-text-muted);
  text-transform: uppercase;
  background: var(--color-canvas);
  padding: 0.1rem 0.4rem;
  border-radius: 3px;
}
.timeline-headline {
  font-size: 0.85rem;
  font-weight: 600;
  line-height: 1.35;
  color: var(--color-text-headline);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  transition: color var(--duration-fast);
}
.timeline-item:hover .timeline-headline {
  color: var(--color-brand-primary);
}
.timeline-widget-footer {
  border-top: 1px solid var(--color-border-hairline);
  padding-top: 0.75rem;
  margin-top: 0.75rem;
  text-align: center;
}
.timeline-view-all {
  font-size: 0.8125rem;
  font-weight: 700;
  color: var(--color-brand-primary);
  text-decoration: none;
}
.timeline-view-all:hover {
  text-decoration: underline;
}

/* 2. MEGASTORY / E-MAGAZINE BÁO NHÂN DÂN SHOWCASE */
.nhandan-megastory-section {
  margin-bottom: 3.5rem;
}
.megastory-inner-card {
  background: linear-gradient(135deg, #240A10 0%, #15060A 100%);
  border: 1px solid #4D1420;
  border-radius: var(--radius-lg);
  overflow: hidden;
  display: grid;
  grid-template-columns: 1.1fr 1.3fr;
  box-shadow: var(--shadow-lg);
  cursor: pointer;
  position: relative;
}
.megastory-content-col {
  padding: 3rem 2.5rem;
  color: #FFFFFF;
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: relative;
  z-index: 2;
}
.megastory-badge-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}
.megastory-pill-gold {
  background: #B38634;
  color: #18090C;
  font-weight: 800;
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-full);
}
.megastory-serial-no {
  font-size: 0.75rem;
  color: #E2BDB0;
  font-weight: 600;
  letter-spacing: 0.05em;
}
.megastory-quote-mark {
  font-family: var(--font-editorial);
  font-size: 5rem;
  line-height: 1;
  color: rgba(255, 255, 255, 0.12);
  position: absolute;
  top: 1.5rem;
  right: 2rem;
  pointer-events: none;
}
.megastory-title {
  font-family: var(--font-editorial);
  font-size: 2.25rem;
  font-weight: 800;
  color: #FFFFFF;
  line-height: 1.22;
  margin-bottom: 1rem;
}
.megastory-sapo {
  font-size: 1rem;
  color: #EADCDD;
  line-height: 1.65;
  margin-bottom: 2rem;
}
.megastory-action {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}
.btn-megastory-action {
  background: #FFFFFF;
  color: var(--color-brand-primary);
  border: none;
  border-radius: var(--radius-full);
  font-weight: 700;
  font-size: 0.875rem;
  padding: 0.65rem 1.4rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all var(--duration-fast);
  box-shadow: 0 4px 14px rgba(0,0,0,0.2);
}
.btn-megastory-action:hover {
  background: #FAF7F4;
  transform: translateY(-2px);
}
.megastory-readtime {
  font-size: 0.8125rem;
  color: #D6BCBE;
  font-weight: 600;
}
.megastory-visual-col {
  position: relative;
  min-height: 380px;
}
.megastory-hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.megastory-caption-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(180deg, transparent 0%, rgba(20, 6, 10, 0.85) 100%);
  padding: 1.5rem 1.5rem 1rem 1.5rem;
  color: #FFFFFF;
  font-size: 0.85rem;
  font-weight: 500;
  font-style: italic;
}

/* 3. Section Headers (Nhân Dân Style with red ribbon) */
.nhandan-section-block {
  margin-bottom: 3.5rem;
}
.nhandan-section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 2px solid var(--color-brand-primary);
  padding-bottom: 0.65rem;
  margin-bottom: 1.5rem;
}
.nhandan-sec-title-wrap {
  display: flex;
  align-items: center;
  gap: 0.65rem;
}
.nhandan-sec-ribbon {
  width: 5px;
  height: 22px;
  background: var(--color-brand-primary);
  border-radius: 2px;
}
.nhandan-sec-title {
  font-family: var(--font-sans);
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--color-brand-primary);
  letter-spacing: 0.02em;
}
.nhandan-sec-sub {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  margin-left: 0.5rem;
}
.nhandan-sec-more {
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--color-brand-primary);
  text-decoration: none;
}
.nhandan-sec-more:hover {
  text-decoration: underline;
}

/* 4. Society Asymmetric Grid (60% Lead + 40% Side Stack) */
.society-asymm-grid {
  display: grid;
  grid-template-columns: 1.35fr 1fr;
  gap: 1.5rem;
}
.society-lead-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  box-shadow: var(--shadow-sm);
  transition: transform var(--duration-normal) var(--ease-spring), box-shadow var(--duration-normal) var(--ease-spring);
}
.society-lead-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}
.society-lead-media {
  height: 250px;
  position: relative;
  overflow: hidden;
}
.society-lead-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.society-lead-tag {
  position: absolute;
  top: 1rem;
  left: 1rem;
  background: var(--color-brand-primary);
  color: #FFFFFF;
  font-size: 0.6875rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  padding: 0.3rem 0.75rem;
  border-radius: var(--radius-full);
}
.society-lead-info {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.society-lead-headline {
  font-family: var(--font-editorial);
  font-size: 1.45rem;
  font-weight: 800;
  line-height: 1.3;
  color: var(--color-text-headline);
  margin-bottom: 0.65rem;
}
.society-lead-desc {
  font-size: 0.925rem;
  color: var(--color-text-body);
  line-height: 1.55;
  margin-bottom: 1rem;
  flex-grow: 1;
}
.society-lead-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--color-border-hairline);
  padding-top: 0.75rem;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  font-weight: 600;
}
.society-side-stack {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.society-mini-row {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-md);
  padding: 0.85rem 1rem;
  display: flex;
  gap: 1rem;
  align-items: center;
  cursor: pointer;
  box-shadow: var(--shadow-sm);
  transition: transform var(--duration-fast), box-shadow var(--duration-fast);
}
.society-mini-row:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}
.society-mini-thumb {
  width: 95px;
  height: 80px;
  flex-shrink: 0;
  border-radius: var(--radius-sm);
  overflow: hidden;
}
.mini-thumb-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.society-mini-text {
  flex-grow: 1;
}
.society-mini-cat {
  font-size: 0.6875rem;
  font-weight: 800;
  color: var(--color-brand-accent);
  letter-spacing: 0.05em;
  display: block;
  margin-bottom: 0.2rem;
}
.society-mini-title {
  font-family: var(--font-serif);
  font-size: 0.95rem;
  font-weight: 700;
  line-height: 1.35;
  color: var(--color-text-headline);
  margin-bottom: 0.25rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.society-mini-meta {
  font-size: 0.75rem;
  color: var(--color-text-muted);
  font-weight: 600;
}

/* 5. Photojournalism Mosaic (Human Stories) */
.photojournalism-mosaic {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 1.5rem;
}
.mosaic-hero-card {
  position: relative;
  border-radius: var(--radius-lg);
  overflow: hidden;
  min-height: 380px;
  cursor: pointer;
  box-shadow: var(--shadow-md);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
.mosaic-hero-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
  transition: transform 0.6s var(--ease-spring);
}
.mosaic-hero-card:hover .mosaic-hero-img {
  transform: scale(1.03);
}
.mosaic-overlay {
  position: relative;
  z-index: 2;
  background: linear-gradient(180deg, transparent 0%, rgba(15, 6, 9, 0.92) 100%);
  padding: 2.5rem 2rem 1.75rem 2rem;
  color: #FFFFFF;
}
.mosaic-kicker {
  font-size: 0.75rem;
  font-weight: 800;
  letter-spacing: 0.1em;
  color: #FFA5B0;
  display: block;
  margin-bottom: 0.5rem;
}
.mosaic-title {
  font-family: var(--font-editorial);
  font-size: 1.65rem;
  font-weight: 800;
  line-height: 1.3;
  color: #FFFFFF;
  margin-bottom: 0.65rem;
}
.mosaic-excerpt {
  font-size: 0.925rem;
  color: #F0E0E2;
  line-height: 1.55;
  margin-bottom: 1rem;
}
.mosaic-meta {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  font-size: 0.8125rem;
  color: #D6BDC0;
  font-weight: 600;
}
.mosaic-side-stack {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}
.mosaic-card-small {
  position: relative;
  border-radius: var(--radius-lg);
  overflow: hidden;
  flex: 1;
  min-height: 180px;
  cursor: pointer;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}
.mosaic-small-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
  transition: transform 0.6s var(--ease-spring);
}
.mosaic-card-small:hover .mosaic-small-img {
  transform: scale(1.04);
}
.mosaic-small-overlay {
  position: relative;
  z-index: 2;
  background: linear-gradient(180deg, transparent 0%, rgba(15, 6, 9, 0.9) 100%);
  padding: 1.25rem 1.25rem 1rem 1.25rem;
  color: #FFFFFF;
}
.mosaic-small-title {
  font-family: var(--font-serif);
  font-size: 1.05rem;
  font-weight: 700;
  line-height: 1.35;
  color: #FFFFFF;
  margin-bottom: 0.35rem;
}
.mosaic-small-meta {
  font-size: 0.75rem;
  color: #E0C8CB;
  font-weight: 600;
}

/* 6. Op-Ed Column & Civic Poll Strip */
.nhandan-opinion-strip {
  display: grid;
  grid-template-columns: 1.25fr 1fr;
  gap: 1.5rem;
  margin-bottom: 3.5rem;
}
.opinion-box {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-left: 4px solid var(--color-brand-primary);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
}
.opinion-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--color-border-hairline);
  padding-bottom: 0.75rem;
  margin-bottom: 1.25rem;
}
.opinion-badge {
  font-size: 0.775rem;
  font-weight: 800;
  color: var(--color-brand-primary);
  letter-spacing: 0.08em;
}
.opinion-edition {
  font-size: 0.75rem;
  color: var(--color-text-muted);
  font-weight: 600;
}
.opinion-author-row {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  margin-bottom: 1.25rem;
}
.opinion-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: var(--color-brand-primary);
  color: #FFFFFF;
  font-weight: 800;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.05rem;
}
.opinion-author-name {
  font-family: var(--font-serif);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--color-text-headline);
}
.opinion-author-title {
  font-size: 0.8rem;
  color: var(--color-text-muted);
  font-weight: 500;
}
.opinion-quote {
  font-family: var(--font-serif);
  font-size: 1.15rem;
  font-style: italic;
  line-height: 1.65;
  color: var(--color-brand-primary);
  margin-bottom: 1rem;
}
.opinion-note {
  font-size: 0.8125rem;
  color: var(--color-text-muted);
}

/* 7. Culture & Slow Living (Mind & Soul / In-depth) */
.culture-asymm-grid {
  display: grid;
  grid-template-columns: 1.15fr 1fr;
  gap: 1.5rem;
}
.culture-hero-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  box-shadow: var(--shadow-sm);
  transition: transform var(--duration-normal) var(--ease-spring), box-shadow var(--duration-normal) var(--ease-spring);
}
.culture-hero-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}
.culture-hero-media {
  height: 240px;
  position: relative;
  overflow: hidden;
}
.culture-hero-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.culture-tag {
  position: absolute;
  top: 1rem;
  left: 1rem;
  background: var(--color-brand-primary);
  color: #FFFFFF;
  font-size: 0.6875rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  padding: 0.3rem 0.75rem;
  border-radius: var(--radius-full);
}
.culture-hero-body {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.culture-hero-title {
  font-family: var(--font-editorial);
  font-size: 1.35rem;
  font-weight: 800;
  line-height: 1.35;
  color: var(--color-text-headline);
  margin-bottom: 0.65rem;
}
.culture-hero-excerpt {
  font-size: 0.9rem;
  color: var(--color-text-body);
  line-height: 1.55;
  margin-bottom: 1rem;
  flex-grow: 1;
}
.culture-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--color-border-hairline);
  padding-top: 0.75rem;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  font-weight: 600;
}
.culture-list-col {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.culture-list-item {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-md);
  padding: 0.85rem 1rem;
  display: flex;
  gap: 1rem;
  align-items: center;
  cursor: pointer;
  box-shadow: var(--shadow-sm);
  transition: transform var(--duration-fast), box-shadow var(--duration-fast);
}
.culture-list-item:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}
.culture-item-thumb {
  width: 95px;
  height: 80px;
  flex-shrink: 0;
  border-radius: var(--radius-sm);
  overflow: hidden;
}
.culture-thumb-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.culture-item-content {
  flex-grow: 1;
}
.culture-item-cat {
  font-size: 0.6875rem;
  font-weight: 800;
  color: var(--color-brand-accent);
  letter-spacing: 0.05em;
  display: block;
  margin-bottom: 0.2rem;
}
.culture-item-title {
  font-family: var(--font-serif);
  font-size: 0.95rem;
  font-weight: 700;
  line-height: 1.35;
  color: var(--color-text-headline);
  margin-bottom: 0.25rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.culture-item-desc {
  font-size: 0.8rem;
  color: var(--color-text-muted);
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* 8. Asymmetric Category Page Layout (68% Main List : 32% Sidebar) */
.category-page-asymm {
  display: grid;
  grid-template-columns: 2fr 0.95fr;
  gap: 2rem;
  margin-bottom: 3.5rem;
}
.category-main-stream {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.category-stream-row {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  padding: 1.25rem;
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: 1.5rem;
  cursor: pointer;
  box-shadow: var(--shadow-sm);
  transition: transform var(--duration-fast), box-shadow var(--duration-fast);
}
.category-stream-row:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
}
.category-stream-thumb-wrap {
  height: 160px;
  border-radius: var(--radius-md);
  overflow: hidden;
}
.category-stream-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.category-stream-body {
  display: flex;
  flex-direction: column;
}
.category-stream-title {
  font-family: var(--font-editorial);
  font-size: 1.25rem;
  font-weight: 800;
  line-height: 1.3;
  color: var(--color-text-headline);
  margin-bottom: 0.5rem;
}
.category-stream-excerpt {
  font-size: 0.9rem;
  color: var(--color-text-body);
  line-height: 1.55;
  margin-bottom: 1rem;
  flex-grow: 1;
}
.category-stream-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid var(--color-border-hairline);
  padding-top: 0.65rem;
  font-size: 0.8125rem;
  color: var(--color-text-muted);
  font-weight: 600;
}

/* Category Sidebar Widgets */
.category-sidebar {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
.sidebar-widget-card {
  background: #FFFFFF;
  border: 1px solid var(--color-border-hairline);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  box-shadow: var(--shadow-sm);
}
.sidebar-widget-title {
  font-family: var(--font-sans);
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--color-brand-primary);
  border-bottom: 2px solid var(--color-brand-primary);
  padding-bottom: 0.6rem;
  margin-bottom: 1.25rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.top-read-list {
  display: flex;
  flex-direction: column;
  gap: 1.15rem;
}
.top-read-item {
  display: flex;
  gap: 1rem;
  align-items: baseline;
  cursor: pointer;
}
.top-read-num {
  font-family: var(--font-editorial);
  font-size: 1.75rem;
  font-weight: 900;
  color: var(--color-brand-primary);
  line-height: 1;
  flex-shrink: 0;
  width: 24px;
}
.top-read-headline {
  font-family: var(--font-serif);
  font-size: 0.925rem;
  font-weight: 700;
  line-height: 1.35;
  color: var(--color-text-headline);
  transition: color var(--duration-fast);
}
.top-read-item:hover .top-read-headline {
  color: var(--color-brand-primary);
  text-decoration: underline;
}

/* Responsive adjustments for asymmetric layout */
@media (max-width: 1080px) {
  .nhandan-top-cluster {
    grid-template-columns: 1fr 1fr;
  }
  .focal-timeline-col {
    grid-column: 1 / -1;
  }
  .society-asymm-grid,
  .photojournalism-mosaic,
  .nhandan-opinion-strip,
  .culture-asymm-grid,
  .category-page-asymm {
    grid-template-columns: 1fr;
  }
  .megastory-inner-card {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .nhandan-top-cluster {
    grid-template-columns: 1fr;
  }
  .category-stream-row {
    grid-template-columns: 1fr;
  }
  .category-stream-thumb-wrap {
    height: 180px;
  }
}
"""

with open("css/style.css", "a", encoding="utf-8") as f:
    f.write(nhandan_css)

print("Báo Nhân Dân asymmetric CSS suite added to css/style.css!")
