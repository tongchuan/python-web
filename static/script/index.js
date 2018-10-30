(function(window,$){
	$(document).ready(function(){
		$('#mySubmit').bind('click',function(){
			var key = $('#key').val();
			var content = $('#content').val()
			var data = {
				key,
				content
			}
			console.log(data)
			console.log(key,content)
			$.ajax({
				url:'/redis/set',
				type: 'POST',
				data: JSON.stringify(data),
				contentType: 'application/json',
				dataType: 'json',
				success:function(data){
					console.log(data)
				},
				error:function(xhr, msg, err){
					console.log([xhr, msg, err])
				}
			})
		})
	})
})(window, jQuery)