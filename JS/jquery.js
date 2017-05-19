$('.open').click(function() {
    $("#panel").animate({
        width: 'toggle'
    }, 300);
});

$(function() {
  $('#hidetest').click(function() {
    $('.hidetest').hide();
  });
});
