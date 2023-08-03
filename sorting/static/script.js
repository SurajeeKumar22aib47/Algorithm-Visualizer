// Get references to the modal and the modal trigger button
const modal = document.getElementById("modal");
const modalTrigger = document.getElementById("modal-trigger");
const closeModalBtn = document.getElementById("close-modal");

// Function to open the modal
function openModal() {
  modal.style.display = "block";
}

// Function to close the modal
function closeModal() {
  modal.style.display = "none";
}

// Event listener to open the modal when the trigger button is clicked
modalTrigger.addEventListener("click", openModal);

// Event listener to close the modal when the close button is clicked
closeModalBtn.addEventListener("click", closeModal);

// Event listener to close the modal when the user clicks outside the modal content
window.addEventListener("click", function(event) {
  if (event.target === modal) {
    closeModal();
  }
});
