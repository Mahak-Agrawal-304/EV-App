// You can add JavaScript functionality here later if needed.
// For now, this is just a static landing page.

// script.js

// Function to handle active navigation link
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.nav-link-item'); // Select all links with this class

    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            // Prevent default link behavior if you're simulating page change
            // If these links will eventually go to different URLs, you might remove this
            event.preventDefault();

            // Remove 'active-link' from all nav links
            navLinks.forEach(item => item.classList.remove('active-link'));

            // Add 'active-link' to the clicked link
            this.classList.add('active-link');

            // Optionally, you can add logic here to load different content
            // based on which link was clicked. For now, it just changes the active state.
            const clickedLinkId = this.id;
            console.log(`Active link is now: ${clickedLinkId}`); // For debugging
            // Example: if (clickedLinkId === 'business-link') { loadBusinessContent(); }
            // else if (clickedLinkId === 'drivers-link') { loadDriversContent(); }
        });
    });

    // You can also trigger a click on the default active link on page load
    // to ensure the initial content for 'Business' (or 'Drivers') is shown if you add content loading.
    // document.getElementById('business-link').click(); // Uncomment if you add content loading
});

// Existing smooth scrolling example (keep if you still need it)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});