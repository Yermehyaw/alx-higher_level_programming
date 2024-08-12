/**
 * Translate the <header> based on user input
 */
const $ = window.$;
$(document).ready(function () {
  const lang = $('input#language_code').val();
  const url = 'https://api.cors.lol/url=' + `https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`;
  $('input#btn_translate').on('click', function () {
    $.get(url, function (response, status) {
      if (status === 'success')
        $('div#hello').text(response.hello)
    });
  });
});
