
button5.onpointerdown = function (){
    //clear interval
    clearInterval(checkIt);
    //Created condition to getting Text
    if (count > 2){
        // Get Request Text3
        fetch('/', {method : 'Get'})
        .then(function(response) {
            if (response.ok) return response.json();
            throw new Error('Request Failed');
        });
    }else if (count > 0){
        // Get Request Text2
        fetch('/', {method : 'Get'})
        .then(function(response) {
            if (response.ok) return response.json();
            throw new Error('Request Failed');
        });
    }else{
        //Get Request Text1
        fetch('/', {method : 'Get'})
        .then(function(response) {
            if (response.ok) return response.json();
            throw new Error('Request Failed');
        });
    }
} 