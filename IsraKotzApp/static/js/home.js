/**
 * Created by Nir on 10/17/13.
 */

$(document).ready(function() {
	//////////////
	///First Page
	/////////////
	$('#submit').click(function(){
		var destination = $('#searchBox').val();
		var dictionary = {
			"city": destination
		}
		$.ajax({
			url: "/api/budget",
			type: "POST",
			data: dictionary,
			success: function(data){
				$('.content_wrapper').html(data);
			}
		});
	});

	$("#searchBox").keyup(function(event){
		var code = event.which;
		if(code == 13){
			document.getElementById("submit").click();
		}
	});


	//////////////
	///Second Page
	/////////////

	$('#submit2').click(function(){
		var destination = $('#searchBox2').val();
		var dictionary = {
			"city": destination
		}
		$.ajax({
			url: "/api/budget",
			type: "POST",
			data: dictionary,
			success: function(data){
				$('.content_wrapper').html(data);
			}
		});
	});

	$(".category_container").click(function(){
		if(!$(this).hasClass('opened')){
			$(this).animate({height: "400px"});
			//$(".categoey_details", this).slideDown(200);
			var obj = $(this).closest(".main_container").find(".opened");
			if(obj != null){
				//$(".categoey_details", obj).slideUp(100);
				obj.animate({height: "30px"});
				obj.removeClass("opened");
				obj.closest('.categoey_details').addClass('hide');
			}
			$(this).addClass('opened');
			$(this).closest('.categoey_details').removeClass('hide');
		}
	});
});

// (function() {
// 	$('dd').filter(':nth-child(n+3)').addClass('hide');

// 	$('dl').on('click', 'dt', function() {
// 		$(this)
// 			.next()
// 				.slideDown(200)
// 				.siblings('dd')
// 					.slideUp(200);
// 	});
// })();