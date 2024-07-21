const deleteButtons = document.getElementsByClassName("btn-delete");
var myModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
  button.addEventListener("click", (a) => {
    console.log("1")
    let exerciseId = a.currentTarget.dataset.exercise_id;
    console.log('Exercise ID:', exerciseId);
    deleteConfirm.href = `basket/delete_item/${itemline.id}`;
    console.log('Delete Confirm Href:', deleteConfirm.href); 
    myModal.show();
  });
}
