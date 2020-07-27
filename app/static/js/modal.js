
modalFile =function(){
// Get the modal
let modal = document.querySelector(".modal-image");

let content_list = document.querySelector('.content-list');



for(size_div of content_list.children){

    let link = size_div.children[0];
    if(link.children[0].classList.contains('my-art')){
        link.addEventListener('click', showModal);
    }
    
}

let captionText = document.querySelector(".modal-caption");
let modalImg = document.querySelector('.modal-content')

let span = document.querySelector(".modal-close");


modalImg.addEventListener('webkitAnimationEnd', () => {

    //Close modal only after animation ended
    span.addEventListener('click', closeModal);
    document.addEventListener('click', closeModal);
    document.addEventListener('keydown', pressEsc);
    
})


function pressEsc(event){
    if(event.key == 'Escape'){closeModal();}
    
}

function showModal(event){
    event.preventDefault();
    
    modal.style.display = "block";
    modalImg.src = event.target.src;
    captionText.innerHTML = event.target.alt;
}

function closeModal(){
    modal.style.display = 'none';
    span.removeEventListener('click', closeModal)
    document.removeEventListener('click', closeModal);
    document.removeEventListener('keydown', pressEsc);
}
}

modalFile();
