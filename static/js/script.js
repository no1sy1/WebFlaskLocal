document.getElementById("open-modal-btn").addEventListener("click", function() {
  document.getElementById("my-modal").classList.add("open")
});

window.addEventListener('keydown', (e) => {
  if (e.key === "Escape") {
    document.getElementById("my-modal").classList.remove("open")
  }
});
