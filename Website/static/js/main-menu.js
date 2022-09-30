// for loader ---
var loader = document.getElementById("preloader");

window.addEventListener("load", function () {
  loader.style.opacity = 0;
  loader.style.zIndex = 1;
});

// Animation

var human1 = document.getElementById("human1");
var human = document.getElementById("human");
var mice1 = document.getElementById("mice1");
var mice = document.getElementById("mice");
var alien1 = document.getElementById("alien1");
var alien = document.getElementById("alien");
var image1 = document.getElementById("image1");
var content1 = document.getElementById("content1");
var circle1 = document.getElementById("circle1");

human.onclick = function () {
  human1.setAttribute("Class", "active");
  mice1.setAttribute("Class", "radio-image");
  alien1.setAttribute("Class", "radio-image");
  circle1.setAttribute("Class", "circle-opened");
  content1.setAttribute("Class", "content-opened");
  image1.setAttribute("Class", "image-opened");
};

mice.onclick = function () {
  human1.setAttribute("Class", "radio-image");
  mice1.setAttribute("Class", "active");
  alien1.setAttribute("Class", "radio-image");
  circle1.setAttribute("Class", "circle-opened");
  content1.setAttribute("Class", "content-opened");
  image1.setAttribute("Class", "image-opened");
};

alien.onclick = function () {
  human1.setAttribute("Class", "radio-image");
  mice1.setAttribute("Class", "radio-image");
  alien1.setAttribute("Class", "active");
  circle1.setAttribute("Class", "circle-opened");
  content1.setAttribute("Class", "content-opened");
  image1.setAttribute("Class", "image-opened");
};

var human12 = document.getElementById("human12");
var human2 = document.getElementById("human2");
var mice12 = document.getElementById("mice12");
var mice2 = document.getElementById("mice2");
var alien12 = document.getElementById("alien12");
var alien2 = document.getElementById("alien2");
var image2 = document.getElementById("image2");
var content2 = document.getElementById("content2");
var circle2 = document.getElementById("circle2");

human2.onclick = function () {
  human12.setAttribute("Class", "active");
  mice12.setAttribute("Class", "radio-image");
  alien12.setAttribute("Class", "radio-image");
  circle2.setAttribute("Class", "circle-opened");
  content2.setAttribute("Class", "content-opened");
  image2.setAttribute("Class", "image-opened");
};

mice2.onclick = function () {
  human12.setAttribute("Class", "radio-image");
  mice12.setAttribute("Class", "active");
  alien12.setAttribute("Class", "radio-image");
  circle2.setAttribute("Class", "circle-opened");
  content2.setAttribute("Class", "content-opened");
  image2.setAttribute("Class", "image-opened");
};

alien2.onclick = function () {
  human12.setAttribute("Class", "radio-image");
  mice12.setAttribute("Class", "radio-image");
  alien12.setAttribute("Class", "active");
  circle2.setAttribute("Class", "circle-opened");
  content2.setAttribute("Class", "content-opened");
  image2.setAttribute("Class", "image-opened");
};

var human13 = document.getElementById("human13");
var human3 = document.getElementById("human3");
var mice13 = document.getElementById("mice13");
var mice3 = document.getElementById("mice3");
var alien13 = document.getElementById("alien13");
var alien3 = document.getElementById("alien3");
var image3 = document.getElementById("image3");
var content3 = document.getElementById("content3");
var circle3 = document.getElementById("circle3");

human3.onclick = function () {
  human13.setAttribute("Class", "active");
  mice13.setAttribute("Class", "radio-image");
  alien13.setAttribute("Class", "radio-image");
  circle3.setAttribute("Class", "circle-opened");
  content3.setAttribute("Class", "content-opened");
  image3.setAttribute("Class", "image-opened");
};

mice3.onclick = function () {
  human13.setAttribute("Class", "radio-image");
  mice13.setAttribute("Class", "active");
  alien13.setAttribute("Class", "radio-image");
  circle3.setAttribute("Class", "circle-opened");
  content3.setAttribute("Class", "content-opened");
  image3.setAttribute("Class", "image-opened");
};

alien3.onclick = function () {
  human13.setAttribute("Class", "radio-image");
  mice13.setAttribute("Class", "radio-image");
  alien13.setAttribute("Class", "active");
  circle3.setAttribute("Class", "circle-opened");
  content3.setAttribute("Class", "content-opened");
  image3.setAttribute("Class", "image-opened");
};

var human14 = document.getElementById("human14");
var human4 = document.getElementById("human4");
var mice14 = document.getElementById("mice14");
var mice4 = document.getElementById("mice4");
var alien14 = document.getElementById("alien14");
var alien4 = document.getElementById("alien4");
var image4 = document.getElementById("image4");
var content4 = document.getElementById("content4");
var circle4 = document.getElementById("circle4");

human4.onclick = function () {
  human14.setAttribute("Class", "active");
  mice14.setAttribute("Class", "radio-image");
  alien14.setAttribute("Class", "radio-image");
  circle4.setAttribute("Class", "circle-opened");
  content4.setAttribute("Class", "content-opened");
  image4.setAttribute("Class", "image-opened");
};

mice4.onclick = function () {
  human14.setAttribute("Class", "radio-image");
  mice14.setAttribute("Class", "active");
  alien14.setAttribute("Class", "radio-image");
  circle4.setAttribute("Class", "circle-opened");
  content4.setAttribute("Class", "content-opened");
  image4.setAttribute("Class", "image-opened");
};

alien4.onclick = function () {
  human14.setAttribute("Class", "radio-image");
  mice14.setAttribute("Class", "radio-image");
  alien14.setAttribute("Class", "active");
  circle4.setAttribute("Class", "circle-opened");
  content4.setAttribute("Class", "content-opened");
  image4.setAttribute("Class", "image-opened");
};
