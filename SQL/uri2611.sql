"""
Created on Tue Jan  4 22:14:12 2022

@author: camila

Action Movies

A video store contractor hired her services to catalog her movies. They need you to select the code and the name of the movies whose description of the genre is 'Action'.
"""

SELECT 
    movies.id,
    movies.name
FROM movies
JOIN genres ON genres.id = movies.id_genres
WHERE genres.description = 'Action';