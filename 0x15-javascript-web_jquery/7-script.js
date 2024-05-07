$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (chars) {
      const charName = chars.name;

      $('#character').text(charName);
    });
});
