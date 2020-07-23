let articles_url = '/text_files/';

elements = document.querySelectorAll('.include-html');

function getFile(url, on_load_func){
    request = new XMLHttpRequest;
    request.open('GET', url);
    request.onload = on_load_func;
    request.send();
}

for(el of elements){
    console.log(el);
    file_name = el.id + '.html';

    getFile(articles_url+file_name, (event)=>{
        
        if(event.target.status == 200){
            el.innerHTML = event.target.response;
        }
        else{
            el.innerHTML = 'Ooopsy I dhink we couldn"t find the ardizle';
        }
        
    })
    
}



