import sys

with open("about-us.html", "r") as f:
    text = f.read()

start_marker = "<!-- Memberships, Awards & Grants Section -->"
end_marker = "<!-- Features Section -->"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    sys.exit(1)

new_content = """<!-- Memberships, Awards & Grants Section -->
      <style>
        .bento-section {
          background: linear-gradient(135deg, #fdfdfd 0%, #e2ebf0 100%);
          border-radius: 40px;
          padding: 80px 40px;
          margin-top: 60px;
          margin-bottom: 60px;
          box-shadow: inset 0 0 100px rgba(255,255,255,0.5);
        }
        .bento-grid {
          display: grid;
          grid-template-columns: 1fr 1fr 1fr;
          grid-auto-rows: minmax(300px, auto);
          gap: 24px;
        }
        .bento-card {
          background: rgba(255, 255, 255, 0.7);
          backdrop-filter: blur(20px);
          -webkit-backdrop-filter: blur(20px);
          border: 1px solid rgba(255, 255, 255, 0.8);
          border-radius: 30px;
          padding: 40px;
          box-shadow: 0 20px 40px rgba(0, 0, 0, 0.04);
          transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
          position: relative;
          overflow: hidden;
        }
        .bento-card:hover {
          transform: translateY(-8px);
          box-shadow: 0 30px 60px rgba(0, 174, 191, 0.12);
        }
        .bento-card::before {
          content: '';
          position: absolute;
          top: 0; left: 0; right: 0; bottom: 0;
          border-radius: 30px;
          padding: 2px;
          background: linear-gradient(135deg, rgba(255,255,255,0.8), rgba(255,255,255,0.1));
          -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
          -webkit-mask-composite: xor;
          mask-composite: exclude;
          pointer-events: none;
        }
        .card-tall { grid-row: span 2; grid-column: span 1; }
        .card-wide { grid-row: span 1; grid-column: span 2; }
        
        .bento-icon {
          width: 60px; height: 60px;
          border-radius: 16px;
          display: flex; align-items: center; justify-content: center;
          margin-bottom: 24px;
          color: #fff;
        }
        .icon-blue { background: linear-gradient(135deg, #00c6d7, #00aebf); box-shadow: 0 10px 20px rgba(0, 174, 191, 0.3); }
        .icon-orange { background: linear-gradient(135deg, #ff9900, #ff5500); box-shadow: 0 10px 20px rgba(255, 85, 0, 0.3); }
        .icon-green { background: linear-gradient(135deg, #2ecc71, #27ae60); box-shadow: 0 10px 20px rgba(46, 204, 113, 0.3); }
        
        .bento-title {
          font-size: 2rem;
          color: var(--primary-color);
          margin-bottom: 20px;
          font-weight: 700;
        }
        
        /* Badges */
        .modern-badges { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 30px; }
        .modern-badge { 
          padding: 8px 18px; border-radius: 50px; 
          font-size: 0.9rem; font-weight: 500;
          background: rgba(255,255,255,0.9); box-shadow: 0 4px 10px rgba(0,0,0,0.03);
          border: 1px solid rgba(0,174,191,0.2); transition: all 0.3s ease; color: var(--primary-color);
        }
        .modern-badge:hover { background: var(--secondary-color); color: #fff; border-color: var(--secondary-color); transform: translateY(-2px); box-shadow: 0 8px 15px rgba(0, 174, 191, 0.2); }
        
        /* Lists */
        .modern-list { list-style: none; padding: 0; display: flex; flex-direction: column; gap: 16px; }
        .modern-list li {
          display: flex; gap: 16px; align-items: flex-start;
          padding: 16px; background: rgba(255,255,255,0.6);
          border-radius: 16px; transition: background 0.3s ease, transform 0.3s ease;
          border: 1px solid rgba(255,255,255,0.8);
        }
        .modern-list li:hover { background: #fff; transform: translateX(5px); box-shadow: 0 5px 15px rgba(0,0,0,0.02); }
        .li-icon { flex-shrink: 0; margin-top: 2px; }
        .li-content strong { display: block; font-size: 1.1rem; color: var(--primary-color); margin-bottom: 4px; }
        .li-content span { font-size: 0.95rem; color: var(--text-muted); line-height: 1.5; display: block; }
        .badge-former { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; background: rgba(0,0,0,0.05); padding: 3px 10px; border-radius: 20px; margin-left: 8px; vertical-align: middle; font-weight: 600; color: #888; }

        @media (max-width: 992px) {
          .bento-grid { grid-template-columns: 1fr; }
          .card-tall, .card-wide { grid-row: auto; grid-column: span 1; }
          .bento-section { padding: 40px 20px; }
          .modern-list[style] { grid-template-columns: 1fr !important; }
        }
      </style>
      <section class="bento-section container">
        <div class="text-center mb-4">
          <span class="subtitle" style="font-size: 0.85rem; color: var(--secondary-color); font-weight: 700; letter-spacing: 2px;">PROFESSIONAL EXCELLENCE</span>
          <h2 style="font-size: 3rem; margin-top: 10px; color: var(--primary-color); margin-bottom: 40px; font-weight: 700;">Memberships &amp; Recognitions</h2>
        </div>

        <div class="bento-grid">
          
          <!-- Memberships (Tall) -->
          <div class="bento-card card-tall" id="memberships">
            <div class="bento-icon icon-blue">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
            </div>
            <h3 class="bento-title">Memberships</h3>
            
            <h4 style="font-size: 1rem; color: var(--secondary-color); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 20px; margin-top: 30px;">Societies</h4>
            <div class="modern-badges">
              <span class="modern-badge">Urological Society of India</span>
              <span class="modern-badge">NZUSI</span>
              <span class="modern-badge">European Association of Urology</span>
              <span class="modern-badge">American Urological Association</span>
              <span class="modern-badge">SIU</span>
            </div>

            <h4 style="font-size: 1rem; color: var(--secondary-color); text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 20px; margin-top: 40px;">Roles &amp; Committees</h4>
            <ul class="modern-list">
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00aebf" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg></div>
                <div class="li-content">
                  <strong>Editorial Member</strong>
                  <span>IJU, WJUR, BMC Urology</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00aebf" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg></div>
                <div class="li-content">
                  <strong>Council Member</strong>
                  <span>YOU</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="2"><path d="M12 2l3 6 6 .5-4.5 4L18 19l-6-3.5L6 19l1.5-6.5L3 8.5l6-.5z"></path></svg></div>
                <div class="li-content">
                  <strong>Core Committee<span class="badge-former">former</span></strong>
                  <span>Indian School of Urology</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="2"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"></path><polyline points="14 2 14 8 20 8"></polyline></svg></div>
                <div class="li-content">
                  <strong>Scientific Committee<span class="badge-former">former</span></strong>
                  <span>YOU</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg></div>
                <div class="li-content">
                  <strong>Associate Member<span class="badge-former">former</span></strong>
                  <span>EAU YAU Group on renal cancers</span>
                </div>
              </li>
            </ul>
          </div>

          <!-- Awards (Wide) -->
          <div class="bento-card card-wide" id="awards">
            <div class="bento-icon icon-orange">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path><path d="M4 22h16"></path><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path></svg>
            </div>
            <h3 class="bento-title">Awards</h3>
            <ul class="modern-list" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="#ff9900" stroke="#ff5500" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
                <div class="li-content" style="margin-top: 2px;">
                  <span style="font-size: 1.05rem;">Secured <strong style="display: inline; color: var(--primary-color);">first prize</strong> in the &ldquo;Uro Quiz- USICON 2021&rdquo;.</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="#ff9900" stroke="#ff5500" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
                <div class="li-content" style="margin-top: 2px;">
                  <span style="font-size: 1.05rem;">Selected for <strong style="display: inline; color: var(--primary-color);">USI Travel fellowship</strong> for the year 2021.</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="#ff9900" stroke="#ff5500" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
                <div class="li-content" style="margin-top: 2px;">
                  <span style="font-size: 1.05rem;"><strong style="display: inline; color: var(--primary-color);">Second Prize</strong> in CMC best poster for NZUSICON 2021.</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="#ff9900" stroke="#ff5500" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
                <div class="li-content" style="margin-top: 2px;">
                  <span style="font-size: 1.05rem;"><strong style="display: inline; color: var(--primary-color);">Second Prize</strong> CMC best poster for NZUSICON 2022.</span>
                </div>
              </li>
              <li style="grid-column: span 2;">
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="#ff9900" stroke="#ff5500" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg></div>
                <div class="li-content" style="margin-top: 2px;">
                  <span style="font-size: 1.05rem;"><strong style="display: inline; color: var(--primary-color);">Prof DS Subramanyam Gold Medal</strong> for best research 2021 (PGIMER).</span>
                </div>
              </li>
            </ul>
          </div>

          <!-- Grants & Fellowships (Wide) -->
          <div class="bento-card card-wide" style="margin-top:-24px;">
            <div class="bento-icon icon-green">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
            </div>
            <h3 class="bento-title">Grants &amp; Fellowships</h3>
            <ul class="modern-list" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2ecc71" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
                <div class="li-content" style="margin-top: 1px;">
                  <span style="font-size: 1.05rem;"><strong style="display: inline; color: var(--primary-color);">Travel Grant</strong> from &ldquo;Vattikuti Foundation&rdquo; for EAU 2023 Milan.</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2ecc71" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
                <div class="li-content" style="margin-top: 1px;">
                  <span style="font-size: 1.05rem;"><strong style="display: inline; color: var(--primary-color);">Travel Grant</strong> from &ldquo;Vattikuti Foundation&rdquo; for RUFCON 2022, India.</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2ecc71" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
                <div class="li-content" style="margin-top: 1px;">
                  <span style="font-size: 1.05rem;">Awarded <strong style="display: inline; color: var(--primary-color);">Urooncology Travelling Fellowship</strong> grant to Miami Cancer Institute (2021).</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2ecc71" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
                <div class="li-content" style="margin-top: 1px;">
                  <span style="font-size: 1.05rem;"><strong style="display: inline; color: var(--primary-color);">Visiting Fellowship</strong> at San Rafael Hospital Milan Italy (March 2023).</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2ecc71" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
                <div class="li-content" style="margin-top: 1px;">
                  <span style="font-size: 1.05rem;"><strong style="display: inline; color: var(--primary-color);">EUSP Travelling Fellowship</strong> to Imperial College London.</span>
                </div>
              </li>
              <li>
                <div class="li-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2ecc71" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg></div>
                <div class="li-content" style="margin-top: 1px;">
                  <span style="font-size: 1.05rem;">Selected for <strong style="display: inline; color: var(--primary-color);">UAA Young Urologist's Fellowship 2023</strong>.</span>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </section>
"""

new_text = text[:start_idx] + new_content + text[end_idx:]

with open("about-us.html", "w") as f:
    f.write(new_text)

print("Replaced successfully!")
