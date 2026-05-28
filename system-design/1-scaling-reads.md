# Scaling Reads
- Most application read to write ratio is 10:1, but content read heary system link youtube, instagram, twitter etc. it's 100:1 or even 1000:1 ratio.

- And, databse struggels in this heavy read load, disk IO has physical limit. Even we use SSD we eventually hit situation where can't pull more data from a signle machine. 

- It's one of tha common system desing problem.

- Solution:
  - Optimize read performance whitin your database(indexing & demornaliztion)
  - Scale your database horizontallly(read replicas and/or sharding)
  - Add external caching layers(application and/or CDN)


1.1 Indexing
  - Without indexing databse do full table scan, so we have to avoid this. 
  - Index makes write slow but modern db hanldes it really really well/efficiently. So many peoples do under indexing in many application instead of over indexing. Under indexing is much larger problem then over indexing. 

1.2 Vertical Scaling
  - Use larger maching: 8GB(db.m6g.large) to 16TB(db.r6g.4xlarger) but make sure it's under devices limit like IO limit.

1.3 Denormalization
  - We do normaliztion to avoid avoid duplication, but it adds overhead on join, and if there we have lots of read it can be slwower. So denormalization can help on this. 
  - Saving realated data in one table only, but it adds write complexity as we need to update same data in multiplaces(rows).

2 Horizontal Scalling
2.1 Read Replicas
- Read replicas copy data from primary database(Leader) to additional DB(Followers). All writes goes to Primary and read to to any of replicas. 
- If primary DB goes down one of the replicas promote to primary DB

2.2 Sharding
- Read replicas works well if all of the data fits in one database, but it dataset grown so big even well indexed query becomes slow or sinlge machine can't store all of the data in disk, then need to go for sharding.
- It split data into multiple databases like posts in one DB, Uses into another etc.. so single db desn't need to server all the data. It makes query faster as it need to look up less data even for indexed table, read get distrubuted across multiple shards.
- Functional Sharding: split data as per features, all posts in one, all users in another etc
- Split a sinlge large table into multiple DB using shard key like user_id or post_id, each shard hold slice of data. And, the app use shard key to decide which DB to query.  The right approach totaly depends on query pattern. 
- In case of read sharing it adds lot of complexity, we need to manage shard map, rebalance data in case of new shard added or removed, cross shard query, so coordinating mandy DB takes lot of work. So its adopted as last resort. But in case common in write, as typically we don't have that many options. 
- So it your only limitation is read throughput, and datasize is still reasonable go for read replicas or caching, avoid sharing unless it's truly needed. 

3.1 Caching
- Caching gives far better results as compared to read replicas and shard in read heady systems. 
- As most application have higly skewed access patter like in twitter most people read trending tweets which doesn't change on every requests.
- It stores those hot results in memory and which gives in O(1)
- Application cache: like redish, memechece check cache first if not fallback to DB
- CDN: Content Delivery Network, which is spread across the world. Originally it was used for static contents like photos, videos, js etc. Modern CDN can cache dynamic content like api response, some database queries etc(they border usage)
- So it remove a lot of latency by removing round trip to another part of globe. 
- As it read from closese CDN from the client.

- It comes with it's own tradeoff, you have to manage cache invalidation across all those multiple location, that can be complex.



# Common Deep Dive
## What happens when your queries start taking londer as your dataset grows? 
-- Before: full table scan
SELECT * from users WHERE email = 'user@example.com';

-- Add index
CREATE INDEX idx_users_email on users(email);

-- After: Index scan
SELECT * from users WHERE email = 'user@example.com';


-- Explain 
EXPLAIN SELECT * from users WHERE email = 'user@example.com';
it shows all of the rows scaned, so we can see how many steps perfomred?
