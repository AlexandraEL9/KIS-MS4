// Polyfill for TextEncoder in Node.js
const { TextEncoder, TextDecoder } = require('util');
const $ = require('jquery');
global.$ = global.jQuery = $;
global.TextEncoder = TextEncoder;
global.TextDecoder = TextDecoder;
