activities = function(){

// UPDATING DB
function db_update(event){
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



// RESIZING
let content = document.querySelector('.content-container');
let feed = document.querySelector('.rssfeed');
let activities = document.querySelector('.activities');


function fit_size(){
	
	if(window.matchMedia("(max-width: 1400px)").matches == false){
		
		let sizeDiff = 0;
		for(let el of feed.children){
			if(el.classList.contains('activities') == false){sizeDiff += el.offsetHeight;}
		}
		
		padding = parseInt(window.getComputedStyle(activities).paddingTop) + parseInt(window.getComputedStyle(activities).paddingTop);
		let targetHeight = content.offsetHeight - sizeDiff - padding;
		activities.style['max-height'] = targetHeight + 'px';
	}
}


window.addEventListener('load', () =>{
	setTimeout(fit_size, 50);
	window.addEventListener('resize', fit_size);
});
}

activities();