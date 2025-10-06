document.getElementById("showFormBtn").onclick = function () {
  var form = document.getElementById("addEvaluationForm");
  form.classList.toggle("hidden");
};

function openModal(actionUrl) {
  const modal = document.getElementById("deleteModal");
  const form = document.getElementById("deleteForm");
  form.action = actionUrl;
  modal.classList.remove("hidden");
}

function closeModal() {
  document.getElementById("deleteModal").classList.add("hidden");
}
