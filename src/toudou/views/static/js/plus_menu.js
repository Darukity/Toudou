const plus = document.querySelector(".plus-button");
const x = document.querySelector(".x-svg");
const options = document.querySelector(".plus-button-options");
const img1 = document.querySelector(".nav1")
const img2 = document.querySelector(".nav2")


plus.addEventListener("click", () => {
  plus.classList.toggle("toggle");
  options.classList.toggle("show");
  x.classList.toggle("rotate");
  img1.classList.toggle("show");
  img2.classList.toggle("show");
});