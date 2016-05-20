If you want copy some text into your clipboard use JavaScript, you can use [`document.execCommand('copy')`](https://developer.mozilla.org/en-US/docs/Web/API/Document/execCommand). Here's a full example:

    // add an event listener to the button `btn`
    document.getElementById('btn').addEventListener('click', event => {
        var area = document.getElementById('area');  // get the textarea element which we're going to copy
        area.select();  // select the content of the textarea
        document.execCommand('copy');  // try to copy the text
    });

HTML code:

    <p><textarea id="area">The text to copy is here.</textarea></p>
    <p><button id="btn">Copy it!</button></p>

You can also check [this Stack Overflow answer](http://stackoverflow.com/a/30810322/5299236) for more details.
