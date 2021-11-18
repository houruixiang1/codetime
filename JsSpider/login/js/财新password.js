var Cr = require("crypto-js");
function encode(t) {
    var e = Cr.enc.Utf8.parse("G3JH98Y8MY9GWKWG")
      , a = Cr.enc.Utf8.parse(t)
      , A = Cr.AES.encrypt(a, e, {
        mode: Cr.mode.ECB,
        padding: Cr.pad.Pkcs7
    });
    return encodeURIComponent(A.toString())
}
function d(t) {
    var xx = encode(t)
    return encodeURIComponent(xx)
}