-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
    -- each record displays: <TV Show genre> - <Number of shows linked to this genre>.
    -- first column is called 'genre'.
    -- second column is called 'number_of_shows'.
    -- don’t displays a genre that doesn’t have any shows linked.
    -- results sorted in descending order by the number of shows linked.
SELECT tv_genres.name AS "genre", COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_show_genres INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
