console.log("Google Classroom Assistant is ready!");

const popupButton = document.createElement('button');
popupButton.innerHTML = 'Do you need help?';
popupButton.style.position = 'fixed';
popupButton.style.bottom = '20px';
popupButton.style.right = '20px';
popupButton.style.padding = '10px 20px';
popupButton.style.backgroundColor = '#007bff';
popupButton.style.color = '#fff';
popupButton.style.border = 'none';
popupButton.style.borderRadius = '5px';
popupButton.style.cursor = 'pointer';

popupButton.addEventListener('click', () => {
  chrome.runtime.sendMessage({ action: 'open_popup' });
});

document.body.appendChild(popupButton);
