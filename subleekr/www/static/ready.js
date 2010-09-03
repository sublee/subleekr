var body = $( document.body ),
    checkTooNarrow = function() {
        var positions = [],
            categories = $( ".sites" );

        categories.each(function() {
            positions.push( $( this ).position().left );
        });

        if ( $.unique( positions ).length === 1 ) {
            body.addClass( "mobile" );
        } else {
            body.removeClass( "mobile" );
        }
    };

$( window ).resize( checkTooNarrow ).resize();

if ( body.hasClass( "mobile" ) ) {
    $( window ).scrollTop( 1 );
}

