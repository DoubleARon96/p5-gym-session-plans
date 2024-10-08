const deleteButtons = document.getElementsByClassName("btn-delete");
var myModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (a) => {
    let exerciseId = a.currentTarget.dataset.exercise_id;
    deleteConfirm.href = `exercise_delete_url/${exerciseId}`; 
    myModal.show();
  });
}
