const editButtons = document.getElementsByClassName("btn-edit");
const newsText = document.getElementById("id_body");
const submitButton = document.getElementById("submitButton");


for (let button of editButtons) {
  button.addEventListener("click", (a) => {
    let homenews_id = a.target.dataset.homenews_id;
    let node = document.getElementById(`homenews${homenews_id}`);

    let homenewsContent = node.innerText;
    commentText.value = homenewsContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_homenews/${homenews_id}/`);
  });
}