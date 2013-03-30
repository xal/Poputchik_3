/**
 * User: Den Schigrov <dennytwix@gmail.com>
 * Created: 18.02.13
 *
 * Id: $Id$
 */
$(document).ready(function(){
    $('#id_category').change(function(){
        var category = $('#id_category option:selected').val();
        var subcategory = $('#id_subcategory option:selected').val();
        $.getJSON(
           '/api/products/subcategories/' + category,
            function(data){
                var options = $('#id_subcategory');
                options.find('option').remove();
                $.each(data, function() {
                    options.append($("<option />").val(this.id).text(this.title));
                });
                if (subcategory > 0){
                    $('#id_subcategory option').each(function(){
                        if ($(this).val() == subcategory){
                            $(this).attr('selected', 'selected');
                        }
                    });
                }
                $('#id_subcategory').trigger('change');
            }
        );
    });
    $('#id_subcategory').change(function(){
        var category = $('#id_category option:selected').val();
        var subcategory = $('#id_subcategory option:selected').val();
        var group = $('#id_group option:selected').val();
        $.getJSON(
            '/api/products/groups/' + category + '/' + subcategory,
            function(data){
                var options = $('#id_group');
                options.find('option').remove();
                $.each(data, function() {
                    options.append($("<option />").val(this.id).text(this.title));
                });
                if (group > 0){
                    $('#id_group option').each(function(){
                        if ($(this).val() == group){
                            $(this).attr('selected', 'selected');
                        }
                    });
                }
            }
        );
    });
    $('#id_category').trigger('change');
});