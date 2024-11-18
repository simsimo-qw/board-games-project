# board-games-project #
Analyzing and ranking board games based on user ratings and reviews from BoardGameGeek

### Introduction ###
This project analyzes datasets containing millions of board game reviews and user comments to generate meaningful insights and rankings. The main objective is to rank games based on user liking while ensuring the reliability of the rankings. A simple average rating is insufficient for trustworthy analysis, as it can be biased by low-rating games with minimal votes. To address this, we implement a Bayesian average function, which accounts for the number of votes and the global average rating.

In addition, we perform a deeper analysis by examining the number of comments for each game. By comparing the number of votes to the number of comments, we explore whether reviews significantly impact the likability of a game and determine if these factors are correlated.

