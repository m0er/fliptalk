(function ($, undefined) {
    $.fn.flip = function (options) {
        return this.each(function(index) {
            var opts = $.extend({}, $.fn.flip.defaults, options),
            	$this = $(this),
            	$target = $(opts.target),
            	$front = $target.find('.front'),
            	$back = $target.find('.back');
            
            $this.click(function(e) {
            	e.preventDefault();
            	
            	$target.toggleClass('flipped');
            	
            	if ($target.hasClass('flipped')) {
            		setTimeout(function() {
            			$back.toggleClass('hide');
            			$front.toggleClass('hide');
            		}, 320); // 5000:1600
            		setTimeout(function() {
            			jsPlumb.ready(function() {
            				jsPlumb.endpointClass = "endpoint";
            				jsPlumb.connectorClass = "connector";
            				
            				var offsetY = 0,
	            				stateMachineConnectorToRight = {
	        						connector:"StateMachine",
	        						detachable:false,
	        						paintStyle: {lineWidth: 2, strokeStyle:"#ED9E34"},
	            					overlays:[ ["PlainArrow", {location:1, width:15, length:12} ]],
	        						endpoint:"Blank",
	        						// RightMiddle + offset
	        						anchors:[[1, 0.5, 0, 0, 0, offsetY - 10], "LeftMiddle"]
	            				}, stateMachineConnectorToLeft = {
	        						connector:"StateMachine",
	        						detachable:false,
	        						paintStyle: {lineWidth: 2, strokeStyle:"#3175C0"},
	            					overlays:[ ["PlainArrow", {location:1, width:15, length:12} ]],
	        						endpoint:"Blank",
	        						anchors:["LeftMiddle", "RightMiddle"]
	                			};
            				
            				jsPlumb.connect({
            					source: 'context0agree0',
            					target: 'context0disagree0',
            					container: $('#flipTalkComment .comments').first()
            				}, stateMachineConnectorToRight);
            				
            				offsetY = offsetY + 10;
            				stateMachineConnectorToRight.anchors[0][5] = offsetY;
            				
            				jsPlumb.connect({
            					source: 'context0agree0',
            					target: 'context0disagree1',
            					container: $('#flipTalkComment .comments').first()
            				}, stateMachineConnectorToRight);
            				
            				jsPlumb.connect({
            					source: 'context0disagree0',
            					target: 'context0agree1',
            					container: $('#flipTalkComment .comments').first()
            				}, stateMachineConnectorToLeft);
            			});
            		}, 800); // 1000 : 800
            	} else {
            		setTimeout(function() {
            			$front.toggleClass('hide');
            			$back.toggleClass('hide');
            		}, 320);
            	}
            });
        });
    };
    
    $.fn.flip.defaults = {
    	target: null
    };
})(jQuery);

$(document).ready(function() {
	
	$('#agree, #disagree').flip({
		target: $('#flipTalkComment')
	});
	
	$('#flipTalkContent .flip-content-icon').flip({
		target: $('#flipTalkContent')
	});
	
	$('.comment').each(function() {
		var $this = $(this);
		
		$this.find('.flip-content-icon').flip({
			target: $this
		});
	});
	
	$('.dial').knob({
		readOnly: true
	});
});