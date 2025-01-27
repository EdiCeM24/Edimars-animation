const container = document.querySelector('.info-container'); 


const createAnime = () => {
    const anime = document.createElement('div');

    anime.classList.add('anime');

    const size = Math.random()*3;

    anime.style.width = `${size}px`;
    anime.style.height = `${size+5}px`;

    anime.style.left = `${Math.random()*100}%`;
    anime.style.top = `${Math.random()*100}%`;

    anime.style.animationDelay = `${Math.random() + 5}s`;
    anime.style.animationDelay = `${Math.random()*3+2}s`;

    return anime;
}

for(let i = 0; i < 30; i++){
    container.appendChild(createAnime());
    
}


//** ===== FOR NAVBAR TOGGLER ===== **/
const menu = document.querySelector('.nav-items');
const menuBtn = document.querySelector('#open-menu-btn');
const closeBtn = document.querySelector('#close-menu-btn');

menuBtn.addEventListener('click', () => {
   menu.style.display = 'flex';
   closeBtn.style.display = 'inline-block';
   menuBtn.style.display = 'none'; 
});

//** ===== HIDE MENU ON CLICK ===== **/
const closeNav = () => {
    menu.style.display = 'none';
    closeBtn.style.display = 'none';
    menuBtn.style.display = 'inline-block';
}

closeBtn.addEventListener('click', closeNav);
//** ===== HIDE MENU ON CLICK OUTSIDE ===== **/



//** ===== HIRE ME BUTTON SECTION ===== **/
function myFunc() {
    window.location.href = './pages/contact.html';
}


//** ===== DOWNLOAD BUTTON SECTION ===== **/
function download() {
    const image = "./images/best_resumes.pdf";
    const link = document.createElement('a');
    link.href = image;
    link.download = document.body.appendChild(link);
    link.click(link);
    document.body.removeChild(link);
}




