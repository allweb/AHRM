function process(ahrm_action) {
    document.forms[0].action = ahrm_action;
    document.forms[0].submit();
}

function openPopup(url) {
	//window.open(url,'popup','height=515,width=800,toolbar=no,status=no,scrollbars=yes,location=no,menubars=no,directories=no,resizable=no');
	
	//return false;
	
	 WindowObjectReference = window.open("/about_ahrm", "DescriptiveWindowName", "height=515,width=800,resizable=no,scrollbars=yes,status=yes");
	
    
}