pragma solidity ^0.8.0;

contract HelloWorld {
    string public message;

    constructor(string memory _message) {
        message = _message;
    }

    // function to set the message
    function update(string memory _message) public {
        message = _message;
    }

    // function to get the message
    function retrieve() public view returns (string memory) {
        return message;
    }

}
```