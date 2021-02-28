
function GetPermutation(Something){
    let Permutation = [];
    
    if (Something.length == 0) return [];

    if (Something.length ==1) return [Something];
    
    for (let i =0; i< Something.length; i++){
        // Get a first character
        //ex [A , B , 4 , 7] get an A
        const char = Something[i];

        //get remaining list after get First character
        //ex [B , 4 , 7]
        const remainingSomething = Something.slice(0, i).concat(Something.slice(i+1));

        //throw remaining list to recursion
        const remainingSomethingPermuted = GetPermutation(remainingSomething);
        // loop for permutation
        for (let j =0; j< remainingSomethingPermuted.length; j++){
            const permutedArray = [char].concat(remainingSomethingPermuted[j]);

            Permutation.push(permutedArray);
        }
    }
    return Permutation
}