$(document).ready(function() {
    $("select[class='location_list_dropdown']").change(function(event) {
        let text = this.options[$( ".location_list_dropdown option:selected").index()].text;
        $('.area_location_filter').hide();
        $('tr').filter(":contains('" + text + "')").show();
    });
});