var logo = $( "h1 img" ),
    duration = window.DURATION || 70,
    maskSize = {
        x: 80,
        y: 110
    },
    textureSize = {
        x: 640,
        y: 480
    };

function rand(min, max) {
    return Math.round(Math.random() * (max - min) + min);
}

function blaze() {
    var position = {
        x: rand( 0, textureSize.x - maskSize.x ),
        y: rand( 0, textureSize.y - maskSize.y )
    };
    logo.css({
        backgroundPosition: "-" + position.x + "px -" + position.y + "px"
    });
}

/*
$( "<img />", {
    src: "/static/texture.jpg",
    css: {
        visibility: "hidden",
        position: "absolute",
        top: -9999
    }
}).load(function() {
    $( this ).remove();
}).appendTo( document.body );
*/

if ( $.browser.msie && $.browser.version < 7 ) {
    document.execCommand( "BackgroundImageCache", false, true );
    var src = logo.attr( "src" ),
        filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(" +
                 'src="' + src + '", sizingMethod="scale")';
    logo.attr( "src", "/static/transparent.gif" );
    logo.css( "filter", filter );
}

setInterval( blaze, duration );
