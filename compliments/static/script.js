document.addEventListener('DOMContentLoaded', function() {
    const complimentText = document.getElementById('complimentText');
    const getLoveBtn = document.getElementById('getLoveBtn');
    const loadingBar = document.getElementById('loadingBar');
    const shareBtn = document.getElementById('shareBtn');
    let currentComplimentId = null;

    function animateLoadingBar() {
        loadingBar.style.width = '0%';
        let width = 0;
        const interval = setInterval(() => {
            if (width >= 100) {
                clearInterval(interval);
            } else {
                width += 2;
                loadingBar.style.width = width + '%';
            }
        }, 20);
    }

    function createFloatingHeart() {
        const heart = document.createElement('div');
        heart.className = 'heart';
        heart.style.left = Math.random() * 100 + '%';
        document.querySelector('.hearts-container').appendChild(heart);
        setTimeout(() => heart.remove(), 4000);
    }

    function getCompliment() {
        getLoveBtn.disabled = true;
        animateLoadingBar();
        
        fetch('/get-compliment/')
            .then(response => response.json())
            .then(data => {
                setTimeout(() => {
                    complimentText.textContent = data.text;
                    currentComplimentId = data.id;
                    getLoveBtn.disabled = false;
                    shareBtn.style.display = 'inline-block';
                    
                    // Create floating hearts
                    for (let i = 0; i < 5; i++) {
                        setTimeout(() => createFloatingHeart(), i * 300);
                    }
                }, 1000);
            });
    }

    function shareCompliment() {
        if (!currentComplimentId) return;
        
        fetch(`/share/${currentComplimentId}/`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const shareUrl = window.location.origin + data.share_url;
                    navigator.clipboard.writeText(shareUrl)
                        .then(() => alert('Share link copied to clipboard! 💕'));
                }
            });
    }

    if (getLoveBtn) {
        getLoveBtn.addEventListener('click', getCompliment);
    }
    
    if (shareBtn) {
        shareBtn.addEventListener('click', shareCompliment);
    }
});
document.addEventListener("DOMContentLoaded", () => {
    const bubbleContainer = document.querySelector(".bubbles");

    for (let i = 0; i < 50; i++) {
        const bubble = document.createElement("span");
        const size = Math.random() * 50 + 10; 
        bubble.style.width = `${size}px`;
        bubble.style.height = `${size}px`;
        bubble.style.left = `${Math.random() * 100}%`; 
        bubble.style.animationDuration = `${Math.random() * 10 + 5}s`; 
        bubble.style.animationDelay = `${Math.random() * 5}s`; 
        bubbleContainer.appendChild(bubble);
    }
});