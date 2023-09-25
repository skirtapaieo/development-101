pragma solidity ^0.8.0; // Improvement 6: Updated Solidity Version

contract EtherElection {
    address private owner;

    address[] private candidates;
    mapping(address => bool) private isCandidate; // Improvement 3: Checking Candidate Enrollment
    mapping(address => uint256) private votes;
    mapping(address => bool) private voted; // store who has already voted

    address private winner;
    bool private winnerWithdrew;

    uint256 constant ENROLLMENT_FEE = 1 ether; // Improvement 1: Using a Constant for Fees
    uint256 constant VOTING_FEE = 10000 wei; // Improvement 1: Using a Constant for Fees

    // Events
    event Enrolled(address candidate); // Improvement 4: Events
    event Voted(address voter, address candidate); // Improvement 4: Events
    event WinnerDeclared(address winner); // Improvement 4: Events
    event RewardClaimed(address winner); // Improvement 4: Events

    modifier onlyOwner() {
        // Improvement 2: Enhanced Access Control
        require(msg.sender == owner, "only the owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function enroll() public payable {
        require(candidates.length < 3, "3 candidates have already enrolled");
        require(msg.value == ENROLLMENT_FEE, "you must send exactly one ether");
        require(!isCandidate[msg.sender], "you are already a candidate");

        candidates.push(msg.sender);
        isCandidate[msg.sender] = true;

        emit Enrolled(msg.sender); // Logging event
    }

    function vote(address candidate) public payable {
        require(candidates.length == 3, "enrollment is not done");
        require(isCandidate[candidate], "invalid candidate"); // Improvement 3: Checking Candidate Enrollment
        require(winner == address(0), "voting has ended");
        require(!voted[msg.sender], "you have already voted");
        require(msg.value == VOTING_FEE, "incorrect fee"); // Improvement 1: Using a Constant for Fees

        voted[msg.sender] = true;
        votes[candidate]++;

        if (votes[candidate] == 5) {
            winner = candidate;
            emit WinnerDeclared(winner); // Logging event
        }

        emit Voted(msg.sender, candidate); // Logging event
    }

    function getWinner() public view returns (address) {
        require(winner != address(0), "winner has not been declared");
        return winner;
    }

    function claimReward() public {
        require(winner != address(0), "winner has not been declared");
        require(msg.sender == winner, "you are not the winner");
        require(!winnerWithdrew, "you have already withdrawn your reward");

        winnerWithdrew = true;
        (bool sent, ) = payable(winner).call{value: 3 ether}("");
        require(sent, "transfer failed");

        emit RewardClaimed(winner); // Logging event
    }

    function collectFees() public onlyOwner {
        // Improvement 2: Enhanced Access Control
        require(winnerWithdrew, "winner has not yet withdrawn reward");
        selfdestruct(payable(owner));
    }
}
