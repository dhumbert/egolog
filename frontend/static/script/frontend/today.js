function onLoad() {
    loadQuote();
}

function loadQuote() {
    jQuery.getJSON(quoteAjaxUrl, function(data) {
        if (data) {
            jQuery('#quote-text').text(data.text);
            jQuery('#quote-cite-author').text(data.author);

            if (data.source) {
                jQuery('#quote-cite-source').text(', ' + data.source);
            }

            jQuery("#quote").fadeIn(1000);
        }
    });
}


jQuery(document).ready(onLoad);