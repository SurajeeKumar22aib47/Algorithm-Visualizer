function performSwap(stepNumber) {
  // ... your existing code ...

  setTimeout(() => {
    animateSwap(element1, element2);
    highlightSwap(element1, element2);
  }, stepNumber * 1500); // Adjust the delay time as needed (e.g., 1500ms)
}
let isPlaying = false;
const playButton = document.getElementById('play-button');

function playAnimation() {
  if (isPlaying) return;
  isPlaying = true;
  playButton.disabled = true;

  for (let i = 1; i <= steps.length; i++) {
    setTimeout(() => {
      performSwap(i);

      // Enable the play button when the animation finishes
      if (i === steps.length) {
        isPlaying = false;
        playButton.disabled = false;
      }
    }, i * 1500); // Adjust the delay time as needed (e.g., 1500ms)
  }
}
function animateSwap(element1, element2) {
  const temp = $('<div>');
  element1.before(temp);
  element2.before(element1);
  temp.before(element2);
  temp.remove();
  element1.removeClass('swapping'); // Remove any previous swapping class
  element2.removeClass('swapping'); // Remove any previous swapping class
}
let isPlaying = false;
const playButton = document.getElementById('play-button');

function playAnimation() {
  if (isPlaying) return;
  isPlaying = true;
  playButton.disabled = true;

  // Remove the "swapping" class from all array elements before starting the animation
  $('.array').removeClass('swapping');

  for (let i = 1; i <= steps.length; i++) {
    setTimeout(() => {
      performSwap(i);

      // Enable the play button when the animation finishes
      if (i === steps.length) {
        isPlaying = false;
        playButton.disabled = false;
      }
    }, i * 1500); // Adjust the delay time as needed (e.g., 1500ms)
  }
}
