// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AdvancedCounter {
    // A mapping to store counters for each address with string id as key
    mapping(address => mapping(string => int)) private counters;
    // A mapping to keep track of the number of counters for each address
    mapping(address => uint) private counterCount;

    // Maximum number of counters allowed per address
    uint constant MAX_COUNTERS = 3;

    // Function to create a counter
    function createCounter(string memory id, int value) public {
        require(
            counterCount[msg.sender] < MAX_COUNTERS,
            "Maximum counters reached"
        );
        require(
            counters[msg.sender][id] == 0 && counters[msg.sender][id] != value,
            "Counter ID already exists"
        );
        counters[msg.sender][id] = value;
        counterCount[msg.sender]++;
    }

    // Function to delete a counter
    function deleteCounter(string memory id) public {
        require(
            counters[msg.sender][id] != 0 || counters[msg.sender][id] == 0,
            "Counter ID does not exist"
        );
        delete counters[msg.sender][id];
        counterCount[msg.sender]--;
    }

    // Function to increment a counter
    function incrementCounter(string memory id) public {
        require(
            counters[msg.sender][id] != 0 || counters[msg.sender][id] == 0,
            "Counter ID does not exist"
        );
        counters[msg.sender][id]++;
    }

    // Function to decrement a counter
    function decrementCounter(string memory id) public {
        require(
            counters[msg.sender][id] != 0 || counters[msg.sender][id] == 0,
            "Counter ID does not exist"
        );
        counters[msg.sender][id]--;
    }

    // Function to get the count of a specific counter
    function getCount(string memory id) public view returns (int) {
        require(
            counters[msg.sender][id] != 0 || counters[msg.sender][id] == 0,
            "Counter ID does not exist"
        );
        return counters[msg.sender][id];
    }
}
