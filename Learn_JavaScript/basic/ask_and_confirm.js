var name = prompt('Hey, what is your name?');

while (confirm('So your name is '+name+' right?') != true){
    name = prompt('Hey, what is your name?');
}

alert('Hello '+name);

