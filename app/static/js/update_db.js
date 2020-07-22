
function db_update(event){
  //let response = await fetch('/update-activities')
  
  // if(response.ok){
  //   let json = await response.json();
  //   console.log(response.text);
  // }else{
  //   alert("HTTP-Error: " + response.status);
  // }

  
  fetch('/update-activities')
    .then(response => response.json())
    .then(data => {
      console.log(data);
      let btn = document.querySelector('#update-activities-btn');
      
      btn.textContent = 'Updated'
    })
}


let update_btn = document.querySelector('#update-activities-btn');
update_btn.addEventListener('click', db_update);
