// Get the modal
let modal = document.querySelector(".modal-image");

let content_list = document.querySelector('.content-list');



for(size_div of content_list.children){
    let link = size_div.children[0];
    link.addEventListener('click', showModal);
}

let captionText = document.querySelector(".modal-caption");
let modalImg = document.querySelector('.modal-content')

let span = document.querySelector(".modal-close");
span.addEventListener('click', closeModal)

document.addEventListener('keydown', (event) =>{
    if(event.key == 'Escape'){closeModal();}
})



function showModal(event){
    event.preventDefault();
    
    modal.style.display = "block";
    modalImg.src = event.target.src;
    captionText.innerHTML = event.target.alt;
}

function closeModal(){
    modal.style.display = 'none';
}