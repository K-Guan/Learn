If you're trying to find a way to use `$(document).ready` but without jQuery,  you can just use [`DOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Web/Events/DOMContentLoaded).

For example:

```javascript
document.addEventListener("DOMContentLoaded", function(event) { 
    console.log('The DOM content has been loaded')
});
```

You can also use [`window.onload`](https://developer.mozilla.org/en-US/docs/Web/API/GlobalEventHandlers/onload) instead, just like below:

```javascript
window.onload = function() {
    console.log('Everything has been loaded')
};
```

The difference between them is:


> `window.onload`: Fires at the end of the document loading process. At this point, all of the objects in the document are in the DOM, and all the images, scripts, links and sub-frames have finished loading.
>
> `DOMContentLoaded`: Fired after the DOM for the page has been constructed, but do not wait for other resources to finish loading.


For more details, check [this answer on Stack Overflow](http://stackoverflow.com/a/800010/5299236) and the links above.
