# Online Community - Reddit API (algoexpert excercise)

## Initial questions

- Design the Reddit API - main objects are User and SubReddit
- MAke post, comment, voting on posts is core

## Other experience

Not a lot of recent experiences

- Slussen (CMS+tools)
- Skandia (CMS+more tools)
- Spray.se/Ekonomi (even more tools)

## Core Design

The core design is the "subreddits", that are based on posts, comments, votes (down/up), sharing, report the posts, moderation

### Initial thoughts

Sure, I'll provide an outline for a simple content management system (CMS) that would allow users to make posts, comment on posts, and vote on posts, similar to the functionality offered by Reddit. This is quite a complex topic and we would normally involve a team of designers, UX researchers, and developers to create such a system, but for this exercise, I'll simplify it as much as possible.

**1. Making a Post:**

We'll need an interface that allows users to create new posts. This could include:

a) **Post Creation Page:** A simple, user-friendly interface that contains an input field for the post title, a text box for the post content, and an optional field for attaching media files (images, videos, links, etc.).

b) **Post Type Options:** Allow users to select the type of their post, such as text, link, image, or video. This will change the available fields accordingly.

c) **Subreddit Selection:** Users should be able to select or type in the subreddit they want to post in.

d) **Preview and Post Buttons:** Users should be able to preview their post before submitting and then a button to submit the post.

e) **Drafts Functionality:** Users can save their work as drafts and come back to it later.

**2. Commenting on a Post:**

The commenting system should allow for nested comments, enabling users to reply directly to others' comments. Here's what we'll need:

a) **Comment Input Field:** Each post will have a text box under it where users can write and submit comments.

b) **Nested Comments:** To allow for conversations and discussions, each comment should also have a reply button, that when clicked, opens another comment input field right below that comment.

c) **Comment Sorting:** Allow users to sort comments by top, new, controversial, old, etc.

d) **Editing and Deleting Comments:** Users should be able to edit or delete their own comments.

**3. Voting on a Post:**

Voting is a crucial feature of Reddit-like platforms, as it allows the community to self-moderate and promotes quality content. For this, we need:

a) **Upvote and Downvote Buttons:** Each post and comment should have an upvote and downvote button next to it.

b) **Vote Count Display:** The number of votes (upvotes - downvotes) should be displayed between the upvote and downvote buttons.

c) **Vote Persistence:** Users' votes need to be remembered and displayed correctly if they navigate away and then return to the page.

d) **Sorting by Votes:** Allow users to sort posts by votes (hot, top, new, etc.).

Note that this is a simplified version of what would be required. In practice, many more features would be needed, such as user authentication and management, spam prevention, moderation tools, a search function, personalized feeds, etc. Additionally, design should be informed by user research, usability testing, and iterative design processes to ensure it meets user needs.

### Services and API's

Sure, let's represent these details in a tabular form for better readability.

| **Service**        | **API Endpoints**                                                                                                                                                                                                                                                                                                                                | **Model**                                                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| User Management    | `POST /users` Create a new user<br>`GET /users/{userId}` Retrieve details of a specific user<br>`PUT /users/{userId}` Update user information                                                                                                                                                                                                    | User: `{userId, username, passwordHash, email, joinDate, profileImageURL, etc.}`                                               |
| Post Management    | `POST /posts` Create a new post<br>`GET /posts/{postId}` Retrieve a specific post<br>`PUT /posts/{postId}` Update a post<br>`DELETE /posts/{postId}` Delete a post<br>`GET /posts` List all posts, with filters for sorting (new, hot, top), time range, and subreddit                                                                           | Post: `{postId, userId, subredditId, title, content, contentType (text/image/link/video), postDate, imageUrl, videoUrl, etc.}` |
| Comment Management | `POST /posts/{postId}/comments` Add a new comment to a post<br>`GET /posts/{postId}/comments` Retrieve all comments for a post, with filters for sorting (new, top, controversial)<br>`GET /comments/{commentId}` Retrieve a specific comment<br>`PUT /comments/{commentId}` Update a comment<br>`DELETE /comments/{commentId}` Delete a comment | Comment: `{commentId, userId, postId, parentCommentId (for nested comments), text, commentDate}`                               |
| Vote Management    | `POST /votes` Create a new vote (could be on a post or comment)<br>`DELETE /votes/{voteId}` Delete a vote                                                                                                                                                                                                                                        | Vote: `{voteId, userId, postId (null if vote is on a comment), commentId (null if vote is on a post), voteType (up/down)}`     |

Again, remember that this is a simplified model and a real-world application would have more comprehensive and complex structures for handling various functionalities and scenarios.

### Adding awards

Certainly, here is the additional service to manage awards:

| **Service**      | **API Endpoints**                                                                                                                                                                                                                                                          | **Model**                                                                                                         |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Award Management | `POST /awards` Create a new award<br>`GET /awards/{awardId}` Retrieve details of a specific award<br>`DELETE /awards/{awardId}` Delete an award<br>`GET /users/{userId}/awards` Retrieve all awards given by a user<br>`POST /users/{userId}/awards` User purchases awards | Award: `{awardId, userId, postId, commentId, awardType, awardDate}`<br>UserAward: `{userId, awardType, quantity}` |

The `Award` model has `postId` and `commentId` which are null if the award is not yet given to a post or comment. `awardType` is the type of award the user has purchased or given to a post or comment.

The `UserAward` model is used to track the awards purchased by the user. It has `awardType` which is the type of award the user has purchased and `quantity` which is the number of such awards the user has.

Here are the additional endpoints explained:

- `POST /awards`: User gives an award to a post or comment. The request body should include the postId/commentId and awardType.
- `GET /awards/{awardId}`: Retrieve the details of a specific award given by a user. The awardId is the unique identifier of the award.
- `DELETE /awards/{awardId}`: Revoke an award given by a user. This might not be commonly used, but is included for completeness.
- `GET /users/{userId}/awards`: Retrieve all the awards purchased by a user.
- `POST /users/{userId}/awards`: User purchases awards. The request body should include the awardType and quantity.

Again, this is a simplified model and additional considerations should be made in a real-world scenario, such as transaction management for purchasing awards, notifications for receiving awards, etc.

## Architecture

### Front-end

### Back-end

### Data Pipeline

### Infrastructure

### Algorithms
