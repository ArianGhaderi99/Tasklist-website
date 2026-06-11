// accounts.js
document.addEventListener('DOMContentLoaded', function() {
    const tabLinks = document.querySelectorAll('.tab-link');
    const panes = document.querySelectorAll('.tab-pane');

    function switchTab(tabId) {
        panes.forEach(pane => pane.classList.remove('active'));
        document.getElementById(tabId).classList.add('active');
        tabLinks.forEach(link => link.classList.remove('active'));
        document.querySelector(`.tab-link[data-tab="${tabId}"]`).classList.add('active');
    }

    tabLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const tabId = this.getAttribute('data-tab');
            switchTab(tabId);
        });
    });

    // فعال کردن پنلی که خطاهای فرم را دارد (بعد از رفرش صفحه)
    const loginPane = document.getElementById('login-pane');
    const registerPane = document.getElementById('register-pane');
    const loginHasError = loginPane ? loginPane.querySelector('.errorlist, .non-field-errors') : false;
    const registerHasError = registerPane ? registerPane.querySelector('.errorlist, .non-field-errors') : false;
    
    if (registerHasError) {
        switchTab('register-pane');
    } else if (loginHasError) {
        if (loginPane && !loginPane.classList.contains('active')) {
            switchTab('login-pane');
        }
    }
});