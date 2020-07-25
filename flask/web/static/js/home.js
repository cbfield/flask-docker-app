var page_content = document.getElementById('content')
var tag = document.createElement('h2')
var text = document.createTextNode("Javascreept")

tag.appendChild(text)
tag.className += " text-light p-3"
page_content.appendChild(tag)
