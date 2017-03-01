
$(window).load(function(){
	var pub = window.location.pathname.split('/')[3]
	$.ajax({
	  type: "GET",
	  url: "/taps_oan/yelp/"+pub+"/",
	}).done(function(res){
		var pub = res.businesses[0];
		console.log(pub)
		var cat;
		for(var i in pub.categories)
			$("#pub_description").append("<p class='pub_cat'>"+pub.categories[i].title+"</p>");
		$("#pub_price").text(pub.price);
		$("#pub_rating").text("★".repeat(pub.rating));
		$("#pub_pic").attr("src",pub.image_url)
		$("#pub_pic").css('width',"750px");
		$("#pub_rating_no").text("("+pub.review_count+")")
		var status = $("#pub_status")
		console.log(pub.is_closed)
		if(!pub.is_closed) { 
			status.text("Open");
			status.addClass('open_pub');
		}
		else
		{
			status.text("Closed");
			status.addClass('closed_pub');
		}
	})
	// $("#pub_pic").load(function(){

	// 	if($(".profile_list").height() > $("#pub_pic").height())
	// 	{
	// 		console.log("TRUE ",$(".profile_list").height() , $("#pub_pic").height())
	// 		var height = $("#pub_pic").height() - 26;
	// 		$(".profile_list").height(height+"px");
	// 	}
	// 	else
	// 		console.log("STAY");
	// })
})
