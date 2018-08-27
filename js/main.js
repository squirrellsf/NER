$(document).ready(function(){
	$("#postag").click(function(){
		$.ajax({ 
		    type: "POST", 	
			url: "http://127.0.0.1:5000/POSTagging/",
            data: JSON.stringify({
            content: $("#inputSentence").val(),
            }),
			contentType: 'application/json',
			dataType: "json",
			success: function(data){
				if (data.success) { 
					$("#analysisResult").val(data.msg);
				} else {
					$("#analysisResult").val("出现错误：" + data.msg);
				}  
			},
			error: function(jqXHR){     
			   alert("发生错误：" + jqXHR.status);  
			},     
		});
	});
});
