/* ==========================================================================
   Apple-Style Clean Lightbox Modal (Vanilla JS, 100% Offline & Reliable)
   ========================================================================== */

(function() {
    // Create Modal HTML element
    const modalHtml = `
        <div id="appleLightboxModal" class="apple-lightbox" aria-hidden="true" role="dialog">
            <div class="apple-lightbox-backdrop"></div>
            <div class="apple-lightbox-dialog">
                <button class="apple-lightbox-close" aria-label="Close photo preview">&times;</button>
                <button class="apple-lightbox-prev" aria-label="Previous photo">&#10094;</button>
                <button class="apple-lightbox-next" aria-label="Next photo">&#10095;</button>
                <div class="apple-lightbox-content">
                    <img id="appleLightboxImg" src="" alt="Enlarged photo preview">
                    <div class="apple-lightbox-caption">
                        <span id="appleLightboxTitle"></span>
                        <span id="appleLightboxCounter"></span>
                    </div>
                </div>
            </div>
        </div>
    `;

    // Lightbox CSS
    const modalCss = `
        .apple-lightbox {
            display: none;
            position: fixed;
            inset: 0;
            z-index: 99999;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.25s ease;
        }
        .apple-lightbox.active {
            display: flex;
            opacity: 1;
        }
        .apple-lightbox-backdrop {
            position: absolute;
            inset: 0;
            background: rgba(11, 23, 44, 0.92);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
        }
        .apple-lightbox-dialog {
            position: relative;
            z-index: 2;
            max-width: 90vw;
            max-height: 90vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .apple-lightbox-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            max-width: 100%;
            max-height: 85vh;
        }
        #appleLightboxImg {
            max-width: 85vw;
            max-height: 75vh;
            object-fit: contain;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            border: 2px solid rgba(255, 255, 255, 0.15);
            transition: transform 0.2s ease;
        }
        .apple-lightbox-caption {
            margin-top: 1rem;
            color: #ffffff;
            font-size: 0.95rem;
            font-weight: 500;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            max-width: 85vw;
            padding: 0 0.5rem;
        }
        #appleLightboxCounter {
            font-size: 0.8rem;
            color: #94a3b8;
            font-weight: 600;
            background: rgba(255, 255, 255, 0.1);
            padding: 0.2rem 0.6rem;
            border-radius: 980px;
        }
        .apple-lightbox-close {
            position: fixed;
            top: 20px;
            right: 25px;
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #ffffff;
            font-size: 2rem;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            line-height: 1;
            transition: all 0.2s;
            z-index: 10;
        }
        .apple-lightbox-close:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: scale(1.08);
        }
        .apple-lightbox-prev, .apple-lightbox-next {
            position: fixed;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #ffffff;
            font-size: 1.5rem;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
            z-index: 10;
        }
        .apple-lightbox-prev:hover, .apple-lightbox-next:hover {
            background: #1a56db;
            border-color: #1a56db;
            transform: translateY(-50%) scale(1.08);
        }
        .apple-lightbox-prev { left: 25px; }
        .apple-lightbox-next { right: 25px; }

        @media (max-width: 640px) {
            .apple-lightbox-prev { left: 10px; width: 40px; height: 40px; font-size: 1.1rem; }
            .apple-lightbox-next { right: 10px; width: 40px; height: 40px; font-size: 1.1rem; }
            .apple-lightbox-close { top: 12px; right: 12px; width: 38px; height: 38px; font-size: 1.6rem; }
        }
    `;

    // Inject to DOM on load
    document.addEventListener('DOMContentLoaded', function() {
        const style = document.createElement('style');
        style.textContent = modalCss;
        document.head.appendChild(style);

        const div = document.createElement('div');
        div.innerHTML = modalHtml;
        document.body.appendChild(div.firstElementChild);

        const modal = document.getElementById('appleLightboxModal');
        const img = document.getElementById('appleLightboxImg');
        const title = document.getElementById('appleLightboxTitle');
        const counter = document.getElementById('appleLightboxCounter');
        const closeBtn = modal.querySelector('.apple-lightbox-close');
        const backdrop = modal.querySelector('.apple-lightbox-backdrop');
        const prevBtn = modal.querySelector('.apple-lightbox-prev');
        const nextBtn = modal.querySelector('.apple-lightbox-next');

        let galleryItems = [];
        let currentIndex = 0;

        // Collect all lightbox links
        const links = document.querySelectorAll('a[data-lightbox], a.lightbox-trigger');
        links.forEach((link, idx) => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Group by dataset group or section
                const group = link.getAttribute('data-lightbox') || 'default';
                galleryItems = Array.from(document.querySelectorAll(`a[data-lightbox="${group}"]`));
                if (galleryItems.length === 0) galleryItems = [link];

                currentIndex = galleryItems.indexOf(link);
                if (currentIndex === -1) currentIndex = 0;

                openModal(currentIndex);
            });
        });

        function openModal(index) {
            const currentLink = galleryItems[index];
            if (!currentLink) return;

            const imgSrc = currentLink.getAttribute('href') || (currentLink.querySelector('img') ? currentLink.querySelector('img').src : '');
            const imgTitle = currentLink.getAttribute('data-title') || (currentLink.querySelector('img') ? currentLink.querySelector('img').alt : 'Xavier College Photo');

            img.src = imgSrc;
            title.textContent = imgTitle;
            counter.textContent = `${index + 1} of ${galleryItems.length}`;

            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeModal() {
            modal.classList.remove('active');
            document.body.style.overflow = '';
            img.src = '';
        }

        function showNext() {
            if (galleryItems.length <= 1) return;
            currentIndex = (currentIndex + 1) % galleryItems.length;
            openModal(currentIndex);
        }

        function showPrev() {
            if (galleryItems.length <= 1) return;
            currentIndex = (currentIndex - 1 + galleryItems.length) % galleryItems.length;
            openModal(currentIndex);
        }

        closeBtn.addEventListener('click', closeModal);
        backdrop.addEventListener('click', closeModal);
        nextBtn.addEventListener('click', showNext);
        prevBtn.addEventListener('click', showPrev);

        document.addEventListener('keydown', function(e) {
            if (!modal.classList.contains('active')) return;
            if (e.key === 'Escape') closeModal();
            if (e.key === 'ArrowRight') showNext();
            if (e.key === 'ArrowLeft') showPrev();
        });
    });
})();
