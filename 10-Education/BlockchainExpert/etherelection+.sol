/*
Improvements:

1 - Using a Constant for Fees: Using constants for the enrollment fee and voting fee enhances code readability and maintainability.
2 - Enhanced Access Control: Added owner-only modifier and utilized it where needed.
3 - Checking Candidate Enrollment: Replaced linear search with a mapping to check if a candidate is enrolled.
4 - Events: Added events to log significant contract activities.
5 - Explicitly Defined Variables: Removed uninitialized loop variable warning by explicitly initializing idx in the loop.
6 - Updated Solidity Version: Specified a more recent version of Solidity, promoting best practices.
*/

// Improvement 6: Updated Solidity Version
//pragma solidity >=0.4.22 <=0.8.17;
pragma solidity ^0.8.0; // +

contract EtherElection {
    address private owner;

    address[] private candidates;
    // Improvement 3: Checking Candidate Enrollment
    // mapping(address => uint256) votes;
    mapping(address => bool) private isCandidate; // +
    mapping(address => uint256) private votes;
    mapping(address => bool) private voted;

    address private winner;
    bool private winnerWithdrew;

    // Improvement 1: Using a Constant for Fees
    uint256 constant ENROLLMENT_FEE = 1 ether; // +
    uint256 constant VOTING_FEE = 10000 wei; // +

    // Improvement 4: Events
    event Enrolled(address candidate); // +
    event Voted(address voter, address candidate); // +
    event WinnerDeclared(address winner); // +
    event RewardClaimed(address winner); // +

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
        isCandidate[msg.sender] = true; // +

        emit Enrolled(msg.sender); // +
    }

    function vote(address candidate) public payable {
        require(candidates.length == 3, "enrollment is not done");
        // require(isCandidateInCandidates(candidate), "invalid candidate");
        require(isCandidate[candidate], "invalid candidate"); // +
        require(winner == address(0), "voting has ended");
        require(!voted[msg.sender], "you have already voted");
        require(msg.value == VOTING_FEE, "incorrect fee"); // +

        voted[msg.sender] = true;
        votes[candidate]++;

        if (votes[candidate] == 5) {
            winner = candidate;
            emit WinnerDeclared(winner); // +
        }

        emit Voted(msg.sender, candidate); // +
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

        emit RewardClaimed(winner); // +
    }

    function collectFees() public onlyOwner {
        // Improvement 2: Enhanced Access Control
        require(winnerWithdrew, "winner has not yet withdrawn reward");
        selfdestruct(payable(owner));
    }
}
