document.addEventListener('DOMContentLoaded', () => {
    const sizeLabels = document.querySelectorAll('.size-label');
    sizeLabels.forEach(label => {
      label.addEventListener('click', () => {
        sizeLabels.forEach(l => l.classList.remove('selected-size'));
        label.classList.add('selected-size'); 
      });
    });
  
  });
  
