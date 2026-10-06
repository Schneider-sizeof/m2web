/**
 * M2web Maroc - Main JavaScript
 * Version: 2.0
 */
(function() {
    'use strict';

    document.addEventListener('DOMContentLoaded', function() {
        
        // 1. Animated Counters with IntersectionObserver
        const animateCounters = () => {
            const counters = document.querySelectorAll('.counter, .stat-number');
            if (!counters.length) return;

            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.1
            };

            const easeOutExpo = (t, b, c, d) => {
                return (t === d) ? b + c : c * (-Math.pow(2, -10 * t / d) + 1) + b;
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const targetElement = entry.target;
                        const target = parseInt(targetElement.getAttribute('data-target') || targetElement.innerText.replace(/,/g, ''), 10);
                        const duration = 2500; // 2.5s
                        const startTime = performance.now();
                        const suffix = targetElement.getAttribute('data-suffix') || '';

                        const updateCounter = (currentTime) => {
                            const elapsedTime = currentTime - startTime;
                            if (elapsedTime < duration) {
                                const currentValue = Math.floor(easeOutExpo(elapsedTime, 0, target, duration));
                                targetElement.innerText = currentValue.toLocaleString() + suffix;
                                requestAnimationFrame(updateCounter);
                            } else {
                                targetElement.innerText = target.toLocaleString() + suffix;
                            }
                        };
                        
                        // Clear out text before starting if needed, but here we just start animation
                        targetElement.innerText = '0' + suffix;
                        requestAnimationFrame(updateCounter);
                        observer.unobserve(targetElement); // Only animate once
                    }
                });
            }, observerOptions);

            counters.forEach(counter => observer.observe(counter));
        };

        // 2. Navbar Scroll Effect
        const handleNavbarScroll = () => {
            const navbar = document.querySelector('.navbar');
            if (!navbar) return;

            const onScroll = () => {
                if (window.scrollY > 40) {
                    navbar.classList.add('scrolled');
                } else {
                    navbar.classList.remove('scrolled');
                }
            };
            
            // Check immediately on load
            onScroll();
            
            // Listen with requestAnimationFrame for performance
            let ticking = false;
            window.addEventListener('scroll', () => {
                if (!ticking) {
                    window.requestAnimationFrame(() => {
                        onScroll();
                        ticking = false;
                    });
                    ticking = true;
                }
            }, { passive: true });
        };

        // 3. Scroll Animations (animate-on-scroll)
        const initScrollAnimations = () => {
            const animatedElements = document.querySelectorAll('.animate-on-scroll');
            if (!animatedElements.length) return;

            const observerOptions = {
                root: null,
                rootMargin: '0px 0px -50px 0px',
                threshold: 0.1
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const el = entry.target;
                        // Handle staggered delays if they are children of a grid/row
                        const parent = el.parentElement;
                        if (parent) {
                            const children = Array.from(parent.querySelectorAll('.animate-on-scroll'));
                            const index = children.indexOf(el);
                            if (index > 0) {
                                el.style.transitionDelay = `${index * 0.1}s`;
                            }
                        }
                        
                        el.classList.add('visible');
                        observer.unobserve(el);
                    }
                });
            }, observerOptions);

            animatedElements.forEach(el => observer.observe(el));
        };

        // 4. Smooth Scroll for Anchor Links
        const initSmoothScroll = () => {
            document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach(anchor => {
                anchor.addEventListener('click', function(e) {
                    const targetId = this.getAttribute('href');
                    const targetElement = document.querySelector(targetId);
                    
                    if (targetElement) {
                        e.preventDefault();
                        const headerOffset = 100; // Account for fixed navbar
                        const elementPosition = targetElement.getBoundingClientRect().top;
                        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                        
                        window.scrollTo({
                            top: offsetPosition,
                            behavior: "smooth"
                        });
                    }
                });
            });
        };

        // 5. Back to Top Button
        const initBackToTop = () => {
            const backToTopBtn = document.getElementById('backToTop');
            if (!backToTopBtn) return;

            let ticking = false;
            window.addEventListener('scroll', () => {
                if (!ticking) {
                    window.requestAnimationFrame(() => {
                        if (window.scrollY > 400) {
                            backToTopBtn.classList.add('show');
                        } else {
                            backToTopBtn.classList.remove('show');
                        }
                        ticking = false;
                    });
                    ticking = true;
                }
            }, { passive: true });

            backToTopBtn.addEventListener('click', (e) => {
                e.preventDefault();
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        };

        // 6. Form Validation Enhancement
        const initFormValidation = () => {
            const forms = document.querySelectorAll('.needs-validation');
            
            // Auto add form-control if missing on inputs
            document.querySelectorAll('input:not([type="checkbox"]):not([type="radio"]):not(.form-control), textarea:not(.form-control)').forEach(el => {
                el.classList.add('form-control');
            });
            document.querySelectorAll('select:not(.form-select)').forEach(el => {
                el.classList.add('form-select');
            });

            Array.prototype.slice.call(forms).forEach(function (form) {
                form.addEventListener('submit', function (event) {
                    if (!form.checkValidity()) {
                        event.preventDefault();
                        event.stopPropagation();
                    }
                    form.classList.add('was-validated');
                }, false);
            });
        };

        // 7. Lazy Loading Images
        const initLazyLoading = () => {
            const lazyImages = document.querySelectorAll('img[data-src]');
            if (!lazyImages.length) return;

            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.getAttribute('data-src');
                        img.removeAttribute('data-src');
                        imageObserver.unobserve(img);
                    }
                });
            }, { rootMargin: '50px 0px', threshold: 0.01 });

            lazyImages.forEach(img => imageObserver.observe(img));
        };

        // 8. Active Nav Highlight (clean logic that respects server-side active class)
        const highlightActiveNav = () => {
            // If Django has already set the active class server-side, keep it intact
            if (document.querySelector('.navbar-nav .nav-link.active')) {
                return;
            }
            
            const currentPath = window.location.pathname.replace(/\/$/, '') || '/';
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
            
            navLinks.forEach(link => {
                const linkHref = (link.getAttribute('href') || '').replace(/\/$/, '') || '/';
                if (linkHref === currentPath) {
                    link.classList.add('active');
                } else {
                    link.classList.remove('active');
                }
            });
        };

        // 9. Universal Touch Swipe Support for All Carousels (RTL-aware)
        const initCarouselSwipe = () => {
            const isRtl = document.documentElement.getAttribute('dir') === 'rtl';
            const carouselIds = ['#testimonialCarousel', '#heroCarousel', '#screenshotCarousel'];
            
            carouselIds.forEach(id => {
                const carousel = document.querySelector(id);
                if (!carousel || !window.bootstrap || !bootstrap.Carousel) return;
                
                const bsCarousel = bootstrap.Carousel.getInstance(carousel) || new bootstrap.Carousel(carousel);
                let touchStartX = 0;
                let touchEndX = 0;
                
                carousel.addEventListener('touchstart', e => {
                    touchStartX = e.changedTouches[0].screenX;
                }, {passive: true});
                
                carousel.addEventListener('touchend', e => {
                    touchEndX = e.changedTouches[0].screenX;
                    const threshold = 50;
                    const diff = touchEndX - touchStartX;
                    if (isRtl) {
                        // In RTL, swipe directions are reversed
                        if (diff > threshold) bsCarousel.next();
                        if (diff < -threshold) bsCarousel.prev();
                    } else {
                        if (diff < -threshold) bsCarousel.next();
                        if (diff > threshold) bsCarousel.prev();
                    }
                }, {passive: true});
            });
        };

        // 10. Mobile menu auto-close on link click (exclude dropdown toggles)
        const initMobileMenuClose = () => {
            const navLinks = document.querySelectorAll('.navbar-nav .nav-link:not(.dropdown-toggle), .navbar-nav .dropdown-item');
            const navbarToggler = document.querySelector('.navbar-toggler');
            const navbarCollapse = document.querySelector('.navbar-collapse');
            
            if (!navbarToggler || !navbarCollapse) return;

            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.getComputedStyle(navbarToggler).display !== 'none' && 
                        navbarCollapse.classList.contains('show')) {
                        // Use Bootstrap collapse API if available or click toggler
                        if (window.bootstrap && bootstrap.Collapse) {
                            const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
                            if (bsCollapse) {
                                bsCollapse.hide();
                                return;
                            }
                        }
                        navbarToggler.click(); // Trigger close
                    }
                });
            });
        };

        // Initialize all features
        animateCounters();
        handleNavbarScroll();
        initScrollAnimations();
        initSmoothScroll();
        initBackToTop();
        initFormValidation();
        initLazyLoading();
        highlightActiveNav();
        initCarouselSwipe();
        initMobileMenuClose();

    });
})();
