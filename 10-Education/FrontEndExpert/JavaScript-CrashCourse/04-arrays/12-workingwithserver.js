

const form = document.querySelector('form');
form.addEventListener('submit', onSubmit);

/* asynch function onSubmit(e) {
    event.preventDefault();

    const options = {
        method: 'POST',
        body: JSON.stringify({
            name: 'Patrik',
            age: 35
        }),
    }
    try {
        const response = await fetch('http://localhost:3000/users');
    }   const text = await response.text();
    console.log(text);
    } catch (error) {
        console.log('Oh no: ' + error);
    } */



