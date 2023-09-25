import { useState } from "react";

export default function CustomInput(props) {
    const [value, setValue] = useState("");

    return (
        <input
        {...props}
        value={value}
        onChange={(event) => setValue(event.target.value)}
        style=({color: "red"}) />
    );
};
