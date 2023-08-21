import './App.css';


export default function App() {
  return (
    <button onClick={handleClick}>Click Me</button>
  );
}

function handleClick(event) {
  console.log(event);
}

function MyButton(props) {
  return (
    <button
      {...props}
      style={{
        color: 'red'
      }} />
  );
}

/*   return (
    <>
      <p>Hello Patrik</p>
      <p>Hello Emma</p>
      <p>Hello Gabriel</p>
      <Hello name="Patrik" />
      <Comment username="Gunnar" time="2021-10-10 10:10:10">
        <h1>This is a comment</h1>
      </Comment>
    </>
  )
}

function Hello({name = 'User'}) {
  return <p>Hello {name}</p>
}

function Comment({username, time, children}) {
  return (
    <div>
      <p>{username}</p>
      <p>{time}</p>
      <p>{children}</p>
    </div>
  )
} */
