// ==UserScript==
// @name         SO link to JavaScript tag
// @namespace    https://stackoverflow.com/users/5299236/kevin-guan
// @author       Kevin
// @description  Change the link of Stack Overflow main logo.
// @version      0.1
// @include      /^https?:\/\/\w*.?stackoverflow.com\/.*/
// @require      https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.6.15/browser-polyfill.min.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.6.15/browser.min.js
// ==/UserScript==

/* jshint ignore:start */
var inline_src = (<><![CDATA[
/* jshint ignore:end */
/* jshint esnext: true */

const logo = document.getElementById('hlogo');
logo.getElementsByTagName('a')[0].href = 'https://stackoverflow.com/questions/tagged/javascript';


/* jshint ignore:start */
]]></>).toString();
var c = babel.transform(inline_src);
eval(c.code);
/* jshint ignore:end */
