document.addEventListener('DOMContentLoaded', function() {
  const header = document.querySelector('header');
  const updateBtn = document.getElementById('update_header');

  updateBtn.addEventListener('click', function() {
    header.textContent = 'New Header!!!';
  });
});
