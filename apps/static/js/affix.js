var yueDu = document.getElementById("yueDu");
	var body = document.body;
	let array = ["red", "blue", "yellow", "white", "black", "green", "orange","#FFF"];
	let index = 0;
	yueDu.onclick = function () {
		body.style.backgroundImage= array[index];
		index = (index + 1) % array.length;
	}