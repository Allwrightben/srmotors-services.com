// iOS fallback for parallax backgrounds
document.addEventListener('DOMContentLoaded', function() {
    const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent);

    if (isIOS) {
        // For banner sections, replace background with img tag
        const banners = document.querySelectorAll('.tools-banner, .tools-banner-red');
        banners.forEach(banner => {
            const src = banner.dataset.src;
            if (src) {
                banner.innerHTML = `<img src="${src}" alt="" style="width: 100%; height: 100%; object-fit: cover;">`;
                banner.style.backgroundImage = 'none';
            }
        });

        // For CTA section, change background-attachment to scroll
        const cta = document.querySelector('.cta-section');
        if (cta) {
            cta.style.backgroundAttachment = 'scroll';
        }
    }
});