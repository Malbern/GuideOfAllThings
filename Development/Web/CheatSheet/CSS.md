##cssaselector
a:link {
  color: %fill:lcolor%;
  text-decoration: %fill:ldec%;
}

a:visited {
  color: %fill:vcolor%;
  text-decoration: %fill:vdecoration%;
}

a:hover a:focus {
  color: %fill:hcolor% ;
  text-decoration: %fill:hdecoration%;
}

a:active {
  color: %fill:acolor%;
  text-decoration: %fill:adecoration%;
}

%|
##cssbackground
background: %fill:color% %fill:image% %fill:repeat% %fill:attachment% %fill:position%;
##cssbordercolor
border-color: %|;
##cssborder
border: %fill:top% %fill:right% %fill:bottom% %fill:left%;
##cssstyle
border-style: %|;
##csswidth
border-width: %|;
##cssclass
.%| {

}
##csscomment
/*%|*/
##cssfont
font-family: %fill:family% ;
  font-size: %fill:size% ;
  font-style: %fill:style% ;
  font-weight: %fill:weight% ;
  font-variant: %fill:variant% ;

%|
##cssid
 #%| {

}
##cssmargin
margin: %fill:top% %fill:right% %fill:bottom% %fill:left%;
##csspadding
padding: %fill:top% %fill:right% %fill:bottom% %fill:left%;
##cssselector
%| {

}
##cssspacing
line-height: %fill:line height% ;
   word-spacing: %fill:word spacing% ;
   letter-spacing: %fill:letter spacing% ;

%|
##csstext
text-align: %fill:align% ;
  text-decoration: %fill:decoration% ;
  text-indent: %fill:indent% ;
  text-transform: %fill:transform% ;
  text-shadow: %fill:shadow%;