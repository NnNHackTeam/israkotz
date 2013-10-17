/**
 * Created by Nir on 10/17/13.
 */

// $(document).ready(function() {
// 	$(".category_container").click(function(){
// 		if(!$(this).hasClass('opened')){
// 			$(this).animate({height: "200px"});
// 			$(".table_container", this).slideDown(200);
// 			var obj = $(this).closest(".main_container").find(".opened");
// 			if(obj != null){
// 				$(".table_container", obj).slideUp(100);
// 				obj.animate({height: "30px"});
// 				obj.removeClass("opened");
// 			}
// 			$(this).addClass('opened');
// 		}
// 	});
// });

$(document).ready(function() {
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
		if(event.keyCode == 13){
			$("#submit").click();
		}
	});
});