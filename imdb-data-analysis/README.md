# IMDb Data Analysis

This project analyzes IMDb data using SQL and PostgreSQL to explore ratings, genres, title types, runtime, and actor appearances.

## Tools
- SQL
- PostgreSQL
- DataGrip

## Files
- `schema.sql` - creates the database tables
- `queries.sql` - contains analysis queries

## Questions Explored
- Which titles have the highest ratings with strong vote counts?
- Which genres have the highest average ratings?
- How do ratings vary by title type and year?
- How does runtime relate to ratings?
- Which actors appear most often in highly rated titles?

## Runtime vs Rating

It seems like longer movies tend to have higher average ratings, possibly because they give viewers more time to become immersed in the story.

![Runtime vs Rating](runtime_vs_rating.png)

## Genre Analysis

I found it interesting that certain genres had consistently higher ratings. I was also surprised by the number of votes for Western movies.

![Genre Analysis](genre_analysis.png)

## Actor Performance Analysis

Manipulated the data to find well-known actors based on their number of appearances and compare their average ratings.
![Actor Analysis](actor_analysis.png)
