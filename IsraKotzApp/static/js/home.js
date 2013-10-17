/**
 * Created by Nir on 10/17/13.
 */
$(document).ready(function() {
   $(".category_container").click(function(){
       $(this).animate({height: "200px"});
        $(".table_container", this).show();
   });
});