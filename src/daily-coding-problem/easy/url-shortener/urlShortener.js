/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

- shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
- restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?

*/

function shortenUrl(len) {
  if (typeof len !== "number") {
    return null;
  }
  const originalUrls = {};
  const options =
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  const shortenedLength = len;
  function generateShortUrl() {
    let shortened = "";
    for (let i = 0; i < shortenedLength; i++) {
      const choice = Math.floor(Math.random() * options.length);
      shortened += options[choice];
    }
    return shortened;
  }
  function shorten(url) {
    if (typeof url !== "string") {
      return null;
    }
    let final = null;
    while (!final) {
      const result = generateShortUrl(shortenedLength);
      if (!originalUrls[result]) {
        originalUrls[result] = url;
        final = result;
      }
    }
    return final;
  }
  function restore(shortenedUrl) {
    if (typeof shortenedUrl !== "string") {
      return null;
    }
    const originalUrl = originalUrls[shortenedUrl];
    if (!originalUrl) {
      return null;
    }
    return originalUrl;
  }
  return [shorten, restore];
}

module.exports = shortenUrl;
