var CryptoJs = require("crypto-js");
var pry = "22XsF8ZJdQWcTjbF";
// function getpry(l) {
//     l = l || 32;
//     for (var n = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678", t = n.length, e = "", a = 0; a < l; a++)
//         e += n.charAt(Math.floor(Math.random() * t));
//     return e
// }
function decode(l) {
    var n = CryptoJs.enc.Base64.parse(l)
      // , zxc = CryptoJs.enc.Base64.stringify(l)
        // 接口数据的解密的秘钥   5P37dwCSkKAwra2n
        // 访问接口参数的秘钥     GxffjB3S5iitMG3j
      , t = CryptoJs.enc.Utf8.parse(pry)
      , e = CryptoJs.enc.Utf8.parse(pry)
      , a = CryptoJs.lib.CipherParams.create({
        ciphertext: n
    });
    return xxx = CryptoJs.AES.decrypt(a, t, {
        iv: e,
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    }).toString(CryptoJs.enc.Utf8)
    // var decryptedData = JSON.parse(xxx);
    // return decryptedData
}

function get_data(data){
     var n = data.replace(/[\r\n]/g, "")
      , t = decode(n);
    return t
}
function encode(l) {
    var n = CryptoJs.enc.Utf8.parse(pry)
      , t = CryptoJs.enc.Utf8.parse(pry)
      , e = CryptoJs.enc.Utf8.parse(l)
      , a = CryptoJs.AES.encrypt(e, n, {
        iv: t,
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    });
    return CryptoJs.enc.Base64.stringify(a.ciphertext)
}
function get_canshu(data){
    var m = encode(data)
    return m
}

