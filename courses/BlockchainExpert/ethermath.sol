// Improvements:
// 1. Updated Solidity version.
// 2. Implemented a modifier for owner-only functions.
// 3. Used a mapping to store numbers instead of looping through an array to verify.
// 4. Improved function visibility by defining some functions as external.
// 5. Added events for better monitoring and interaction.
// 6. Cleared arrays properly.

pragma solidity ^0.8.0; // 1+

contract EtherMath {
    int256[] usableNumbers;
    int256 sum;
    uint256 reward;

    address owner;

    mapping(address => uint256) unclaimedRewards;
    mapping(int256 => bool) numberExistence; // 3+

    address[] submittedSolution;

    modifier onlyOwner() {
        // 2+
        require(msg.sender == owner, "only the owner can call this function");
        _;
    }

    // 5+ Events
    event ChallengeSubmitted(
        int256[] array,
        int256 targetSum,
        uint256 rewardAmount
    );
    event SolutionSubmitted(address user, bool success);
    event RewardsClaimed(address user, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    function verifySolution(
        int256[] memory solution
    ) internal view returns (bool) {
        int256 solutionSum;

        for (uint256 idx; idx < solution.length; idx++) {
            // bool numberExists;
            // for (uint256 j; j < usableNumbers.length; j++) {
            //     if (usableNumbers[j] == solution[idx]) {
            //         numberExists = true;
            //     }
            // }
            if (!numberExistence[solution[idx]]) return false; // 3+

            // if (!numberExists) {
            //     return false;
            // }
            solutionSum += solution[idx];
        }

        return solutionSum == sum;
    }

    function submitChallenge(
        int256[] memory array,
        int256 targetSum
    )
        public
        payable
        onlyOwner // 2+
    {
        require(reward == 0, "a challenge is already active");
        require(msg.value > 0, "you must send a non-zero value for the reward");
        reward = msg.value;
        usableNumbers = array;
        sum = targetSum;

        for (uint i = 0; i < array.length; i++) {
            // 3+
            numberExistence[array[i]] = true;
        }

        // 6+
        delete submittedSolution;

        emit ChallengeSubmitted(array, targetSum, msg.value); // 5+
    }

    function submitSolution(int256[] memory solution) public {
        require(reward != 0, "no challenge is currently active");
        require(
            !userSubmittedSolution(msg.sender),
            "you have already submitted a solution"
        );

        submittedSolution.push(msg.sender);
        bool success = verifySolution(solution); // 5+
        if (success) {
            unclaimedRewards[msg.sender] += reward;
            reward = 0;
            sum = 0;
            // 6+
            delete usableNumbers;
            delete numberExistence; // 3+
        }

        emit SolutionSubmitted(msg.sender, success); // 5+
    }

    function claimRewards() external {
        // 4+
        uint256 userReward = unclaimedRewards[msg.sender];
        unclaimedRewards[msg.sender] = 0;
        (bool sent, ) = payable(msg.sender).call{value: userReward}("");
        require(sent, "transfer failed");

        emit RewardsClaimed(msg.sender, userReward); // 5+
    }

    function userSubmittedSolution(address user) internal view returns (bool) {
        for (uint256 idx; idx < submittedSolution.length; idx++) {
            address currentUser = submittedSolution[idx];
            if (currentUser == user) {
                return true;
            }
        }
        return false;
    }
}
