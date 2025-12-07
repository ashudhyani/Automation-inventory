document.addEventListener('DOMContentLoaded', function() {
    const loginBtn = document.getElementById('loginBtn');
    const loadingOverlay = document.getElementById('loadingOverlay');
    const messageToast = document.getElementById('messageToast');
    const toastMessage = document.getElementById('toastMessage');
    
    // Login button click handler
    if (loginBtn) {
        loginBtn.addEventListener('click', function() {
            handleLogin();
        });
    }
    
    // Handle login API call
    async function handleLogin() {
        // Show loading overlay
        loadingOverlay.classList.remove('hidden');
        
        try {
            const response = await fetch('/api/login-automation/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    email: 'swanim@yopmail.com',
                    password: 'Test@123'
                })
            });
            
            const data = await response.json();
            
            // Hide loading overlay
            loadingOverlay.classList.add('hidden');
            
            // Show toast message
            if (data.status === 'success') {
                showToast('Login automation completed successfully!', 'success');
            } else {
                showToast('Error: ' + data.message, 'error');
            }
            
        } catch (error) {
            // Hide loading overlay
            loadingOverlay.classList.add('hidden');
            
            // Show error toast
            showToast('An error occurred: ' + error.message, 'error');
            console.error('Login error:', error);
        }
    }
    
    // Show toast message
    function showToast(message, type = 'success') {
        toastMessage.textContent = message;
        messageToast.className = 'toast ' + type;
        messageToast.classList.remove('hidden');
        
        // Auto hide after 5 seconds
        setTimeout(() => {
            messageToast.classList.add('hidden');
        }, 5000);
    }
    
    // Add click handlers for other buttons (placeholder for future functionality)
    const otherButtons = document.querySelectorAll('.menu-button:not(#loginBtn)');
    otherButtons.forEach(button => {
        button.addEventListener('click', function() {
            const action = this.getAttribute('data-action');
            console.log('Button clicked:', action);
            // Placeholder for future functionality
            showToast(`${action.charAt(0).toUpperCase() + action.slice(1)} feature coming soon!`, 'success');
        });
    });
});
