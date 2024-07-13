const deleteButtons = document.getElementsByClassName("btn-delete");
var myModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (a) => {
    console.log("1")
    let exerciseId = a.currentTarget.dataset.exercise_id;
    console.log('Exercise ID:', exerciseId);
    deleteConfirm.href = `userprograms_delete_url/${exerciseId}`;
    console.log('Delete Confirm Href:', deleteConfirm.href); 
    myModal.show();
  });
}

var myModal = new bootstrap.Modal(document.getElementById('deleteModal'));


for (let button of deleteButtons) {
  button.addEventListener("click", (a) => {
    let mainId = a.target.dataset.main_id;
    deleteConfirm.href = `userprograms_delete_url/${mainId}`;
    myModal.show();
  });
}
