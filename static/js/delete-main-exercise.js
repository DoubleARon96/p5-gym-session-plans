const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
var myModal = new bootstrap.Modal(document.getElementById('deleteModal'));


for (let button of deleteButtons) {
  button.addEventListener("click", (a) => {
    let mainId = a.target.dataset.main_id;
    deleteConfirm.href = `userprograms_delete_url/${mainId}`;
    myModal.show();
  });
}
