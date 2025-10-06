function toggleStrike(checkbox, labelId) {
  const label = document.getElementById(labelId);
  if (checkbox.checked) {
    label.style.textDecoration = "line-through";
    label.style.color = "#888";
  } else {
    label.style.textDecoration = "none";
    label.style.color = "";
  }
}

function openModal(actionUrl) {
  const modal = document.getElementById("deleteModal");
  const form = document.getElementById("deleteForm");
  form.action = actionUrl;
  modal.classList.remove("hidden");
}

function closeModal() {
  document.getElementById("deleteModal").classList.add("hidden");
}
