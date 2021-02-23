
//Generating 4 random character

function Select(){
    //declaring variable for select random character.
    let Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";


    //declaring variable for store random character.
    let Start_Value = []; 


    for (var i=0; i<4; i++){
        // loop for Adding random character to array.
        Start_Value.push(Alphabet.charAt(Math.floor(Math.random()*Alphabet.length)))
    }

    alert(Start_Value);
}
