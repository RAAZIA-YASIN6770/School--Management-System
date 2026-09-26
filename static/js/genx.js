/**
 * Gen'X Vision School System — JavaScript Foundation
 * ====================================================
 * Sprint:       SPRINT-01
 * Task:         Sprint-01 Task 5 — Static Asset Foundation
 * Traceability: TBD-003 (Bootstrap 5.3 + HTMX 1.9), NFR-006 (Usability),
 *               NFR-007 (Mobile Responsiveness)
 *
 * This file provides base JavaScript infrastructure only.
 * Business-logic JavaScript belongs to future sprint module templates.
 *
 * Sprint-01 provides:
 *   - CSRF token handling for HTMX
 *   - Bootstrap tooltip/popover initialization
 *   - Flash message auto-dismiss
 *   - Loading state management
 */

'use strict';

// =============================================================================
// GEN'X VISION SCHOOL SYSTEM — APPLICATION NAMESPACE
// =============================================================================
const GenX = {

    /**
     * Application version (Sprint-01 foundation)
     */
    version: '1.0.0-sprint01',

    /**
     * Initialize all foundation components.
     * Called once when DOM is ready.
     */
    init() {
        this.initBootstrapComponents();
        this.initFlashMessages();
        this.initHTMXHandlers();
        console.debug('[GenX] Foundation initialized — Sprint-01');
    },

    // =========================================================================
    // BOOTSTRAP COMPONENT INITIALIZATION
    // =========================================================================
    initBootstrapComponents() {
        // Initialize all Bootstrap tooltips
        const tooltipEls = document.querySelectorAll('[data-bs-toggle="tooltip"]');
        tooltipEls.forEach(el => {
            new bootstrap.Tooltip(el, {
                trigger: 'hover focus',
                placement: 'auto',
            });
        });

        // Initialize all Bootstrap popovers
        const popoverEls = document.querySelectorAll('[data-bs-toggle="popover"]');
        popoverEls.forEach(el => {
            new bootstrap.Popover(el);
        });
    },

    // =========================================================================
    // FLASH MESSAGE AUTO-DISMISS
    // Django messages displayed in base.html auto-dismiss after 5 seconds.
    // =========================================================================
    initFlashMessages() {
        const flashContainer = document.getElementById('flashMessages');
        if (!flashContainer) return;

        const alerts = flashContainer.querySelectorAll('.alert');
        alerts.forEach(alert => {
            // Auto-dismiss success and info alerts after 5 seconds
            if (alert.classList.contains('alert-success') ||
                alert.classList.contains('alert-info')) {
                setTimeout(() => {
                    const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
                    if (bsAlert) {
                        bsAlert.close();
                    }
                }, 5000);
            }
        });
    },

    // =========================================================================
    // HTMX EVENT HANDLERS
    // Provides global HTMX configuration and error handling.
    // CSRF token injection is handled in base.html <script> block.
    // =========================================================================
    initHTMXHandlers() {
        if (typeof htmx === 'undefined') {
            console.warn('[GenX] HTMX not loaded — partial page updates unavailable.');
            return;
        }

        // Handle HTMX request errors gracefully
        document.body.addEventListener('htmx:responseError', function (event) {
            const status = event.detail.xhr.status;
            console.error('[GenX] HTMX response error:', status);

            if (status === 403) {
                // CSRF error — reload page to refresh token
                window.location.reload();
            } else if (status === 500) {
                // Server error — show user-friendly message
                GenX.showAlert('A server error occurred. Please try again.', 'danger');
            }
        });

        // Show loading spinner for slow HTMX requests (> 200ms)
        document.body.addEventListener('htmx:beforeRequest', function () {
            // Loading indicators handled by htmx-indicator CSS class
        });
    },

    // =========================================================================
    // UTILITY: Show temporary alert message
    // =========================================================================
    showAlert(message, level = 'info') {
        const container = document.getElementById('flashMessages')
            || document.querySelector('.container-fluid');

        if (!container) return;

        const alertEl = document.createElement('div');
        alertEl.className = `alert alert-${level} alert-dismissible fade show`;
        alertEl.setAttribute('role', 'alert');
        alertEl.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"
                    aria-label="Close"></button>
        `;

        container.prepend(alertEl);

        // Auto-dismiss after 5 seconds for success/info
        if (level === 'success' || level === 'info') {
            setTimeout(() => {
                const bsAlert = bootstrap.Alert.getOrCreateInstance(alertEl);
                if (bsAlert) bsAlert.close();
            }, 5000);
        }
    },

    // =========================================================================
    // UTILITY: Format currency as PKR
    // TBD-017: Currency is PKR.
    // =========================================================================
    formatPKR(amount) {
        return new Intl.NumberFormat('en-PK', {
            style: 'currency',
            currency: 'PKR',
            minimumFractionDigits: 0,
            maximumFractionDigits: 0,
        }).format(amount);
    },
};

// =============================================================================
// ENTRY POINT
// =============================================================================
document.addEventListener('DOMContentLoaded', function () {
    GenX.init();
});
