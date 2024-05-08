$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    const greet = data.hello;
    $('#hello').text(greet);
  });
});
