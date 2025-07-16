function Fibonacci(n){
	if (n === 0 ) {
        return [];
}
    if (n === 1) {
        return [0];
    }
		
	output = [0,1];

	let i = 2;
	while (output.length < n) {
		let x = output[i - 1] + output[i - 2];
		output.push(x);
		i++;
	}
	return output;
}

console.log(Fibonacci(5)); // [0, 1, 1, 2, 3]
console.log(Fibonacci(8)); // [0, 1, 1, 2, 3, 5, 8, 13]
console.log(Fibonacci(0)); // []
console.log(Fibonacci(1)); // [0]
console.log(Fibonacci(2)); // [0, 1]
