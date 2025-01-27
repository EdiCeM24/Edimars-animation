

window.addEventListener('scroll', () => {
    document.querySelector('#header').classList.toggle('window-scroll', window.scrollY > 0)
});



//** ===== SHOW/HIDE FAQ ANSWER ===== **/
const faqs = document.querySelectorAll(".faq");

faqs.forEach(item => {
    item.addEventListener("click", () => {
        item.classList.toggle("open");

        //** === CHANGE ICON === **/
        const icon = item.querySelector(".faq__icon i");
        if(icon.className === "bx bx-plus") {
            icon.className = "bx bx-minus";
        } else {
            icon.className = "bx bx-plus";
        }
    }); 
});