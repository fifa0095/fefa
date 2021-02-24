
//Generating 4 random character

function Select(){
    //declaring variable for select random character.
    const Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";


    //declaring variable for store random character.
    //Using Set Class for always making characters uniques
    let Random_char = new Set(); 

    // generates loop for adding random character
    
    while (Random_char.size < 4){
        Random_char.add(Alphabet.charAt(Math.floor(Math.random()*Alphabet.length)))
    };


    // for checking values
    const Start_Value = Array.from(Random_char);
    console.log(Start_Value);

}


Select();
