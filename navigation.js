// Leonne's Angel Machine - Navigation JavaScript

// Initialize folder toggles
document.addEventListener('DOMContentLoaded', function() {
    // Handle folder toggle clicks
    const folderToggles = document.querySelectorAll('.folder-toggle');
    
    folderToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const folderItem = this.parentElement;
            folderItem.classList.toggle('open');
            
            // Save state to localStorage
            const folderId = this.dataset.folder;
            const isOpen = folderItem.classList.contains('open');
            localStorage.setItem(`folder-${folderId}`, isOpen);
        });
    });
    
    // Restore folder states from localStorage
    document.querySelectorAll('.folder-item').forEach(folder => {
        const toggle = folder.querySelector('.folder-toggle');
        if (toggle) {
            const folderId = toggle.dataset.folder;
            const isOpen = localStorage.getItem(`folder-${folderId}`) === 'true';
            if (isOpen) {
                folder.classList.add('open');
            }
        }
    });
    
    // Highlight active page in sidebar
    const currentPath = window.location.pathname;
    document.querySelectorAll('.file-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
            // Open parent folder if exists
            const parentFolder = link.closest('.folder-item');
            if (parentFolder) {
                parentFolder.classList.add('open');
            }
        }
    });
    
    // Mobile menu toggle
    const menuToggle = document.getElementById('mobile-menu-toggle');
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            document.querySelector('.sidebar').classList.toggle('open');
        });
    }
});
