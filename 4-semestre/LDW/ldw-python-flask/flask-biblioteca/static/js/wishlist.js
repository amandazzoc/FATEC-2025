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
