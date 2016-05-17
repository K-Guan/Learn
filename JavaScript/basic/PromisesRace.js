function randomLag(result) {
    return new Promise(resolve => {
        var time = Math.random() * 100;
        console.log(result, time);

        setTimeout(() => resolve(result), time);
    }
)}


// `Promise.race()` will handle the Promise that resolves first
Promise.race([randomLag(1), randomLag(2), randomLag(3)])
    .then(winner => console.log(winner));
