function plus(number) {
    return new Promise((resolve, reject) => {
        resolve(number + 10);
    });
}

Promise.all([
    plus(20),
    plus(30),
    plus(40)
]).then(numbers => {
    numbers.forEach(number => console.log(number - 10));
})
