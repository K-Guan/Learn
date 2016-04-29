chrome.webRequest.onBeforeRequest.addListener(function(details) {

    if (details.url.endsWith('.srt') || details.url.endsWith('.flv')) {
        console.log(details.url);
        window.open(details.url + '?');
    }

}, { urls: ['*://mov.bn.netease.com/*',
            '*://oc-caption-srt.nos.netease.com/*'] });
