const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-link");
const menuBtnIcon = document.querySelector("i");

menuBtn.addEventListener("click", (e) => {
    navLinks.classList.toggle("open");
    const isopen = navLinks.classList.contains("open");menuBtnIcon.setAttribute("class", isopen ? "ri-close-line" : "ri-menu-line");
});

navLinks.addEventListener("click", (e) => {
    navLinks.classList.remove("open");
    menuBtnIcon.setAttribute("class", "ri-menu-line");
})

