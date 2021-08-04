-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name != "Comedy" OR tv_show_genres.show_id IS NULL
GROUP BY tv_shows.title
ORDER BY title ASC;