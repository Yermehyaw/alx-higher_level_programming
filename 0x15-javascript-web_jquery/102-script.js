/**
 * Translate the <header> based on user input
 *
 * NOTE: 'https://www.fourtonfish.com/hellosalut/hello/' has been permanently
 * moved to 'https://hellosalut.stefanbohacek.dev/'
 * Try https://www.fourtonfish.com/hellosalut/hello/lang=fr to see the broken
 * webpage
 */
const $ = window.$;
$(document).ready(function () {
  const proxy = `https://api.cors.lol/url=`;
  $('input#btn_translate').on('click', function () {
    const lang = $('input#language_code').val();
    const url = `${proxy}https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
    $.get(url, function (response, status) {
      if (status === 'success')
        $('div#hello').text(response.hello)
    });
  });
});
