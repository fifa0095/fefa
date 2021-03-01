
// call element on html pages
const button1 = document.getElementById("Char1")
const button2 = document.getElementById("Char2")
const button3 = document.getElementById("Char3")
const button4 = document.getElementById("Char4")

const button5 = document.getElementById("Submit")

const button6 = document.getElementById('Reject')

const List = document.getElementById("Element")


// create arrays for storing input
let cretedCha = [];
let sentChar = [];

//add event listener when the button was cliked
button1.onpointerdown = function(){
    cretedCha.push(button1.textContent);
}

button2.onpointerdown = function(){
    cretedCha.push(button2.textContent);
}

button3.onpointerdown = function(){
    cretedCha.push(button3.textContent);
}

button4.onpointerdown = function(){
    cretedCha.push(button4.textContent);
}

//add remove button
button6.onpointerdown = function(){
    sentChar.pop();
}

// create function for check input
function CheckArray(){
    //create statement for getting 4 random characters in 1 array
    if (cretedCha.length === 4){
        //put to main Array
        sentChar.push(cretedCha);
        
        
        //reset array
        cretedCha = [];
    }
    
    //check for Input list has 5 array
    if (sentChar.length === 5){
        button1.disabled = true;
        button2.disabled = true;
        button3.disabled = true;
        button4.disabled = true;
        button5.disabled = false;
    }
}


//update Input list
//Input List
function Update(){
    List.textContent = sentChar.join(' | ')
}

const checkIt= setInterval(CheckArray, 1000);

const upDatepara = setInterval(Update, 1000);