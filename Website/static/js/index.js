var home = document.getElementById("home");
var info = document.getElementById("info");
var contact = document.getElementById("contact");
var about = document.getElementById("about");

home.onclick = function () {
    home.setAttribute("Class", "active");
    contact.setAttribute("Class", "");
    info.setAttribute("Class", "");
    about.setAttribute("Class", "");
};

info.onclick = function () {
    home.setAttribute("Class", "");
    info.setAttribute("Class", "active");
    contact.setAttribute("Class", "");
    about.setAttribute("Class", "");
};

contact.onclick = function () {
    home.setAttribute("Class", "");
    info.setAttribute("Class", "");
    contact.setAttribute("Class", "active");
    about.setAttribute("Class", "");
};

about.onclick = function () {
    home.setAttribute("Class", "");
    info.setAttribute("Class", "");
    contact.setAttribute("Class", "");
    about.setAttribute("Class", "active");
};