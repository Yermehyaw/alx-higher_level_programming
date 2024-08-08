/**
 * Add, remove and delete list by clicks
 */
const $ = window.$;
$(document).ready(function () {
  const lang = $('input#language_code').content()
  url = 'https://www.fourtonfish.com/hellosalut/hello/?lang={lang}';
  $.get(url, function (response, status) {
    $('input#btn_translate').on('click', function () {
      if (status === 'success')
	$('div#hello').text(response.hello)
    });
  });
});
