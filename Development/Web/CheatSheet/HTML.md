## htmlaudio
<audio src=“Audio” controls />

## htmlbody
<body>
Body
</body>
##htmlbold
<b>Bold</b>
##htmlblockquote
<blockquote>Blockquote</blockquote>
##htmlcenter
<center>Center</center>
##htmlcheckbox
<input type=“checkbox” name=“%fill:name%” id=“%fill:name%” />
##htmlcite
<cite>%|</cite>
##htmlcode
<code>%|</code>
##htmlcomment
<!— Comment —>
##htmlcontenttype
<meta http-equiv=“content-type” content=“text/html; charset=UTF-8” />
##htmlcsslink
<link rel=“stylesheet” href=“%|” type=“text/css” media=“screen” />
##htmldd
<dd>%|</dd>
##htmldefinitionlist
<dl>
    <dt>%fill:term 01%</dt>
        <dd>%fill:definition 01%</dd>
    <dt>%fill:term 02%</dt>
        <dd>%fill:definition 02%</dd>
</dl>

%|
##htmldiv
<div class=“%|”>

</div>
##htmldoctype
<!DOCTYPE html PUBLIC “-//W3C//DTD XHTML 1.0 Transitional//EN” 
“http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd”>
##htmlemphasize
<em>%|</em>
##htmlfigcaption
<figcaption>Caption</figcaption>
##htmlfigure
Used with figcaption to implement captions under media.
<figure>Figure</figure>
##htmlfooter
<footer> </footer>
##htmlform
<form action=“%fill:action%” method=“%fill:method%”>

%|

</form>
##htmlhead
<head>

<title>%fill:title of the page%</title>

<meta name=“robots” content=“noindex,follow”>

<meta name=“description” content=“%fill:describe the contents of the page%”>

<meta name=“keywords” content=“%fill:keywords list%”>

<meta http-equiv=“Content-Type” content=“text/html; charset=UTF-8”>

</head>

%|
##htmlheader1
<h%fill:level% class=“%fill:class%”>%fill:title%</h%fill:level%>
##htmlheader2
<h2>Header</h2>
##htmlheader3
<h3>Header</h3>
##htmlhorizontalrule
<hr>
##htmlhtml
<html xmlns=“http://www.w3.org/1999/xhtml”>

%|

</html>
##htmliframe
<iframe width=“500” height=“500” src=“6.22.html” />
##htmlimage
<img src=“url” alt=image description=”description” width=“px” height=“px” border=“px” align=“px”/>
##htmljslink
<script src=“%|” type=“text/javascript” language=“javascript”></script>
##htmllabel
<label for=“%fill:id%”>%fill:Label%</label>
%|
##htmllinebreak
<br />
##htmllistitem
<li>Item</li>
##htmlmailto
<a href=“mailto:%fill:email%?subject=%fill:subject%”>%fill:link text%</a>
##htmlnav
<nav id=“%|”>



</nav>
##htmlnoscript
<noscript>%|</noscript>
##htmlorderedlist
<ol>

	<li>%fill:item 1%</li>
	<li>%fill:item 2%</li>
	<li>%fill:item 3%</li>
	<li>%fill:item 4%</li>

</ol>

%|			
##htmlparagraph
<p class=“%|”></p>
##htmlradiobutton
<input type=“radio” name=“%fill:name%” value=“%fill:value%” />
%|
##htmlresetbutton
<button type=“reset” name=“%fill:name%” id=“%fill:name%”>%fill:button text%</button>
##htmlscript
<script type=“text/javascript” language=“Javascript” src=“%|”>


</script>
##htmlselect
<select name=%fill:name%” id=%fill:name%”>
	<option value=“%fill:option1%”>%fill:option1%</option>
	<option value=“%fill:option2%”>%fill:option2%</option>
	<option value=“%fill:option3%”>%fill:option3%</option>
</select>

%|
##htmlsidebar
<sidebar id=“%|”>


</sidebar>  
##htmlspan
<span id=“%|”></span>
##htmlstrong
<strong>%|</strong>
##htmlstyle
<style type=“text/css”>

%|

</style>
##htmlsubmitbutton
<button type=“submit” name=“%fill:name%” id=“%fill:name%” >%fill:button text%</button>
##htmltable
<table border=“0”>
    <tr>
		<th>%|</th>
		<th></th>
    </tr>
    <tr>
		<td></td>
		<td></td>		
    </tr>
</table>
##htmltd
<td>%|</td>
##htmltermdefinition
<dt>%fill:term%</dt>
    <dd>%fill:definition%</dd>
%|
##htmltextarea
<textarea name=“%fill:name%” rows=“%fill:rows%” cols=“%fill:columns%”></textarea>
##htmltextfield
<input type=“text” name=“%fill:name%” value=“%fill:value%” size=“%fill:size%” />
##htmltitle
<title>%|</title>
##htmltr
<tr>%|</tr>
##htmlunderscore
<u>Underscore</u>
##htmlunorderedlist
<ul>

	<li>%fill:item 1%</li>
	<li>%fill:item 2%</li>
	<li>%fill:item 3%</li>
	<li>%fill:item 4%</li>

</ul>

%|
##htmlurl
<a href=“http://%fill:url%”>%fill:link text%</a>
##htmlvideo
<video width=“%fill:width%” height=“%fill:height%” controls=“controls”>

  <source src=“%fill:ogg%” type=“video/ogg” />
  <source src=“%fill:mp4%” type=“video/mp4” />
</video>