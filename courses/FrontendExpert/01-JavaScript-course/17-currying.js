
function sum(a,b,c)) {
    return a + b + c;
}

function substraction(a,b,c)) {
    return a - b - c;
}

function curry(func) {
    return (a) => (b) => (c) => func(a,b,c);
}


