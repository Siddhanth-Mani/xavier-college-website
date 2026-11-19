import json, os

with open('dept_data.json', 'r', encoding='utf-8') as f:
    dept_data = json.load(f)

# Helper to generate global header
def get_header(active_nav="home", active_dept=""):
    return f'''    <header class="site-header">
        <div class="nav-container">
            <a href="index.html" class="brand-link">
                <img src="logo.jpg" alt="Xavier College Crest" class="brand-logo" onerror="this.src='Images/favicon1.jpg'">
                <div class="brand-text">
                    <span class="brand-name">Xavier College</span>
                    <span class="brand-location">Ba, Fiji · Est. 1953</span>
                </div>
            </a>

            <nav>
                <ul class="primary-nav" id="primaryNav">
                    <li class="nav-item {'active' if active_nav == 'home' else ''}">
                        <a href="index.html" class="nav-link">Home</a>
                    </li>
                    <li class="nav-item {'active' if active_nav == 'about' else ''}">
                        <a href="about.html" class="nav-link">About <span class="chevron">▾</span></a>
                        <ul class="nav-dropdown">
                            <li><a href="about.html" class="dropdown-link">The College & History</a></li>
                            <li><a href="about.html#location" class="dropdown-link">Location & Map</a></li>
                            <li><a href="about.html#contact" class="dropdown-link">Contact Details</a></li>
                        </ul>
                    </li>
                    <li class="nav-item {'active' if active_nav == 'departments' else ''}">
                        <a href="DScience.html" class="nav-link">Departments <span class="chevron">▾</span></a>
                        <ul class="nav-dropdown wide">
                            <li><a href="DLanguage.html" class="dropdown-link {'active-sub' if active_dept == 'DLanguage.html' else ''}">Language</a></li>
                            <li><a href="DMaths.html" class="dropdown-link {'active-sub' if active_dept == 'DMaths.html' else ''}">Maths & Physics</a></li>
                            <li><a href="DScience.html" class="dropdown-link {'active-sub' if active_dept == 'DScience.html' else ''}">Science</a></li>
                            <li><a href="DSocial.html" class="dropdown-link {'active-sub' if active_dept == 'DSocial.html' else ''}">Social Science</a></li>
                            <li><a href="DHome.html" class="dropdown-link {'active-sub' if active_dept == 'DHome.html' else ''}">Home Economics</a></li>
                            <li><a href="DComputer.html" class="dropdown-link {'active-sub' if active_dept == 'DComputer.html' else ''}">Office Tech & Comp</a></li>
                            <li><a href="DPemac.html" class="dropdown-link {'active-sub' if active_dept == 'DPemac.html' else ''}">PEMAC</a></li>
                            <li><a href="DIndustrial.html" class="dropdown-link {'active-sub' if active_dept == 'DIndustrial.html' else ''}">Industrial Arts</a></li>
                            <li><a href="DCommence.html" class="dropdown-link {'active-sub' if active_dept == 'DCommence.html' else ''}">Commerce</a></li>
                            <li><a href="DAgriculture.html" class="dropdown-link {'active-sub' if active_dept == 'DAgriculture.html' else ''}">Agriculture</a></li>
                        </ul>
                    </li>
                    <li class="nav-item {'active' if active_nav == 'programmes' else ''}">
                        <a href="achievements.html" class="nav-link">School Programmes</a>
                    </li>
                    <li class="nav-item {'active' if active_nav == 'resources' else ''}">
                        <a href="Resources.html" class="nav-link">Resources <span class="chevron">▾</span></a>
                        <ul class="nav-dropdown">
                            <li><a href="Resources.html" class="dropdown-link">Ministry Portals</a></li>
                            <li><a href="Resources.html#learning" class="dropdown-link">Online Learning Tools</a></li>
                        </ul>
                    </li>
                    <li class="nav-item {'active' if active_nav == 'gallery' else ''}">
                        <a href="photos.html" class="nav-link">Gallery <span class="chevron">▾</span></a>
                        <ul class="nav-dropdown">
                            <li><a href="photos.html#campus" class="dropdown-link">Campus</a></li>
                            <li><a href="photos.html#memories" class="dropdown-link">Memories</a></li>
                            <li><a href="photos.html#sports" class="dropdown-link">Inter-House</a></li>
                            <li><a href="photos.html#awards" class="dropdown-link">Awards</a></li>
                            <li><a href="photos.html#cadets" class="dropdown-link">Cadets</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>

            <button class="mobile-toggle" id="mobileToggle" aria-label="Toggle navigation">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>'''

