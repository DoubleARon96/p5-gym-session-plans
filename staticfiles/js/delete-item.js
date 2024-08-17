const deleteButtons = document.getElementsByClassName("btn-delete");
var myModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (a) => {
    let basket_item_id = a.currentTarget.dataset.basket_item_id;
    deleteConfirm.href = `/basket/adjust_basket/${basket_item_id}`;
    myModal.show();
  });
}



