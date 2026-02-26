/**
 * Core Scripts — Dr. Gopal Sharma Portfolio
 */

document.addEventListener('DOMContentLoaded', () => {

  /* ── 1. MOBILE HAMBURGER MENU ─────────────────────────── */
  const toggle = document.querySelector('.mobile-menu-toggle');
  const nav    = document.querySelector('.main-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('active');
      toggle.innerHTML  = isOpen ? '&times;' : '&#9776;';
      toggle.setAttribute('aria-expanded', isOpen);
      // Prevent body scroll when menu is open
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // Close menu on nav link click
    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        nav.classList.remove('active');
        toggle.innerHTML = '&#9776;';
        toggle.setAttribute('aria-expanded', false);
        document.body.style.overflow = '';
      });
    });

    // Close menu on outside click
    document.addEventListener('click', (e) => {
      if (nav.classList.contains('active') &&
          !nav.contains(e.target) &&
          !toggle.contains(e.target)) {
        nav.classList.remove('active');
        toggle.innerHTML = '&#9776;';
        document.body.style.overflow = '';
      }
    });
  }

  /* ── 2. STICKY HEADER ON SCROLL ──────────────────────── */
  const header = document.querySelector('.site-header');
  if (header) {
    const makeSticky = () => {
      if (window.scrollY > 60) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', makeSticky, { passive: true });
    makeSticky(); // run once on load
  }

  /* ── 3. SMOOTH SCROLL FOR ANCHOR LINKS ───────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const headerH = header ? header.offsetHeight : 80;
        const top = target.getBoundingClientRect().top + window.scrollY - headerH - 20;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* ── 4. GALLERY LIGHTBOX (simple) ────────────────────── */
  const galleryItems = document.querySelectorAll('.gallery-item img');
  if (galleryItems.length > 0) {
    // Create overlay
    const overlay = document.createElement('div');
    overlay.id = 'gallery-lightbox';
    overlay.style.cssText = `
      display:none; position:fixed; inset:0; z-index:9999;
      background:rgba(0,0,0,0.92); justify-content:center;
      align-items:center; cursor:zoom-out;
    `;
    const lightboxImg = document.createElement('img');
    lightboxImg.style.cssText = `
      max-width:90vw; max-height:90vh; object-fit:contain;
      border-radius:12px; box-shadow:0 20px 60px rgba(0,0,0,0.5);
    `;
    const closeBtn = document.createElement('button');
    closeBtn.innerHTML = '&times;';
    closeBtn.style.cssText = `
      position:absolute; top:20px; right:28px; background:none;
      border:none; color:#fff; font-size:2.5rem; cursor:pointer;
      line-height:1;
    `;
    overlay.appendChild(lightboxImg);
    overlay.appendChild(closeBtn);
    document.body.appendChild(overlay);

    galleryItems.forEach(img => {
      img.style.cursor = 'zoom-in';
      img.addEventListener('click', () => {
        lightboxImg.src = img.src;
        lightboxImg.alt = img.alt;
        overlay.style.display = 'flex';
        document.body.style.overflow = 'hidden';
      });
    });

    const closeLightbox = () => {
      overlay.style.display = 'none';
      document.body.style.overflow = '';
    };
    closeBtn.addEventListener('click', closeLightbox);
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) closeLightbox();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeLightbox();
    });
  }

  /* ── 5. ACTIVE NAV LINK (current page) ───────────────── */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-list a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === currentPage) {
      a.classList.add('active');
    } else {
      a.classList.remove('active');
    }
  });

});
