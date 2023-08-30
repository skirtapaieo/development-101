/* const promise = Promise(resolve(3);

 promise.all([
    Promise.resolve(1),
    Promise.resolve(2),
    new Promise((resolve, reject) => setTimeout(() => resolve(3), 3000)),{

]).then(console.log).catch(console.log);
 */

async function test() {
    await new Promise((resolve, reject) => setTimeout(() => resolve(3), 3000));
    console.log('done');
    return 3;
}

console.log(test());
