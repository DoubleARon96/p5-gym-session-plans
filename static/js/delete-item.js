const deleteButtons = document.getElementsByClassName("btn-delete");
var myModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (a) => {
    console.log("1")
    let basket_item_id = a.currentTarget.dataset.basket_item_id;
    console.log('Exercise ID:', basket_item.id);
    deleteConfirm.href = `basket/delete_item/${basket_item_id}`;
    console.log('Delete Confirm Href:', deleteConfirm.href); 
    myModal.show();
  });
}
