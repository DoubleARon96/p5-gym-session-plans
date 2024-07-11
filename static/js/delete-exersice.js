const deleteButtons = document.getElementsByClassName("btn-delete");
var myModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of deleteButtons) {
  button.addEventListener("click", (a) => {
    let exerciseId = a.target.dataset.exercise_id;
    console.log(exerciseId)
    deleteConfirm.href = `userprograms_delete_url/${exerciseId}`;
    myModal.show();
  });
}