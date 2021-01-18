function theRating(aprov){

	if(aprov % 1 !== 0){
	   var naprov=aprov-0.5
	}else{
			var naprov=aprov
	}
	var niveles=5
	for(var i=0; i < naprov; i++){
		var sp = document.createElement('span');
		sp.setAttribute('class', 'fa fa-star checked');
	    document.getElementById('container').appendChild(sp);
	}
    	if(aprov<niveles && aprov % 1 !== 0){
    			var restante=niveles-aprov
    			for(var j=0; j < 1; j++){
    			var sp = document.createElement('span');
    			sp.setAttribute('class', 'fa fa-star-half-o');
    			document.getElementById('container').appendChild(sp);
    		}
        }
    	if(aprov<niveles && aprov % 1 !== 0){
    		    var oaprov=aprov+0.5
    			var restante=niveles-aprov-1
    			//console.log(aprov)
    			for(var j=0; j < restante; j++){
    			var sp = document.createElement('span');
    			sp.setAttribute('class', 'fa fa-star-o');
    			document.getElementById('container').appendChild(sp);
    		}
        } else{
    			var restante=niveles-aprov
    			//console.log(restante)
    			for(var j=0; j < restante; j++){
    			var sp = document.createElement('span');
    			sp.setAttribute('class', 'fa fa-star-o');
    			document.getElementById('container').appendChild(sp);
    		}
        }
    }
