function sumOfArray(input){
    let result = 0;
    for (let i = 0; i < input.length; i++){
        result += input[i]
    }
    return result;
}

console.log(sumOfArray([1, 2, 3, 4, 5]));
console.log(sumOfArray([10, -2, 3]));
console.log(sumOfArray([]));