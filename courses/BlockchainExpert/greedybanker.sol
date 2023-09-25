// Copyright © 2023 AlgoExpert LLC. All rights reserved.

pragma solidity ^0.8.0;

contract GreedyBanker {
    uint256 constant fee = 1000 wei;

    mapping(address => uint256) private balances;
    mapping(address => uint256) private depositCount;

    uint256 private feesCollected;

    address private owner;

    // Events to log important contract activities
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event FeesCollected(address indexed owner, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "only the owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    receive() external payable {
        uint256 depositFee = calculateDepositFee();
        balances[msg.sender] += msg.value - depositFee;
        feesCollected += depositFee;
        depositCount[msg.sender]++;
        emit Deposited(msg.sender, msg.value - depositFee);
    }

    fallback() external payable {
        feesCollected += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "insufficient balance");
        balances[msg.sender] -= amount;
        (bool sent, ) = payable(msg.sender).call{value: amount}("");
        require(sent, "withdraw failed");
        emit Withdrawn(msg.sender, amount);
    }

    function collectFees() external onlyOwner {
        uint256 totalFees = feesCollected;
        feesCollected = 0;
        (bool sent, ) = payable(owner).call{value: totalFees}("");
        require(sent, "transfer failed");
        emit FeesCollected(owner, totalFees);
    }

    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }

    function calculateDepositFee() internal returns (uint256) {
        if (depositCount[msg.sender] >= 1) {
            require(msg.value >= fee, "amount is not enough to cover the fee");
            return fee;
        }
        return 0;
    }
}
