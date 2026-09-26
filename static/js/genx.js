/**
 * Gen'X Vision School System — JavaScript Foundation & UI Controller
 * ==================================================================
 * Sprint: SPRINT-01 & Master Layout Controller
 */

'use strict';

const GenX = {
    version: '1.0.0',

    init() {
        this.initMobileSidebar();
        this.initFlashMessages();
        this.initBootstrapComponents();
        this.initHTMXHandlers();
        console.debug('[GenX] Master Layout & UI Initialized');
    },

    // Mobile Sidebar Drawer Toggle
    initMobileSidebar() {
        const toggleBtn = document.getElementById('sidebarToggleBtn');
        const closeBtn = document.getElementById('sidebarCloseBtn');
        const sidebar = document.getElementById('sidebarMenu');
        const backdrop = document.getElementById('sidebarBackdrop');

        if (!sidebar) return;

        function openSidebar() {
            sidebar.classList.add('show');
            if (backdrop) backdrop.classList.add('show');
            document.body.style.overflow = 'hidden';
        }

        function closeSidebar() {
            sidebar.classList.remove('show');
            if (backdrop) backdrop.classList.remove('show');
            document.body.style.overflow = '';
        }

        if (toggleBtn) {
            toggleBtn.addEventListener('click', openSidebar);
        }
        if (closeBtn) {
            closeBtn.addEventListener('click', closeSidebar);
        }
        if (backdrop) {
            backdrop.addEventListener('click', closeSidebar);
        }
    },

    // Bootstrap Tooltips / Popovers
    initBootstrapComponents() {
        if (typeof bootstrap === 'undefined') return;

        const tooltipEls = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        tooltipEls.forEach(el => new bootstrap.Tooltip(el));
    },

    // Flash Messages Auto-dismiss
    initFlashMessages() {
        const flashContainer = document.getElementById('flashMessages');
        if (!flashContainer) return;

        const alerts = flashContainer.querySelectorAll('.alert');
        alerts.forEach(alert => {
            if (alert.classList.contains('alert-success') || alert.classList.contains('alert-info')) {
                setTimeout(() => {
                    if (typeof bootstrap !== 'undefined') {
                        const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
                        if (bsAlert) bsAlert.close();
                    }
                }, 5000);
            }
        });
    },

    // HTMX Handlers
    initHTMXHandlers() {
        if (typeof htmx === 'undefined') return;

        document.body.addEventListener('htmx:responseError', function (event) {
            console.error('[GenX] HTMX response error:', event.detail.xhr.status);
        });
    }
};

document.addEventListener('DOMContentLoaded', () => {
    GenX.init();
});
