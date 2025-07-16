

document.addEventListener('DOMContentLoaded', function () {
  const cartForms = document.querySelectorAll('.ajax-add-to-cart');
  const popup = document.querySelector('#cart-popup');
  const popupBody = document.querySelector('#cart-popup-items');
  const popupTotal = document.querySelector('#popup-total');
  const popupCloseBtn = popup.querySelector('.close-popup');
  const checkoutLink = popup.querySelector('.popup-footer a');

  // Submit event for all forms with class 'ajax-add-to-cart'
  cartForms.forEach((form) => {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const formData = new FormData(form);
      const productId = form.dataset.productId;
      const url = `/cart/add/${productId}/`;

      fetch(url, {
        method: 'POST',
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
        },
        body: formData,
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then((data) => {
          showCartPopup(data);
        })
        .catch((error) => {
          console.error('AJAX add-to-cart error:', error);
        });
    });
  });

  function showCartPopup(data) {
    // Clear current popup content
    popupBody.innerHTML = '';

    // Add all items to popup body
    data.items.forEach((item) => {
      const itemHTML = `
        <div class="popup-item d-flex gap-3 align-items-center border-bottom py-2">
          <img src="${item.image_url}" alt="${item.name}" class="img-thumbnail" width="60" height="60">
          <div>
            <p class="mb-1 fw-bold">${item.name}</p>
            <p class="mb-0 small">Quantity: ${item.quantity}</p>
            ${item.size ? `<p class="mb-0 small">Size: ${item.size}</p>` : ''}
          </div>
        </div>
      `;
      popupBody.insertAdjacentHTML('beforeend', itemHTML);
    });

    // Update total
    popupTotal.textContent = `Total: $${data.total}`;

    // Update button
    checkoutLink.textContent = 'View Shopping Bag →';
    checkoutLink.setAttribute('href', '/cart/');

    // Show popup
    popup.classList.add('show');

    // Hide popup after 6s
    setTimeout(() => {
      popup.classList.remove('show');
    }, 6000);
  }

  // Manual close
  if (popupCloseBtn) {
    popupCloseBtn.addEventListener('click', () => {
      popup.classList.remove('show');
    });
  }

  // Expose a function to clear popup externally (e.g. after clear cart)
  window.clearCartPopup = function () {
    popupBody.innerHTML = '';
    popupTotal.textContent = 'Total: $0.00';
    popup.classList.remove('show');
  };
});
