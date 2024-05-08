$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;

    movies.forEach(function (movie) {
      const movieItem = $('<li>').text(movie.title);

      $('#list_movies').append(movieItem);
    });
  });
});
