const img = document.getElementById('imagine');
let toggle = true;
img.addEventListener('click', function(){

	toggle = !toggle;
	if(toggle){
	img.src = 'imagini\\N5.jpg';
	}
	else{
		img.src = 'imagini\\N6.jpg';
	}
})
