const button = document.querySelector('button');

button.addEventListener('click', onClick);

document.body.addEventListener('click', onClick);

function onClick() {
    console.log(event);
    console.log(event.type);
    console.log(event.target);
    console.log(this));
    console.log('Button was clicked!');
}
