import Counter from "./Counter";
import CustomInput from "./CustomInput";
import './App.css';

export default function App() {
  return (
    <>
        <Counter ref={counterRef} />
        <CustomInput placeholder="type something..." />
        <button onClick={() => {

        }}>
            Reset
        </button>
    </>
  );
}

function forwardRef(function (props,ref) {
    return <input ref={props.inputRef} />;
}
