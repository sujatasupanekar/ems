$(document).ready(function() {
    $("select[class='location_list_dropdown']").change(function(event) {
        let text = this.options[$( ".location_list_dropdown option:selected").index()].text;
        if(text=='--Select a Location--') {
            $('.area_location_filter').show();
        } else {
            $('.area_location_filter').hide();
            $('tr').filter(":contains('" + text + "')").show();
        }
    });
});