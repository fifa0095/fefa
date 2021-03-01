
const R = document.getElementById("Host_id").textContent; 

button5.onpointerdown = function (){

    // Created loop through 2 Array
    for(let i=0; i<Answer.length; i++) {
        //Loop through 2nd array
        for(let j=0;j<sentChar.length; j++){
            if( JSON.stringify(Answer[i]) == JSON.stringify(sentChar[j]) ){
                count++;
            }
        }
    }
    
    //clear interval
    clearInterval(checkIt);
    //Created condition to getting Text
    if (count > 2){
        // Get Request Text3
        fetch(`/STORY/${R}/3`, {method : 'Get'})
        .then(function(response) {
            if (response.ok) return response.json();
            throw new Error('Request Failed');
        });
    }else if (count > 0){
        // Get Request Text2
        fetch(`/STORY/${R}/2`, {method : 'Get'})
        .then(function(response) {
            if (response.ok) return response.json();
            throw new Error('Request Failed');
        });
    }else{
        //Get Request Text1
        fetch(`/STORY/${R}/1`, {method : 'Get'})
        .then(function(response) {
            if (response.ok) return response.json();
            throw new Error('Request Failed');
        });
    }
} 