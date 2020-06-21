
var tag = document.createElement('h2')
const text = document.createTextNode("The javscript link works")
tag.appendChild(text)

var page_content = document.getElementById('content')
page_content.appendChild(tag)
