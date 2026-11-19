# Xavier College Website (high-school project)

A multi-page school website I built in high school (2022) for Xavier College, Ba, Fiji, as a class project. It is **not** the school's official site.

**Live:** https://siddhanth-mani.github.io/xavier-college-website/

## What's in it

- 15 pages: home, about, achievements, resources, a photo gallery and a page for each of 10 departments
- An image slider on the home page (Jssor) and a photo gallery with 50+ campus photos
- A shared header and navigation menu, styled in plain CSS
- Bootstrap and jQuery for layout and interactions

Built with HTML, CSS and JavaScript, plus jQuery, Bootstrap and Jssor Slider.

## Tidied up for publishing (2026)

The pages, slideshow, gallery and content are the ones I built. For publishing I added an iOS-style layer (`CSS/ios.css`) on top of the original stylesheets: system fonts, a frosted sticky navigation bar, context-menu dropdowns, rounded cards, and a layout that works on phones. I also:

- rebuilt the navigation menu. The Departments link pointed nowhere and the ten department pages sat in a second-level menu that touch screens couldn't open. `js/ios.js` adds a phone menu and tap-to-open dropdowns.

- added a banner making clear it's a student project, not the official site
- removed things that didn't belong in a public repo: a bundled `ngrok.exe`, school calendar documents, a local Flask test server, screenshots and unused duplicate images
- linked gallery thumbnails to photos that exist (the large versions were never in the project) and replaced Lightbox2 with a small viewer in `js/ios.js` that centres each photo, scales it to the screen and supports swipe, arrow keys and Esc
- removed the fixed pixel heights every page set on its content area, which made text run into the footer on some pages and left large blank gaps on others
- rebuilt the footer so it is centred and the same on every page, and laid out the home page vision, mission and theme as three cards
- turned the Resources links into tappable cards grouped by source
- matched file-name capitalisation to the links, because GitHub Pages is case-sensitive and Windows isn't
- resized the largest photos (33 MB down to 7 MB) so the slideshow and gallery load quickly
- fixed a table set to 150% width and slideshow slides that spilled out of their frame, which together caused sideways scrolling

## Known limitations

These are left as they were, since they're part of what I built then:

- Content is laid out with HTML tables, which was common in tutorials at the time

- A few decorative images referenced in the CSS were never added to the project
