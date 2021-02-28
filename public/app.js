
// Created Element for Checking score
let Char = [button1.textContent, button2.textContent, button3.textContent, button4.textContent];
let Answer = GetPermutation(Char).reverse().slice(5, 10);
let count = 0;

// Created loop through 2 Array
for(let i=0; i<List.length; i++) {
    //Loop through 2nd array
    for(let j=0;j<sentChar.length; j++){
        if( JSON.stringify(Answer[i]) == JSON.stringify(sentChar[j]) ){
            count++;
        }
    }
}