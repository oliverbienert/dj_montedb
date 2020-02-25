django.jQuery( function() {
    django.jQuery(".hasDatepicker").datepicker('option', 'changeYear', true);
    django.jQuery(".hasDatepicker").datepicker('option', 'yearRange', '-100:+0');
    var language_code = django.jQuery('html').attr('lang');
    django.jQuery(".hasDatepicker").datepicker('option', django.jQuery.datepicker.regional[language_code]);
});