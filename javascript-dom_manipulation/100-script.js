document.addEventListener('DOMContentLoaded', function () {
  const addItemBtn = document.getElementById('add_item');
  const removeItemBtn = document.getElementById('remove_item');
  const clearListBtn = document.getElementById('clear_list');
  const myList = document.querySelector('.my_list');

  addItemBtn.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  removeItemBtn.addEventListener('click', function () {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      myList.removeChild(lastItem);
    }
  });

  clearListBtn.addEventListener('click', function () {
    myList.innerHTML = '';
  });
});
