
// call element on html pages
const button1 = document.getElementById("Char1")
const button2 = document.getElementById("Char2")
const button3 = document.getElementById("Char3")
const button4 = document.getElementById("Char4")

const button5 = document.getElementById("Summit")

const button6 = document.getElementById('Reject')

const List = document.getElementById("Element")


// create arrays for storing input
let cretedCha = [];
let sentChar = [];

//add event listener when the button was cliked
button1.onpointerdown = function(){
    cretedCha.push("A");
}

button2.onpointerdown = function(){
    cretedCha.push("B");
}

button3.onpointerdown = function(){
    cretedCha.push("C");
}

button4.onpointerdown = function(){
    cretedCha.push("D");
}

//add remove button
button6.onpointerdown = function(){
    sentChar.pop();
}


// remove array value function
function removeItem(arr, item) {
    return arr.filter(f => f !== item)
}

// create function for check input
function CheckArray(){
    //create statement for getting 4 random characters in 1 array
    //update Input list
    if (cretedCha.length === 4){
        //put to main Array
        sentChar.push(cretedCha);
        
        
        //reset array
        cretedCha = [];
    }
    
    //check for Input list has 5 array
    if (sentChar.length === 5){
        clearInterval(checkIt);
    }
    //Input List
    List.textContent = sentChar.join(' | ')
}

const checkIt= setInterval(CheckArray, 1000);