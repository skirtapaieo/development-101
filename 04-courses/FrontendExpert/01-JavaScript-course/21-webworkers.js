// webworkes exercise

// create a webworker
const worker = new Worker('worker.js');

// send a message to the webworker
worker.postMessage('Hello from the main thread');

worker.addEventListener('message', (event) => {
    console.log(event.data);
});

postMessage('Hello from the main thread');

addEventListener('message', (event) => {
    console.log(event.data);
}


