function ajax_update() {
    jQuery.ajax({url: "/update-activities", success: function(result){
      if (result == 'success') {
        jQuery("#update").text("Updated");
      }
      if(result == 'successs'){
        jQuery("#update").text("Successsss")
      }
      console.log(result)
    }});
  }