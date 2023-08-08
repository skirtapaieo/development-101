# Netflix - streaming services

# Initial questions/thoughts

# Other experience

- Spotify design (reusable?)
- Digital TV broadcast (STB-applications)

# Core design

- Use cases
- Information model
- Services/APIs
- Examples
- Sequence diagrams

## From Spotify design

### Services

1. User management
2. Music metadata management
3. Music/Podcast audio management
4. Search service
5. Music streaming service
6. Recommendation service
7. Analytics service

### Music streaming is central

Music streaming is a critical feature for an application like Spotify, and it needs to be highly efficient to provide a smooth user experience. There are several aspects to consider:

1. **Audio File Compression:** The raw audio files are large, so they're compressed to make them more manageable for streaming. Spotify uses Ogg Vorbis and AAC for audio compression. The streaming quality can be adjusted based on the user's preference and network condition.

2. **Content Delivery Network (CDN):** Spotify uses a CDN to deliver music streams to users. A CDN is a network of servers distributed across various locations around the world. When a user requests a song, it is served from the nearest server in the CDN. This reduces the latency and improves the streaming experience. AWS CloudFront could be an example of a CDN in an AWS-based architecture.

3. **Caching:** Frequently accessed songs can be cached at various levels (CDN, Spotify backend servers, user's device) to reduce the load on the servers and decrease the latency.

4. **Adaptive Streaming:** The streaming quality can be dynamically adjusted based on the network condition. If the network is slow, the server can switch to a lower bitrate stream to avoid buffering. This requires encoding the song in multiple bitrates and switching between them as needed.

5. **Pre-fetching:** Spotify uses a technique called pre-fetching where it predicts the next song the user is likely to play (like the next song in the playlist) and starts buffering it in advance. This reduces the perceived latency when the song is actually played.

6. **Load Balancing:** Load balancers are used to distribute the network traffic evenly across multiple servers. This helps in efficiently handling large numbers of concurrent streaming requests.

7. **Fault Tolerance and Redundancy:** The system should be designed to be fault-tolerant and have redundancies in place. If one server or data center fails, the requests should automatically be routed to another healthy server or data center.

8. **Offline Playback:** Spotify also allows users to download songs for offline playback. This helps in situations where the network connection is slow or unavailable.

These are some of the techniques to manage highly efficient music streaming. It's a complex problem involving various trade-offs, and the actual implementation may vary based on the specific needs and constraints.

# Architecture

## Front-end

## Back-end

## Data (pipeline)

## Infrastructure

## Additional

- Security
- Protocols
- Algorithms
