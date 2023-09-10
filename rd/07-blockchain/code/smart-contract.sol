

// Importing the ERC721 contract from the OpenZeppelin contracts library.
// OpenZeppelin contracts are pre-audited reusable components.

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

// Define our contract, ArtMarketplace, which inherits from the ERC721 contract.
contract ArtMarketplace is ERC721 {

    // This variable will increment with each new art that's minted, providing a unique ID.
    uint public artId = 0;

    // Constructor function that gets called when the contract is deployed.
    // It calls the constructor of the ERC721 contract with the name and symbol of our NFT.

    constructor() ERC721("ArtMarketplace", "ART") public {}

    // Function to mint new art.
    // This function takes a string (_tokenURI) as a parameter, which points to metadata about the art.
    // The function is public, so anyone can call it.
    
  function mintArt(string memory _tokenURI) public {
        // Calling the _mint function from the ERC721 contract to create a new NFT.
        _mint(msg.sender, artId);
  
        // Calling the _setTokenURI function from the ERC721 contract to set the metadata URI of the NFT.
        _setTokenURI(artId, _tokenURI);
     
        // Incrementing the artId for the next piece of art.
        artId++;
    }

    // Function to buy art.
    // This function takes an integer (_artId) as a parameter, which is the ID of the art to buy.
    // The function is public and payable, so it can receive Ether.
    
  function buyArt(uint _artId) public payable {
  
        // Require that the amount of Ether sent with the function call is at least 0.01.
        require(msg.value >= 0.01 ether, "Not enough ETH sent; check price!");
        
        // Transfer ownership of the NFT from the current owner to the caller of this function.
        _transfer(ownerOf(_artId), msg.sender, _artId);
    }
}



/*
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract ArtMarketplace is ERC721 {
    uint public artId = 0;

    constructor() ERC721("ArtMarketplace", "ART") public {}

    function mintArt(string memory _tokenURI) public {
        _mint(msg.sender, artId);
        _setTokenURI(artId, _tokenURI);
        artId++;
    }
    
    function buyArt(uint _artId) public payable {
        require(msg.value >= 0.01 ether, "Not enough ETH sent; check price!");
        _transfer(ownerOf(_artId), msg.sender, _artId);
    }
}

*/

