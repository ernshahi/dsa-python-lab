# Recommendation System Infra Basics

1. What do users want?
2. How can we scale?

Scenarios:
- we have millions of users and billions of videos(items)

## 1. Black box ML/AI approach:
- we train a model on a large dataset and use it to recommend videos to users.
- We pass user and vides to the model and it returns scores for each video.
- We then sort the videos by the scores and return the top N videos to the user.
- It takes several milliseconds to score a video.

- For billions of videos, it's not feasible to score all videos for each user. It will take too much time and resources. Which is why we need to use a more efficient approach.
- Even if we take scroing in the background, it will still take too much time and resources. which is not feasible as it takes to much resources to score all videos for each user.




## Dead Simple Recommendation System:
- Take top videos on the platform and feeds those to the user on a loop. That still how radio works today. 
- We can do bit better by using Candidate Generation and Ranking to get the top videos for the user.



## Candidate Generation -> Ranking -> Re-ranking
- Candidate Generation:
  - We generate a list of videos that are likely to be relevant to the user based on the user's history and the videos' metadata. like:
  - Channels I'm subscribed to
  - Top Vides on the platform

- It takes candidates and users to the system and returns list of relavenet candidates for the user. which is likely to be watched by the user.

- For candidates like Videos similar to the one I just liked, Videos watched by users who are similar to me, etc.
- We can do this by basic databse queries by creating embeddings or vector of videos and storing them in the database. and then use cosine similarity to find similar videos.
- Vector DBs like Pinecone, Qdrant, etc. can be used to store and query the vectors. These are optimized for similarity search like finding nearest neighbors.

- Re-Ranking:
- Exploration and Exploitation:
    - We recommend videos that are not yet watched by the user.
    - We might not recommned which are blocked by the users or they might be sensitive content. 