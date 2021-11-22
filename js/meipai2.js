// var decodeMp4 = this;
var h = "substring"
      , i = "split"
      , j = "replace"
      , k = "substr";
function base64_decode(a) {
        var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
        if (a = a.replace(/=+$/, ""),
        a.length % 4 == 1)
            throw f;
        for (var b, c, d = 0, g = 0, h = ""; c = a.charAt(g++); ~c && (b = d % 4 ? 64 * b + c : c,
        d++ % 4) ? h += String.fromCharCode(255 & b >> (-2 * d & 6)) : 0)
            c = e.indexOf(c);
        return h
    };
    decodeMp4 = {
        getHex: function(a) {
            return {
                str: a[h](4),
                hex: a[h](0, 4)[i]("").reverse().join("")
            }
        },
        getDec: function(a) {
            var b = parseInt(a, 16).toString();
            return {
                pre: b[h](0, 2)[i](""),
                tail: b[h](2)[i]("")
            }
        },
        substr: function(a, b) {
            var c = a[h](0, b[0])
              , d = a[k](b[0], b[1]);
            return c + a[h](b[0])[j](d, "")
        },
        getPos: function(a, b) {
            return b[0] = a.length - b[0] - b[1],
            b
        },

        decode: function(a) {
            var b = this.getHex(a)
              , c = this.getDec(b.hex)
              , d = this[k](b.str, c.pre);
            return base64_decode(this[k](d, this.getPos(d, c.tail)))
        }
    };
    function get_mp4(){
    var a = "2f60LeQYWbpZy9tdnZpZGVvMTAubWVpdHVkYXRhLmNvbS82MTdjZWEwMTk0Yjk2bmxidHJ1MDczNDI0NJEod6UzFi5tcDQ=";
    return decodeMp4.decode(a)
}