# Helper to generate global footer
def get_footer():
    return '''    <footer class="site-footer">
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h4>Xavier College, Ba</h4>
                    <p>A Catholic secondary school dedicated to developing upright, creative, and compassionate leaders through holistic education in Fiji since 1953.</p>
                    <p style="margin-top:0.75rem; font-size:0.8rem; color:var(--apple-gold); font-weight:600;">
                        "Do Your Best and Leave the Rest to God"
                    </p>
                </div>
                <div class="footer-col">
                    <h5>Quick Navigation</h5>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About College</a></li>
                        <li><a href="achievements.html">School Programmes</a></li>
                        <li><a href="Resources.html">Online Resources</a></li>
                        <li><a href="photos.html">Photo Gallery</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h5>Departments</h5>
                    <ul class="footer-links">
                        <li><a href="DLanguage.html">Language Department</a></li>
                        <li><a href="DMaths.html">Maths & Physics</a></li>
                        <li><a href="DScience.html">Science Department</a></li>
                        <li><a href="DSocial.html">Social Science & Geog</a></li>
                        <li><a href="DComputer.html">Office Tech & Computer</a></li>
                        <li><a href="DCommence.html">Commerce Department</a></li>
                    </ul>
                </div>
                <div class="footer-col footer-contact">
                    <h5>Contact Information</h5>
                    <p><strong>Address:</strong> Namosau, Ba, Fiji Islands</p>
                    <p><strong>Phone:</strong> +679 667 0342</p>
                    <p><strong>Email:</strong> <a href="mailto:xaviercollege198@gmail.com">xaviercollege198@gmail.com</a></p>
                    <p style="margin-top:0.6rem;">
                        <a href="http://www.education.gov.fj/" target="_blank" rel="noopener">Ministry of Education Fiji ↗</a>
                    </p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2024 Xavier College Fiji. All rights reserved. &nbsp;·&nbsp; Webdesigner: <a href="https://about.me/siddhanthmani" target="_blank" rel="noopener">Siddhanth Mani</a></p>
                <p>Catholic Archdiocese of Suva &nbsp;·&nbsp; Western Division, Fiji</p>
            </div>
        </div>
    </footer>

    <script>
        // Mobile navigation toggle
        const toggleBtn = document.getElementById('mobileToggle');
        const navMenu = document.getElementById('primaryNav');
        if (toggleBtn && navMenu) {
            toggleBtn.addEventListener('click', () => {
                navMenu.classList.toggle('open');
            });
        }
    </script>'''

# Department Quick Nav Strip Helper
def get_dept_nav_strip(current_file):
    depts = [
        ("DLanguage.html", "Language"),
        ("DMaths.html", "Maths & Physics"),
        ("DScience.html", "Science"),
        ("DSocial.html", "Social Science"),
        ("DHome.html", "Home Economics"),
        ("DComputer.html", "Office Tech"),
        ("DPemac.html", "PEMAC"),
        ("DIndustrial.html", "Industrial Arts"),
        ("DCommence.html", "Commerce"),
        ("DAgriculture.html", "Agriculture")
    ]
    pills = []
    for f, name in depts:
        active_cls = "active" if f == current_file else ""
        pills.append(f'<a href="{f}" class="dept-pill {active_cls}">{name}</a>')
    
    return f'''    <div class="dept-nav-strip">
        <span class="dept-nav-label">Departments</span>
        {' '.join(pills)}
    </div>'''

print("Helper templates configured.")
