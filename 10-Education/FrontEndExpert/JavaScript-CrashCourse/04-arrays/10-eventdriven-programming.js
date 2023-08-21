const button = document.querySelector('button'); // select the first button element

// add event listener to window
window.addEventListener('load', (event) => {
    console.log('page is fully loaded');
});

// add event listener to the document
document.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM is fully loaded');
});

// add event listener to the body
document.body.addEventListener('click', (event) => {
    console.log('body was clicked');
});

button.addEventListener('click', onClick); // add event listener to the button

document.body.addEventListener('click', onClick,{
    capture: true, // capture the event in the capturing phase
    once: true, // remove the event listener after the first time it is triggered
    passive: true // the event listener will not call preventDefault()
    signal: abortController.signal // abort the event listener when the signal is aborted
}
); // add event listener to the body

function onClick(event) {
    console.log(event);
    console.log(event.target);
    console.log(this);
    console.log('Button was clicked!');
}
