(function () {
    const accents = {
        'mun.html': '#1F51BA',
        'modelothon.html': '#ea580c',
        'exquizit.html': '#06b6d4',
        'arduinoexp.html': '#14b8a6',
        'catapultikon.html': '#D4AF37',
        'mathamaze.html': '#9D4EDD'
    };
    const qrCodes = {
    'mun.html': 'images/qr_mun.png',
    'modelothon.html': 'images/qr_modelothon.png',
    'jso.html': 'images/qr_jso.png',
    'exquizit.html': 'images/qr_exquizit.png',
    'arduinoexp.html': 'images/qr_arduino.png',
    'catapultikon.html': 'images/qr_catapultikon.png',
    'mathamaze.html': 'images/qr_mathamaze.png'
};
    const forms = document.querySelectorAll('form');

    forms.forEach((form) => {
        const pageName = window.location.pathname.split('/').pop();
        const accent = accents[pageName] || '#00aa66';
        const qrCode = qrCodes[pageName];
        console.log("Current page:", pageName);
        console.log("QR path:", qrCode);
        console.log("Full QR URL:", new URL(qrCode, window.location.href).href);
        const submitButton = form.querySelector('button[type="submit"]');
        if (!submitButton) return;

        const container = document.createElement('section');
        container.className = 'flex flex-col gap-3 pt-2';
        container.innerHTML = `
            <div class="flex items-center justify-between text-xs font-black uppercase tracking-widest" style="color: ${accent}">
                <span>Payment screenshot</span><span>Required</span>
            </div>
            <img 
            src="${qrCode}" 
            alt="Sample payment QR code" 
            id="payment-qr"
            class="mx-auto w-40 rounded-xl cursor-pointer transition-transform duration-300 hover:scale-105"
            title="Click to enlarge QR code"
           >
            <label class="text-xs font-bold uppercase tracking-wider" style="color: ${accent}">
                Upload payment screenshot
                <input type="file" accept="image/jpeg,image/png,image/webp" required class="mt-2 block w-full rounded-lg border border-current bg-transparent px-3 py-2 text-xs">
            </label>
            <button type="button" class="rounded-xl border px-4 py-3 text-sm font-black uppercase tracking-widest transition-opacity hover:opacity-80" style="border-color: ${accent}; color: ${accent}">Upload Image</button>
            <p class="hidden text-center text-xs font-bold" role="status" aria-live="polite"></p>
        `;
        submitButton.before(container);

        const fileInput = container.querySelector('input[type="file"]');
        const uploadButton = container.querySelector('button');
        const status = container.querySelector('[role="status"]');
        let uploaded = false;

        function showStatus(message, isError) {
            status.textContent = message;
            status.style.color = isError ? '#ef4444' : accent;
            status.classList.remove('hidden');
        }

        fileInput.addEventListener('change', () => {
            uploaded = false;
            if (fileInput.files[0]) {
                showStatus('Click Upload Image to upload this payment screenshot.', true);
            } else {
                status.classList.add('hidden');
            }
        });

        uploadButton.addEventListener('click', async () => {
            const image = fileInput.files[0];
            if (!image) {
                showStatus('Please choose a payment screenshot first.', true);
                return;
            }

            uploaded = false;
            uploadButton.disabled = true;
            uploadButton.textContent = 'Uploading...';
            showStatus('Uploading payment screenshot...', false);

            try {
                const data = new FormData();
                data.append('image', image);
                const response = await fetch('/api/upload', { method: 'POST', body: data });
                const result = await response.json().catch(() => ({}));

                if (!response.ok) {
                    throw new Error(result.detail || result.error || 'Image upload failed.');
                }

                uploaded = true;
                showStatus(result.message || 'Payment screenshot uploaded successfully.', false);
            } catch (error) {
                showStatus(error.message || 'Unable to upload image. Please try again.', true);
            } finally {
                uploadButton.disabled = false;
                uploadButton.textContent = 'Upload Image';
            }
        });

        // Capture phase runs before each page's existing form-submit handler.
        form.addEventListener('submit', (event) => {
            if (uploaded) return;
            event.preventDefault();
            event.stopImmediatePropagation();
            showStatus('Upload the payment screenshot before registering.', true);
            fileInput.focus();
        }, true);

        form.addEventListener('reset', () => {
            uploaded = false;
            status.classList.add('hidden');
        });
    });
})();
// =========================================
// QR CODE CLICK TO ENLARGE
// =========================================

document.addEventListener('click', function (event) {

    const qr = event.target.closest('#payment-qr');

    if (qr) {
        const modal = document.getElementById('qr-modal');
        const largeQR = document.getElementById('qr-large');

        largeQR.src = qr.src;
        modal.classList.add('active');

        document.body.style.overflow = 'hidden';
    }

    if (
        event.target.id === 'qr-close' ||
        event.target.id === 'qr-modal'
    ) {
        const modal = document.getElementById('qr-modal');

        modal.classList.remove('active');

        document.body.style.overflow = '';
    }
});
