import json, os
from build_helpers import get_header, get_footer, get_dept_nav_strip

with open('dept_data.json', 'r', encoding='utf-8') as f:
    dept_data = json.load(f)

# ==============================================================================
# 1. GENERATE INDEX.HTML
# ==============================================================================
index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xavier College · Ba, Fiji</title>
    <link rel="shortcut icon" href="Images/favicon1.jpg" type="image/x-icon">
    <link rel="stylesheet" href="CSS/apple-theme.css">
    <style>
        /* Hero Section Styling — Fixed Container & Vibrant Collegiate Palette */
        .home-hero {{
            background: linear-gradient(180deg, #e8f1fc 0%, #ffffff 100%);
            border-bottom: 1px solid var(--apple-card-border);
            padding: 3.75rem 0 3.5rem;
            margin-bottom: 2.5rem;
        }}
        .hero-container {{
            max-width: 1140px;
            margin: 0 auto;
            padding: 0 1.5rem;
        }}
        .home-hero-grid {{
            display: grid;
            grid-template-columns: 1.25fr 0.75fr;
            gap: 3.5rem;
            align-items: center;
        }}
        .home-hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: var(--xav-gold-dark);
            background-color: var(--xav-gold-light);
            border: 1px solid var(--xav-gold-border);
            padding: 0.35rem 0.9rem;
            border-radius: 980px;
            margin-bottom: 1.25rem;
        }}
        .home-hero-title {{
            font-size: clamp(2.4rem, 4.2vw, 3.6rem);
            font-weight: 800;
            letter-spacing: -0.03em;
            line-height: 1.1;
            color: var(--xav-blue-dark);
            margin-bottom: 0.75rem;
        }}
        .home-hero-motto {{
            font-size: 1.2rem;
            font-style: italic;
            color: var(--xav-blue);
            font-weight: 600;
            margin-bottom: 1.25rem;
        }}
        .home-hero-lead {{
            font-size: 1.05rem;
            color: var(--apple-text-secondary);
            line-height: 1.7;
            margin-bottom: 2rem;
            max-width: 580px;
        }}
        .home-hero-buttons {{
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }}
        .hero-crest-card {{
            background: #ffffff;
            border: 2px solid var(--xav-blue-border);
            border-radius: 24px;
            padding: 2.5rem 2rem;
            text-align: center;
            box-shadow: 0 10px 30px rgba(26, 86, 219, 0.08);
            position: relative;
        }}
        .hero-crest-card::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 6px;
            background: linear-gradient(90deg, var(--xav-blue) 0%, var(--xav-gold) 100%);
            border-radius: 24px 24px 0 0;
        }}
        .hero-crest-img {{
            width: 140px;
            height: 140px;
            border-radius: 50%;
            border: 4px solid var(--xav-gold);
            box-shadow: 0 4px 18px rgba(217, 119, 6, 0.25);
            margin: 0.5rem auto 1.25rem;
            object-fit: cover;
        }}
        .hero-crest-caption h3 {{
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--xav-blue-dark);
            margin-bottom: 0.25rem;
        }}
        .hero-crest-caption p {{
            font-size: 0.85rem;
            color: var(--xav-gold-dark);
            font-weight: 600;
        }}

        /* Stat Numbers — Colorful & Engaging */
        .stat-card {{
            background: #ffffff;
            border: 1px solid var(--apple-card-border);
            border-radius: 18px;
            padding: 1.75rem 1.5rem;
            text-align: center;
            box-shadow: var(--apple-card-shadow);
            transition: all 0.2s ease;
        }}
        .stat-card:hover {{
            transform: translateY(-3px);
            box-shadow: var(--apple-card-shadow-hover);
        }}
        .stat-card.blue {{
            border-top: 4px solid var(--xav-blue);
            background: linear-gradient(180deg, #f0f7ff 0%, #ffffff 40%);
        }}
        .stat-card.blue .stat-num {{ color: var(--xav-blue); }}

        .stat-card.gold {{
            border-top: 4px solid var(--xav-gold);
            background: linear-gradient(180deg, #fffbeb 0%, #ffffff 40%);
        }}
        .stat-card.gold .stat-num {{ color: var(--xav-gold); }}

        .stat-card.green {{
            border-top: 4px solid var(--xav-green);
            background: linear-gradient(180deg, #ecfdf5 0%, #ffffff 40%);
        }}
        .stat-card.green .stat-num {{ color: var(--xav-green); }}

        .stat-card.purple {{
            border-top: 4px solid var(--xav-purple);
            background: linear-gradient(180deg, #f5f3ff 0%, #ffffff 40%);
        }}
        .stat-card.purple .stat-num {{ color: var(--xav-purple); }}

        .stat-num {{
            font-size: 2.6rem;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
        }}
        .stat-title {{
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--apple-text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        /* Outline Card Sections */
        .outline-section-title {{
            font-size: 1.65rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            color: var(--xav-blue-dark);
            margin-bottom: 1.25rem;
        }}
        .outline-box {{
            background: #ffffff;
            border: 1px solid var(--apple-card-border);
            border-radius: 18px;
            padding: 2.25rem;
            margin-bottom: 2.25rem;
            box-shadow: var(--apple-card-shadow);
        }}

        /* Department Cards — Colorful & Distinct */
        .dept-grid-card {{
            background: #ffffff;
            border: 1px solid var(--apple-card-border);
            border-left: 4px solid var(--xav-blue);
            border-radius: 14px;
            padding: 1.5rem;
            text-decoration: none;
            color: inherit;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.2s ease;
        }}
        .dept-grid-card:hover {{
            border-color: var(--xav-blue);
            box-shadow: 0 8px 24px rgba(26, 86, 219, 0.12);
            transform: translateY(-2px);
            text-decoration: none;
        }}
        .dept-grid-title {{
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--xav-blue-dark);
            margin-bottom: 0.35rem;
        }}
        .dept-grid-hod {{
            font-size: 0.84rem;
            color: var(--xav-blue);
            font-weight: 600;
            margin-bottom: 0.75rem;
        }}
        .dept-grid-desc {{
            font-size: 0.88rem;
            color: var(--apple-text-secondary);
            line-height: 1.55;
            margin-bottom: 1.15rem;
            flex: 1;
        }}
        .dept-grid-link {{
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--xav-blue);
            display: flex;
            align-items: center;
            gap: 0.3rem;
        }}

        /* Photo scroll row */
        .photo-scroll-strip {{
            display: flex;
            gap: 1.2rem;
            overflow-x: auto;
            padding: 0.5rem 0 1rem;
        }}
        .photo-scroll-item {{
            flex-shrink: 0;
            width: 270px;
            height: 190px;
            border-radius: 14px;
            overflow: hidden;
            border: 1px solid var(--apple-card-border);
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
        }}
        .photo-scroll-item img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.25s ease;
        }}
        .photo-scroll-item:hover img {{
            transform: scale(1.05);
        }}

        @media (max-width: 860px) {{
            .home-hero-grid {{
                grid-template-columns: 1fr;
                gap: 2.5rem;
            }}
            .hero-crest-card {{
                max-width: 360px;
                margin: 0 auto;
            }}
        }}
    </style>
</head>
<body>

{get_header("home")}

    <!-- Hero Section with Corrected Hero Container (No overlap) -->
    <section class="home-hero">
        <div class="hero-container">
            <div class="home-hero-grid">
                <div>
                    <span class="home-hero-badge">⭐ Catholic Secondary Education · Ba, Fiji</span>
                    <h1 class="home-hero-title">Welcome to<br>Xavier College</h1>
                    <p class="home-hero-motto">"Do Your Best and Leave the Rest to God"</p>
                    <p class="home-hero-lead">
                        Established in 1953 in Ba, Fiji, Xavier College provides a high standard of academic,
                        spiritual, and moral education for youth of all cultural and religious backgrounds across western Fiji.
                    </p>
                    <div class="home-hero-buttons">
                        <a href="about.html" class="btn-apple-primary">About Our College</a>
                        <a href="achievements.html" class="btn-apple-secondary">School Programmes</a>
                        <a href="Resources.html" class="btn-apple-secondary">Student Resources</a>
                    </div>
                </div>
                <div>
                    <div class="hero-crest-card">
                        <img src="logo.jpg" alt="Official Xavier College Crest" class="hero-crest-img">
                        <div class="hero-crest-caption">
                            <h3>Xavier College</h3>
                            <p>Founded 1953 · Ba, Fiji</p>
                            <p style="margin-top:0.6rem; font-size:0.82rem; color:var(--apple-text-secondary); line-height:1.4;">
                                Columban Fathers &amp; Catholic Archdiocese of Suva
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <main class="main-content">

        <!-- 4 Colorful Stat Outlines -->
        <div class="grid-4" style="margin-bottom: 2.5rem;">
            <div class="stat-card blue">
                <div class="stat-num">70+</div>
                <div class="stat-title">Years of Excellence</div>
            </div>
            <div class="stat-card gold">
                <div class="stat-num">10</div>
                <div class="stat-title">Academic Departments</div>
            </div>
            <div class="stat-card green">
                <div class="stat-num">1,200+</div>
                <div class="stat-title">Enrolled Students</div>
            </div>
            <div class="stat-card purple">
                <div class="stat-num">80+</div>
                <div class="stat-title">Teachers &amp; Staff</div>
            </div>
        </div>

        <!-- Welcome & About Outline -->
        <div class="outline-box">
            <div class="card-header">
                <div>
                    <span class="card-eyebrow">College Overview</span>
                    <h2 class="outline-section-title" style="margin:0.35rem 0 0;">Welcome to Our School Community</h2>
                </div>
            </div>
            <p style="font-size:1.02rem; color:var(--apple-text-secondary); line-height:1.75; margin-bottom:1.25rem;">
                Xavier College offers its students a broad choice of subjects and activities in a caring and supportive secondary school learning environment. As an educator or parent, your words and actions have the ability to lift students up or break them down. Encouraging words and actions are often internalized by students and have the power to motivate them to succeed. Encouragement can even be the difference between students completing school and giving up on themselves.
            </p>
            <p style="font-size:1.02rem; color:var(--apple-text-secondary); line-height:1.75; margin-bottom:1.5rem;">
                When a student and their parents are comfortable with others being informed of a diagnosis, an agreement can be made to inform and educate other students that every individual presents a unique way of thinking and experiencing the world. Strengths should be celebrated, challenges supported, and potential nurtured. We value the diversity of cultures at our school and warmly welcome all students to join our school community.
            </p>
            <div>
                <a href="about.html" class="btn-apple-secondary" style="font-size:0.88rem;">Read Full History &amp; Heritage →</a>
            </div>
        </div>

        <!-- Vision, Mission & Theme Outlines (Color Accented) -->
        <div class="outline-box">
            <div class="card-header">
                <div>
                    <span class="card-eyebrow gold">Foundational Pillars</span>
                    <h2 class="outline-section-title" style="margin:0.35rem 0 0;">Our Vision, Mission &amp; Theme</h2>
                </div>
            </div>
            <div class="grid-3">
                <div class="apple-card highlight-blue" style="margin-bottom:0; padding:1.75rem; background:#ffffff;">
                    <span class="card-eyebrow" style="color:var(--xav-blue);">Vision</span>
                    <h3 style="font-size:1.2rem; font-weight:800; color:var(--xav-blue-dark); margin:0.5rem 0 0.75rem;">Quality Education</h3>
                    <p style="font-size:0.92rem; color:var(--apple-text-secondary); line-height:1.65;">
                        All round quality education for every youth enrolled at Xavier College based on Christian principles and values, fostering academic and moral growth.
                    </p>
                </div>
                <div class="apple-card highlight-gold" style="margin-bottom:0; padding:1.75rem; background:#ffffff;">
                    <span class="card-eyebrow gold">Mission</span>
                    <h3 style="font-size:1.2rem; font-weight:800; color:var(--xav-gold-dark); margin:0.5rem 0 0.75rem;">Youth Development</h3>
                    <p style="font-size:0.92rem; color:var(--apple-text-secondary); line-height:1.65;">
                        Developing youth into upright, creative and loyal citizens imbibed with love and concern for others, equipped to contribute to the economic and cultural progress of Fiji.
                    </p>
                </div>
                <div class="apple-card highlight-green" style="margin-bottom:0; padding:1.75rem; background:#ffffff;">
                    <span class="card-eyebrow" style="color:var(--xav-green); background:var(--xav-green-light);">Annual Theme</span>
                    <h3 style="font-size:1.2rem; font-weight:800; color:var(--xav-green-dark); margin:0.5rem 0 0.75rem;">Educational Value</h3>
                    <p style="font-size:0.92rem; color:var(--apple-text-secondary); line-height:1.65;">
                        Genuine desire for value-added effectiveness in delivering education — ensuring purposeful learning outcomes for all students.
                    </p>
                </div>
            </div>
        </div>

        <!-- Academic Departments Grid -->
        <div class="outline-box">
            <div class="card-header">
                <div>
                    <span class="card-eyebrow">10 Academic Disciplines</span>
                    <h2 class="outline-section-title" style="margin:0.35rem 0 0.25rem;">Academic Departments</h2>
                    <p style="font-size:0.92rem; color:var(--apple-text-secondary);">Comprehensive subject options led by dedicated heads of department.</p>
                </div>
            </div>
            <div class="grid-2">
                <a href="DLanguage.html" class="dept-grid-card">
                    <div>
                        <div class="dept-grid-title">Language Department</div>
                        <div class="dept-grid-hod">Mrs. Ashika Arti Nair · HOD Language</div>
                        <p class="dept-grid-desc">English language and literature, fostering literacy, expression, and critical communication skills for global opportunities.</p>
                    </div>
                    <span class="dept-grid-link">Explore Curriculum →</span>
                </a>

                <a href="DMaths.html" class="dept-grid-card">
                    <div>
                        <div class="dept-grid-title">Mathematics &amp; Physics Department</div>
                        <div class="dept-grid-hod">Mr. Rupesh Rohit Kumar · HOD Mathematics &amp; Physics</div>
                        <p class="dept-grid-desc">Rigorous quantitative analysis, logical reasoning, pure mathematics, applied statistics, and experimental physical sciences.</p>
                    </div>
                    <span class="dept-grid-link">Explore Curriculum →</span>
                </a>

                <a href="DScience.html" class="dept-grid-card">
                    <div>
                        <div class="dept-grid-title">Science Department</div>
                        <div class="dept-grid-hod">Mrs. Zina Zafial Inus · HOD Science</div>
                        <p class="dept-grid-desc">Comprehensive biological, chemical, and physical sciences with modern laboratory facilities and inquiry-based pedagogy.</p>
                    </div>
                    <span class="dept-grid-link">Explore Curriculum →</span>
                </a>

                <a href="DSocial.html" class="dept-grid-card">
                    <div>
                        <div class="dept-grid-title">Social Science &amp; Geography Department</div>
                        <div class="dept-grid-hod">Mrs. Rachna Singh · HOD Geography &amp; Social Science</div>
                        <p class="dept-grid-desc">Fijian, Pacific, and world history, human and physical geography, civic responsibility, and environmental awareness.</p>
                    </div>
                    <span class="dept-grid-link">Explore Curriculum →</span>
                </a>

                <a href="DHome.html" class="dept-grid-card">
                    <div>
                        <div class="dept-grid-title">Home Economics Department</div>
                        <div class="dept-grid-hod">Mrs. Sangeeta Shalini Ram · HOD Home Economics</div>
                        <p class="dept-grid-desc">Nutritional science, food preparation, garment construction, and household management skills for worthwhile living.</p>
                    </div>
                    <span class="dept-grid-link">Explore Curriculum →</span>
                </a>

                <a href="DComputer.html" class="dept-grid-card">
                    <div>
                        <div class="dept-grid-title">Office Technology &amp; Computer Studies</div>
                        <div class="dept-grid-hod">Mrs. Ashna Chand · HOD Office Tech &amp; Computers</div>
                        <p class="dept-grid-desc">Digital literacy, office productivity software, computer science foundations, and administrative data processing.</p>
                    </div>
                    <span class="dept-grid-link">Explore Curriculum →</span>
                </a>

                <a href="DPemac.html" class="dept-grid-card">
                    <div>
                        <div class="dept-grid-title">PEMAC (Physical Education, Music, Art &amp; Craft)</div>
                        <div class="dept-grid-hod">Mrs. Aseri Misimisi · HOD PEMAC</div>
                        <p class="dept-grid-desc">Developing holistic wellbeing through athletics, team sports, music education, and fine art craft disciplines.</p>
                    </div>
                    <span class="dept-grid-link">Explore Curriculum →</span>
                </a>

                <a href="DIndustrial.html" class="dept-grid-card">
                    <div>
                        <div class="dept-grid-title">Industrial Arts Department</div>
                        <div class="dept-grid-hod">Mr. Nilesh Ram · HOD Industrial Arts</div>
                        <p class="dept-grid-desc">Technical drawing, woodcraft, metalwork, and vocational skills under the Technical Vocational Education (TVET) framework.</p>
                    </div>
                    <span class="dept-grid-link">Explore Curriculum →</span>
                </a>

                <a href="DCommence.html" class="dept-grid-card">
                    <div>
                        <div class="dept-grid-title">Commerce Department</div>
                        <div class="dept-grid-hod">Mr. Nitesh Bhan · HOD Commerce</div>
                        <p class="dept-grid-desc">Accounting principles, business enterprise, economic theory, and commercial law for future business leaders.</p>
                    </div>
                    <span class="dept-grid-link">Explore Curriculum →</span>
                </a>

                <a href="DAgriculture.html" class="dept-grid-card">
                    <div>
                        <div class="dept-grid-title">Agricultural Science Department</div>
                        <div class="dept-grid-hod">Mrs. Roneel Chand · HOD Agriculture</div>
                        <p class="dept-grid-desc">Sustainable crop cultivation, animal husbandry, soil science, and agri-business vital for Fiji's economic sustainability.</p>
                    </div>
                    <span class="dept-grid-link">Explore Curriculum →</span>
                </a>
            </div>
        </div>

        <!-- Campus Highlights Strip -->
        <div class="outline-box">
            <div class="card-header">
                <div>
                    <span class="card-eyebrow">Gallery Preview</span>
                    <h2 class="outline-section-title" style="margin:0.35rem 0 0.25rem;">Campus Life &amp; Activities</h2>
                    <p style="font-size:0.92rem; color:var(--apple-text-secondary);">Photographic snapshots of student life, academic celebrations, and sporting events.</p>
                </div>
                <a href="photos.html" class="btn-apple-primary" style="font-size:0.85rem;">View All Photos &amp; Archives →</a>
            </div>
            <div class="photo-scroll-strip">
                <div class="photo-scroll-item"><img src="img/sid1.jpg" alt="Xavier College campus"></div>
                <div class="photo-scroll-item"><img src="img/sid2.jpg" alt="Xavier College activities"></div>
                <div class="photo-scroll-item"><img src="img/sid7.jpg" alt="Xavier College events"></div>
                <div class="photo-scroll-item"><img src="img/test3.jpg" alt="Xavier College students"></div>
                <div class="photo-scroll-item"><img src="img/test4.jpg" alt="Xavier College classroom"></div>
                <div class="photo-scroll-item"><img src="img/sid3.jpg" alt="Xavier College campus life"></div>
            </div>
        </div>

    </main>

{get_footer()}
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print("Updated index.html")

# ==============================================================================
# 2. UPDATE PHOTOS.HTML WITH NATIVE APPLE LIGHTBOX
# ==============================================================================
photos_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photo Gallery · Xavier College Ba, Fiji</title>
    <link rel="shortcut icon" href="Images/favicon1.jpg" type="image/x-icon">
    <link rel="stylesheet" href="CSS/apple-theme.css">
    <style>
        .gallery-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.25rem;
            margin-top: 1.25rem;
        }}
        .gallery-item {{
            background: #ffffff;
            border: 1px solid var(--apple-card-border);
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
            transition: all 0.25s ease;
            position: relative;
        }}
        .gallery-item:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(26, 86, 219, 0.15);
            border-color: var(--xav-blue);
        }}
        .gallery-item a {{
            display: block;
            position: relative;
            cursor: pointer;
        }}
        .gallery-item img {{
            width: 100%;
            height: 220px;
            object-fit: cover;
            display: block;
            transition: transform 0.3s ease;
        }}
        .gallery-item:hover img {{
            transform: scale(1.03);
        }}
        .gallery-item-badge {{
            position: absolute;
            bottom: 10px;
            right: 10px;
            background: rgba(11, 37, 69, 0.85);
            color: #ffffff;
            font-size: 0.72rem;
            font-weight: 600;
            padding: 0.25rem 0.55rem;
            border-radius: 6px;
            backdrop-filter: blur(4px);
        }}
        @media (max-width: 768px) {{
            .gallery-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}
        @media (max-width: 480px) {{
            .gallery-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>

{get_header("gallery")}

    <section class="page-hero">
        <div class="page-hero-inner">
            <nav class="breadcrumb">
                <a href="index.html">Home</a> <span>/</span> <span>Gallery</span>
            </nav>
            <h1 class="page-title">Xavier College Photo Gallery</h1>
            <p class="page-subtitle">A visual archive celebrating campus heritage, athletics, cadet parades, and commemorative moments.</p>
        </div>
    </section>

    <main class="main-content">

        <!-- Category 1: Xavier Campus -->
        <article class="apple-card" id="campus">
            <div class="card-header">
                <div>
                    <span class="card-eyebrow">Campus Grounds</span>
                    <h2 class="card-title">Xavier Campus</h2>
                </div>
                <span style="font-size:0.84rem; color:var(--xav-blue); font-weight:700;">🔍 Click any photo to enlarge</span>
            </div>
            <div class="gallery-grid">
                <div class="gallery-item"><a href="dist/Gallery3/k01.jpg" data-lightbox="campus" data-title="Xavier College Main Campus Grounds"><img src="dist/Gallery3/k01.jpg" alt="Xavier Campus"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k02.jpg" data-lightbox="campus" data-title="Academic Blocks and Walkways"><img src="dist/Gallery3/k02.jpg" alt="Academic Buildings"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k04.jpg" data-lightbox="campus" data-title="Campus Grounds &amp; Facilities"><img src="dist/Gallery3/k04.jpg" alt="Campus Facility"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k05.jpg" data-lightbox="campus" data-title="Central Courtyard &amp; Assembly"><img src="dist/Gallery3/k05.jpg" alt="School Courtyard"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k06.jpg" data-lightbox="campus" data-title="Classroom Corridors and Architecture"><img src="dist/Gallery3/k06.jpg" alt="College Architecture"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k07.jpg" data-lightbox="campus" data-title="Secondary Block &amp; Gardens"><img src="dist/Gallery3/k07.jpg" alt="Classroom Blocks"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
            </div>
        </article>

        <!-- Category 2: Xaverian Memories -->
        <article class="apple-card" id="memories">
            <div class="card-header">
                <div>
                    <span class="card-eyebrow gold">Historical Collection</span>
                    <h2 class="card-title">Xaverian Memories</h2>
                </div>
                <span style="font-size:0.84rem; color:var(--xav-gold-dark); font-weight:700;">🔍 Click any photo to enlarge</span>
            </div>
            <div class="gallery-grid">
                <div class="gallery-item"><a href="dist/Gallery3/S04.jpg" data-lightbox="memories" data-title="Student Class Assembly"><img src="dist/Gallery3/S04.jpg" alt="Memories 1"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/S10.jpg" data-lightbox="memories" data-title="Auditorium Celebrations"><img src="dist/Gallery3/S10.jpg" alt="Memories 2"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k16.JPG" data-lightbox="memories" data-title="School Community Gatherings"><img src="dist/Gallery3/k16.JPG" alt="Memories 3"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k08.JPG" data-lightbox="memories" data-title="Classroom Academic Session"><img src="dist/Gallery3/k08.JPG" alt="Memories 4"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k09.JPG" data-lightbox="memories" data-title="Educational Presentations"><img src="dist/Gallery3/k09.JPG" alt="Memories 5"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k10.JPG" data-lightbox="memories" data-title="Fellowship &amp; Study"><img src="dist/Gallery3/k10.JPG" alt="Memories 6"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k11.JPG" data-lightbox="memories" data-title="College Traditions"><img src="dist/Gallery3/k11.JPG" alt="Memories 7"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k12.JPG" data-lightbox="memories" data-title="Cultural Exchange &amp; Friendship"><img src="dist/Gallery3/k12.JPG" alt="Memories 8"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k13.JPG" data-lightbox="memories" data-title="Xavier Spirit"><img src="dist/Gallery3/k13.JPG" alt="Memories 9"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
            </div>
        </article>

        <!-- Category 3: Inter-House Athletics -->
        <article class="apple-card" id="sports">
            <div class="card-header">
                <div>
                    <span class="card-eyebrow" style="color:var(--xav-green); background:var(--xav-green-light);">Sports Excellence</span>
                    <h2 class="card-title">Inter-House Athletics 2022</h2>
                </div>
                <span style="font-size:0.84rem; color:var(--xav-green); font-weight:700;">🔍 Click any photo to enlarge</span>
            </div>
            <div class="gallery-grid">
                <div class="gallery-item"><a href="dist/Gallery3/k18.JPG" data-lightbox="sports" data-title="Track &amp; Field Sprints"><img src="dist/Gallery3/k18.JPG" alt="Athletics 1"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k19.JPG" data-lightbox="sports" data-title="House Athletic Competitions"><img src="dist/Gallery3/k19.JPG" alt="Athletics 2"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k20.JPG" data-lightbox="sports" data-title="100m &amp; 200m Track Dash"><img src="dist/Gallery3/k20.JPG" alt="Athletics 3"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k21.JPG" data-lightbox="sports" data-title="Long Jump &amp; Field Events"><img src="dist/Gallery3/k21.JPG" alt="Athletics 4"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k22.JPG" data-lightbox="sports" data-title="Inter-House Relay Finals"><img src="dist/Gallery3/k22.JPG" alt="Athletics 5"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k23.JPG" data-lightbox="sports" data-title="House Cheerleaders &amp; Supporters"><img src="dist/Gallery3/k23.JPG" alt="Athletics 6"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
            </div>
        </article>

        <!-- Category 4: Award Ceremony -->
        <article class="apple-card" id="awards">
            <div class="card-header">
                <div>
                    <span class="card-eyebrow" style="color:var(--xav-purple); background:var(--xav-purple-light);">Academic Honours</span>
                    <h2 class="card-title">Annual Award Ceremony</h2>
                </div>
                <span style="font-size:0.84rem; color:var(--xav-purple); font-weight:700;">🔍 Click any photo to enlarge</span>
            </div>
            <div class="gallery-grid">
                <div class="gallery-item"><a href="dist/Gallery3/k36.JPG" data-lightbox="awards" data-title="Academic Prize Giving"><img src="dist/Gallery3/k36.JPG" alt="Award 1"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k37.JPG" data-lightbox="awards" data-title="Honouring Subject Champions"><img src="dist/Gallery3/k37.JPG" alt="Award 2"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k38.JPG" data-lightbox="awards" data-title="Recognition of Student Leadership"><img src="dist/Gallery3/k38.JPG" alt="Award 3"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k39.JPG" data-lightbox="awards" data-title="Presentation of Certificates"><img src="dist/Gallery3/k39.JPG" alt="Award 4"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k40.JPG" data-lightbox="awards" data-title="College Faculty &amp; Guests"><img src="dist/Gallery3/k40.JPG" alt="Award 5"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k41.JPG" data-lightbox="awards" data-title="Dux and High Achiever Awards"><img src="dist/Gallery3/k41.JPG" alt="Award 6"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
            </div>
        </article>

        <!-- Category 5: Cadets Pass Out -->
        <article class="apple-card" id="cadets">
            <div class="card-header">
                <div>
                    <span class="card-eyebrow">Discipline &amp; Leadership</span>
                    <h2 class="card-title">Cadets Pass Out Parade</h2>
                </div>
                <span style="font-size:0.84rem; color:var(--xav-blue); font-weight:700;">🔍 Click any photo to enlarge</span>
            </div>
            <div class="gallery-grid">
                <div class="gallery-item"><a href="dist/Gallery3/k48.jpg" data-lightbox="cadets" data-title="RFMF Officer Inspection"><img src="dist/Gallery3/k48.jpg" alt="Cadets 1"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k49.jpg" data-lightbox="cadets" data-title="Military Drill Contingents"><img src="dist/Gallery3/k49.jpg" alt="Cadets 2"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k50.jpg" data-lightbox="cadets" data-title="Pass Out Parade Formations"><img src="dist/Gallery3/k50.jpg" alt="Cadets 3"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k51.jpg" data-lightbox="cadets" data-title="March Past in Review"><img src="dist/Gallery3/k51.jpg" alt="Cadets 4"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k52.jpg" data-lightbox="cadets" data-title="Salute to Inspecting Commander"><img src="dist/Gallery3/k52.jpg" alt="Cadets 5"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
                <div class="gallery-item"><a href="dist/Gallery3/k53.jpg" data-lightbox="cadets" data-title="Cadet Trophy Presentation"><img src="dist/Gallery3/k53.jpg" alt="Cadets 6"><span class="gallery-item-badge">Enlarge ↗</span></a></div>
            </div>
        </article>

    </main>

{get_footer()}

    <!-- Apple Lightbox Interactive Modal Script -->
    <script src="js/apple-lightbox.js"></script>
</body>
</html>'''

with open('photos.html', 'w', encoding='utf-8') as f:
    f.write(photos_html)
print("Updated photos.html with Apple Lightbox")

print("Regeneration complete.")
