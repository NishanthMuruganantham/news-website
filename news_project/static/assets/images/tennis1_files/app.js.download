! function(e) {
    function t(i) {
        if (n[i]) return n[i].exports;
        var o = n[i] = {
            i: i,
            l: !1,
            exports: {}
        };
        return e[i].call(o.exports, o, o.exports, t), o.l = !0, o.exports
    }
    var n = {};
    t.m = e, t.c = n, t.d = function(e, n, i) {
        t.o(e, n) || Object.defineProperty(e, n, {
            configurable: !1,
            enumerable: !0,
            get: i
        })
    }, t.n = function(e) {
        var n = e && e.__esModule ? function() {
            return e.default
        } : function() {
            return e
        };
        return t.d(n, "a", n), n
    }, t.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }, t.p = "", t(t.s = 0)
}({
    0: function(e, t, n) {
        n("sV/x"), e.exports = n("xZZD")
    },
    OF5A: function(e, t, n) {
        var i, o;
        ! function(t, n) {
            "object" == typeof e && "object" == typeof e.exports ? e.exports = t.document ? n(t, !0) : function(e) {
                if (!e.document) throw new Error("jQuery requires a window with a document");
                return n(e)
            } : n(t)
        }("undefined" != typeof window ? window : this, function(r, a) {
            function s(e) {
                var t = !!e && "length" in e && e.length,
                    n = ue.type(e);
                return "function" !== n && !ue.isWindow(e) && ("array" === n || 0 === t || "number" == typeof t && t > 0 && t - 1 in e)
            }

            function l(e, t, n) {
                if (ue.isFunction(t)) return ue.grep(e, function(e, i) {
                    return !!t.call(e, i, e) !== n
                });
                if (t.nodeType) return ue.grep(e, function(e) {
                    return e === t !== n
                });
                if ("string" == typeof t) {
                    if (xe.test(t)) return ue.filter(t, e, n);
                    t = ue.filter(t, e)
                }
                return ue.grep(e, function(e) {
                    return oe.call(t, e) > -1 !== n
                })
            }

            function c(e, t) {
                for (;
                    (e = e[t]) && 1 !== e.nodeType;);
                return e
            }

            function u(e) {
                var t = {};
                return ue.each(e.match(Te) || [], function(e, n) {
                    t[n] = !0
                }), t
            }

            function d() {
                ee.removeEventListener("DOMContentLoaded", d), r.removeEventListener("load", d), ue.ready()
            }

            function f() {
                this.expando = ue.expando + f.uid++
            }

            function p(e, t, n) {
                var i;
                if (void 0 === n && 1 === e.nodeType)
                    if (i = "data-" + t.replace(qe, "-$&").toLowerCase(), "string" == typeof(n = e.getAttribute(i))) {
                        try {
                            n = "true" === n || "false" !== n && ("null" === n ? null : +n + "" === n ? +n : je.test(n) ? ue.parseJSON(n) : n)
                        } catch (e) {}
                        Fe.set(e, t, n)
                    } else n = void 0;
                return n
            }

            function h(e, t, n, i) {
                var o, r = 1,
                    a = 20,
                    s = i ? function() {
                        return i.cur()
                    } : function() {
                        return ue.css(e, t, "")
                    },
                    l = s(),
                    c = n && n[3] || (ue.cssNumber[t] ? "" : "px"),
                    u = (ue.cssNumber[t] || "px" !== c && +l) && Ne.exec(ue.css(e, t));
                if (u && u[3] !== c) {
                    c = c || u[3], n = n || [], u = +l || 1;
                    do {
                        r = r || ".5", u /= r, ue.style(e, t, u + c)
                    } while (r !== (r = s() / l) && 1 !== r && --a)
                }
                return n && (u = +u || +l || 0, o = n[1] ? u + (n[1] + 1) * n[2] : +n[2], i && (i.unit = c, i.start = u, i.end = o)), o
            }

            function m(e, t) {
                var n = void 0 !== e.getElementsByTagName ? e.getElementsByTagName(t || "*") : void 0 !== e.querySelectorAll ? e.querySelectorAll(t || "*") : [];
                return void 0 === t || t && ue.nodeName(e, t) ? ue.merge([e], n) : n
            }

            function g(e, t) {
                for (var n = 0, i = e.length; i > n; n++) Oe.set(e[n], "globalEval", !t || Oe.get(t[n], "globalEval"))
            }

            function v(e, t, n, i, o) {
                for (var r, a, s, l, c, u, d = t.createDocumentFragment(), f = [], p = 0, h = e.length; h > p; p++)
                    if ((r = e[p]) || 0 === r)
                        if ("object" === ue.type(r)) ue.merge(f, r.nodeType ? [r] : r);
                        else if ($e.test(r)) {
                    for (a = a || d.appendChild(t.createElement("div")), s = (Me.exec(r) || ["", ""])[1].toLowerCase(), l = ze[s] || ze._default, a.innerHTML = l[1] + ue.htmlPrefilter(r) + l[2], u = l[0]; u--;) a = a.lastChild;
                    ue.merge(f, a.childNodes), a = d.firstChild, a.textContent = ""
                } else f.push(t.createTextNode(r));
                for (d.textContent = "", p = 0; r = f[p++];)
                    if (i && ue.inArray(r, i) > -1) o && o.push(r);
                    else if (c = ue.contains(r.ownerDocument, r), a = m(d.appendChild(r), "script"), c && g(a), n)
                    for (u = 0; r = a[u++];) He.test(r.type || "") && n.push(r);
                return d
            }

            function b() {
                return !0
            }

            function y() {
                return !1
            }

            function x() {
                try {
                    return ee.activeElement
                } catch (e) {}
            }

            function w(e, t, n, i, o, r) {
                var a, s;
                if ("object" == typeof t) {
                    "string" != typeof n && (i = i || n, n = void 0);
                    for (s in t) w(e, s, n, i, t[s], r);
                    return e
                }
                if (null == i && null == o ? (o = n, i = n = void 0) : null == o && ("string" == typeof n ? (o = i, i = void 0) : (o = i, i = n, n = void 0)), !1 === o) o = y;
                else if (!o) return e;
                return 1 === r && (a = o, o = function(e) {
                    return ue().off(e), a.apply(this, arguments)
                }, o.guid = a.guid || (a.guid = ue.guid++)), e.each(function() {
                    ue.event.add(this, t, o, i, n)
                })
            }

            function C(e, t) {
                return ue.nodeName(e, "table") && ue.nodeName(11 !== t.nodeType ? t : t.firstChild, "tr") ? e.getElementsByTagName("tbody")[0] || e.appendChild(e.ownerDocument.createElement("tbody")) : e
            }

            function k(e) {
                return e.type = (null !== e.getAttribute("type")) + "/" + e.type, e
            }

            function S(e) {
                var t = Qe.exec(e.type);
                return t ? e.type = t[1] : e.removeAttribute("type"), e
            }

            function T(e, t) {
                var n, i, o, r, a, s, l, c;
                if (1 === t.nodeType) {
                    if (Oe.hasData(e) && (r = Oe.access(e), a = Oe.set(t, r), c = r.events)) {
                        delete a.handle, a.events = {};
                        for (o in c)
                            for (n = 0, i = c[o].length; i > n; n++) ue.event.add(t, o, c[o][n])
                    }
                    Fe.hasData(e) && (s = Fe.access(e), l = ue.extend({}, s), Fe.set(t, l))
                }
            }

            function A(e, t) {
                var n = t.nodeName.toLowerCase();
                "input" === n && Ie.test(e.type) ? t.checked = e.checked : "input" !== n && "textarea" !== n || (t.defaultValue = e.defaultValue)
            }

            function E(e, t, n, i) {
                t = ne.apply([], t);
                var o, r, a, s, l, c, u = 0,
                    d = e.length,
                    f = d - 1,
                    p = t[0],
                    h = ue.isFunction(p);
                if (h || d > 1 && "string" == typeof p && !le.checkClone && Xe.test(p)) return e.each(function(o) {
                    var r = e.eq(o);
                    h && (t[0] = p.call(this, o, r.html())), E(r, t, n, i)
                });
                if (d && (o = v(t, e[0].ownerDocument, !1, e, i), r = o.firstChild, 1 === o.childNodes.length && (o = r), r || i)) {
                    for (a = ue.map(m(o, "script"), k), s = a.length; d > u; u++) l = o, u !== f && (l = ue.clone(l, !0, !0), s && ue.merge(a, m(l, "script"))), n.call(e[u], l, u);
                    if (s)
                        for (c = a[a.length - 1].ownerDocument, ue.map(a, S), u = 0; s > u; u++) l = a[u], He.test(l.type || "") && !Oe.access(l, "globalEval") && ue.contains(c, l) && (l.src ? ue._evalUrl && ue._evalUrl(l.src) : ue.globalEval(l.textContent.replace(Ye, "")))
                }
                return e
            }

            function D(e, t, n) {
                for (var i, o = t ? ue.filter(t, e) : e, r = 0; null != (i = o[r]); r++) n || 1 !== i.nodeType || ue.cleanData(m(i)), i.parentNode && (n && ue.contains(i.ownerDocument, i) && g(m(i, "script")), i.parentNode.removeChild(i));
                return e
            }

            function O(e, t) {
                var n = ue(t.createElement(e)).appendTo(t.body),
                    i = ue.css(n[0], "display");
                return n.detach(), i
            }

            function F(e) {
                var t = ee,
                    n = Ke[e];
                return n || (n = O(e, t), "none" !== n && n || (Ge = (Ge || ue("<iframe frameborder='0' width='0' height='0'/>")).appendTo(t.documentElement), t = Ge[0].contentDocument, t.write(), t.close(), n = O(e, t), Ge.detach()), Ke[e] = n), n
            }

            function j(e, t, n) {
                var i, o, r, a, s = e.style;
                return n = n || et(e), a = n ? n.getPropertyValue(t) || n[t] : void 0, "" !== a && void 0 !== a || ue.contains(e.ownerDocument, e) || (a = ue.style(e, t)), n && !le.pixelMarginRight() && Ze.test(a) && Je.test(t) && (i = s.width, o = s.minWidth, r = s.maxWidth, s.minWidth = s.maxWidth = s.width = a, a = n.width, s.width = i, s.minWidth = o, s.maxWidth = r), void 0 !== a ? a + "" : a
            }

            function q(e, t) {
                return {
                    get: function() {
                        return e() ? void delete this.get : (this.get = t).apply(this, arguments)
                    }
                }
            }

            function L(e) {
                if (e in st) return e;
                for (var t = e[0].toUpperCase() + e.slice(1), n = at.length; n--;)
                    if ((e = at[n] + t) in st) return e
            }

            function N(e, t, n) {
                var i = Ne.exec(t);
                return i ? Math.max(0, i[2] - (n || 0)) + (i[3] || "px") : t
            }

            function P(e, t, n, i, o) {
                for (var r = n === (i ? "border" : "content") ? 4 : "width" === t ? 1 : 0, a = 0; 4 > r; r += 2) "margin" === n && (a += ue.css(e, n + Pe[r], !0, o)), i ? ("content" === n && (a -= ue.css(e, "padding" + Pe[r], !0, o)), "margin" !== n && (a -= ue.css(e, "border" + Pe[r] + "Width", !0, o))) : (a += ue.css(e, "padding" + Pe[r], !0, o), "padding" !== n && (a += ue.css(e, "border" + Pe[r] + "Width", !0, o)));
                return a
            }

            function R(e, t, n) {
                var i = !0,
                    o = "width" === t ? e.offsetWidth : e.offsetHeight,
                    r = et(e),
                    a = "border-box" === ue.css(e, "boxSizing", !1, r);
                if (0 >= o || null == o) {
                    if (o = j(e, t, r), (0 > o || null == o) && (o = e.style[t]), Ze.test(o)) return o;
                    i = a && (le.boxSizingReliable() || o === e.style[t]), o = parseFloat(o) || 0
                }
                return o + P(e, t, n || (a ? "border" : "content"), i, r) + "px"
            }

            function I(e, t) {
                for (var n, i, o, r = [], a = 0, s = e.length; s > a; a++) i = e[a], i.style && (r[a] = Oe.get(i, "olddisplay"), n = i.style.display, t ? (r[a] || "none" !== n || (i.style.display = ""), "" === i.style.display && Re(i) && (r[a] = Oe.access(i, "olddisplay", F(i.nodeName)))) : (o = Re(i), "none" === n && o || Oe.set(i, "olddisplay", o ? n : ue.css(i, "display"))));
                for (a = 0; s > a; a++) i = e[a], i.style && (t && "none" !== i.style.display && "" !== i.style.display || (i.style.display = t ? r[a] || "" : "none"));
                return e
            }

            function M(e, t, n, i, o) {
                return new M.prototype.init(e, t, n, i, o)
            }

            function H() {
                return r.setTimeout(function() {
                    lt = void 0
                }), lt = ue.now()
            }

            function z(e, t) {
                var n, i = 0,
                    o = {
                        height: e
                    };
                for (t = t ? 1 : 0; 4 > i; i += 2 - t) n = Pe[i], o["margin" + n] = o["padding" + n] = e;
                return t && (o.opacity = o.width = e), o
            }

            function $(e, t, n) {
                for (var i, o = (W.tweeners[t] || []).concat(W.tweeners["*"]), r = 0, a = o.length; a > r; r++)
                    if (i = o[r].call(n, t, e)) return i
            }

            function V(e, t, n) {
                var i, o, r, a, s, l, c, u = this,
                    d = {},
                    f = e.style,
                    p = e.nodeType && Re(e),
                    h = Oe.get(e, "fxshow");
                n.queue || (s = ue._queueHooks(e, "fx"), null == s.unqueued && (s.unqueued = 0, l = s.empty.fire, s.empty.fire = function() {
                    s.unqueued || l()
                }), s.unqueued++, u.always(function() {
                    u.always(function() {
                        s.unqueued--, ue.queue(e, "fx").length || s.empty.fire()
                    })
                })), 1 === e.nodeType && ("height" in t || "width" in t) && (n.overflow = [f.overflow, f.overflowX, f.overflowY], c = ue.css(e, "display"), "inline" === ("none" === c ? Oe.get(e, "olddisplay") || F(e.nodeName) : c) && "none" === ue.css(e, "float") && (f.display = "inline-block")), n.overflow && (f.overflow = "hidden", u.always(function() {
                    f.overflow = n.overflow[0], f.overflowX = n.overflow[1], f.overflowY = n.overflow[2]
                }));
                for (i in t)
                    if (o = t[i], ut.exec(o)) {
                        if (delete t[i], r = r || "toggle" === o, o === (p ? "hide" : "show")) {
                            if ("show" !== o || !h || void 0 === h[i]) continue;
                            p = !0
                        }
                        d[i] = h && h[i] || ue.style(e, i)
                    } else c = void 0;
                if (ue.isEmptyObject(d)) "inline" === ("none" === c ? F(e.nodeName) : c) && (f.display = c);
                else {
                    h ? "hidden" in h && (p = h.hidden) : h = Oe.access(e, "fxshow", {}), r && (h.hidden = !p), p ? ue(e).show() : u.done(function() {
                        ue(e).hide()
                    }), u.done(function() {
                        var t;
                        Oe.remove(e, "fxshow");
                        for (t in d) ue.style(e, t, d[t])
                    });
                    for (i in d) a = $(p ? h[i] : 0, i, u), i in h || (h[i] = a.start, p && (a.end = a.start, a.start = "width" === i || "height" === i ? 1 : 0))
                }
            }

            function B(e, t) {
                var n, i, o, r, a;
                for (n in e)
                    if (i = ue.camelCase(n), o = t[i], r = e[n], ue.isArray(r) && (o = r[1], r = e[n] = r[0]), n !== i && (e[i] = r, delete e[n]), (a = ue.cssHooks[i]) && "expand" in a) {
                        r = a.expand(r), delete e[i];
                        for (n in r) n in e || (e[n] = r[n], t[n] = o)
                    } else t[i] = o
            }

            function W(e, t, n) {
                var i, o, r = 0,
                    a = W.prefilters.length,
                    s = ue.Deferred().always(function() {
                        delete l.elem
                    }),
                    l = function() {
                        if (o) return !1;
                        for (var t = lt || H(), n = Math.max(0, c.startTime + c.duration - t), i = n / c.duration || 0, r = 1 - i, a = 0, l = c.tweens.length; l > a; a++) c.tweens[a].run(r);
                        return s.notifyWith(e, [c, r, n]), 1 > r && l ? n : (s.resolveWith(e, [c]), !1)
                    },
                    c = s.promise({
                        elem: e,
                        props: ue.extend({}, t),
                        opts: ue.extend(!0, {
                            specialEasing: {},
                            easing: ue.easing._default
                        }, n),
                        originalProperties: t,
                        originalOptions: n,
                        startTime: lt || H(),
                        duration: n.duration,
                        tweens: [],
                        createTween: function(t, n) {
                            var i = ue.Tween(e, c.opts, t, n, c.opts.specialEasing[t] || c.opts.easing);
                            return c.tweens.push(i), i
                        },
                        stop: function(t) {
                            var n = 0,
                                i = t ? c.tweens.length : 0;
                            if (o) return this;
                            for (o = !0; i > n; n++) c.tweens[n].run(1);
                            return t ? (s.notifyWith(e, [c, 1, 0]), s.resolveWith(e, [c, t])) : s.rejectWith(e, [c, t]), this
                        }
                    }),
                    u = c.props;
                for (B(u, c.opts.specialEasing); a > r; r++)
                    if (i = W.prefilters[r].call(c, e, u, c.opts)) return ue.isFunction(i.stop) && (ue._queueHooks(c.elem, c.opts.queue).stop = ue.proxy(i.stop, i)), i;
                return ue.map(u, $, c), ue.isFunction(c.opts.start) && c.opts.start.call(e, c), ue.fx.timer(ue.extend(l, {
                    elem: e,
                    anim: c,
                    queue: c.opts.queue
                })), c.progress(c.opts.progress).done(c.opts.done, c.opts.complete).fail(c.opts.fail).always(c.opts.always)
            }

            function U(e) {
                return e.getAttribute && e.getAttribute("class") || ""
            }

            function _(e) {
                return function(t, n) {
                    "string" != typeof t && (n = t, t = "*");
                    var i, o = 0,
                        r = t.toLowerCase().match(Te) || [];
                    if (ue.isFunction(n))
                        for (; i = r[o++];) "+" === i[0] ? (i = i.slice(1) || "*", (e[i] = e[i] || []).unshift(n)) : (e[i] = e[i] || []).push(n)
                }
            }

            function X(e, t, n, i) {
                function o(s) {
                    var l;
                    return r[s] = !0, ue.each(e[s] || [], function(e, s) {
                        var c = s(t, n, i);
                        return "string" != typeof c || a || r[c] ? a ? !(l = c) : void 0 : (t.dataTypes.unshift(c), o(c), !1)
                    }), l
                }
                var r = {},
                    a = e === Ft;
                return o(t.dataTypes[0]) || !r["*"] && o("*")
            }

            function Q(e, t) {
                var n, i, o = ue.ajaxSettings.flatOptions || {};
                for (n in t) void 0 !== t[n] && ((o[n] ? e : i || (i = {}))[n] = t[n]);
                return i && ue.extend(!0, e, i), e
            }

            function Y(e, t, n) {
                for (var i, o, r, a, s = e.contents, l = e.dataTypes;
                    "*" === l[0];) l.shift(), void 0 === i && (i = e.mimeType || t.getResponseHeader("Content-Type"));
                if (i)
                    for (o in s)
                        if (s[o] && s[o].test(i)) {
                            l.unshift(o);
                            break
                        }
                if (l[0] in n) r = l[0];
                else {
                    for (o in n) {
                        if (!l[0] || e.converters[o + " " + l[0]]) {
                            r = o;
                            break
                        }
                        a || (a = o)
                    }
                    r = r || a
                }
                return r ? (r !== l[0] && l.unshift(r), n[r]) : void 0
            }

            function G(e, t, n, i) {
                var o, r, a, s, l, c = {},
                    u = e.dataTypes.slice();
                if (u[1])
                    for (a in e.converters) c[a.toLowerCase()] = e.converters[a];
                for (r = u.shift(); r;)
                    if (e.responseFields[r] && (n[e.responseFields[r]] = t), !l && i && e.dataFilter && (t = e.dataFilter(t, e.dataType)), l = r, r = u.shift())
                        if ("*" === r) r = l;
                        else if ("*" !== l && l !== r) {
                    if (!(a = c[l + " " + r] || c["* " + r]))
                        for (o in c)
                            if (s = o.split(" "), s[1] === r && (a = c[l + " " + s[0]] || c["* " + s[0]])) {
                                !0 === a ? a = c[o] : !0 !== c[o] && (r = s[0], u.unshift(s[1]));
                                break
                            }
                    if (!0 !== a)
                        if (a && e.throws) t = a(t);
                        else try {
                            t = a(t)
                        } catch (e) {
                            return {
                                state: "parsererror",
                                error: a ? e : "No conversion from " + l + " to " + r
                            }
                        }
                }
                return {
                    state: "success",
                    data: t
                }
            }

            function K(e, t, n, i) {
                var o;
                if (ue.isArray(t)) ue.each(t, function(t, o) {
                    n || Nt.test(e) ? i(e, o) : K(e + "[" + ("object" == typeof o && null != o ? t : "") + "]", o, n, i)
                });
                else if (n || "object" !== ue.type(t)) i(e, t);
                else
                    for (o in t) K(e + "[" + o + "]", t[o], n, i)
            }

            function J(e) {
                return ue.isWindow(e) ? e : 9 === e.nodeType && e.defaultView
            }
            var Z = [],
                ee = r.document,
                te = Z.slice,
                ne = Z.concat,
                ie = Z.push,
                oe = Z.indexOf,
                re = {},
                ae = re.toString,
                se = re.hasOwnProperty,
                le = {},
                ce = "2.2.4",
                ue = function(e, t) {
                    return new ue.fn.init(e, t)
                },
                de = /^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,
                fe = /^-ms-/,
                pe = /-([\da-z])/gi,
                he = function(e, t) {
                    return t.toUpperCase()
                };
            ue.fn = ue.prototype = {
                jquery: ce,
                constructor: ue,
                selector: "",
                length: 0,
                toArray: function() {
                    return te.call(this)
                },
                get: function(e) {
                    return null != e ? 0 > e ? this[e + this.length] : this[e] : te.call(this)
                },
                pushStack: function(e) {
                    var t = ue.merge(this.constructor(), e);
                    return t.prevObject = this, t.context = this.context, t
                },
                each: function(e) {
                    return ue.each(this, e)
                },
                map: function(e) {
                    return this.pushStack(ue.map(this, function(t, n) {
                        return e.call(t, n, t)
                    }))
                },
                slice: function() {
                    return this.pushStack(te.apply(this, arguments))
                },
                first: function() {
                    return this.eq(0)
                },
                last: function() {
                    return this.eq(-1)
                },
                eq: function(e) {
                    var t = this.length,
                        n = +e + (0 > e ? t : 0);
                    return this.pushStack(n >= 0 && t > n ? [this[n]] : [])
                },
                end: function() {
                    return this.prevObject || this.constructor()
                },
                push: ie,
                sort: Z.sort,
                splice: Z.splice
            }, ue.extend = ue.fn.extend = function() {
                var e, t, n, i, o, r, a = arguments[0] || {},
                    s = 1,
                    l = arguments.length,
                    c = !1;
                for ("boolean" == typeof a && (c = a, a = arguments[s] || {}, s++), "object" == typeof a || ue.isFunction(a) || (a = {}), s === l && (a = this, s--); l > s; s++)
                    if (null != (e = arguments[s]))
                        for (t in e) n = a[t], i = e[t], a !== i && (c && i && (ue.isPlainObject(i) || (o = ue.isArray(i))) ? (o ? (o = !1, r = n && ue.isArray(n) ? n : []) : r = n && ue.isPlainObject(n) ? n : {}, a[t] = ue.extend(c, r, i)) : void 0 !== i && (a[t] = i));
                return a
            }, ue.extend({
                expando: "jQuery" + (ce + Math.random()).replace(/\D/g, ""),
                isReady: !0,
                error: function(e) {
                    throw new Error(e)
                },
                noop: function() {},
                isFunction: function(e) {
                    return "function" === ue.type(e)
                },
                isArray: Array.isArray,
                isWindow: function(e) {
                    return null != e && e === e.window
                },
                isNumeric: function(e) {
                    var t = e && e.toString();
                    return !ue.isArray(e) && t - parseFloat(t) + 1 >= 0
                },
                isPlainObject: function(e) {
                    var t;
                    if ("object" !== ue.type(e) || e.nodeType || ue.isWindow(e)) return !1;
                    if (e.constructor && !se.call(e, "constructor") && !se.call(e.constructor.prototype || {}, "isPrototypeOf")) return !1;
                    for (t in e);
                    return void 0 === t || se.call(e, t)
                },
                isEmptyObject: function(e) {
                    var t;
                    for (t in e) return !1;
                    return !0
                },
                type: function(e) {
                    return null == e ? e + "" : "object" == typeof e || "function" == typeof e ? re[ae.call(e)] || "object" : typeof e
                },
                globalEval: function(e) {
                    var t, n = eval;
                    (e = ue.trim(e)) && (1 === e.indexOf("use strict") ? (t = ee.createElement("script"), t.text = e, ee.head.appendChild(t).parentNode.removeChild(t)) : n(e))
                },
                camelCase: function(e) {
                    return e.replace(fe, "ms-").replace(pe, he)
                },
                nodeName: function(e, t) {
                    return e.nodeName && e.nodeName.toLowerCase() === t.toLowerCase()
                },
                each: function(e, t) {
                    var n, i = 0;
                    if (s(e))
                        for (n = e.length; n > i && !1 !== t.call(e[i], i, e[i]); i++);
                    else
                        for (i in e)
                            if (!1 === t.call(e[i], i, e[i])) break;
                    return e
                },
                trim: function(e) {
                    return null == e ? "" : (e + "").replace(de, "")
                },
                makeArray: function(e, t) {
                    var n = t || [];
                    return null != e && (s(Object(e)) ? ue.merge(n, "string" == typeof e ? [e] : e) : ie.call(n, e)), n
                },
                inArray: function(e, t, n) {
                    return null == t ? -1 : oe.call(t, e, n)
                },
                merge: function(e, t) {
                    for (var n = +t.length, i = 0, o = e.length; n > i; i++) e[o++] = t[i];
                    return e.length = o, e
                },
                grep: function(e, t, n) {
                    for (var i = [], o = 0, r = e.length, a = !n; r > o; o++) !t(e[o], o) !== a && i.push(e[o]);
                    return i
                },
                map: function(e, t, n) {
                    var i, o, r = 0,
                        a = [];
                    if (s(e))
                        for (i = e.length; i > r; r++) null != (o = t(e[r], r, n)) && a.push(o);
                    else
                        for (r in e) null != (o = t(e[r], r, n)) && a.push(o);
                    return ne.apply([], a)
                },
                guid: 1,
                proxy: function(e, t) {
                    var n, i, o;
                    return "string" == typeof t && (n = e[t], t = e, e = n), ue.isFunction(e) ? (i = te.call(arguments, 2), o = function() {
                        return e.apply(t || this, i.concat(te.call(arguments)))
                    }, o.guid = e.guid = e.guid || ue.guid++, o) : void 0
                },
                now: Date.now,
                support: le
            }), "function" == typeof Symbol && (ue.fn[Symbol.iterator] = Z[Symbol.iterator]), ue.each("Boolean Number String Function Array Date RegExp Object Error Symbol".split(" "), function(e, t) {
                re["[object " + t + "]"] = t.toLowerCase()
            });
            var me = function(e) {
                function t(e, t, n, i) {
                    var o, r, a, s, c, d, f, p, h = t && t.ownerDocument,
                        m = t ? t.nodeType : 9;
                    if (n = n || [], "string" != typeof e || !e || 1 !== m && 9 !== m && 11 !== m) return n;
                    if (!i && ((t ? t.ownerDocument || t : M) !== F && O(t), t = t || F, q)) {
                        if (11 !== m && (d = me.exec(e)))
                            if (o = d[1]) {
                                if (9 === m) {
                                    if (!(a = t.getElementById(o))) return n;
                                    if (a.id === o) return n.push(a), n
                                } else if (h && (a = h.getElementById(o)) && R(t, a) && a.id === o) return n.push(a), n
                            } else {
                                if (d[2]) return G.apply(n, t.getElementsByTagName(e)), n;
                                if ((o = d[3]) && y.getElementsByClassName && t.getElementsByClassName) return G.apply(n, t.getElementsByClassName(o)), n
                            }
                        if (y.qsa && !B[e + " "] && (!L || !L.test(e))) {
                            if (1 !== m) h = t, p = e;
                            else if ("object" !== t.nodeName.toLowerCase()) {
                                for ((s = t.getAttribute("id")) ? s = s.replace(ve, "\\$&") : t.setAttribute("id", s = I), f = k(e), r = f.length, c = ue.test(s) ? "#" + s : "[id='" + s + "']"; r--;) f[r] = c + " " + u(f[r]);
                                p = f.join(","), h = ge.test(e) && l(t.parentNode) || t
                            }
                            if (p) try {
                                return G.apply(n, h.querySelectorAll(p)), n
                            } catch (e) {} finally {
                                s === I && t.removeAttribute("id")
                            }
                        }
                    }
                    return T(e.replace(re, "$1"), t, n, i)
                }

                function n() {
                    function e(n, i) {
                        return t.push(n + " ") > x.cacheLength && delete e[t.shift()], e[n + " "] = i
                    }
                    var t = [];
                    return e
                }

                function i(e) {
                    return e[I] = !0, e
                }

                function o(e) {
                    var t = F.createElement("div");
                    try {
                        return !!e(t)
                    } catch (e) {
                        return !1
                    } finally {
                        t.parentNode && t.parentNode.removeChild(t), t = null
                    }
                }

                function r(e, t) {
                    for (var n = e.split("|"), i = n.length; i--;) x.attrHandle[n[i]] = t
                }

                function a(e, t) {
                    var n = t && e,
                        i = n && 1 === e.nodeType && 1 === t.nodeType && (~t.sourceIndex || U) - (~e.sourceIndex || U);
                    if (i) return i;
                    if (n)
                        for (; n = n.nextSibling;)
                            if (n === t) return -1;
                    return e ? 1 : -1
                }

                function s(e) {
                    return i(function(t) {
                        return t = +t, i(function(n, i) {
                            for (var o, r = e([], n.length, t), a = r.length; a--;) n[o = r[a]] && (n[o] = !(i[o] = n[o]))
                        })
                    })
                }

                function l(e) {
                    return e && void 0 !== e.getElementsByTagName && e
                }

                function c() {}

                function u(e) {
                    for (var t = 0, n = e.length, i = ""; n > t; t++) i += e[t].value;
                    return i
                }

                function d(e, t, n) {
                    var i = t.dir,
                        o = n && "parentNode" === i,
                        r = z++;
                    return t.first ? function(t, n, r) {
                        for (; t = t[i];)
                            if (1 === t.nodeType || o) return e(t, n, r)
                    } : function(t, n, a) {
                        var s, l, c, u = [H, r];
                        if (a) {
                            for (; t = t[i];)
                                if ((1 === t.nodeType || o) && e(t, n, a)) return !0
                        } else
                            for (; t = t[i];)
                                if (1 === t.nodeType || o) {
                                    if (c = t[I] || (t[I] = {}), l = c[t.uniqueID] || (c[t.uniqueID] = {}), (s = l[i]) && s[0] === H && s[1] === r) return u[2] = s[2];
                                    if (l[i] = u, u[2] = e(t, n, a)) return !0
                                }
                    }
                }

                function f(e) {
                    return e.length > 1 ? function(t, n, i) {
                        for (var o = e.length; o--;)
                            if (!e[o](t, n, i)) return !1;
                        return !0
                    } : e[0]
                }

                function p(e, n, i) {
                    for (var o = 0, r = n.length; r > o; o++) t(e, n[o], i);
                    return i
                }

                function h(e, t, n, i, o) {
                    for (var r, a = [], s = 0, l = e.length, c = null != t; l > s; s++)(r = e[s]) && (n && !n(r, i, o) || (a.push(r), c && t.push(s)));
                    return a
                }

                function m(e, t, n, o, r, a) {
                    return o && !o[I] && (o = m(o)), r && !r[I] && (r = m(r, a)), i(function(i, a, s, l) {
                        var c, u, d, f = [],
                            m = [],
                            g = a.length,
                            v = i || p(t || "*", s.nodeType ? [s] : s, []),
                            b = !e || !i && t ? v : h(v, f, e, s, l),
                            y = n ? r || (i ? e : g || o) ? [] : a : b;
                        if (n && n(b, y, s, l), o)
                            for (c = h(y, m), o(c, [], s, l), u = c.length; u--;)(d = c[u]) && (y[m[u]] = !(b[m[u]] = d));
                        if (i) {
                            if (r || e) {
                                if (r) {
                                    for (c = [], u = y.length; u--;)(d = y[u]) && c.push(b[u] = d);
                                    r(null, y = [], c, l)
                                }
                                for (u = y.length; u--;)(d = y[u]) && (c = r ? J(i, d) : f[u]) > -1 && (i[c] = !(a[c] = d))
                            }
                        } else y = h(y === a ? y.splice(g, y.length) : y), r ? r(null, a, y, l) : G.apply(a, y)
                    })
                }

                function g(e) {
                    for (var t, n, i, o = e.length, r = x.relative[e[0].type], a = r || x.relative[" "], s = r ? 1 : 0, l = d(function(e) {
                            return e === t
                        }, a, !0), c = d(function(e) {
                            return J(t, e) > -1
                        }, a, !0), p = [function(e, n, i) {
                            var o = !r && (i || n !== A) || ((t = n).nodeType ? l(e, n, i) : c(e, n, i));
                            return t = null, o
                        }]; o > s; s++)
                        if (n = x.relative[e[s].type]) p = [d(f(p), n)];
                        else {
                            if (n = x.filter[e[s].type].apply(null, e[s].matches), n[I]) {
                                for (i = ++s; o > i && !x.relative[e[i].type]; i++);
                                return m(s > 1 && f(p), s > 1 && u(e.slice(0, s - 1).concat({
                                    value: " " === e[s - 2].type ? "*" : ""
                                })).replace(re, "$1"), n, i > s && g(e.slice(s, i)), o > i && g(e = e.slice(i)), o > i && u(e))
                            }
                            p.push(n)
                        }
                    return f(p)
                }

                function v(e, n) {
                    var o = n.length > 0,
                        r = e.length > 0,
                        a = function(i, a, s, l, c) {
                            var u, d, f, p = 0,
                                m = "0",
                                g = i && [],
                                v = [],
                                b = A,
                                y = i || r && x.find.TAG("*", c),
                                w = H += null == b ? 1 : Math.random() || .1,
                                C = y.length;
                            for (c && (A = a === F || a || c); m !== C && null != (u = y[m]); m++) {
                                if (r && u) {
                                    for (d = 0, a || u.ownerDocument === F || (O(u), s = !q); f = e[d++];)
                                        if (f(u, a || F, s)) {
                                            l.push(u);
                                            break
                                        }
                                    c && (H = w)
                                }
                                o && ((u = !f && u) && p--, i && g.push(u))
                            }
                            if (p += m, o && m !== p) {
                                for (d = 0; f = n[d++];) f(g, v, a, s);
                                if (i) {
                                    if (p > 0)
                                        for (; m--;) g[m] || v[m] || (v[m] = Q.call(l));
                                    v = h(v)
                                }
                                G.apply(l, v), c && !i && v.length > 0 && p + n.length > 1 && t.uniqueSort(l)
                            }
                            return c && (H = w, A = b), g
                        };
                    return o ? i(a) : a
                }
                var b, y, x, w, C, k, S, T, A, E, D, O, F, j, q, L, N, P, R, I = "sizzle" + 1 * new Date,
                    M = e.document,
                    H = 0,
                    z = 0,
                    $ = n(),
                    V = n(),
                    B = n(),
                    W = function(e, t) {
                        return e === t && (D = !0), 0
                    },
                    U = 1 << 31,
                    _ = {}.hasOwnProperty,
                    X = [],
                    Q = X.pop,
                    Y = X.push,
                    G = X.push,
                    K = X.slice,
                    J = function(e, t) {
                        for (var n = 0, i = e.length; i > n; n++)
                            if (e[n] === t) return n;
                        return -1
                    },
                    Z = "checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped",
                    ee = "[\\x20\\t\\r\\n\\f]",
                    te = "(?:\\\\.|[\\w-]|[^\\x00-\\xa0])+",
                    ne = "\\[" + ee + "*(" + te + ")(?:" + ee + "*([*^$|!~]?=)" + ee + "*(?:'((?:\\\\.|[^\\\\'])*)'|\"((?:\\\\.|[^\\\\\"])*)\"|(" + te + "))|)" + ee + "*\\]",
                    ie = ":(" + te + ")(?:\\((('((?:\\\\.|[^\\\\'])*)'|\"((?:\\\\.|[^\\\\\"])*)\")|((?:\\\\.|[^\\\\()[\\]]|" + ne + ")*)|.*)\\)|)",
                    oe = new RegExp(ee + "+", "g"),
                    re = new RegExp("^" + ee + "+|((?:^|[^\\\\])(?:\\\\.)*)" + ee + "+$", "g"),
                    ae = new RegExp("^" + ee + "*," + ee + "*"),
                    se = new RegExp("^" + ee + "*([>+~]|" + ee + ")" + ee + "*"),
                    le = new RegExp("=" + ee + "*([^\\]'\"]*?)" + ee + "*\\]", "g"),
                    ce = new RegExp(ie),
                    ue = new RegExp("^" + te + "$"),
                    de = {
                        ID: new RegExp("^#(" + te + ")"),
                        CLASS: new RegExp("^\\.(" + te + ")"),
                        TAG: new RegExp("^(" + te + "|[*])"),
                        ATTR: new RegExp("^" + ne),
                        PSEUDO: new RegExp("^" + ie),
                        CHILD: new RegExp("^:(only|first|last|nth|nth-last)-(child|of-type)(?:\\(" + ee + "*(even|odd|(([+-]|)(\\d*)n|)" + ee + "*(?:([+-]|)" + ee + "*(\\d+)|))" + ee + "*\\)|)", "i"),
                        bool: new RegExp("^(?:" + Z + ")$", "i"),
                        needsContext: new RegExp("^" + ee + "*[>+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\\(" + ee + "*((?:-\\d)?\\d*)" + ee + "*\\)|)(?=[^-]|$)", "i")
                    },
                    fe = /^(?:input|select|textarea|button)$/i,
                    pe = /^h\d$/i,
                    he = /^[^{]+\{\s*\[native \w/,
                    me = /^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/,
                    ge = /[+~]/,
                    ve = /'|\\/g,
                    be = new RegExp("\\\\([\\da-f]{1,6}" + ee + "?|(" + ee + ")|.)", "ig"),
                    ye = function(e, t, n) {
                        var i = "0x" + t - 65536;
                        return i !== i || n ? t : 0 > i ? String.fromCharCode(i + 65536) : String.fromCharCode(i >> 10 | 55296, 1023 & i | 56320)
                    },
                    xe = function() {
                        O()
                    };
                try {
                    G.apply(X = K.call(M.childNodes), M.childNodes), X[M.childNodes.length].nodeType
                } catch (e) {
                    G = {
                        apply: X.length ? function(e, t) {
                            Y.apply(e, K.call(t))
                        } : function(e, t) {
                            for (var n = e.length, i = 0; e[n++] = t[i++];);
                            e.length = n - 1
                        }
                    }
                }
                y = t.support = {}, C = t.isXML = function(e) {
                    var t = e && (e.ownerDocument || e).documentElement;
                    return !!t && "HTML" !== t.nodeName
                }, O = t.setDocument = function(e) {
                    var t, n, i = e ? e.ownerDocument || e : M;
                    return i !== F && 9 === i.nodeType && i.documentElement ? (F = i, j = F.documentElement, q = !C(F), (n = F.defaultView) && n.top !== n && (n.addEventListener ? n.addEventListener("unload", xe, !1) : n.attachEvent && n.attachEvent("onunload", xe)), y.attributes = o(function(e) {
                        return e.className = "i", !e.getAttribute("className")
                    }), y.getElementsByTagName = o(function(e) {
                        return e.appendChild(F.createComment("")), !e.getElementsByTagName("*").length
                    }), y.getElementsByClassName = he.test(F.getElementsByClassName), y.getById = o(function(e) {
                        return j.appendChild(e).id = I, !F.getElementsByName || !F.getElementsByName(I).length
                    }), y.getById ? (x.find.ID = function(e, t) {
                        if (void 0 !== t.getElementById && q) {
                            var n = t.getElementById(e);
                            return n ? [n] : []
                        }
                    }, x.filter.ID = function(e) {
                        var t = e.replace(be, ye);
                        return function(e) {
                            return e.getAttribute("id") === t
                        }
                    }) : (delete x.find.ID, x.filter.ID = function(e) {
                        var t = e.replace(be, ye);
                        return function(e) {
                            var n = void 0 !== e.getAttributeNode && e.getAttributeNode("id");
                            return n && n.value === t
                        }
                    }), x.find.TAG = y.getElementsByTagName ? function(e, t) {
                        return void 0 !== t.getElementsByTagName ? t.getElementsByTagName(e) : y.qsa ? t.querySelectorAll(e) : void 0
                    } : function(e, t) {
                        var n, i = [],
                            o = 0,
                            r = t.getElementsByTagName(e);
                        if ("*" === e) {
                            for (; n = r[o++];) 1 === n.nodeType && i.push(n);
                            return i
                        }
                        return r
                    }, x.find.CLASS = y.getElementsByClassName && function(e, t) {
                        return void 0 !== t.getElementsByClassName && q ? t.getElementsByClassName(e) : void 0
                    }, N = [], L = [], (y.qsa = he.test(F.querySelectorAll)) && (o(function(e) {
                        j.appendChild(e).innerHTML = "<a id='" + I + "'></a><select id='" + I + "-\r\\' msallowcapture=''><option selected=''></option></select>", e.querySelectorAll("[msallowcapture^='']").length && L.push("[*^$]=" + ee + "*(?:''|\"\")"), e.querySelectorAll("[selected]").length || L.push("\\[" + ee + "*(?:value|" + Z + ")"), e.querySelectorAll("[id~=" + I + "-]").length || L.push("~="), e.querySelectorAll(":checked").length || L.push(":checked"), e.querySelectorAll("a#" + I + "+*").length || L.push(".#.+[+~]")
                    }), o(function(e) {
                        var t = F.createElement("input");
                        t.setAttribute("type", "hidden"), e.appendChild(t).setAttribute("name", "D"), e.querySelectorAll("[name=d]").length && L.push("name" + ee + "*[*^$|!~]?="), e.querySelectorAll(":enabled").length || L.push(":enabled", ":disabled"), e.querySelectorAll("*,:x"), L.push(",.*:")
                    })), (y.matchesSelector = he.test(P = j.matches || j.webkitMatchesSelector || j.mozMatchesSelector || j.oMatchesSelector || j.msMatchesSelector)) && o(function(e) {
                        y.disconnectedMatch = P.call(e, "div"), P.call(e, "[s!='']:x"), N.push("!=", ie)
                    }), L = L.length && new RegExp(L.join("|")), N = N.length && new RegExp(N.join("|")), t = he.test(j.compareDocumentPosition), R = t || he.test(j.contains) ? function(e, t) {
                        var n = 9 === e.nodeType ? e.documentElement : e,
                            i = t && t.parentNode;
                        return e === i || !(!i || 1 !== i.nodeType || !(n.contains ? n.contains(i) : e.compareDocumentPosition && 16 & e.compareDocumentPosition(i)))
                    } : function(e, t) {
                        if (t)
                            for (; t = t.parentNode;)
                                if (t === e) return !0;
                        return !1
                    }, W = t ? function(e, t) {
                        if (e === t) return D = !0, 0;
                        var n = !e.compareDocumentPosition - !t.compareDocumentPosition;
                        return n || (n = (e.ownerDocument || e) === (t.ownerDocument || t) ? e.compareDocumentPosition(t) : 1, 1 & n || !y.sortDetached && t.compareDocumentPosition(e) === n ? e === F || e.ownerDocument === M && R(M, e) ? -1 : t === F || t.ownerDocument === M && R(M, t) ? 1 : E ? J(E, e) - J(E, t) : 0 : 4 & n ? -1 : 1)
                    } : function(e, t) {
                        if (e === t) return D = !0, 0;
                        var n, i = 0,
                            o = e.parentNode,
                            r = t.parentNode,
                            s = [e],
                            l = [t];
                        if (!o || !r) return e === F ? -1 : t === F ? 1 : o ? -1 : r ? 1 : E ? J(E, e) - J(E, t) : 0;
                        if (o === r) return a(e, t);
                        for (n = e; n = n.parentNode;) s.unshift(n);
                        for (n = t; n = n.parentNode;) l.unshift(n);
                        for (; s[i] === l[i];) i++;
                        return i ? a(s[i], l[i]) : s[i] === M ? -1 : l[i] === M ? 1 : 0
                    }, F) : F
                }, t.matches = function(e, n) {
                    return t(e, null, null, n)
                }, t.matchesSelector = function(e, n) {
                    if ((e.ownerDocument || e) !== F && O(e), n = n.replace(le, "='$1']"), y.matchesSelector && q && !B[n + " "] && (!N || !N.test(n)) && (!L || !L.test(n))) try {
                        var i = P.call(e, n);
                        if (i || y.disconnectedMatch || e.document && 11 !== e.document.nodeType) return i
                    } catch (e) {}
                    return t(n, F, null, [e]).length > 0
                }, t.contains = function(e, t) {
                    return (e.ownerDocument || e) !== F && O(e), R(e, t)
                }, t.attr = function(e, t) {
                    (e.ownerDocument || e) !== F && O(e);
                    var n = x.attrHandle[t.toLowerCase()],
                        i = n && _.call(x.attrHandle, t.toLowerCase()) ? n(e, t, !q) : void 0;
                    return void 0 !== i ? i : y.attributes || !q ? e.getAttribute(t) : (i = e.getAttributeNode(t)) && i.specified ? i.value : null
                }, t.error = function(e) {
                    throw new Error("Syntax error, unrecognized expression: " + e)
                }, t.uniqueSort = function(e) {
                    var t, n = [],
                        i = 0,
                        o = 0;
                    if (D = !y.detectDuplicates, E = !y.sortStable && e.slice(0), e.sort(W), D) {
                        for (; t = e[o++];) t === e[o] && (i = n.push(o));
                        for (; i--;) e.splice(n[i], 1)
                    }
                    return E = null, e
                }, w = t.getText = function(e) {
                    var t, n = "",
                        i = 0,
                        o = e.nodeType;
                    if (o) {
                        if (1 === o || 9 === o || 11 === o) {
                            if ("string" == typeof e.textContent) return e.textContent;
                            for (e = e.firstChild; e; e = e.nextSibling) n += w(e)
                        } else if (3 === o || 4 === o) return e.nodeValue
                    } else
                        for (; t = e[i++];) n += w(t);
                    return n
                }, x = t.selectors = {
                    cacheLength: 50,
                    createPseudo: i,
                    match: de,
                    attrHandle: {},
                    find: {},
                    relative: {
                        ">": {
                            dir: "parentNode",
                            first: !0
                        },
                        " ": {
                            dir: "parentNode"
                        },
                        "+": {
                            dir: "previousSibling",
                            first: !0
                        },
                        "~": {
                            dir: "previousSibling"
                        }
                    },
                    preFilter: {
                        ATTR: function(e) {
                            return e[1] = e[1].replace(be, ye), e[3] = (e[3] || e[4] || e[5] || "").replace(be, ye), "~=" === e[2] && (e[3] = " " + e[3] + " "), e.slice(0, 4)
                        },
                        CHILD: function(e) {
                            return e[1] = e[1].toLowerCase(), "nth" === e[1].slice(0, 3) ? (e[3] || t.error(e[0]), e[4] = +(e[4] ? e[5] + (e[6] || 1) : 2 * ("even" === e[3] || "odd" === e[3])), e[5] = +(e[7] + e[8] || "odd" === e[3])) : e[3] && t.error(e[0]), e
                        },
                        PSEUDO: function(e) {
                            var t, n = !e[6] && e[2];
                            return de.CHILD.test(e[0]) ? null : (e[3] ? e[2] = e[4] || e[5] || "" : n && ce.test(n) && (t = k(n, !0)) && (t = n.indexOf(")", n.length - t) - n.length) && (e[0] = e[0].slice(0, t), e[2] = n.slice(0, t)), e.slice(0, 3))
                        }
                    },
                    filter: {
                        TAG: function(e) {
                            var t = e.replace(be, ye).toLowerCase();
                            return "*" === e ? function() {
                                return !0
                            } : function(e) {
                                return e.nodeName && e.nodeName.toLowerCase() === t
                            }
                        },
                        CLASS: function(e) {
                            var t = $[e + " "];
                            return t || (t = new RegExp("(^|" + ee + ")" + e + "(" + ee + "|$)")) && $(e, function(e) {
                                return t.test("string" == typeof e.className && e.className || void 0 !== e.getAttribute && e.getAttribute("class") || "")
                            })
                        },
                        ATTR: function(e, n, i) {
                            return function(o) {
                                var r = t.attr(o, e);
                                return null == r ? "!=" === n : !n || (r += "", "=" === n ? r === i : "!=" === n ? r !== i : "^=" === n ? i && 0 === r.indexOf(i) : "*=" === n ? i && r.indexOf(i) > -1 : "$=" === n ? i && r.slice(-i.length) === i : "~=" === n ? (" " + r.replace(oe, " ") + " ").indexOf(i) > -1 : "|=" === n && (r === i || r.slice(0, i.length + 1) === i + "-"))
                            }
                        },
                        CHILD: function(e, t, n, i, o) {
                            var r = "nth" !== e.slice(0, 3),
                                a = "last" !== e.slice(-4),
                                s = "of-type" === t;
                            return 1 === i && 0 === o ? function(e) {
                                return !!e.parentNode
                            } : function(t, n, l) {
                                var c, u, d, f, p, h, m = r !== a ? "nextSibling" : "previousSibling",
                                    g = t.parentNode,
                                    v = s && t.nodeName.toLowerCase(),
                                    b = !l && !s,
                                    y = !1;
                                if (g) {
                                    if (r) {
                                        for (; m;) {
                                            for (f = t; f = f[m];)
                                                if (s ? f.nodeName.toLowerCase() === v : 1 === f.nodeType) return !1;
                                            h = m = "only" === e && !h && "nextSibling"
                                        }
                                        return !0
                                    }
                                    if (h = [a ? g.firstChild : g.lastChild], a && b) {
                                        for (f = g, d = f[I] || (f[I] = {}), u = d[f.uniqueID] || (d[f.uniqueID] = {}), c = u[e] || [], p = c[0] === H && c[1], y = p && c[2], f = p && g.childNodes[p]; f = ++p && f && f[m] || (y = p = 0) || h.pop();)
                                            if (1 === f.nodeType && ++y && f === t) {
                                                u[e] = [H, p, y];
                                                break
                                            }
                                    } else if (b && (f = t, d = f[I] || (f[I] = {}), u = d[f.uniqueID] || (d[f.uniqueID] = {}), c = u[e] || [], p = c[0] === H && c[1], y = p), !1 === y)
                                        for (;
                                            (f = ++p && f && f[m] || (y = p = 0) || h.pop()) && ((s ? f.nodeName.toLowerCase() !== v : 1 !== f.nodeType) || !++y || (b && (d = f[I] || (f[I] = {}), u = d[f.uniqueID] || (d[f.uniqueID] = {}), u[e] = [H, y]), f !== t)););
                                    return (y -= o) === i || y % i == 0 && y / i >= 0
                                }
                            }
                        },
                        PSEUDO: function(e, n) {
                            var o, r = x.pseudos[e] || x.setFilters[e.toLowerCase()] || t.error("unsupported pseudo: " + e);
                            return r[I] ? r(n) : r.length > 1 ? (o = [e, e, "", n], x.setFilters.hasOwnProperty(e.toLowerCase()) ? i(function(e, t) {
                                for (var i, o = r(e, n), a = o.length; a--;) i = J(e, o[a]), e[i] = !(t[i] = o[a])
                            }) : function(e) {
                                return r(e, 0, o)
                            }) : r
                        }
                    },
                    pseudos: {
                        not: i(function(e) {
                            var t = [],
                                n = [],
                                o = S(e.replace(re, "$1"));
                            return o[I] ? i(function(e, t, n, i) {
                                for (var r, a = o(e, null, i, []), s = e.length; s--;)(r = a[s]) && (e[s] = !(t[s] = r))
                            }) : function(e, i, r) {
                                return t[0] = e, o(t, null, r, n), t[0] = null, !n.pop()
                            }
                        }),
                        has: i(function(e) {
                            return function(n) {
                                return t(e, n).length > 0
                            }
                        }),
                        contains: i(function(e) {
                            return e = e.replace(be, ye),
                                function(t) {
                                    return (t.textContent || t.innerText || w(t)).indexOf(e) > -1
                                }
                        }),
                        lang: i(function(e) {
                            return ue.test(e || "") || t.error("unsupported lang: " + e), e = e.replace(be, ye).toLowerCase(),
                                function(t) {
                                    var n;
                                    do {
                                        if (n = q ? t.lang : t.getAttribute("xml:lang") || t.getAttribute("lang")) return (n = n.toLowerCase()) === e || 0 === n.indexOf(e + "-")
                                    } while ((t = t.parentNode) && 1 === t.nodeType);
                                    return !1
                                }
                        }),
                        target: function(t) {
                            var n = e.location && e.location.hash;
                            return n && n.slice(1) === t.id
                        },
                        root: function(e) {
                            return e === j
                        },
                        focus: function(e) {
                            return e === F.activeElement && (!F.hasFocus || F.hasFocus()) && !!(e.type || e.href || ~e.tabIndex)
                        },
                        enabled: function(e) {
                            return !1 === e.disabled
                        },
                        disabled: function(e) {
                            return !0 === e.disabled
                        },
                        checked: function(e) {
                            var t = e.nodeName.toLowerCase();
                            return "input" === t && !!e.checked || "option" === t && !!e.selected
                        },
                        selected: function(e) {
                            return e.parentNode && e.parentNode.selectedIndex, !0 === e.selected
                        },
                        empty: function(e) {
                            for (e = e.firstChild; e; e = e.nextSibling)
                                if (e.nodeType < 6) return !1;
                            return !0
                        },
                        parent: function(e) {
                            return !x.pseudos.empty(e)
                        },
                        header: function(e) {
                            return pe.test(e.nodeName)
                        },
                        input: function(e) {
                            return fe.test(e.nodeName)
                        },
                        button: function(e) {
                            var t = e.nodeName.toLowerCase();
                            return "input" === t && "button" === e.type || "button" === t
                        },
                        text: function(e) {
                            var t;
                            return "input" === e.nodeName.toLowerCase() && "text" === e.type && (null == (t = e.getAttribute("type")) || "text" === t.toLowerCase())
                        },
                        first: s(function() {
                            return [0]
                        }),
                        last: s(function(e, t) {
                            return [t - 1]
                        }),
                        eq: s(function(e, t, n) {
                            return [0 > n ? n + t : n]
                        }),
                        even: s(function(e, t) {
                            for (var n = 0; t > n; n += 2) e.push(n);
                            return e
                        }),
                        odd: s(function(e, t) {
                            for (var n = 1; t > n; n += 2) e.push(n);
                            return e
                        }),
                        lt: s(function(e, t, n) {
                            for (var i = 0 > n ? n + t : n; --i >= 0;) e.push(i);
                            return e
                        }),
                        gt: s(function(e, t, n) {
                            for (var i = 0 > n ? n + t : n; ++i < t;) e.push(i);
                            return e
                        })
                    }
                }, x.pseudos.nth = x.pseudos.eq;
                for (b in {
                        radio: !0,
                        checkbox: !0,
                        file: !0,
                        password: !0,
                        image: !0
                    }) x.pseudos[b] = function(e) {
                    return function(t) {
                        return "input" === t.nodeName.toLowerCase() && t.type === e
                    }
                }(b);
                for (b in {
                        submit: !0,
                        reset: !0
                    }) x.pseudos[b] = function(e) {
                    return function(t) {
                        var n = t.nodeName.toLowerCase();
                        return ("input" === n || "button" === n) && t.type === e
                    }
                }(b);
                return c.prototype = x.filters = x.pseudos, x.setFilters = new c, k = t.tokenize = function(e, n) {
                    var i, o, r, a, s, l, c, u = V[e + " "];
                    if (u) return n ? 0 : u.slice(0);
                    for (s = e, l = [], c = x.preFilter; s;) {
                        i && !(o = ae.exec(s)) || (o && (s = s.slice(o[0].length) || s), l.push(r = [])), i = !1, (o = se.exec(s)) && (i = o.shift(), r.push({
                            value: i,
                            type: o[0].replace(re, " ")
                        }), s = s.slice(i.length));
                        for (a in x.filter) !(o = de[a].exec(s)) || c[a] && !(o = c[a](o)) || (i = o.shift(), r.push({
                            value: i,
                            type: a,
                            matches: o
                        }), s = s.slice(i.length));
                        if (!i) break
                    }
                    return n ? s.length : s ? t.error(e) : V(e, l).slice(0)
                }, S = t.compile = function(e, t) {
                    var n, i = [],
                        o = [],
                        r = B[e + " "];
                    if (!r) {
                        for (t || (t = k(e)), n = t.length; n--;) r = g(t[n]), r[I] ? i.push(r) : o.push(r);
                        r = B(e, v(o, i)), r.selector = e
                    }
                    return r
                }, T = t.select = function(e, t, n, i) {
                    var o, r, a, s, c, d = "function" == typeof e && e,
                        f = !i && k(e = d.selector || e);
                    if (n = n || [], 1 === f.length) {
                        if (r = f[0] = f[0].slice(0), r.length > 2 && "ID" === (a = r[0]).type && y.getById && 9 === t.nodeType && q && x.relative[r[1].type]) {
                            if (!(t = (x.find.ID(a.matches[0].replace(be, ye), t) || [])[0])) return n;
                            d && (t = t.parentNode), e = e.slice(r.shift().value.length)
                        }
                        for (o = de.needsContext.test(e) ? 0 : r.length; o-- && (a = r[o], !x.relative[s = a.type]);)
                            if ((c = x.find[s]) && (i = c(a.matches[0].replace(be, ye), ge.test(r[0].type) && l(t.parentNode) || t))) {
                                if (r.splice(o, 1), !(e = i.length && u(r))) return G.apply(n, i), n;
                                break
                            }
                    }
                    return (d || S(e, f))(i, t, !q, n, !t || ge.test(e) && l(t.parentNode) || t), n
                }, y.sortStable = I.split("").sort(W).join("") === I, y.detectDuplicates = !!D, O(), y.sortDetached = o(function(e) {
                    return 1 & e.compareDocumentPosition(F.createElement("div"))
                }), o(function(e) {
                    return e.innerHTML = "<a href='#'></a>", "#" === e.firstChild.getAttribute("href")
                }) || r("type|href|height|width", function(e, t, n) {
                    return n ? void 0 : e.getAttribute(t, "type" === t.toLowerCase() ? 1 : 2)
                }), y.attributes && o(function(e) {
                    return e.innerHTML = "<input/>", e.firstChild.setAttribute("value", ""), "" === e.firstChild.getAttribute("value")
                }) || r("value", function(e, t, n) {
                    return n || "input" !== e.nodeName.toLowerCase() ? void 0 : e.defaultValue
                }), o(function(e) {
                    return null == e.getAttribute("disabled")
                }) || r(Z, function(e, t, n) {
                    var i;
                    return n ? void 0 : !0 === e[t] ? t.toLowerCase() : (i = e.getAttributeNode(t)) && i.specified ? i.value : null
                }), t
            }(r);
            ue.find = me, ue.expr = me.selectors, ue.expr[":"] = ue.expr.pseudos, ue.uniqueSort = ue.unique = me.uniqueSort, ue.text = me.getText, ue.isXMLDoc = me.isXML, ue.contains = me.contains;
            var ge = function(e, t, n) {
                    for (var i = [], o = void 0 !== n;
                        (e = e[t]) && 9 !== e.nodeType;)
                        if (1 === e.nodeType) {
                            if (o && ue(e).is(n)) break;
                            i.push(e)
                        }
                    return i
                },
                ve = function(e, t) {
                    for (var n = []; e; e = e.nextSibling) 1 === e.nodeType && e !== t && n.push(e);
                    return n
                },
                be = ue.expr.match.needsContext,
                ye = /^<([\w-]+)\s*\/?>(?:<\/\1>|)$/,
                xe = /^.[^:#\[\.,]*$/;
            ue.filter = function(e, t, n) {
                var i = t[0];
                return n && (e = ":not(" + e + ")"), 1 === t.length && 1 === i.nodeType ? ue.find.matchesSelector(i, e) ? [i] : [] : ue.find.matches(e, ue.grep(t, function(e) {
                    return 1 === e.nodeType
                }))
            }, ue.fn.extend({
                find: function(e) {
                    var t, n = this.length,
                        i = [],
                        o = this;
                    if ("string" != typeof e) return this.pushStack(ue(e).filter(function() {
                        for (t = 0; n > t; t++)
                            if (ue.contains(o[t], this)) return !0
                    }));
                    for (t = 0; n > t; t++) ue.find(e, o[t], i);
                    return i = this.pushStack(n > 1 ? ue.unique(i) : i), i.selector = this.selector ? this.selector + " " + e : e, i
                },
                filter: function(e) {
                    return this.pushStack(l(this, e || [], !1))
                },
                not: function(e) {
                    return this.pushStack(l(this, e || [], !0))
                },
                is: function(e) {
                    return !!l(this, "string" == typeof e && be.test(e) ? ue(e) : e || [], !1).length
                }
            });
            var we, Ce = /^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]*))$/;
            (ue.fn.init = function(e, t, n) {
                var i, o;
                if (!e) return this;
                if (n = n || we, "string" == typeof e) {
                    if (!(i = "<" === e[0] && ">" === e[e.length - 1] && e.length >= 3 ? [null, e, null] : Ce.exec(e)) || !i[1] && t) return !t || t.jquery ? (t || n).find(e) : this.constructor(t).find(e);
                    if (i[1]) {
                        if (t = t instanceof ue ? t[0] : t, ue.merge(this, ue.parseHTML(i[1], t && t.nodeType ? t.ownerDocument || t : ee, !0)), ye.test(i[1]) && ue.isPlainObject(t))
                            for (i in t) ue.isFunction(this[i]) ? this[i](t[i]) : this.attr(i, t[i]);
                        return this
                    }
                    return o = ee.getElementById(i[2]), o && o.parentNode && (this.length = 1, this[0] = o), this.context = ee, this.selector = e, this
                }
                return e.nodeType ? (this.context = this[0] = e, this.length = 1, this) : ue.isFunction(e) ? void 0 !== n.ready ? n.ready(e) : e(ue) : (void 0 !== e.selector && (this.selector = e.selector, this.context = e.context), ue.makeArray(e, this))
            }).prototype = ue.fn, we = ue(ee);
            var ke = /^(?:parents|prev(?:Until|All))/,
                Se = {
                    children: !0,
                    contents: !0,
                    next: !0,
                    prev: !0
                };
            ue.fn.extend({
                has: function(e) {
                    var t = ue(e, this),
                        n = t.length;
                    return this.filter(function() {
                        for (var e = 0; n > e; e++)
                            if (ue.contains(this, t[e])) return !0
                    })
                },
                closest: function(e, t) {
                    for (var n, i = 0, o = this.length, r = [], a = be.test(e) || "string" != typeof e ? ue(e, t || this.context) : 0; o > i; i++)
                        for (n = this[i]; n && n !== t; n = n.parentNode)
                            if (n.nodeType < 11 && (a ? a.index(n) > -1 : 1 === n.nodeType && ue.find.matchesSelector(n, e))) {
                                r.push(n);
                                break
                            }
                    return this.pushStack(r.length > 1 ? ue.uniqueSort(r) : r)
                },
                index: function(e) {
                    return e ? "string" == typeof e ? oe.call(ue(e), this[0]) : oe.call(this, e.jquery ? e[0] : e) : this[0] && this[0].parentNode ? this.first().prevAll().length : -1
                },
                add: function(e, t) {
                    return this.pushStack(ue.uniqueSort(ue.merge(this.get(), ue(e, t))))
                },
                addBack: function(e) {
                    return this.add(null == e ? this.prevObject : this.prevObject.filter(e))
                }
            }), ue.each({
                parent: function(e) {
                    var t = e.parentNode;
                    return t && 11 !== t.nodeType ? t : null
                },
                parents: function(e) {
                    return ge(e, "parentNode")
                },
                parentsUntil: function(e, t, n) {
                    return ge(e, "parentNode", n)
                },
                next: function(e) {
                    return c(e, "nextSibling")
                },
                prev: function(e) {
                    return c(e, "previousSibling")
                },
                nextAll: function(e) {
                    return ge(e, "nextSibling")
                },
                prevAll: function(e) {
                    return ge(e, "previousSibling")
                },
                nextUntil: function(e, t, n) {
                    return ge(e, "nextSibling", n)
                },
                prevUntil: function(e, t, n) {
                    return ge(e, "previousSibling", n)
                },
                siblings: function(e) {
                    return ve((e.parentNode || {}).firstChild, e)
                },
                children: function(e) {
                    return ve(e.firstChild)
                },
                contents: function(e) {
                    return e.contentDocument || ue.merge([], e.childNodes)
                }
            }, function(e, t) {
                ue.fn[e] = function(n, i) {
                    var o = ue.map(this, t, n);
                    return "Until" !== e.slice(-5) && (i = n), i && "string" == typeof i && (o = ue.filter(i, o)), this.length > 1 && (Se[e] || ue.uniqueSort(o), ke.test(e) && o.reverse()), this.pushStack(o)
                }
            });
            var Te = /\S+/g;
            ue.Callbacks = function(e) {
                e = "string" == typeof e ? u(e) : ue.extend({}, e);
                var t, n, i, o, r = [],
                    a = [],
                    s = -1,
                    l = function() {
                        for (o = e.once, i = t = !0; a.length; s = -1)
                            for (n = a.shift(); ++s < r.length;) !1 === r[s].apply(n[0], n[1]) && e.stopOnFalse && (s = r.length, n = !1);
                        e.memory || (n = !1), t = !1, o && (r = n ? [] : "")
                    },
                    c = {
                        add: function() {
                            return r && (n && !t && (s = r.length - 1, a.push(n)), function t(n) {
                                ue.each(n, function(n, i) {
                                    ue.isFunction(i) ? e.unique && c.has(i) || r.push(i) : i && i.length && "string" !== ue.type(i) && t(i)
                                })
                            }(arguments), n && !t && l()), this
                        },
                        remove: function() {
                            return ue.each(arguments, function(e, t) {
                                for (var n;
                                    (n = ue.inArray(t, r, n)) > -1;) r.splice(n, 1), s >= n && s--
                            }), this
                        },
                        has: function(e) {
                            return e ? ue.inArray(e, r) > -1 : r.length > 0
                        },
                        empty: function() {
                            return r && (r = []), this
                        },
                        disable: function() {
                            return o = a = [], r = n = "", this
                        },
                        disabled: function() {
                            return !r
                        },
                        lock: function() {
                            return o = a = [], n || (r = n = ""), this
                        },
                        locked: function() {
                            return !!o
                        },
                        fireWith: function(e, n) {
                            return o || (n = n || [], n = [e, n.slice ? n.slice() : n], a.push(n), t || l()), this
                        },
                        fire: function() {
                            return c.fireWith(this, arguments), this
                        },
                        fired: function() {
                            return !!i
                        }
                    };
                return c
            }, ue.extend({
                Deferred: function(e) {
                    var t = [
                            ["resolve", "done", ue.Callbacks("once memory"), "resolved"],
                            ["reject", "fail", ue.Callbacks("once memory"), "rejected"],
                            ["notify", "progress", ue.Callbacks("memory")]
                        ],
                        n = "pending",
                        i = {
                            state: function() {
                                return n
                            },
                            always: function() {
                                return o.done(arguments).fail(arguments), this
                            },
                            then: function() {
                                var e = arguments;
                                return ue.Deferred(function(n) {
                                    ue.each(t, function(t, r) {
                                        var a = ue.isFunction(e[t]) && e[t];
                                        o[r[1]](function() {
                                            var e = a && a.apply(this, arguments);
                                            e && ue.isFunction(e.promise) ? e.promise().progress(n.notify).done(n.resolve).fail(n.reject) : n[r[0] + "With"](this === i ? n.promise() : this, a ? [e] : arguments)
                                        })
                                    }), e = null
                                }).promise()
                            },
                            promise: function(e) {
                                return null != e ? ue.extend(e, i) : i
                            }
                        },
                        o = {};
                    return i.pipe = i.then, ue.each(t, function(e, r) {
                        var a = r[2],
                            s = r[3];
                        i[r[1]] = a.add, s && a.add(function() {
                            n = s
                        }, t[1 ^ e][2].disable, t[2][2].lock), o[r[0]] = function() {
                            return o[r[0] + "With"](this === o ? i : this, arguments), this
                        }, o[r[0] + "With"] = a.fireWith
                    }), i.promise(o), e && e.call(o, o), o
                },
                when: function(e) {
                    var t, n, i, o = 0,
                        r = te.call(arguments),
                        a = r.length,
                        s = 1 !== a || e && ue.isFunction(e.promise) ? a : 0,
                        l = 1 === s ? e : ue.Deferred(),
                        c = function(e, n, i) {
                            return function(o) {
                                n[e] = this, i[e] = arguments.length > 1 ? te.call(arguments) : o, i === t ? l.notifyWith(n, i) : --s || l.resolveWith(n, i)
                            }
                        };
                    if (a > 1)
                        for (t = new Array(a), n = new Array(a), i = new Array(a); a > o; o++) r[o] && ue.isFunction(r[o].promise) ? r[o].promise().progress(c(o, n, t)).done(c(o, i, r)).fail(l.reject) : --s;
                    return s || l.resolveWith(i, r), l.promise()
                }
            });
            var Ae;
            ue.fn.ready = function(e) {
                return ue.ready.promise().done(e), this
            }, ue.extend({
                isReady: !1,
                readyWait: 1,
                holdReady: function(e) {
                    e ? ue.readyWait++ : ue.ready(!0)
                },
                ready: function(e) {
                    (!0 === e ? --ue.readyWait : ue.isReady) || (ue.isReady = !0, !0 !== e && --ue.readyWait > 0 || (Ae.resolveWith(ee, [ue]), ue.fn.triggerHandler && (ue(ee).triggerHandler("ready"), ue(ee).off("ready"))))
                }
            }), ue.ready.promise = function(e) {
                return Ae || (Ae = ue.Deferred(), "complete" === ee.readyState || "loading" !== ee.readyState && !ee.documentElement.doScroll ? r.setTimeout(ue.ready) : (ee.addEventListener("DOMContentLoaded", d), r.addEventListener("load", d))), Ae.promise(e)
            }, ue.ready.promise();
            var Ee = function(e, t, n, i, o, r, a) {
                    var s = 0,
                        l = e.length,
                        c = null == n;
                    if ("object" === ue.type(n)) {
                        o = !0;
                        for (s in n) Ee(e, t, s, n[s], !0, r, a)
                    } else if (void 0 !== i && (o = !0, ue.isFunction(i) || (a = !0), c && (a ? (t.call(e, i), t = null) : (c = t, t = function(e, t, n) {
                            return c.call(ue(e), n)
                        })), t))
                        for (; l > s; s++) t(e[s], n, a ? i : i.call(e[s], s, t(e[s], n)));
                    return o ? e : c ? t.call(e) : l ? t(e[0], n) : r
                },
                De = function(e) {
                    return 1 === e.nodeType || 9 === e.nodeType || !+e.nodeType
                };
            f.uid = 1, f.prototype = {
                register: function(e, t) {
                    var n = t || {};
                    return e.nodeType ? e[this.expando] = n : Object.defineProperty(e, this.expando, {
                        value: n,
                        writable: !0,
                        configurable: !0
                    }), e[this.expando]
                },
                cache: function(e) {
                    if (!De(e)) return {};
                    var t = e[this.expando];
                    return t || (t = {}, De(e) && (e.nodeType ? e[this.expando] = t : Object.defineProperty(e, this.expando, {
                        value: t,
                        configurable: !0
                    }))), t
                },
                set: function(e, t, n) {
                    var i, o = this.cache(e);
                    if ("string" == typeof t) o[t] = n;
                    else
                        for (i in t) o[i] = t[i];
                    return o
                },
                get: function(e, t) {
                    return void 0 === t ? this.cache(e) : e[this.expando] && e[this.expando][t]
                },
                access: function(e, t, n) {
                    var i;
                    return void 0 === t || t && "string" == typeof t && void 0 === n ? (i = this.get(e, t), void 0 !== i ? i : this.get(e, ue.camelCase(t))) : (this.set(e, t, n), void 0 !== n ? n : t)
                },
                remove: function(e, t) {
                    var n, i, o, r = e[this.expando];
                    if (void 0 !== r) {
                        if (void 0 === t) this.register(e);
                        else {
                            ue.isArray(t) ? i = t.concat(t.map(ue.camelCase)) : (o = ue.camelCase(t), t in r ? i = [t, o] : (i = o, i = i in r ? [i] : i.match(Te) || [])), n = i.length;
                            for (; n--;) delete r[i[n]]
                        }(void 0 === t || ue.isEmptyObject(r)) && (e.nodeType ? e[this.expando] = void 0 : delete e[this.expando])
                    }
                },
                hasData: function(e) {
                    var t = e[this.expando];
                    return void 0 !== t && !ue.isEmptyObject(t)
                }
            };
            var Oe = new f,
                Fe = new f,
                je = /^(?:\{[\w\W]*\}|\[[\w\W]*\])$/,
                qe = /[A-Z]/g;
            ue.extend({
                hasData: function(e) {
                    return Fe.hasData(e) || Oe.hasData(e)
                },
                data: function(e, t, n) {
                    return Fe.access(e, t, n)
                },
                removeData: function(e, t) {
                    Fe.remove(e, t)
                },
                _data: function(e, t, n) {
                    return Oe.access(e, t, n)
                },
                _removeData: function(e, t) {
                    Oe.remove(e, t)
                }
            }), ue.fn.extend({
                data: function(e, t) {
                    var n, i, o, r = this[0],
                        a = r && r.attributes;
                    if (void 0 === e) {
                        if (this.length && (o = Fe.get(r), 1 === r.nodeType && !Oe.get(r, "hasDataAttrs"))) {
                            for (n = a.length; n--;) a[n] && (i = a[n].name, 0 === i.indexOf("data-") && (i = ue.camelCase(i.slice(5)), p(r, i, o[i])));
                            Oe.set(r, "hasDataAttrs", !0)
                        }
                        return o
                    }
                    return "object" == typeof e ? this.each(function() {
                        Fe.set(this, e)
                    }) : Ee(this, function(t) {
                        var n, i;
                        if (r && void 0 === t) {
                            if (void 0 !== (n = Fe.get(r, e) || Fe.get(r, e.replace(qe, "-$&").toLowerCase()))) return n;
                            if (i = ue.camelCase(e), void 0 !== (n = Fe.get(r, i))) return n;
                            if (void 0 !== (n = p(r, i, void 0))) return n
                        } else i = ue.camelCase(e), this.each(function() {
                            var n = Fe.get(this, i);
                            Fe.set(this, i, t), e.indexOf("-") > -1 && void 0 !== n && Fe.set(this, e, t)
                        })
                    }, null, t, arguments.length > 1, null, !0)
                },
                removeData: function(e) {
                    return this.each(function() {
                        Fe.remove(this, e)
                    })
                }
            }), ue.extend({
                queue: function(e, t, n) {
                    var i;
                    return e ? (t = (t || "fx") + "queue", i = Oe.get(e, t), n && (!i || ue.isArray(n) ? i = Oe.access(e, t, ue.makeArray(n)) : i.push(n)), i || []) : void 0
                },
                dequeue: function(e, t) {
                    t = t || "fx";
                    var n = ue.queue(e, t),
                        i = n.length,
                        o = n.shift(),
                        r = ue._queueHooks(e, t),
                        a = function() {
                            ue.dequeue(e, t)
                        };
                    "inprogress" === o && (o = n.shift(), i--), o && ("fx" === t && n.unshift("inprogress"), delete r.stop, o.call(e, a, r)), !i && r && r.empty.fire()
                },
                _queueHooks: function(e, t) {
                    var n = t + "queueHooks";
                    return Oe.get(e, n) || Oe.access(e, n, {
                        empty: ue.Callbacks("once memory").add(function() {
                            Oe.remove(e, [t + "queue", n])
                        })
                    })
                }
            }), ue.fn.extend({
                queue: function(e, t) {
                    var n = 2;
                    return "string" != typeof e && (t = e, e = "fx", n--), arguments.length < n ? ue.queue(this[0], e) : void 0 === t ? this : this.each(function() {
                        var n = ue.queue(this, e, t);
                        ue._queueHooks(this, e), "fx" === e && "inprogress" !== n[0] && ue.dequeue(this, e)
                    })
                },
                dequeue: function(e) {
                    return this.each(function() {
                        ue.dequeue(this, e)
                    })
                },
                clearQueue: function(e) {
                    return this.queue(e || "fx", [])
                },
                promise: function(e, t) {
                    var n, i = 1,
                        o = ue.Deferred(),
                        r = this,
                        a = this.length,
                        s = function() {
                            --i || o.resolveWith(r, [r])
                        };
                    for ("string" != typeof e && (t = e, e = void 0), e = e || "fx"; a--;)(n = Oe.get(r[a], e + "queueHooks")) && n.empty && (i++, n.empty.add(s));
                    return s(), o.promise(t)
                }
            });
            var Le = /[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source,
                Ne = new RegExp("^(?:([+-])=|)(" + Le + ")([a-z%]*)$", "i"),
                Pe = ["Top", "Right", "Bottom", "Left"],
                Re = function(e, t) {
                    return e = t || e, "none" === ue.css(e, "display") || !ue.contains(e.ownerDocument, e)
                },
                Ie = /^(?:checkbox|radio)$/i,
                Me = /<([\w:-]+)/,
                He = /^$|\/(?:java|ecma)script/i,
                ze = {
                    option: [1, "<select multiple='multiple'>", "</select>"],
                    thead: [1, "<table>", "</table>"],
                    col: [2, "<table><colgroup>", "</colgroup></table>"],
                    tr: [2, "<table><tbody>", "</tbody></table>"],
                    td: [3, "<table><tbody><tr>", "</tr></tbody></table>"],
                    _default: [0, "", ""]
                };
            ze.optgroup = ze.option, ze.tbody = ze.tfoot = ze.colgroup = ze.caption = ze.thead, ze.th = ze.td;
            var $e = /<|&#?\w+;/;
            ! function() {
                var e = ee.createDocumentFragment(),
                    t = e.appendChild(ee.createElement("div")),
                    n = ee.createElement("input");
                n.setAttribute("type", "radio"), n.setAttribute("checked", "checked"), n.setAttribute("name", "t"), t.appendChild(n), le.checkClone = t.cloneNode(!0).cloneNode(!0).lastChild.checked, t.innerHTML = "<textarea>x</textarea>", le.noCloneChecked = !!t.cloneNode(!0).lastChild.defaultValue
            }();
            var Ve = /^key/,
                Be = /^(?:mouse|pointer|contextmenu|drag|drop)|click/,
                We = /^([^.]*)(?:\.(.+)|)/;
            ue.event = {
                global: {},
                add: function(e, t, n, i, o) {
                    var r, a, s, l, c, u, d, f, p, h, m, g = Oe.get(e);
                    if (g)
                        for (n.handler && (r = n, n = r.handler, o = r.selector), n.guid || (n.guid = ue.guid++), (l = g.events) || (l = g.events = {}), (a = g.handle) || (a = g.handle = function(t) {
                                return void 0 !== ue && ue.event.triggered !== t.type ? ue.event.dispatch.apply(e, arguments) : void 0
                            }), t = (t || "").match(Te) || [""], c = t.length; c--;) s = We.exec(t[c]) || [], p = m = s[1], h = (s[2] || "").split(".").sort(), p && (d = ue.event.special[p] || {}, p = (o ? d.delegateType : d.bindType) || p, d = ue.event.special[p] || {}, u = ue.extend({
                            type: p,
                            origType: m,
                            data: i,
                            handler: n,
                            guid: n.guid,
                            selector: o,
                            needsContext: o && ue.expr.match.needsContext.test(o),
                            namespace: h.join(".")
                        }, r), (f = l[p]) || (f = l[p] = [], f.delegateCount = 0, d.setup && !1 !== d.setup.call(e, i, h, a) || e.addEventListener && e.addEventListener(p, a)), d.add && (d.add.call(e, u), u.handler.guid || (u.handler.guid = n.guid)), o ? f.splice(f.delegateCount++, 0, u) : f.push(u), ue.event.global[p] = !0)
                },
                remove: function(e, t, n, i, o) {
                    var r, a, s, l, c, u, d, f, p, h, m, g = Oe.hasData(e) && Oe.get(e);
                    if (g && (l = g.events)) {
                        for (t = (t || "").match(Te) || [""], c = t.length; c--;)
                            if (s = We.exec(t[c]) || [], p = m = s[1], h = (s[2] || "").split(".").sort(), p) {
                                for (d = ue.event.special[p] || {}, p = (i ? d.delegateType : d.bindType) || p, f = l[p] || [], s = s[2] && new RegExp("(^|\\.)" + h.join("\\.(?:.*\\.|)") + "(\\.|$)"), a = r = f.length; r--;) u = f[r], !o && m !== u.origType || n && n.guid !== u.guid || s && !s.test(u.namespace) || i && i !== u.selector && ("**" !== i || !u.selector) || (f.splice(r, 1), u.selector && f.delegateCount--, d.remove && d.remove.call(e, u));
                                a && !f.length && (d.teardown && !1 !== d.teardown.call(e, h, g.handle) || ue.removeEvent(e, p, g.handle), delete l[p])
                            } else
                                for (p in l) ue.event.remove(e, p + t[c], n, i, !0);
                        ue.isEmptyObject(l) && Oe.remove(e, "handle events")
                    }
                },
                dispatch: function(e) {
                    e = ue.event.fix(e);
                    var t, n, i, o, r, a = [],
                        s = te.call(arguments),
                        l = (Oe.get(this, "events") || {})[e.type] || [],
                        c = ue.event.special[e.type] || {};
                    if (s[0] = e, e.delegateTarget = this, !c.preDispatch || !1 !== c.preDispatch.call(this, e)) {
                        for (a = ue.event.handlers.call(this, e, l), t = 0;
                            (o = a[t++]) && !e.isPropagationStopped();)
                            for (e.currentTarget = o.elem, n = 0;
                                (r = o.handlers[n++]) && !e.isImmediatePropagationStopped();) e.rnamespace && !e.rnamespace.test(r.namespace) || (e.handleObj = r, e.data = r.data, void 0 !== (i = ((ue.event.special[r.origType] || {}).handle || r.handler).apply(o.elem, s)) && !1 === (e.result = i) && (e.preventDefault(), e.stopPropagation()));
                        return c.postDispatch && c.postDispatch.call(this, e), e.result
                    }
                },
                handlers: function(e, t) {
                    var n, i, o, r, a = [],
                        s = t.delegateCount,
                        l = e.target;
                    if (s && l.nodeType && ("click" !== e.type || isNaN(e.button) || e.button < 1))
                        for (; l !== this; l = l.parentNode || this)
                            if (1 === l.nodeType && (!0 !== l.disabled || "click" !== e.type)) {
                                for (i = [], n = 0; s > n; n++) r = t[n], o = r.selector + " ", void 0 === i[o] && (i[o] = r.needsContext ? ue(o, this).index(l) > -1 : ue.find(o, this, null, [l]).length), i[o] && i.push(r);
                                i.length && a.push({
                                    elem: l,
                                    handlers: i
                                })
                            }
                    return s < t.length && a.push({
                        elem: this,
                        handlers: t.slice(s)
                    }), a
                },
                props: "altKey bubbles cancelable ctrlKey currentTarget detail eventPhase metaKey relatedTarget shiftKey target timeStamp view which".split(" "),
                fixHooks: {},
                keyHooks: {
                    props: "char charCode key keyCode".split(" "),
                    filter: function(e, t) {
                        return null == e.which && (e.which = null != t.charCode ? t.charCode : t.keyCode), e
                    }
                },
                mouseHooks: {
                    props: "button buttons clientX clientY offsetX offsetY pageX pageY screenX screenY toElement".split(" "),
                    filter: function(e, t) {
                        var n, i, o, r = t.button;
                        return null == e.pageX && null != t.clientX && (n = e.target.ownerDocument || ee, i = n.documentElement, o = n.body, e.pageX = t.clientX + (i && i.scrollLeft || o && o.scrollLeft || 0) - (i && i.clientLeft || o && o.clientLeft || 0), e.pageY = t.clientY + (i && i.scrollTop || o && o.scrollTop || 0) - (i && i.clientTop || o && o.clientTop || 0)), e.which || void 0 === r || (e.which = 1 & r ? 1 : 2 & r ? 3 : 4 & r ? 2 : 0), e
                    }
                },
                fix: function(e) {
                    if (e[ue.expando]) return e;
                    var t, n, i, o = e.type,
                        r = e,
                        a = this.fixHooks[o];
                    for (a || (this.fixHooks[o] = a = Be.test(o) ? this.mouseHooks : Ve.test(o) ? this.keyHooks : {}), i = a.props ? this.props.concat(a.props) : this.props, e = new ue.Event(r), t = i.length; t--;) n = i[t], e[n] = r[n];
                    return e.target || (e.target = ee), 3 === e.target.nodeType && (e.target = e.target.parentNode), a.filter ? a.filter(e, r) : e
                },
                special: {
                    load: {
                        noBubble: !0
                    },
                    focus: {
                        trigger: function() {
                            return this !== x() && this.focus ? (this.focus(), !1) : void 0
                        },
                        delegateType: "focusin"
                    },
                    blur: {
                        trigger: function() {
                            return this === x() && this.blur ? (this.blur(), !1) : void 0
                        },
                        delegateType: "focusout"
                    },
                    click: {
                        trigger: function() {
                            return "checkbox" === this.type && this.click && ue.nodeName(this, "input") ? (this.click(), !1) : void 0
                        },
                        _default: function(e) {
                            return ue.nodeName(e.target, "a")
                        }
                    },
                    beforeunload: {
                        postDispatch: function(e) {
                            void 0 !== e.result && e.originalEvent && (e.originalEvent.returnValue = e.result)
                        }
                    }
                }
            }, ue.removeEvent = function(e, t, n) {
                e.removeEventListener && e.removeEventListener(t, n)
            }, ue.Event = function(e, t) {
                return this instanceof ue.Event ? (e && e.type ? (this.originalEvent = e, this.type = e.type, this.isDefaultPrevented = e.defaultPrevented || void 0 === e.defaultPrevented && !1 === e.returnValue ? b : y) : this.type = e, t && ue.extend(this, t), this.timeStamp = e && e.timeStamp || ue.now(), void(this[ue.expando] = !0)) : new ue.Event(e, t)
            }, ue.Event.prototype = {
                constructor: ue.Event,
                isDefaultPrevented: y,
                isPropagationStopped: y,
                isImmediatePropagationStopped: y,
                isSimulated: !1,
                preventDefault: function() {
                    var e = this.originalEvent;
                    this.isDefaultPrevented = b, e && !this.isSimulated && e.preventDefault()
                },
                stopPropagation: function() {
                    var e = this.originalEvent;
                    this.isPropagationStopped = b, e && !this.isSimulated && e.stopPropagation()
                },
                stopImmediatePropagation: function() {
                    var e = this.originalEvent;
                    this.isImmediatePropagationStopped = b, e && !this.isSimulated && e.stopImmediatePropagation(), this.stopPropagation()
                }
            }, ue.each({
                mouseenter: "mouseover",
                mouseleave: "mouseout",
                pointerenter: "pointerover",
                pointerleave: "pointerout"
            }, function(e, t) {
                ue.event.special[e] = {
                    delegateType: t,
                    bindType: t,
                    handle: function(e) {
                        var n, i = this,
                            o = e.relatedTarget,
                            r = e.handleObj;
                        return o && (o === i || ue.contains(i, o)) || (e.type = r.origType, n = r.handler.apply(this, arguments), e.type = t), n
                    }
                }
            }), ue.fn.extend({
                on: function(e, t, n, i) {
                    return w(this, e, t, n, i)
                },
                one: function(e, t, n, i) {
                    return w(this, e, t, n, i, 1)
                },
                off: function(e, t, n) {
                    var i, o;
                    if (e && e.preventDefault && e.handleObj) return i = e.handleObj, ue(e.delegateTarget).off(i.namespace ? i.origType + "." + i.namespace : i.origType, i.selector, i.handler), this;
                    if ("object" == typeof e) {
                        for (o in e) this.off(o, t, e[o]);
                        return this
                    }
                    return !1 !== t && "function" != typeof t || (n = t, t = void 0), !1 === n && (n = y), this.each(function() {
                        ue.event.remove(this, e, n, t)
                    })
                }
            });
            var Ue = /<(?!area|br|col|embed|hr|img|input|link|meta|param)(([\w:-]+)[^>]*)\/>/gi,
                _e = /<script|<style|<link/i,
                Xe = /checked\s*(?:[^=]|=\s*.checked.)/i,
                Qe = /^true\/(.*)/,
                Ye = /^\s*<!(?:\[CDATA\[|--)|(?:\]\]|--)>\s*$/g;
            ue.extend({
                htmlPrefilter: function(e) {
                    return e.replace(Ue, "<$1></$2>")
                },
                clone: function(e, t, n) {
                    var i, o, r, a, s = e.cloneNode(!0),
                        l = ue.contains(e.ownerDocument, e);
                    if (!(le.noCloneChecked || 1 !== e.nodeType && 11 !== e.nodeType || ue.isXMLDoc(e)))
                        for (a = m(s), r = m(e), i = 0, o = r.length; o > i; i++) A(r[i], a[i]);
                    if (t)
                        if (n)
                            for (r = r || m(e), a = a || m(s), i = 0, o = r.length; o > i; i++) T(r[i], a[i]);
                        else T(e, s);
                    return a = m(s, "script"), a.length > 0 && g(a, !l && m(e, "script")), s
                },
                cleanData: function(e) {
                    for (var t, n, i, o = ue.event.special, r = 0; void 0 !== (n = e[r]); r++)
                        if (De(n)) {
                            if (t = n[Oe.expando]) {
                                if (t.events)
                                    for (i in t.events) o[i] ? ue.event.remove(n, i) : ue.removeEvent(n, i, t.handle);
                                n[Oe.expando] = void 0
                            }
                            n[Fe.expando] && (n[Fe.expando] = void 0)
                        }
                }
            }), ue.fn.extend({
                domManip: E,
                detach: function(e) {
                    return D(this, e, !0)
                },
                remove: function(e) {
                    return D(this, e)
                },
                text: function(e) {
                    return Ee(this, function(e) {
                        return void 0 === e ? ue.text(this) : this.empty().each(function() {
                            1 !== this.nodeType && 11 !== this.nodeType && 9 !== this.nodeType || (this.textContent = e)
                        })
                    }, null, e, arguments.length)
                },
                append: function() {
                    return E(this, arguments, function(e) {
                        if (1 === this.nodeType || 11 === this.nodeType || 9 === this.nodeType) {
                            C(this, e).appendChild(e)
                        }
                    })
                },
                prepend: function() {
                    return E(this, arguments, function(e) {
                        if (1 === this.nodeType || 11 === this.nodeType || 9 === this.nodeType) {
                            var t = C(this, e);
                            t.insertBefore(e, t.firstChild)
                        }
                    })
                },
                before: function() {
                    return E(this, arguments, function(e) {
                        this.parentNode && this.parentNode.insertBefore(e, this)
                    })
                },
                after: function() {
                    return E(this, arguments, function(e) {
                        this.parentNode && this.parentNode.insertBefore(e, this.nextSibling)
                    })
                },
                empty: function() {
                    for (var e, t = 0; null != (e = this[t]); t++) 1 === e.nodeType && (ue.cleanData(m(e, !1)), e.textContent = "");
                    return this
                },
                clone: function(e, t) {
                    return e = null != e && e, t = null == t ? e : t, this.map(function() {
                        return ue.clone(this, e, t)
                    })
                },
                html: function(e) {
                    return Ee(this, function(e) {
                        var t = this[0] || {},
                            n = 0,
                            i = this.length;
                        if (void 0 === e && 1 === t.nodeType) return t.innerHTML;
                        if ("string" == typeof e && !_e.test(e) && !ze[(Me.exec(e) || ["", ""])[1].toLowerCase()]) {
                            e = ue.htmlPrefilter(e);
                            try {
                                for (; i > n; n++) t = this[n] || {}, 1 === t.nodeType && (ue.cleanData(m(t, !1)), t.innerHTML = e);
                                t = 0
                            } catch (e) {}
                        }
                        t && this.empty().append(e)
                    }, null, e, arguments.length)
                },
                replaceWith: function() {
                    var e = [];
                    return E(this, arguments, function(t) {
                        var n = this.parentNode;
                        ue.inArray(this, e) < 0 && (ue.cleanData(m(this)), n && n.replaceChild(t, this))
                    }, e)
                }
            }), ue.each({
                appendTo: "append",
                prependTo: "prepend",
                insertBefore: "before",
                insertAfter: "after",
                replaceAll: "replaceWith"
            }, function(e, t) {
                ue.fn[e] = function(e) {
                    for (var n, i = [], o = ue(e), r = o.length - 1, a = 0; r >= a; a++) n = a === r ? this : this.clone(!0), ue(o[a])[t](n), ie.apply(i, n.get());
                    return this.pushStack(i)
                }
            });
            var Ge, Ke = {
                    HTML: "block",
                    BODY: "block"
                },
                Je = /^margin/,
                Ze = new RegExp("^(" + Le + ")(?!px)[a-z%]+$", "i"),
                et = function(e) {
                    var t = e.ownerDocument.defaultView;
                    return t && t.opener || (t = r), t.getComputedStyle(e)
                },
                tt = function(e, t, n, i) {
                    var o, r, a = {};
                    for (r in t) a[r] = e.style[r], e.style[r] = t[r];
                    o = n.apply(e, i || []);
                    for (r in t) e.style[r] = a[r];
                    return o
                },
                nt = ee.documentElement;
            ! function() {
                function e() {
                    s.style.cssText = "-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;position:relative;display:block;margin:auto;border:1px;padding:1px;top:1%;width:50%", s.innerHTML = "", nt.appendChild(a);
                    var e = r.getComputedStyle(s);
                    t = "1%" !== e.top, o = "2px" === e.marginLeft, n = "4px" === e.width, s.style.marginRight = "50%", i = "4px" === e.marginRight, nt.removeChild(a)
                }
                var t, n, i, o, a = ee.createElement("div"),
                    s = ee.createElement("div");
                s.style && (s.style.backgroundClip = "content-box", s.cloneNode(!0).style.backgroundClip = "", le.clearCloneStyle = "content-box" === s.style.backgroundClip, a.style.cssText = "border:0;width:8px;height:0;top:0;left:-9999px;padding:0;margin-top:1px;position:absolute", a.appendChild(s), ue.extend(le, {
                    pixelPosition: function() {
                        return e(), t
                    },
                    boxSizingReliable: function() {
                        return null == n && e(), n
                    },
                    pixelMarginRight: function() {
                        return null == n && e(), i
                    },
                    reliableMarginLeft: function() {
                        return null == n && e(), o
                    },
                    reliableMarginRight: function() {
                        var e, t = s.appendChild(ee.createElement("div"));
                        return t.style.cssText = s.style.cssText = "-webkit-box-sizing:content-box;box-sizing:content-box;display:block;margin:0;border:0;padding:0", t.style.marginRight = t.style.width = "0", s.style.width = "1px", nt.appendChild(a), e = !parseFloat(r.getComputedStyle(t).marginRight), nt.removeChild(a), s.removeChild(t), e
                    }
                }))
            }();
            var it = /^(none|table(?!-c[ea]).+)/,
                ot = {
                    position: "absolute",
                    visibility: "hidden",
                    display: "block"
                },
                rt = {
                    letterSpacing: "0",
                    fontWeight: "400"
                },
                at = ["Webkit", "O", "Moz", "ms"],
                st = ee.createElement("div").style;
            ue.extend({
                cssHooks: {
                    opacity: {
                        get: function(e, t) {
                            if (t) {
                                var n = j(e, "opacity");
                                return "" === n ? "1" : n
                            }
                        }
                    }
                },
                cssNumber: {
                    animationIterationCount: !0,
                    columnCount: !0,
                    fillOpacity: !0,
                    flexGrow: !0,
                    flexShrink: !0,
                    fontWeight: !0,
                    lineHeight: !0,
                    opacity: !0,
                    order: !0,
                    orphans: !0,
                    widows: !0,
                    zIndex: !0,
                    zoom: !0
                },
                cssProps: {
                    float: "cssFloat"
                },
                style: function(e, t, n, i) {
                    if (e && 3 !== e.nodeType && 8 !== e.nodeType && e.style) {
                        var o, r, a, s = ue.camelCase(t),
                            l = e.style;
                        return t = ue.cssProps[s] || (ue.cssProps[s] = L(s) || s), a = ue.cssHooks[t] || ue.cssHooks[s], void 0 === n ? a && "get" in a && void 0 !== (o = a.get(e, !1, i)) ? o : l[t] : (r = typeof n, "string" === r && (o = Ne.exec(n)) && o[1] && (n = h(e, t, o), r = "number"), void(null != n && n === n && ("number" === r && (n += o && o[3] || (ue.cssNumber[s] ? "" : "px")), le.clearCloneStyle || "" !== n || 0 !== t.indexOf("background") || (l[t] = "inherit"), a && "set" in a && void 0 === (n = a.set(e, n, i)) || (l[t] = n))))
                    }
                },
                css: function(e, t, n, i) {
                    var o, r, a, s = ue.camelCase(t);
                    return t = ue.cssProps[s] || (ue.cssProps[s] = L(s) || s), a = ue.cssHooks[t] || ue.cssHooks[s], a && "get" in a && (o = a.get(e, !0, n)), void 0 === o && (o = j(e, t, i)), "normal" === o && t in rt && (o = rt[t]), "" === n || n ? (r = parseFloat(o), !0 === n || isFinite(r) ? r || 0 : o) : o
                }
            }), ue.each(["height", "width"], function(e, t) {
                ue.cssHooks[t] = {
                    get: function(e, n, i) {
                        return n ? it.test(ue.css(e, "display")) && 0 === e.offsetWidth ? tt(e, ot, function() {
                            return R(e, t, i)
                        }) : R(e, t, i) : void 0
                    },
                    set: function(e, n, i) {
                        var o, r = i && et(e),
                            a = i && P(e, t, i, "border-box" === ue.css(e, "boxSizing", !1, r), r);
                        return a && (o = Ne.exec(n)) && "px" !== (o[3] || "px") && (e.style[t] = n, n = ue.css(e, t)), N(e, n, a)
                    }
                }
            }), ue.cssHooks.marginLeft = q(le.reliableMarginLeft, function(e, t) {
                return t ? (parseFloat(j(e, "marginLeft")) || e.getBoundingClientRect().left - tt(e, {
                    marginLeft: 0
                }, function() {
                    return e.getBoundingClientRect().left
                })) + "px" : void 0
            }), ue.cssHooks.marginRight = q(le.reliableMarginRight, function(e, t) {
                return t ? tt(e, {
                    display: "inline-block"
                }, j, [e, "marginRight"]) : void 0
            }), ue.each({
                margin: "",
                padding: "",
                border: "Width"
            }, function(e, t) {
                ue.cssHooks[e + t] = {
                    expand: function(n) {
                        for (var i = 0, o = {}, r = "string" == typeof n ? n.split(" ") : [n]; 4 > i; i++) o[e + Pe[i] + t] = r[i] || r[i - 2] || r[0];
                        return o
                    }
                }, Je.test(e) || (ue.cssHooks[e + t].set = N)
            }), ue.fn.extend({
                css: function(e, t) {
                    return Ee(this, function(e, t, n) {
                        var i, o, r = {},
                            a = 0;
                        if (ue.isArray(t)) {
                            for (i = et(e), o = t.length; o > a; a++) r[t[a]] = ue.css(e, t[a], !1, i);
                            return r
                        }
                        return void 0 !== n ? ue.style(e, t, n) : ue.css(e, t)
                    }, e, t, arguments.length > 1)
                },
                show: function() {
                    return I(this, !0)
                },
                hide: function() {
                    return I(this)
                },
                toggle: function(e) {
                    return "boolean" == typeof e ? e ? this.show() : this.hide() : this.each(function() {
                        Re(this) ? ue(this).show() : ue(this).hide()
                    })
                }
            }), ue.Tween = M, M.prototype = {
                constructor: M,
                init: function(e, t, n, i, o, r) {
                    this.elem = e, this.prop = n, this.easing = o || ue.easing._default, this.options = t, this.start = this.now = this.cur(), this.end = i, this.unit = r || (ue.cssNumber[n] ? "" : "px")
                },
                cur: function() {
                    var e = M.propHooks[this.prop];
                    return e && e.get ? e.get(this) : M.propHooks._default.get(this)
                },
                run: function(e) {
                    var t, n = M.propHooks[this.prop];
                    return this.options.duration ? this.pos = t = ue.easing[this.easing](e, this.options.duration * e, 0, 1, this.options.duration) : this.pos = t = e, this.now = (this.end - this.start) * t + this.start, this.options.step && this.options.step.call(this.elem, this.now, this), n && n.set ? n.set(this) : M.propHooks._default.set(this), this
                }
            }, M.prototype.init.prototype = M.prototype, M.propHooks = {
                _default: {
                    get: function(e) {
                        var t;
                        return 1 !== e.elem.nodeType || null != e.elem[e.prop] && null == e.elem.style[e.prop] ? e.elem[e.prop] : (t = ue.css(e.elem, e.prop, ""), t && "auto" !== t ? t : 0)
                    },
                    set: function(e) {
                        ue.fx.step[e.prop] ? ue.fx.step[e.prop](e) : 1 !== e.elem.nodeType || null == e.elem.style[ue.cssProps[e.prop]] && !ue.cssHooks[e.prop] ? e.elem[e.prop] = e.now : ue.style(e.elem, e.prop, e.now + e.unit)
                    }
                }
            }, M.propHooks.scrollTop = M.propHooks.scrollLeft = {
                set: function(e) {
                    e.elem.nodeType && e.elem.parentNode && (e.elem[e.prop] = e.now)
                }
            }, ue.easing = {
                linear: function(e) {
                    return e
                },
                swing: function(e) {
                    return .5 - Math.cos(e * Math.PI) / 2
                },
                _default: "swing"
            }, ue.fx = M.prototype.init, ue.fx.step = {};
            var lt, ct, ut = /^(?:toggle|show|hide)$/,
                dt = /queueHooks$/;
            ue.Animation = ue.extend(W, {
                    tweeners: {
                        "*": [function(e, t) {
                            var n = this.createTween(e, t);
                            return h(n.elem, e, Ne.exec(t), n), n
                        }]
                    },
                    tweener: function(e, t) {
                        ue.isFunction(e) ? (t = e, e = ["*"]) : e = e.match(Te);
                        for (var n, i = 0, o = e.length; o > i; i++) n = e[i], W.tweeners[n] = W.tweeners[n] || [], W.tweeners[n].unshift(t)
                    },
                    prefilters: [V],
                    prefilter: function(e, t) {
                        t ? W.prefilters.unshift(e) : W.prefilters.push(e)
                    }
                }), ue.speed = function(e, t, n) {
                    var i = e && "object" == typeof e ? ue.extend({}, e) : {
                        complete: n || !n && t || ue.isFunction(e) && e,
                        duration: e,
                        easing: n && t || t && !ue.isFunction(t) && t
                    };
                    return i.duration = ue.fx.off ? 0 : "number" == typeof i.duration ? i.duration : i.duration in ue.fx.speeds ? ue.fx.speeds[i.duration] : ue.fx.speeds._default, null != i.queue && !0 !== i.queue || (i.queue = "fx"), i.old = i.complete, i.complete = function() {
                        ue.isFunction(i.old) && i.old.call(this), i.queue && ue.dequeue(this, i.queue)
                    }, i
                }, ue.fn.extend({
                    fadeTo: function(e, t, n, i) {
                        return this.filter(Re).css("opacity", 0).show().end().animate({
                            opacity: t
                        }, e, n, i)
                    },
                    animate: function(e, t, n, i) {
                        var o = ue.isEmptyObject(e),
                            r = ue.speed(t, n, i),
                            a = function() {
                                var t = W(this, ue.extend({}, e), r);
                                (o || Oe.get(this, "finish")) && t.stop(!0)
                            };
                        return a.finish = a, o || !1 === r.queue ? this.each(a) : this.queue(r.queue, a)
                    },
                    stop: function(e, t, n) {
                        var i = function(e) {
                            var t = e.stop;
                            delete e.stop, t(n)
                        };
                        return "string" != typeof e && (n = t, t = e, e = void 0), t && !1 !== e && this.queue(e || "fx", []), this.each(function() {
                            var t = !0,
                                o = null != e && e + "queueHooks",
                                r = ue.timers,
                                a = Oe.get(this);
                            if (o) a[o] && a[o].stop && i(a[o]);
                            else
                                for (o in a) a[o] && a[o].stop && dt.test(o) && i(a[o]);
                            for (o = r.length; o--;) r[o].elem !== this || null != e && r[o].queue !== e || (r[o].anim.stop(n), t = !1, r.splice(o, 1));
                            !t && n || ue.dequeue(this, e)
                        })
                    },
                    finish: function(e) {
                        return !1 !== e && (e = e || "fx"), this.each(function() {
                            var t, n = Oe.get(this),
                                i = n[e + "queue"],
                                o = n[e + "queueHooks"],
                                r = ue.timers,
                                a = i ? i.length : 0;
                            for (n.finish = !0, ue.queue(this, e, []), o && o.stop && o.stop.call(this, !0), t = r.length; t--;) r[t].elem === this && r[t].queue === e && (r[t].anim.stop(!0), r.splice(t, 1));
                            for (t = 0; a > t; t++) i[t] && i[t].finish && i[t].finish.call(this);
                            delete n.finish
                        })
                    }
                }), ue.each(["toggle", "show", "hide"], function(e, t) {
                    var n = ue.fn[t];
                    ue.fn[t] = function(e, i, o) {
                        return null == e || "boolean" == typeof e ? n.apply(this, arguments) : this.animate(z(t, !0), e, i, o)
                    }
                }), ue.each({
                    slideDown: z("show"),
                    slideUp: z("hide"),
                    slideToggle: z("toggle"),
                    fadeIn: {
                        opacity: "show"
                    },
                    fadeOut: {
                        opacity: "hide"
                    },
                    fadeToggle: {
                        opacity: "toggle"
                    }
                }, function(e, t) {
                    ue.fn[e] = function(e, n, i) {
                        return this.animate(t, e, n, i)
                    }
                }), ue.timers = [], ue.fx.tick = function() {
                    var e, t = 0,
                        n = ue.timers;
                    for (lt = ue.now(); t < n.length; t++)(e = n[t])() || n[t] !== e || n.splice(t--, 1);
                    n.length || ue.fx.stop(), lt = void 0
                }, ue.fx.timer = function(e) {
                    ue.timers.push(e), e() ? ue.fx.start() : ue.timers.pop()
                }, ue.fx.interval = 13, ue.fx.start = function() {
                    ct || (ct = r.setInterval(ue.fx.tick, ue.fx.interval))
                }, ue.fx.stop = function() {
                    r.clearInterval(ct), ct = null
                }, ue.fx.speeds = {
                    slow: 600,
                    fast: 200,
                    _default: 400
                }, ue.fn.delay = function(e, t) {
                    return e = ue.fx ? ue.fx.speeds[e] || e : e, t = t || "fx", this.queue(t, function(t, n) {
                        var i = r.setTimeout(t, e);
                        n.stop = function() {
                            r.clearTimeout(i)
                        }
                    })
                },
                function() {
                    var e = ee.createElement("input"),
                        t = ee.createElement("select"),
                        n = t.appendChild(ee.createElement("option"));
                    e.type = "checkbox", le.checkOn = "" !== e.value, le.optSelected = n.selected, t.disabled = !0, le.optDisabled = !n.disabled, e = ee.createElement("input"), e.value = "t", e.type = "radio", le.radioValue = "t" === e.value
                }();
            var ft, pt = ue.expr.attrHandle;
            ue.fn.extend({
                attr: function(e, t) {
                    return Ee(this, ue.attr, e, t, arguments.length > 1)
                },
                removeAttr: function(e) {
                    return this.each(function() {
                        ue.removeAttr(this, e)
                    })
                }
            }), ue.extend({
                attr: function(e, t, n) {
                    var i, o, r = e.nodeType;
                    if (3 !== r && 8 !== r && 2 !== r) return void 0 === e.getAttribute ? ue.prop(e, t, n) : (1 === r && ue.isXMLDoc(e) || (t = t.toLowerCase(), o = ue.attrHooks[t] || (ue.expr.match.bool.test(t) ? ft : void 0)), void 0 !== n ? null === n ? void ue.removeAttr(e, t) : o && "set" in o && void 0 !== (i = o.set(e, n, t)) ? i : (e.setAttribute(t, n + ""), n) : o && "get" in o && null !== (i = o.get(e, t)) ? i : (i = ue.find.attr(e, t), null == i ? void 0 : i))
                },
                attrHooks: {
                    type: {
                        set: function(e, t) {
                            if (!le.radioValue && "radio" === t && ue.nodeName(e, "input")) {
                                var n = e.value;
                                return e.setAttribute("type", t), n && (e.value = n), t
                            }
                        }
                    }
                },
                removeAttr: function(e, t) {
                    var n, i, o = 0,
                        r = t && t.match(Te);
                    if (r && 1 === e.nodeType)
                        for (; n = r[o++];) i = ue.propFix[n] || n, ue.expr.match.bool.test(n) && (e[i] = !1), e.removeAttribute(n)
                }
            }), ft = {
                set: function(e, t, n) {
                    return !1 === t ? ue.removeAttr(e, n) : e.setAttribute(n, n), n
                }
            }, ue.each(ue.expr.match.bool.source.match(/\w+/g), function(e, t) {
                var n = pt[t] || ue.find.attr;
                pt[t] = function(e, t, i) {
                    var o, r;
                    return i || (r = pt[t], pt[t] = o, o = null != n(e, t, i) ? t.toLowerCase() : null, pt[t] = r), o
                }
            });
            var ht = /^(?:input|select|textarea|button)$/i,
                mt = /^(?:a|area)$/i;
            ue.fn.extend({
                prop: function(e, t) {
                    return Ee(this, ue.prop, e, t, arguments.length > 1)
                },
                removeProp: function(e) {
                    return this.each(function() {
                        delete this[ue.propFix[e] || e]
                    })
                }
            }), ue.extend({
                prop: function(e, t, n) {
                    var i, o, r = e.nodeType;
                    if (3 !== r && 8 !== r && 2 !== r) return 1 === r && ue.isXMLDoc(e) || (t = ue.propFix[t] || t, o = ue.propHooks[t]), void 0 !== n ? o && "set" in o && void 0 !== (i = o.set(e, n, t)) ? i : e[t] = n : o && "get" in o && null !== (i = o.get(e, t)) ? i : e[t]
                },
                propHooks: {
                    tabIndex: {
                        get: function(e) {
                            var t = ue.find.attr(e, "tabindex");
                            return t ? parseInt(t, 10) : ht.test(e.nodeName) || mt.test(e.nodeName) && e.href ? 0 : -1
                        }
                    }
                },
                propFix: {
                    for: "htmlFor",
                    class: "className"
                }
            }), le.optSelected || (ue.propHooks.selected = {
                get: function(e) {
                    var t = e.parentNode;
                    return t && t.parentNode && t.parentNode.selectedIndex, null
                },
                set: function(e) {
                    var t = e.parentNode;
                    t && (t.selectedIndex, t.parentNode && t.parentNode.selectedIndex)
                }
            }), ue.each(["tabIndex", "readOnly", "maxLength", "cellSpacing", "cellPadding", "rowSpan", "colSpan", "useMap", "frameBorder", "contentEditable"], function() {
                ue.propFix[this.toLowerCase()] = this
            });
            var gt = /[\t\r\n\f]/g;
            ue.fn.extend({
                addClass: function(e) {
                    var t, n, i, o, r, a, s, l = 0;
                    if (ue.isFunction(e)) return this.each(function(t) {
                        ue(this).addClass(e.call(this, t, U(this)))
                    });
                    if ("string" == typeof e && e)
                        for (t = e.match(Te) || []; n = this[l++];)
                            if (o = U(n), i = 1 === n.nodeType && (" " + o + " ").replace(gt, " ")) {
                                for (a = 0; r = t[a++];) i.indexOf(" " + r + " ") < 0 && (i += r + " ");
                                s = ue.trim(i), o !== s && n.setAttribute("class", s)
                            }
                    return this
                },
                removeClass: function(e) {
                    var t, n, i, o, r, a, s, l = 0;
                    if (ue.isFunction(e)) return this.each(function(t) {
                        ue(this).removeClass(e.call(this, t, U(this)))
                    });
                    if (!arguments.length) return this.attr("class", "");
                    if ("string" == typeof e && e)
                        for (t = e.match(Te) || []; n = this[l++];)
                            if (o = U(n), i = 1 === n.nodeType && (" " + o + " ").replace(gt, " ")) {
                                for (a = 0; r = t[a++];)
                                    for (; i.indexOf(" " + r + " ") > -1;) i = i.replace(" " + r + " ", " ");
                                s = ue.trim(i), o !== s && n.setAttribute("class", s)
                            }
                    return this
                },
                toggleClass: function(e, t) {
                    var n = typeof e;
                    return "boolean" == typeof t && "string" === n ? t ? this.addClass(e) : this.removeClass(e) : ue.isFunction(e) ? this.each(function(n) {
                        ue(this).toggleClass(e.call(this, n, U(this), t), t)
                    }) : this.each(function() {
                        var t, i, o, r;
                        if ("string" === n)
                            for (i = 0, o = ue(this), r = e.match(Te) || []; t = r[i++];) o.hasClass(t) ? o.removeClass(t) : o.addClass(t);
                        else void 0 !== e && "boolean" !== n || (t = U(this), t && Oe.set(this, "__className__", t), this.setAttribute && this.setAttribute("class", t || !1 === e ? "" : Oe.get(this, "__className__") || ""))
                    })
                },
                hasClass: function(e) {
                    var t, n, i = 0;
                    for (t = " " + e + " "; n = this[i++];)
                        if (1 === n.nodeType && (" " + U(n) + " ").replace(gt, " ").indexOf(t) > -1) return !0;
                    return !1
                }
            });
            var vt = /\r/g,
                bt = /[\x20\t\r\n\f]+/g;
            ue.fn.extend({
                val: function(e) {
                    var t, n, i, o = this[0];
                    return arguments.length ? (i = ue.isFunction(e), this.each(function(n) {
                        var o;
                        1 === this.nodeType && (o = i ? e.call(this, n, ue(this).val()) : e, null == o ? o = "" : "number" == typeof o ? o += "" : ue.isArray(o) && (o = ue.map(o, function(e) {
                            return null == e ? "" : e + ""
                        })), (t = ue.valHooks[this.type] || ue.valHooks[this.nodeName.toLowerCase()]) && "set" in t && void 0 !== t.set(this, o, "value") || (this.value = o))
                    })) : o ? (t = ue.valHooks[o.type] || ue.valHooks[o.nodeName.toLowerCase()], t && "get" in t && void 0 !== (n = t.get(o, "value")) ? n : (n = o.value, "string" == typeof n ? n.replace(vt, "") : null == n ? "" : n)) : void 0
                }
            }), ue.extend({
                valHooks: {
                    option: {
                        get: function(e) {
                            var t = ue.find.attr(e, "value");
                            return null != t ? t : ue.trim(ue.text(e)).replace(bt, " ")
                        }
                    },
                    select: {
                        get: function(e) {
                            for (var t, n, i = e.options, o = e.selectedIndex, r = "select-one" === e.type || 0 > o, a = r ? null : [], s = r ? o + 1 : i.length, l = 0 > o ? s : r ? o : 0; s > l; l++)
                                if (n = i[l], (n.selected || l === o) && (le.optDisabled ? !n.disabled : null === n.getAttribute("disabled")) && (!n.parentNode.disabled || !ue.nodeName(n.parentNode, "optgroup"))) {
                                    if (t = ue(n).val(), r) return t;
                                    a.push(t)
                                }
                            return a
                        },
                        set: function(e, t) {
                            for (var n, i, o = e.options, r = ue.makeArray(t), a = o.length; a--;) i = o[a], (i.selected = ue.inArray(ue.valHooks.option.get(i), r) > -1) && (n = !0);
                            return n || (e.selectedIndex = -1), r
                        }
                    }
                }
            }), ue.each(["radio", "checkbox"], function() {
                ue.valHooks[this] = {
                    set: function(e, t) {
                        return ue.isArray(t) ? e.checked = ue.inArray(ue(e).val(), t) > -1 : void 0
                    }
                }, le.checkOn || (ue.valHooks[this].get = function(e) {
                    return null === e.getAttribute("value") ? "on" : e.value
                })
            });
            var yt = /^(?:focusinfocus|focusoutblur)$/;
            ue.extend(ue.event, {
                trigger: function(e, t, n, i) {
                    var o, a, s, l, c, u, d, f = [n || ee],
                        p = se.call(e, "type") ? e.type : e,
                        h = se.call(e, "namespace") ? e.namespace.split(".") : [];
                    if (a = s = n = n || ee, 3 !== n.nodeType && 8 !== n.nodeType && !yt.test(p + ue.event.triggered) && (p.indexOf(".") > -1 && (h = p.split("."), p = h.shift(), h.sort()), c = p.indexOf(":") < 0 && "on" + p, e = e[ue.expando] ? e : new ue.Event(p, "object" == typeof e && e), e.isTrigger = i ? 2 : 3, e.namespace = h.join("."), e.rnamespace = e.namespace ? new RegExp("(^|\\.)" + h.join("\\.(?:.*\\.|)") + "(\\.|$)") : null, e.result = void 0, e.target || (e.target = n), t = null == t ? [e] : ue.makeArray(t, [e]), d = ue.event.special[p] || {}, i || !d.trigger || !1 !== d.trigger.apply(n, t))) {
                        if (!i && !d.noBubble && !ue.isWindow(n)) {
                            for (l = d.delegateType || p, yt.test(l + p) || (a = a.parentNode); a; a = a.parentNode) f.push(a), s = a;
                            s === (n.ownerDocument || ee) && f.push(s.defaultView || s.parentWindow || r)
                        }
                        for (o = 0;
                            (a = f[o++]) && !e.isPropagationStopped();) e.type = o > 1 ? l : d.bindType || p, u = (Oe.get(a, "events") || {})[e.type] && Oe.get(a, "handle"), u && u.apply(a, t), (u = c && a[c]) && u.apply && De(a) && (e.result = u.apply(a, t), !1 === e.result && e.preventDefault());
                        return e.type = p, i || e.isDefaultPrevented() || d._default && !1 !== d._default.apply(f.pop(), t) || !De(n) || c && ue.isFunction(n[p]) && !ue.isWindow(n) && (s = n[c], s && (n[c] = null), ue.event.triggered = p, n[p](), ue.event.triggered = void 0, s && (n[c] = s)), e.result
                    }
                },
                simulate: function(e, t, n) {
                    var i = ue.extend(new ue.Event, n, {
                        type: e,
                        isSimulated: !0
                    });
                    ue.event.trigger(i, null, t)
                }
            }), ue.fn.extend({
                trigger: function(e, t) {
                    return this.each(function() {
                        ue.event.trigger(e, t, this)
                    })
                },
                triggerHandler: function(e, t) {
                    var n = this[0];
                    return n ? ue.event.trigger(e, t, n, !0) : void 0
                }
            }), ue.each("blur focus focusin focusout load resize scroll unload click dblclick mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave change select submit keydown keypress keyup error contextmenu".split(" "), function(e, t) {
                ue.fn[t] = function(e, n) {
                    return arguments.length > 0 ? this.on(t, null, e, n) : this.trigger(t)
                }
            }), ue.fn.extend({
                hover: function(e, t) {
                    return this.mouseenter(e).mouseleave(t || e)
                }
            }), le.focusin = "onfocusin" in r, le.focusin || ue.each({
                focus: "focusin",
                blur: "focusout"
            }, function(e, t) {
                var n = function(e) {
                    ue.event.simulate(t, e.target, ue.event.fix(e))
                };
                ue.event.special[t] = {
                    setup: function() {
                        var i = this.ownerDocument || this,
                            o = Oe.access(i, t);
                        o || i.addEventListener(e, n, !0), Oe.access(i, t, (o || 0) + 1)
                    },
                    teardown: function() {
                        var i = this.ownerDocument || this,
                            o = Oe.access(i, t) - 1;
                        o ? Oe.access(i, t, o) : (i.removeEventListener(e, n, !0), Oe.remove(i, t))
                    }
                }
            });
            var xt = r.location,
                wt = ue.now(),
                Ct = /\?/;
            ue.parseJSON = function(e) {
                return JSON.parse(e + "")
            }, ue.parseXML = function(e) {
                var t;
                if (!e || "string" != typeof e) return null;
                try {
                    t = (new r.DOMParser).parseFromString(e, "text/xml")
                } catch (e) {
                    t = void 0
                }
                return t && !t.getElementsByTagName("parsererror").length || ue.error("Invalid XML: " + e), t
            };
            var kt = /#.*$/,
                St = /([?&])_=[^&]*/,
                Tt = /^(.*?):[ \t]*([^\r\n]*)$/gm,
                At = /^(?:about|app|app-storage|.+-extension|file|res|widget):$/,
                Et = /^(?:GET|HEAD)$/,
                Dt = /^\/\//,
                Ot = {},
                Ft = {},
                jt = "*/".concat("*"),
                qt = ee.createElement("a");
            qt.href = xt.href, ue.extend({
                active: 0,
                lastModified: {},
                etag: {},
                ajaxSettings: {
                    url: xt.href,
                    type: "GET",
                    isLocal: At.test(xt.protocol),
                    global: !0,
                    processData: !0,
                    async: !0,
                    contentType: "application/x-www-form-urlencoded; charset=UTF-8",
                    accepts: {
                        "*": jt,
                        text: "text/plain",
                        html: "text/html",
                        xml: "application/xml, text/xml",
                        json: "application/json, text/javascript"
                    },
                    contents: {
                        xml: /\bxml\b/,
                        html: /\bhtml/,
                        json: /\bjson\b/
                    },
                    responseFields: {
                        xml: "responseXML",
                        text: "responseText",
                        json: "responseJSON"
                    },
                    converters: {
                        "* text": String,
                        "text html": !0,
                        "text json": ue.parseJSON,
                        "text xml": ue.parseXML
                    },
                    flatOptions: {
                        url: !0,
                        context: !0
                    }
                },
                ajaxSetup: function(e, t) {
                    return t ? Q(Q(e, ue.ajaxSettings), t) : Q(ue.ajaxSettings, e)
                },
                ajaxPrefilter: _(Ot),
                ajaxTransport: _(Ft),
                ajax: function(e, t) {
                    function n(e, t, n, s) {
                        var c, d, b, y, w, k = t;
                        2 !== x && (x = 2, l && r.clearTimeout(l), i = void 0, a = s || "", C.readyState = e > 0 ? 4 : 0, c = e >= 200 && 300 > e || 304 === e, n && (y = Y(f, C, n)), y = G(f, y, C, c), c ? (f.ifModified && (w = C.getResponseHeader("Last-Modified"), w && (ue.lastModified[o] = w), (w = C.getResponseHeader("etag")) && (ue.etag[o] = w)), 204 === e || "HEAD" === f.type ? k = "nocontent" : 304 === e ? k = "notmodified" : (k = y.state, d = y.data, b = y.error, c = !b)) : (b = k, !e && k || (k = "error", 0 > e && (e = 0))), C.status = e, C.statusText = (t || k) + "", c ? m.resolveWith(p, [d, k, C]) : m.rejectWith(p, [C, k, b]), C.statusCode(v), v = void 0, u && h.trigger(c ? "ajaxSuccess" : "ajaxError", [C, f, c ? d : b]), g.fireWith(p, [C, k]), u && (h.trigger("ajaxComplete", [C, f]), --ue.active || ue.event.trigger("ajaxStop")))
                    }
                    "object" == typeof e && (t = e, e = void 0), t = t || {};
                    var i, o, a, s, l, c, u, d, f = ue.ajaxSetup({}, t),
                        p = f.context || f,
                        h = f.context && (p.nodeType || p.jquery) ? ue(p) : ue.event,
                        m = ue.Deferred(),
                        g = ue.Callbacks("once memory"),
                        v = f.statusCode || {},
                        b = {},
                        y = {},
                        x = 0,
                        w = "canceled",
                        C = {
                            readyState: 0,
                            getResponseHeader: function(e) {
                                var t;
                                if (2 === x) {
                                    if (!s)
                                        for (s = {}; t = Tt.exec(a);) s[t[1].toLowerCase()] = t[2];
                                    t = s[e.toLowerCase()]
                                }
                                return null == t ? null : t
                            },
                            getAllResponseHeaders: function() {
                                return 2 === x ? a : null
                            },
                            setRequestHeader: function(e, t) {
                                var n = e.toLowerCase();
                                return x || (e = y[n] = y[n] || e, b[e] = t), this
                            },
                            overrideMimeType: function(e) {
                                return x || (f.mimeType = e), this
                            },
                            statusCode: function(e) {
                                var t;
                                if (e)
                                    if (2 > x)
                                        for (t in e) v[t] = [v[t], e[t]];
                                    else C.always(e[C.status]);
                                return this
                            },
                            abort: function(e) {
                                var t = e || w;
                                return i && i.abort(t), n(0, t), this
                            }
                        };
                    if (m.promise(C).complete = g.add, C.success = C.done, C.error = C.fail, f.url = ((e || f.url || xt.href) + "").replace(kt, "").replace(Dt, xt.protocol + "//"), f.type = t.method || t.type || f.method || f.type, f.dataTypes = ue.trim(f.dataType || "*").toLowerCase().match(Te) || [""], null == f.crossDomain) {
                        c = ee.createElement("a");
                        try {
                            c.href = f.url, c.href = c.href, f.crossDomain = qt.protocol + "//" + qt.host != c.protocol + "//" + c.host
                        } catch (e) {
                            f.crossDomain = !0
                        }
                    }
                    if (f.data && f.processData && "string" != typeof f.data && (f.data = ue.param(f.data, f.traditional)), X(Ot, f, t, C), 2 === x) return C;
                    u = ue.event && f.global, u && 0 == ue.active++ && ue.event.trigger("ajaxStart"), f.type = f.type.toUpperCase(), f.hasContent = !Et.test(f.type), o = f.url, f.hasContent || (f.data && (o = f.url += (Ct.test(o) ? "&" : "?") + f.data, delete f.data), !1 === f.cache && (f.url = St.test(o) ? o.replace(St, "$1_=" + wt++) : o + (Ct.test(o) ? "&" : "?") + "_=" + wt++)), f.ifModified && (ue.lastModified[o] && C.setRequestHeader("If-Modified-Since", ue.lastModified[o]), ue.etag[o] && C.setRequestHeader("If-None-Match", ue.etag[o])), (f.data && f.hasContent && !1 !== f.contentType || t.contentType) && C.setRequestHeader("Content-Type", f.contentType), C.setRequestHeader("Accept", f.dataTypes[0] && f.accepts[f.dataTypes[0]] ? f.accepts[f.dataTypes[0]] + ("*" !== f.dataTypes[0] ? ", " + jt + "; q=0.01" : "") : f.accepts["*"]);
                    for (d in f.headers) C.setRequestHeader(d, f.headers[d]);
                    if (f.beforeSend && (!1 === f.beforeSend.call(p, C, f) || 2 === x)) return C.abort();
                    w = "abort";
                    for (d in {
                            success: 1,
                            error: 1,
                            complete: 1
                        }) C[d](f[d]);
                    if (i = X(Ft, f, t, C)) {
                        if (C.readyState = 1, u && h.trigger("ajaxSend", [C, f]), 2 === x) return C;
                        f.async && f.timeout > 0 && (l = r.setTimeout(function() {
                            C.abort("timeout")
                        }, f.timeout));
                        try {
                            x = 1, i.send(b, n)
                        } catch (e) {
                            if (!(2 > x)) throw e;
                            n(-1, e)
                        }
                    } else n(-1, "No Transport");
                    return C
                },
                getJSON: function(e, t, n) {
                    return ue.get(e, t, n, "json")
                },
                getScript: function(e, t) {
                    return ue.get(e, void 0, t, "script")
                }
            }), ue.each(["get", "post"], function(e, t) {
                ue[t] = function(e, n, i, o) {
                    return ue.isFunction(n) && (o = o || i, i = n, n = void 0), ue.ajax(ue.extend({
                        url: e,
                        type: t,
                        dataType: o,
                        data: n,
                        success: i
                    }, ue.isPlainObject(e) && e))
                }
            }), ue._evalUrl = function(e) {
                return ue.ajax({
                    url: e,
                    type: "GET",
                    dataType: "script",
                    async: !1,
                    global: !1,
                    throws: !0
                })
            }, ue.fn.extend({
                wrapAll: function(e) {
                    var t;
                    return ue.isFunction(e) ? this.each(function(t) {
                        ue(this).wrapAll(e.call(this, t))
                    }) : (this[0] && (t = ue(e, this[0].ownerDocument).eq(0).clone(!0), this[0].parentNode && t.insertBefore(this[0]), t.map(function() {
                        for (var e = this; e.firstElementChild;) e = e.firstElementChild;
                        return e
                    }).append(this)), this)
                },
                wrapInner: function(e) {
                    return ue.isFunction(e) ? this.each(function(t) {
                        ue(this).wrapInner(e.call(this, t))
                    }) : this.each(function() {
                        var t = ue(this),
                            n = t.contents();
                        n.length ? n.wrapAll(e) : t.append(e)
                    })
                },
                wrap: function(e) {
                    var t = ue.isFunction(e);
                    return this.each(function(n) {
                        ue(this).wrapAll(t ? e.call(this, n) : e)
                    })
                },
                unwrap: function() {
                    return this.parent().each(function() {
                        ue.nodeName(this, "body") || ue(this).replaceWith(this.childNodes)
                    }).end()
                }
            }), ue.expr.filters.hidden = function(e) {
                return !ue.expr.filters.visible(e)
            }, ue.expr.filters.visible = function(e) {
                return e.offsetWidth > 0 || e.offsetHeight > 0 || e.getClientRects().length > 0
            };
            var Lt = /%20/g,
                Nt = /\[\]$/,
                Pt = /\r?\n/g,
                Rt = /^(?:submit|button|image|reset|file)$/i,
                It = /^(?:input|select|textarea|keygen)/i;
            ue.param = function(e, t) {
                var n, i = [],
                    o = function(e, t) {
                        t = ue.isFunction(t) ? t() : null == t ? "" : t, i[i.length] = encodeURIComponent(e) + "=" + encodeURIComponent(t)
                    };
                if (void 0 === t && (t = ue.ajaxSettings && ue.ajaxSettings.traditional), ue.isArray(e) || e.jquery && !ue.isPlainObject(e)) ue.each(e, function() {
                    o(this.name, this.value)
                });
                else
                    for (n in e) K(n, e[n], t, o);
                return i.join("&").replace(Lt, "+")
            }, ue.fn.extend({
                serialize: function() {
                    return ue.param(this.serializeArray())
                },
                serializeArray: function() {
                    return this.map(function() {
                        var e = ue.prop(this, "elements");
                        return e ? ue.makeArray(e) : this
                    }).filter(function() {
                        var e = this.type;
                        return this.name && !ue(this).is(":disabled") && It.test(this.nodeName) && !Rt.test(e) && (this.checked || !Ie.test(e))
                    }).map(function(e, t) {
                        var n = ue(this).val();
                        return null == n ? null : ue.isArray(n) ? ue.map(n, function(e) {
                            return {
                                name: t.name,
                                value: e.replace(Pt, "\r\n")
                            }
                        }) : {
                            name: t.name,
                            value: n.replace(Pt, "\r\n")
                        }
                    }).get()
                }
            }), ue.ajaxSettings.xhr = function() {
                try {
                    return new r.XMLHttpRequest
                } catch (e) {}
            };
            var Mt = {
                    0: 200,
                    1223: 204
                },
                Ht = ue.ajaxSettings.xhr();
            le.cors = !!Ht && "withCredentials" in Ht, le.ajax = Ht = !!Ht, ue.ajaxTransport(function(e) {
                var t, n;
                return le.cors || Ht && !e.crossDomain ? {
                    send: function(i, o) {
                        var a, s = e.xhr();
                        if (s.open(e.type, e.url, e.async, e.username, e.password), e.xhrFields)
                            for (a in e.xhrFields) s[a] = e.xhrFields[a];
                        e.mimeType && s.overrideMimeType && s.overrideMimeType(e.mimeType), e.crossDomain || i["X-Requested-With"] || (i["X-Requested-With"] = "XMLHttpRequest");
                        for (a in i) s.setRequestHeader(a, i[a]);
                        t = function(e) {
                            return function() {
                                t && (t = n = s.onload = s.onerror = s.onabort = s.onreadystatechange = null, "abort" === e ? s.abort() : "error" === e ? "number" != typeof s.status ? o(0, "error") : o(s.status, s.statusText) : o(Mt[s.status] || s.status, s.statusText, "text" !== (s.responseType || "text") || "string" != typeof s.responseText ? {
                                    binary: s.response
                                } : {
                                    text: s.responseText
                                }, s.getAllResponseHeaders()))
                            }
                        }, s.onload = t(), n = s.onerror = t("error"), void 0 !== s.onabort ? s.onabort = n : s.onreadystatechange = function() {
                            4 === s.readyState && r.setTimeout(function() {
                                t && n()
                            })
                        }, t = t("abort");
                        try {
                            s.send(e.hasContent && e.data || null)
                        } catch (e) {
                            if (t) throw e
                        }
                    },
                    abort: function() {
                        t && t()
                    }
                } : void 0
            }), ue.ajaxSetup({
                accepts: {
                    script: "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript"
                },
                contents: {
                    script: /\b(?:java|ecma)script\b/
                },
                converters: {
                    "text script": function(e) {
                        return ue.globalEval(e), e
                    }
                }
            }), ue.ajaxPrefilter("script", function(e) {
                void 0 === e.cache && (e.cache = !1), e.crossDomain && (e.type = "GET")
            }), ue.ajaxTransport("script", function(e) {
                if (e.crossDomain) {
                    var t, n;
                    return {
                        send: function(i, o) {
                            t = ue("<script>").prop({
                                charset: e.scriptCharset,
                                src: e.url
                            }).on("load error", n = function(e) {
                                t.remove(), n = null, e && o("error" === e.type ? 404 : 200, e.type)
                            }), ee.head.appendChild(t[0])
                        },
                        abort: function() {
                            n && n()
                        }
                    }
                }
            });
            var zt = [],
                $t = /(=)\?(?=&|$)|\?\?/;
            ue.ajaxSetup({
                jsonp: "callback",
                jsonpCallback: function() {
                    var e = zt.pop() || ue.expando + "_" + wt++;
                    return this[e] = !0, e
                }
            }), ue.ajaxPrefilter("json jsonp", function(e, t, n) {
                var i, o, a, s = !1 !== e.jsonp && ($t.test(e.url) ? "url" : "string" == typeof e.data && 0 === (e.contentType || "").indexOf("application/x-www-form-urlencoded") && $t.test(e.data) && "data");
                return s || "jsonp" === e.dataTypes[0] ? (i = e.jsonpCallback = ue.isFunction(e.jsonpCallback) ? e.jsonpCallback() : e.jsonpCallback, s ? e[s] = e[s].replace($t, "$1" + i) : !1 !== e.jsonp && (e.url += (Ct.test(e.url) ? "&" : "?") + e.jsonp + "=" + i), e.converters["script json"] = function() {
                    return a || ue.error(i + " was not called"), a[0]
                }, e.dataTypes[0] = "json", o = r[i], r[i] = function() {
                    a = arguments
                }, n.always(function() {
                    void 0 === o ? ue(r).removeProp(i) : r[i] = o, e[i] && (e.jsonpCallback = t.jsonpCallback, zt.push(i)), a && ue.isFunction(o) && o(a[0]), a = o = void 0
                }), "script") : void 0
            }), ue.parseHTML = function(e, t, n) {
                if (!e || "string" != typeof e) return null;
                "boolean" == typeof t && (n = t, t = !1), t = t || ee;
                var i = ye.exec(e),
                    o = !n && [];
                return i ? [t.createElement(i[1])] : (i = v([e], t, o), o && o.length && ue(o).remove(), ue.merge([], i.childNodes))
            };
            var Vt = ue.fn.load;
            ue.fn.load = function(e, t, n) {
                if ("string" != typeof e && Vt) return Vt.apply(this, arguments);
                var i, o, r, a = this,
                    s = e.indexOf(" ");
                return s > -1 && (i = ue.trim(e.slice(s)), e = e.slice(0, s)), ue.isFunction(t) ? (n = t, t = void 0) : t && "object" == typeof t && (o = "POST"), a.length > 0 && ue.ajax({
                    url: e,
                    type: o || "GET",
                    dataType: "html",
                    data: t
                }).done(function(e) {
                    r = arguments, a.html(i ? ue("<div>").append(ue.parseHTML(e)).find(i) : e)
                }).always(n && function(e, t) {
                    a.each(function() {
                        n.apply(this, r || [e.responseText, t, e])
                    })
                }), this
            }, ue.each(["ajaxStart", "ajaxStop", "ajaxComplete", "ajaxError", "ajaxSuccess", "ajaxSend"], function(e, t) {
                ue.fn[t] = function(e) {
                    return this.on(t, e)
                }
            }), ue.expr.filters.animated = function(e) {
                return ue.grep(ue.timers, function(t) {
                    return e === t.elem
                }).length
            }, ue.offset = {
                setOffset: function(e, t, n) {
                    var i, o, r, a, s, l, c, u = ue.css(e, "position"),
                        d = ue(e),
                        f = {};
                    "static" === u && (e.style.position = "relative"), s = d.offset(), r = ue.css(e, "top"), l = ue.css(e, "left"), c = ("absolute" === u || "fixed" === u) && (r + l).indexOf("auto") > -1, c ? (i = d.position(), a = i.top, o = i.left) : (a = parseFloat(r) || 0, o = parseFloat(l) || 0), ue.isFunction(t) && (t = t.call(e, n, ue.extend({}, s))), null != t.top && (f.top = t.top - s.top + a), null != t.left && (f.left = t.left - s.left + o), "using" in t ? t.using.call(e, f) : d.css(f)
                }
            }, ue.fn.extend({
                offset: function(e) {
                    if (arguments.length) return void 0 === e ? this : this.each(function(t) {
                        ue.offset.setOffset(this, e, t)
                    });
                    var t, n, i = this[0],
                        o = {
                            top: 0,
                            left: 0
                        },
                        r = i && i.ownerDocument;
                    return r ? (t = r.documentElement, ue.contains(t, i) ? (o = i.getBoundingClientRect(), n = J(r), {
                        top: o.top + n.pageYOffset - t.clientTop,
                        left: o.left + n.pageXOffset - t.clientLeft
                    }) : o) : void 0
                },
                position: function() {
                    if (this[0]) {
                        var e, t, n = this[0],
                            i = {
                                top: 0,
                                left: 0
                            };
                        return "fixed" === ue.css(n, "position") ? t = n.getBoundingClientRect() : (e = this.offsetParent(), t = this.offset(), ue.nodeName(e[0], "html") || (i = e.offset()), i.top += ue.css(e[0], "borderTopWidth", !0), i.left += ue.css(e[0], "borderLeftWidth", !0)), {
                            top: t.top - i.top - ue.css(n, "marginTop", !0),
                            left: t.left - i.left - ue.css(n, "marginLeft", !0)
                        }
                    }
                },
                offsetParent: function() {
                    return this.map(function() {
                        for (var e = this.offsetParent; e && "static" === ue.css(e, "position");) e = e.offsetParent;
                        return e || nt
                    })
                }
            }), ue.each({
                scrollLeft: "pageXOffset",
                scrollTop: "pageYOffset"
            }, function(e, t) {
                var n = "pageYOffset" === t;
                ue.fn[e] = function(i) {
                    return Ee(this, function(e, i, o) {
                        var r = J(e);
                        return void 0 === o ? r ? r[t] : e[i] : void(r ? r.scrollTo(n ? r.pageXOffset : o, n ? o : r.pageYOffset) : e[i] = o)
                    }, e, i, arguments.length)
                }
            }), ue.each(["top", "left"], function(e, t) {
                ue.cssHooks[t] = q(le.pixelPosition, function(e, n) {
                    return n ? (n = j(e, t), Ze.test(n) ? ue(e).position()[t] + "px" : n) : void 0
                })
            }), ue.each({
                Height: "height",
                Width: "width"
            }, function(e, t) {
                ue.each({
                    padding: "inner" + e,
                    content: t,
                    "": "outer" + e
                }, function(n, i) {
                    ue.fn[i] = function(i, o) {
                        var r = arguments.length && (n || "boolean" != typeof i),
                            a = n || (!0 === i || !0 === o ? "margin" : "border");
                        return Ee(this, function(t, n, i) {
                            var o;
                            return ue.isWindow(t) ? t.document.documentElement["client" + e] : 9 === t.nodeType ? (o = t.documentElement, Math.max(t.body["scroll" + e], o["scroll" + e], t.body["offset" + e], o["offset" + e], o["client" + e])) : void 0 === i ? ue.css(t, n, a) : ue.style(t, n, i, a)
                        }, t, r ? i : void 0, r, null)
                    }
                })
            }), ue.fn.extend({
                bind: function(e, t, n) {
                    return this.on(e, null, t, n)
                },
                unbind: function(e, t) {
                    return this.off(e, null, t)
                },
                delegate: function(e, t, n, i) {
                    return this.on(t, e, n, i)
                },
                undelegate: function(e, t, n) {
                    return 1 === arguments.length ? this.off(e, "**") : this.off(t, e || "**", n)
                },
                size: function() {
                    return this.length
                }
            }), ue.fn.andSelf = ue.fn.addBack, n("nErl") && (i = [], void 0 !== (o = function() {
                return ue
            }.apply(t, i)) && (e.exports = o));
            var Bt = r.jQuery,
                Wt = r.$;
            return ue.noConflict = function(e) {
                return r.$ === ue && (r.$ = Wt), e && r.jQuery === ue && (r.jQuery = Bt), ue
            }, a || (r.jQuery = r.$ = ue), ue
        })
    },
    OQde: function(e, t) {
        $(document).ready(function() {
            function e() {
                if (0 === $("img.preload").length) return !1;
                var n = 100 - Math.round(($(document).height() - window.pageYOffset) / ($(document).height() / 100)),
                    i = 1e3 * n,
                    r = 1,
                    a = 0;
                $("img.preload").each(function(s) {
                    var l = $(this);
                    if (t(l, i))
                        if (++a <= r) {
                            l.removeClass("preload");
                            var u = l.data("src-retina") ? l.data("src-retina") : l.data("src"),
                                d = o ? u : l.data("src");
                            l.attr("src") != d && l.attr("src", d)
                        } else clearInterval(c), r *= n, c = setInterval(e, 30 * n)
                })
            }

            function t(e, t) {
                "function" == typeof jQuery && e instanceof jQuery && (e = e[0]), t = t || 1e3;
                for (var n = e.offsetTop, i = e.offsetLeft, o = e.offsetWidth, r = e.offsetHeight + t; e.offsetParent;) e = e.offsetParent, n += e.offsetTop, i += e.offsetLeft;
                return n < window.pageYOffset + window.innerHeight + t && i < window.pageXOffset + window.innerWidth && n + r > window.pageYOffset && i + o > window.pageXOffset
            }

            function n() {
                $("#at4-share").removeClass("hide")
            }

            function n() {
                $("#at4-share").removeClass("hide")
            }
            var i = Math.round(window.devicePixelRatio),
                o = i > 1,
                r = window.location.protocol,
                a = r.concat("//"),
                s = a.concat(window.location.hostname),
                l = window.location.href;
            new Clipboard(".clipbb");
            $.ajaxSetup({
                headers: {
                    "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr("content")
                },
                ajaxError: function(e, t, n, i) {}
            });
            var c = setInterval(e, 100),
                u = function() {
                    if ($(window).scrollTop() + $(window).height() > $(document).height() - 1500) {
                        var e = $("#collections_segment .stage");
                        e.length > 0 && ($(".paginator").remove(), 0 == e.data("end") && ($(".loader.collections").addClass("active"), $.ajax({
                            url: e.data("resource"),
                            async: !1,
                            type: "POST"
                        }).success(function(t) {
                            $(".loader.collections").removeClass("active"), e.remove(), $("#collections_segment").append(t)
                        })))
                    }
                };
            window.setInterval(u, 500), $("#collection_popup").popup({
                on: "hover",
                hoverable: !0,
                position: "bottom right",
                lastResort: "bottom right",
                delay: {
                    show: 0,
                    hide: 200
                },
                duration: 5
            }), $(".dropdown").dropdown(), $(".category.dropdown").dropdown({
                maxSelection: 8,
                onChange: function(e, t, n) {
                    window.location = e
                }
            }), $(".ui.sticky").sticky({
                context: "#context",
                bserveChanges: !0,
                offset: 60
            }), $(".ui.sidebar").sidebar({
                returnScroll: !0,
                exclusive: !1,
                dimPage: !1,
                duration: 50
            }).sidebar("attach events", "a.toc");
            var d = $(".cd-top");
            $(window).scroll(function() {
                $(window).scrollTop() > 300 ? d.addClass("cd-is-visible") : d.removeClass("cd-is-visible cd-fade-out"), $(window).scrollTop() > 1200 && d.addClass("cd-fade-out")
            }), d.on("click", function(e) {
                e.preventDefault(), $("body,html").animate({
                    scrollTop: 0
                }, 700)
            }), $("#adsdimmer").modal({
                duration: 0,
                dimmerSettings: {
                    closable: !1,
                    useCSS: !1
                },
                onHide: function() {
                    return n(), !0
                }
            }), window.setIntervalID = null, window.counterWait = function(e) {
                clearInterval(setIntervalID);
                var e = e || 4;
                $("#count").html("Please, wait while your link is generating " + e.toString()), setIntervalID = setInterval(function() {
                    e--, e >= 0 && $("#count").html("Please, wait while your link is generating " + e.toString()), 0 === e && ($("#count").html(""), $("#download").removeClass("hide"), $("#download_menu").removeClass("hide"), $("#adsdimmer .details").removeClass("hide"), clearInterval(setIntervalID))
                }, 1e3)
            }, $(".single_image .ads_popup, .single_image .download_button.ads_popup").on("mousedown", function() {
                var e = $("#" + $(this).data("id"));
                //$.post("/download", { id: $(this).data("id"), slug: $(this).data("slug") } );
                $("#adsdimmer").modal("show"), $("#download").addClass("hide"), $("#download_menu").addClass("hide"), $("#adsdimmer .details").addClass("hide"), $("#adsdimmer #download").attr("href", e.data("download")), $("#adsdimmer .orres").text(e.data("or"));
                var t = '<a href="' + l + '" target="blank"><img src="' + s + e.data("fullimg") + '"></a>';
                $("#adsdimmer #clipboard").val(t), $("#adsdimmer #fsb").attr("href", e.data("fsb")), $("#adsdimmer #tw").attr("href", e.data("tw")), $("#adsdimmer #pin").attr("href", e.data("pin")), $("#adsdimmer .fsl").attr("href", e.data("download")), $("#at4-share").addClass("hide"), counterWait()
            }), $("#adsdimmer .icon.remove, #adsdimmer #download, #keyshelp .icon.remove").on("click", function() {
                $("#adsdimmer").modal("hide")
            }), $("#keyshelp .icon.remove").on("click", function() {
                $("#keyshelp").modal("hide")
            }), $(".adsbygoogle").each(function(e, t) {
                (adsbygoogle = window.adsbygoogle || []).push({})
            }), $(".accordion").accordion(), $("button.uploadcare-uploader").click(function() {
                var e = $(this);
                uploadcare.openDialog(null, {
                    publicKey: window.UPLOADCARE_PUBLIC_KEY,
                    imagesOnly: !0,
                    previewStep: !0,
                    validators: [function(e) {
                        var t = e.originalImageInfo;
                        if (null !== t && t.width * t.height < 786432) throw new Error("Image too small :(")
                    }]
                }).done(function(t) {
                    t.promise().done(function(t) {
                        var n = {
                            cdnUrl: t.cdnUrl,
                            width: t.originalImageInfo.width,
                            height: t.originalImageInfo.height,
                            size: t.size
                        };
                        $.post({
                            url: e.data("resource"),
                            data: n
                        }).success(function(e) {
                            location.reload()
                        })
                    })
                })
            })
        })
    },
    TQvf: function(e, t, n) {
        var i, i;
        ! function(t) {
            e.exports = t()
        }(function() {
            var e;
            return function e(t, n, o) {
                function r(s, l) {
                    if (!n[s]) {
                        if (!t[s]) {
                            var c = "function" == typeof i && i;
                            if (!l && c) return i(s, !0);
                            if (a) return a(s, !0);
                            var u = new Error("Cannot find module '" + s + "'");
                            throw u.code = "MODULE_NOT_FOUND", u
                        }
                        var d = n[s] = {
                            exports: {}
                        };
                        t[s][0].call(d.exports, function(e) {
                            var n = t[s][1][e];
                            return r(n || e)
                        }, d, d.exports, e, t, n, o)
                    }
                    return n[s].exports
                }
                for (var a = "function" == typeof i && i, s = 0; s < o.length; s++) r(o[s]);
                return r
            }({
                1: [function(e, t, n) {
                    function i(e, t) {
                        for (; e && e.nodeType !== o;) {
                            if ("function" == typeof e.matches && e.matches(t)) return e;
                            e = e.parentNode
                        }
                    }
                    var o = 9;
                    if ("undefined" != typeof Element && !Element.prototype.matches) {
                        var r = Element.prototype;
                        r.matches = r.matchesSelector || r.mozMatchesSelector || r.msMatchesSelector || r.oMatchesSelector || r.webkitMatchesSelector
                    }
                    t.exports = i
                }, {}],
                2: [function(e, t, n) {
                    function i(e, t, n, i, r) {
                        var a = o.apply(this, arguments);
                        return e.addEventListener(n, a, r), {
                            destroy: function() {
                                e.removeEventListener(n, a, r)
                            }
                        }
                    }

                    function o(e, t, n, i) {
                        return function(n) {
                            n.delegateTarget = r(n.target, t), n.delegateTarget && i.call(e, n)
                        }
                    }
                    var r = e("./closest");
                    t.exports = i
                }, {
                    "./closest": 1
                }],
                3: [function(e, t, n) {
                    n.node = function(e) {
                        return void 0 !== e && e instanceof HTMLElement && 1 === e.nodeType
                    }, n.nodeList = function(e) {
                        var t = Object.prototype.toString.call(e);
                        return void 0 !== e && ("[object NodeList]" === t || "[object HTMLCollection]" === t) && "length" in e && (0 === e.length || n.node(e[0]))
                    }, n.string = function(e) {
                        return "string" == typeof e || e instanceof String
                    }, n.fn = function(e) {
                        return "[object Function]" === Object.prototype.toString.call(e)
                    }
                }, {}],
                4: [function(e, t, n) {
                    function i(e, t, n) {
                        if (!e && !t && !n) throw new Error("Missing required arguments");
                        if (!s.string(t)) throw new TypeError("Second argument must be a String");
                        if (!s.fn(n)) throw new TypeError("Third argument must be a Function");
                        if (s.node(e)) return o(e, t, n);
                        if (s.nodeList(e)) return r(e, t, n);
                        if (s.string(e)) return a(e, t, n);
                        throw new TypeError("First argument must be a String, HTMLElement, HTMLCollection, or NodeList")
                    }

                    function o(e, t, n) {
                        return e.addEventListener(t, n), {
                            destroy: function() {
                                e.removeEventListener(t, n)
                            }
                        }
                    }

                    function r(e, t, n) {
                        return Array.prototype.forEach.call(e, function(e) {
                            e.addEventListener(t, n)
                        }), {
                            destroy: function() {
                                Array.prototype.forEach.call(e, function(e) {
                                    e.removeEventListener(t, n)
                                })
                            }
                        }
                    }

                    function a(e, t, n) {
                        return l(document.body, e, t, n)
                    }
                    var s = e("./is"),
                        l = e("delegate");
                    t.exports = i
                }, {
                    "./is": 3,
                    delegate: 2
                }],
                5: [function(e, t, n) {
                    function i(e) {
                        var t;
                        if ("SELECT" === e.nodeName) e.focus(), t = e.value;
                        else if ("INPUT" === e.nodeName || "TEXTAREA" === e.nodeName) {
                            var n = e.hasAttribute("readonly");
                            n || e.setAttribute("readonly", ""), e.select(), e.setSelectionRange(0, e.value.length), n || e.removeAttribute("readonly"), t = e.value
                        } else {
                            e.hasAttribute("contenteditable") && e.focus();
                            var i = window.getSelection(),
                                o = document.createRange();
                            o.selectNodeContents(e), i.removeAllRanges(), i.addRange(o), t = i.toString()
                        }
                        return t
                    }
                    t.exports = i
                }, {}],
                6: [function(e, t, n) {
                    function i() {}
                    i.prototype = {
                        on: function(e, t, n) {
                            var i = this.e || (this.e = {});
                            return (i[e] || (i[e] = [])).push({
                                fn: t,
                                ctx: n
                            }), this
                        },
                        once: function(e, t, n) {
                            function i() {
                                o.off(e, i), t.apply(n, arguments)
                            }
                            var o = this;
                            return i._ = t, this.on(e, i, n)
                        },
                        emit: function(e) {
                            var t = [].slice.call(arguments, 1),
                                n = ((this.e || (this.e = {}))[e] || []).slice(),
                                i = 0,
                                o = n.length;
                            for (i; i < o; i++) n[i].fn.apply(n[i].ctx, t);
                            return this
                        },
                        off: function(e, t) {
                            var n = this.e || (this.e = {}),
                                i = n[e],
                                o = [];
                            if (i && t)
                                for (var r = 0, a = i.length; r < a; r++) i[r].fn !== t && i[r].fn._ !== t && o.push(i[r]);
                            return o.length ? n[e] = o : delete n[e], this
                        }
                    }, t.exports = i
                }, {}],
                7: [function(t, n, i) {
                    ! function(o, r) {
                        if ("function" == typeof e && e.amd) e(["module", "select"], r);
                        else if (void 0 !== i) r(n, t("select"));
                        else {
                            var a = {
                                exports: {}
                            };
                            r(a, o.select), o.clipboardAction = a.exports
                        }
                    }(this, function(e, t) {
                        "use strict";

                        function n(e, t) {
                            if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function")
                        }
                        var i = function(e) {
                                return e && e.__esModule ? e : {
                                    default: e
                                }
                            }(t),
                            o = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                                return typeof e
                            } : function(e) {
                                return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                            },
                            r = function() {
                                function e(e, t) {
                                    for (var n = 0; n < t.length; n++) {
                                        var i = t[n];
                                        i.enumerable = i.enumerable || !1, i.configurable = !0, "value" in i && (i.writable = !0), Object.defineProperty(e, i.key, i)
                                    }
                                }
                                return function(t, n, i) {
                                    return n && e(t.prototype, n), i && e(t, i), t
                                }
                            }(),
                            a = function() {
                                function e(t) {
                                    n(this, e), this.resolveOptions(t), this.initSelection()
                                }
                                return r(e, [{
                                    key: "resolveOptions",
                                    value: function() {
                                        var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                                        this.action = e.action, this.container = e.container, this.emitter = e.emitter, this.target = e.target, this.text = e.text, this.trigger = e.trigger, this.selectedText = ""
                                    }
                                }, {
                                    key: "initSelection",
                                    value: function() {
                                        this.text ? this.selectFake() : this.target && this.selectTarget()
                                    }
                                }, {
                                    key: "selectFake",
                                    value: function() {
                                        var e = this,
                                            t = "rtl" == document.documentElement.getAttribute("dir");
                                        this.removeFake(), this.fakeHandlerCallback = function() {
                                            return e.removeFake()
                                        }, this.fakeHandler = this.container.addEventListener("click", this.fakeHandlerCallback) || !0, this.fakeElem = document.createElement("textarea"), this.fakeElem.style.fontSize = "12pt", this.fakeElem.style.border = "0", this.fakeElem.style.padding = "0", this.fakeElem.style.margin = "0", this.fakeElem.style.position = "absolute", this.fakeElem.style[t ? "right" : "left"] = "-9999px";
                                        var n = window.pageYOffset || document.documentElement.scrollTop;
                                        this.fakeElem.style.top = n + "px", this.fakeElem.setAttribute("readonly", ""), this.fakeElem.value = this.text, this.container.appendChild(this.fakeElem), this.selectedText = (0, i.default)(this.fakeElem), this.copyText()
                                    }
                                }, {
                                    key: "removeFake",
                                    value: function() {
                                        this.fakeHandler && (this.container.removeEventListener("click", this.fakeHandlerCallback), this.fakeHandler = null, this.fakeHandlerCallback = null), this.fakeElem && (this.container.removeChild(this.fakeElem), this.fakeElem = null)
                                    }
                                }, {
                                    key: "selectTarget",
                                    value: function() {
                                        this.selectedText = (0, i.default)(this.target), this.copyText()
                                    }
                                }, {
                                    key: "copyText",
                                    value: function() {
                                        var e = void 0;
                                        try {
                                            e = document.execCommand(this.action)
                                        } catch (t) {
                                            e = !1
                                        }
                                        this.handleResult(e)
                                    }
                                }, {
                                    key: "handleResult",
                                    value: function(e) {
                                        this.emitter.emit(e ? "success" : "error", {
                                            action: this.action,
                                            text: this.selectedText,
                                            trigger: this.trigger,
                                            clearSelection: this.clearSelection.bind(this)
                                        })
                                    }
                                }, {
                                    key: "clearSelection",
                                    value: function() {
                                        this.trigger && this.trigger.focus(), window.getSelection().removeAllRanges()
                                    }
                                }, {
                                    key: "destroy",
                                    value: function() {
                                        this.removeFake()
                                    }
                                }, {
                                    key: "action",
                                    set: function() {
                                        var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "copy";
                                        if (this._action = e, "copy" !== this._action && "cut" !== this._action) throw new Error('Invalid "action" value, use either "copy" or "cut"')
                                    },
                                    get: function() {
                                        return this._action
                                    }
                                }, {
                                    key: "target",
                                    set: function(e) {
                                        if (void 0 !== e) {
                                            if (!e || "object" !== (void 0 === e ? "undefined" : o(e)) || 1 !== e.nodeType) throw new Error('Invalid "target" value, use a valid Element');
                                            if ("copy" === this.action && e.hasAttribute("disabled")) throw new Error('Invalid "target" attribute. Please use "readonly" instead of "disabled" attribute');
                                            if ("cut" === this.action && (e.hasAttribute("readonly") || e.hasAttribute("disabled"))) throw new Error('Invalid "target" attribute. You can\'t cut text from elements with "readonly" or "disabled" attributes');
                                            this._target = e
                                        }
                                    },
                                    get: function() {
                                        return this._target
                                    }
                                }]), e
                            }();
                        e.exports = a
                    })
                }, {
                    select: 5
                }],
                8: [function(t, n, i) {
                    ! function(o, r) {
                        if ("function" == typeof e && e.amd) e(["module", "./clipboard-action", "tiny-emitter", "good-listener"], r);
                        else if (void 0 !== i) r(n, t("./clipboard-action"), t("tiny-emitter"), t("good-listener"));
                        else {
                            var a = {
                                exports: {}
                            };
                            r(a, o.clipboardAction, o.tinyEmitter, o.goodListener), o.clipboard = a.exports
                        }
                    }(this, function(e, t, n, i) {
                        "use strict";

                        function o(e) {
                            return e && e.__esModule ? e : {
                                default: e
                            }
                        }

                        function r(e, t) {
                            if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function")
                        }

                        function a(e, t) {
                            if (!e) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                            return !t || "object" != typeof t && "function" != typeof t ? e : t
                        }

                        function s(e, t) {
                            if ("function" != typeof t && null !== t) throw new TypeError("Super expression must either be null or a function, not " + typeof t);
                            e.prototype = Object.create(t && t.prototype, {
                                constructor: {
                                    value: e,
                                    enumerable: !1,
                                    writable: !0,
                                    configurable: !0
                                }
                            }), t && (Object.setPrototypeOf ? Object.setPrototypeOf(e, t) : e.__proto__ = t)
                        }

                        function l(e, t) {
                            var n = "data-clipboard-" + e;
                            if (t.hasAttribute(n)) return t.getAttribute(n)
                        }
                        var c = o(t),
                            u = o(n),
                            d = o(i),
                            f = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
                                return typeof e
                            } : function(e) {
                                return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
                            },
                            p = function() {
                                function e(e, t) {
                                    for (var n = 0; n < t.length; n++) {
                                        var i = t[n];
                                        i.enumerable = i.enumerable || !1, i.configurable = !0, "value" in i && (i.writable = !0), Object.defineProperty(e, i.key, i)
                                    }
                                }
                                return function(t, n, i) {
                                    return n && e(t.prototype, n), i && e(t, i), t
                                }
                            }(),
                            h = function(e) {
                                function t(e, n) {
                                    r(this, t);
                                    var i = a(this, (t.__proto__ || Object.getPrototypeOf(t)).call(this));
                                    return i.resolveOptions(n), i.listenClick(e), i
                                }
                                return s(t, e), p(t, [{
                                    key: "resolveOptions",
                                    value: function() {
                                        var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {};
                                        this.action = "function" == typeof e.action ? e.action : this.defaultAction, this.target = "function" == typeof e.target ? e.target : this.defaultTarget, this.text = "function" == typeof e.text ? e.text : this.defaultText, this.container = "object" === f(e.container) ? e.container : document.body
                                    }
                                }, {
                                    key: "listenClick",
                                    value: function(e) {
                                        var t = this;
                                        this.listener = (0, d.default)(e, "click", function(e) {
                                            return t.onClick(e)
                                        })
                                    }
                                }, {
                                    key: "onClick",
                                    value: function(e) {
                                        var t = e.delegateTarget || e.currentTarget;
                                        this.clipboardAction && (this.clipboardAction = null), this.clipboardAction = new c.default({
                                            action: this.action(t),
                                            target: this.target(t),
                                            text: this.text(t),
                                            container: this.container,
                                            trigger: t,
                                            emitter: this
                                        })
                                    }
                                }, {
                                    key: "defaultAction",
                                    value: function(e) {
                                        return l("action", e)
                                    }
                                }, {
                                    key: "defaultTarget",
                                    value: function(e) {
                                        var t = l("target", e);
                                        if (t) return document.querySelector(t)
                                    }
                                }, {
                                    key: "defaultText",
                                    value: function(e) {
                                        return l("text", e)
                                    }
                                }, {
                                    key: "destroy",
                                    value: function() {
                                        this.listener.destroy(), this.clipboardAction && (this.clipboardAction.destroy(), this.clipboardAction = null)
                                    }
                                }], [{
                                    key: "isSupported",
                                    value: function() {
                                        var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : ["copy", "cut"],
                                            t = "string" == typeof e ? [e] : e,
                                            n = !!document.queryCommandSupported;
                                        return t.forEach(function(e) {
                                            n = n && !!document.queryCommandSupported(e)
                                        }), n
                                    }
                                }]), t
                            }(u.default);
                        e.exports = h
                    })
                }, {
                    "./clipboard-action": 7,
                    "good-listener": 4,
                    "tiny-emitter": 6
                }]
            }, {}, [8])(8)
        })
    },
    WRGp: function(e, t, n) {
        window.$ = window.jQuery = n("OF5A"), n("r/NY"), window.Clipboard = n("TQvf")
    },
    nErl: function(e, t) {
        (function(t) {
            e.exports = t
        }).call(t, {})
    },
    "r/NY": function(e, t) {
        var n = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(e) {
            return typeof e
        } : function(e) {
            return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
        };
        ! function(e, t, n, i) {
            e.site = e.fn.site = function(i) {
                var o, r, a = (new Date).getTime(),
                    s = [],
                    l = arguments[0],
                    c = "string" == typeof l,
                    u = [].slice.call(arguments, 1),
                    d = e.isPlainObject(i) ? e.extend(!0, {}, e.site.settings, i) : e.extend({}, e.site.settings),
                    f = d.namespace,
                    p = d.error,
                    h = "module-" + f,
                    m = e(n),
                    g = m,
                    v = this,
                    b = g.data(h);
                return o = {
                    initialize: function() {
                        o.instantiate()
                    },
                    instantiate: function() {
                        o.verbose("Storing instance of site", o), b = o, g.data(h, o)
                    },
                    normalize: function() {
                        o.fix.console(), o.fix.requestAnimationFrame()
                    },
                    fix: {
                        console: function(e) {
                            function t() {
                                return e.apply(this, arguments)
                            }
                            return t.toString = function() {
                                return e.toString()
                            }, t
                        }(function() {
                            o.debug("Normalizing window.console"), void 0 !== console && void 0 !== console.log || (o.verbose("Console not available, normalizing events"), o.disable.console()), void 0 !== console.group && void 0 !== console.groupEnd && void 0 !== console.groupCollapsed || (o.verbose("Console group not available, normalizing events"), t.console.group = function() {}, t.console.groupEnd = function() {}, t.console.groupCollapsed = function() {}), void 0 === console.markTimeline && (o.verbose("Mark timeline not available, normalizing events"), t.console.markTimeline = function() {})
                        }),
                        consoleClear: function() {
                            o.debug("Disabling programmatic console clearing"), t.console.clear = function() {}
                        },
                        requestAnimationFrame: function() {
                            o.debug("Normalizing requestAnimationFrame"), void 0 === t.requestAnimationFrame && (o.debug("RequestAnimationFrame not available, normalizing event"), t.requestAnimationFrame = t.requestAnimationFrame || t.mozRequestAnimationFrame || t.webkitRequestAnimationFrame || t.msRequestAnimationFrame || function(e) {
                                setTimeout(e, 0)
                            })
                        }
                    },
                    moduleExists: function(t) {
                        return void 0 !== e.fn[t] && void 0 !== e.fn[t].settings
                    },
                    enabled: {
                        modules: function(t) {
                            var n = [];
                            return t = t || d.modules, e.each(t, function(e, t) {
                                o.moduleExists(t) && n.push(t)
                            }), n
                        }
                    },
                    disabled: {
                        modules: function(t) {
                            var n = [];
                            return t = t || d.modules, e.each(t, function(e, t) {
                                o.moduleExists(t) || n.push(t)
                            }), n
                        }
                    },
                    change: {
                        setting: function(t, n, i, r) {
                            i = "string" == typeof i ? "all" === i ? d.modules : [i] : i || d.modules, r = void 0 === r || r, e.each(i, function(i, a) {
                                var s, l = !o.moduleExists(a) || e.fn[a].settings.namespace || !1;
                                o.moduleExists(a) && (o.verbose("Changing default setting", t, n, a), e.fn[a].settings[t] = n, r && l && (s = e(":data(module-" + l + ")"), s.length > 0 && (o.verbose("Modifying existing settings", s), s[a]("setting", t, n))))
                            })
                        },
                        settings: function(t, n, i) {
                            n = "string" == typeof n ? [n] : n || d.modules, i = void 0 === i || i, e.each(n, function(n, r) {
                                var a;
                                o.moduleExists(r) && (o.verbose("Changing default setting", t, r), e.extend(!0, e.fn[r].settings, t), i && f && (a = e(":data(module-" + f + ")"), a.length > 0 && (o.verbose("Modifying existing settings", a), a[r]("setting", t))))
                            })
                        }
                    },
                    enable: {
                        console: function() {
                            o.console(!0)
                        },
                        debug: function(e, t) {
                            e = e || d.modules, o.debug("Enabling debug for modules", e), o.change.setting("debug", !0, e, t)
                        },
                        verbose: function(e, t) {
                            e = e || d.modules, o.debug("Enabling verbose debug for modules", e), o.change.setting("verbose", !0, e, t)
                        }
                    },
                    disable: {
                        console: function() {
                            o.console(!1)
                        },
                        debug: function(e, t) {
                            e = e || d.modules, o.debug("Disabling debug for modules", e), o.change.setting("debug", !1, e, t)
                        },
                        verbose: function(e, t) {
                            e = e || d.modules, o.debug("Disabling verbose debug for modules", e), o.change.setting("verbose", !1, e, t)
                        }
                    },
                    console: function(e) {
                        if (e) {
                            if (void 0 === b.cache.console) return void o.error(p.console);
                            o.debug("Restoring console function"), t.console = b.cache.console
                        } else o.debug("Disabling console function"), b.cache.console = t.console, t.console = {
                            clear: function() {},
                            error: function() {},
                            group: function() {},
                            groupCollapsed: function() {},
                            groupEnd: function() {},
                            info: function() {},
                            log: function() {},
                            markTimeline: function() {},
                            warn: function() {}
                        }
                    },
                    destroy: function() {
                        o.verbose("Destroying previous site for", g), g.removeData(h)
                    },
                    cache: {},
                    setting: function(t, n) {
                        if (e.isPlainObject(t)) e.extend(!0, d, t);
                        else {
                            if (void 0 === n) return d[t];
                            d[t] = n
                        }
                    },
                    internal: function(t, n) {
                        if (e.isPlainObject(t)) e.extend(!0, o, t);
                        else {
                            if (void 0 === n) return o[t];
                            o[t] = n
                        }
                    },
                    debug: function() {
                        d.debug && (d.performance ? o.performance.log(arguments) : (o.debug = Function.prototype.bind.call(console.info, console, d.name + ":"), o.debug.apply(console, arguments)))
                    },
                    verbose: function() {
                        d.verbose && d.debug && (d.performance ? o.performance.log(arguments) : (o.verbose = Function.prototype.bind.call(console.info, console, d.name + ":"), o.verbose.apply(console, arguments)))
                    },
                    error: function() {
                        o.error = Function.prototype.bind.call(console.error, console, d.name + ":"), o.error.apply(console, arguments)
                    },
                    performance: {
                        log: function(e) {
                            var t, n, i;
                            d.performance && (t = (new Date).getTime(), i = a || t, n = t - i, a = t, s.push({
                                Element: v,
                                Name: e[0],
                                Arguments: [].slice.call(e, 1) || "",
                                "Execution Time": n
                            })), clearTimeout(o.performance.timer), o.performance.timer = setTimeout(o.performance.display, 500)
                        },
                        display: function() {
                            var t = d.name + ":",
                                n = 0;
                            a = !1, clearTimeout(o.performance.timer), e.each(s, function(e, t) {
                                n += t["Execution Time"]
                            }), t += " " + n + "ms", (void 0 !== console.group || void 0 !== console.table) && s.length > 0 && (console.table || e.each(s, function(e, t) {})), s = []
                        }
                    },
                    invoke: function(t, n, i) {
                        var a, s, l, c = b;
                        return n = n || u, i = v || i, "string" == typeof t && void 0 !== c && (t = t.split(/[\. ]/), a = t.length - 1, e.each(t, function(n, i) {
                            var r = n != a ? i + t[n + 1].charAt(0).toUpperCase() + t[n + 1].slice(1) : t;
                            if (e.isPlainObject(c[r]) && n != a) c = c[r];
                            else {
                                if (void 0 !== c[r]) return s = c[r], !1;
                                if (!e.isPlainObject(c[i]) || n == a) return void 0 !== c[i] ? (s = c[i], !1) : (o.error(p.method, t), !1);
                                c = c[i]
                            }
                        })), e.isFunction(s) ? l = s.apply(i, n) : void 0 !== s && (l = s), e.isArray(r) ? r.push(l) : void 0 !== r ? r = [r, l] : void 0 !== l && (r = l), s
                    }
                }, c ? (void 0 === b && o.initialize(), o.invoke(l)) : (void 0 !== b && o.destroy(), o.initialize()), void 0 !== r ? r : this
            }, e.site.settings = {
                name: "Site",
                namespace: "site",
                error: {
                    console: "Console cannot be restored, most likely it was overwritten outside of module",
                    method: "The method you called is not defined."
                },
                debug: !1,
                verbose: !1,
                performance: !0,
                modules: ["accordion", "api", "checkbox", "dimmer", "dropdown", "embed", "form", "modal", "nag", "popup", "rating", "shape", "sidebar", "state", "sticky", "tab", "transition", "visit", "visibility"],
                siteNamespace: "site",
                namespaceStub: {
                    cache: {},
                    config: {},
                    sections: {},
                    section: {},
                    utilities: {}
                }
            }, e.extend(e.expr[":"], {
                data: e.expr.createPseudo ? e.expr.createPseudo(function(t) {
                    return function(n) {
                        return !!e.data(n, t)
                    }
                }) : function(t, n, i) {
                    return !!e.data(t, i[3])
                }
            })
        }(jQuery, window, document),
        function(e, t, n, i) {
            "use strict";
            t = void 0 !== t && t.Math == Math ? t : "undefined" != typeof self && self.Math == Math ? self : Function("return this")(), e.fn.form = function(t) {
                var i, o = e(this),
                    r = o.selector || "",
                    a = (new Date).getTime(),
                    s = [],
                    l = arguments[0],
                    c = arguments[1],
                    u = "string" == typeof l,
                    d = [].slice.call(arguments, 1);
                return o.each(function() {
                    var f, p, h, m, g, v, b, y, x, w, C, k, S, T, A, E, D, O, F, j = e(this),
                        q = this,
                        L = [],
                        N = !1;
                    F = {
                        initialize: function() {
                            F.get.settings(), u ? (void 0 === O && F.instantiate(), F.invoke(l)) : (void 0 !== O && O.invoke("destroy"), F.verbose("Initializing form validation", j, y), F.bindEvents(), F.set.defaults(), F.instantiate())
                        },
                        instantiate: function() {
                            F.verbose("Storing instance of module", F), O = F, j.data(E, F)
                        },
                        destroy: function() {
                            F.verbose("Destroying previous module", O), F.removeEvents(), j.removeData(E)
                        },
                        refresh: function() {
                            F.verbose("Refreshing selector cache"), f = j.find(C.field), p = j.find(C.group), h = j.find(C.message), m = j.find(C.prompt), g = j.find(C.submit), v = j.find(C.clear), b = j.find(C.reset)
                        },
                        submit: function() {
                            F.verbose("Submitting form", j), j.submit()
                        },
                        attachEvents: function(t, n) {
                            n = n || "submit", e(t).on("click" + D, function(e) {
                                F[n](), e.preventDefault()
                            })
                        },
                        bindEvents: function() {
                            F.verbose("Attaching form events"), j.on("submit" + D, F.validate.form).on("blur" + D, C.field, F.event.field.blur).on("click" + D, C.submit, F.submit).on("click" + D, C.reset, F.reset).on("click" + D, C.clear, F.clear), y.keyboardShortcuts && j.on("keydown" + D, C.field, F.event.field.keydown), f.each(function() {
                                var t = e(this),
                                    n = t.prop("type"),
                                    i = F.get.changeEvent(n, t);
                                e(this).on(i + D, F.event.field.change)
                            })
                        },
                        clear: function() {
                            f.each(function() {
                                var t = e(this),
                                    n = t.parent(),
                                    i = t.closest(p),
                                    o = i.find(C.prompt),
                                    r = t.data(w.defaultValue) || "",
                                    a = n.is(C.uiCheckbox),
                                    s = n.is(C.uiDropdown);
                                i.hasClass(k.error) && (F.verbose("Resetting error on field", i), i.removeClass(k.error), o.remove()), s ? (F.verbose("Resetting dropdown value", n, r), n.dropdown("clear")) : a ? t.prop("checked", !1) : (F.verbose("Resetting field value", t, r), t.val(""))
                            })
                        },
                        reset: function() {
                            f.each(function() {
                                var t = e(this),
                                    n = t.parent(),
                                    i = t.closest(p),
                                    o = i.find(C.prompt),
                                    r = t.data(w.defaultValue),
                                    a = n.is(C.uiCheckbox),
                                    s = n.is(C.uiDropdown),
                                    l = i.hasClass(k.error);
                                void 0 !== r && (l && (F.verbose("Resetting error on field", i), i.removeClass(k.error), o.remove()), s ? (F.verbose("Resetting dropdown value", n, r), n.dropdown("restore defaults")) : a ? (F.verbose("Resetting checkbox value", n, r), t.prop("checked", r)) : (F.verbose("Resetting field value", t, r), t.val(r)))
                            })
                        },
                        determine: {
                            isValid: function() {
                                var t = !0;
                                return e.each(x, function(e, n) {
                                    F.validate.field(n, e, !0) || (t = !1)
                                }), t
                            }
                        },
                        is: {
                            bracketedRule: function(e) {
                                return e.type && e.type.match(y.regExp.bracket)
                            },
                            empty: function(e) {
                                return !e || 0 === e.length || (e.is('input[type="checkbox"]') ? !e.is(":checked") : F.is.blank(e))
                            },
                            blank: function(t) {
                                return "" === e.trim(t.val())
                            },
                            valid: function(t) {
                                var n = !0;
                                return t ? (F.verbose("Checking if field is valid", t), F.validate.field(x[t], t, !1)) : (F.verbose("Checking if form is valid"), e.each(x, function(e, t) {
                                    F.is.valid(e) || (n = !1)
                                }), n)
                            }
                        },
                        removeEvents: function() {
                            j.off(D), f.off(D), g.off(D), f.off(D)
                        },
                        event: {
                            field: {
                                keydown: function(t) {
                                    var n = e(this),
                                        i = t.which,
                                        o = n.is(C.input),
                                        r = n.is(C.checkbox),
                                        a = n.closest(C.uiDropdown).length > 0,
                                        s = {
                                            enter: 13,
                                            escape: 27
                                        };
                                    i == s.escape && (F.verbose("Escape key pressed blurring field"), n.blur()), t.ctrlKey || i != s.enter || !o || a || r || (N || (n.one("keyup" + D, F.event.field.keyup), F.submit(), F.debug("Enter pressed on input submitting form")), N = !0)
                                },
                                keyup: function() {
                                    N = !1
                                },
                                blur: function(t) {
                                    var n = e(this),
                                        i = n.closest(p),
                                        o = F.get.validation(n);
                                    i.hasClass(k.error) ? (F.debug("Revalidating field", n, o), o && F.validate.field(o)) : "blur" != y.on && "change" != y.on || o && F.validate.field(o)
                                },
                                change: function(t) {
                                    var n = e(this),
                                        i = n.closest(p),
                                        o = F.get.validation(n);
                                    o && ("change" == y.on || i.hasClass(k.error) && y.revalidate) && (clearTimeout(F.timer), F.timer = setTimeout(function() {
                                        F.debug("Revalidating field", n, F.get.validation(n)), F.validate.field(o)
                                    }, y.delay))
                                }
                            }
                        },
                        get: {
                            ancillaryValue: function(e) {
                                return !(!e.type || !e.value && !F.is.bracketedRule(e)) && (void 0 !== e.value ? e.value : e.type.match(y.regExp.bracket)[1] + "")
                            },
                            ruleName: function(e) {
                                return F.is.bracketedRule(e) ? e.type.replace(e.type.match(y.regExp.bracket)[0], "") : e.type
                            },
                            changeEvent: function(e, t) {
                                return "checkbox" == e || "radio" == e || "hidden" == e || t.is("select") ? "change" : F.get.inputEvent()
                            },
                            inputEvent: function() {
                                return void 0 !== n.createElement("input").oninput ? "input" : void 0 !== n.createElement("input").onpropertychange ? "propertychange" : "keyup"
                            },
                            prompt: function(e, t) {
                                var n, i, o, r = F.get.ruleName(e),
                                    a = F.get.ancillaryValue(e),
                                    s = e.prompt || y.prompt[r] || y.text.unspecifiedRule,
                                    l = -1 !== s.search("{value}"),
                                    c = -1 !== s.search("{name}");
                                return (c || l) && (i = F.get.field(t.identifier)), l && (s = s.replace("{value}", i.val())), c && (n = i.closest(C.group).find("label").eq(0), o = 1 == n.length ? n.text() : i.prop("placeholder") || y.text.unspecifiedField, s = s.replace("{name}", o)), s = s.replace("{identifier}", t.identifier), s = s.replace("{ruleValue}", a), e.prompt || F.verbose("Using default validation prompt for type", s, r), s
                            },
                            settings: function() {
                                if (e.isPlainObject(t)) {
                                    var n, i = Object.keys(t);
                                    i.length > 0 && void 0 !== t[i[0]].identifier && void 0 !== t[i[0]].rules ? (y = e.extend(!0, {}, e.fn.form.settings, c), x = e.extend({}, e.fn.form.settings.defaults, t), F.error(y.error.oldSyntax, q), F.verbose("Extending settings from legacy parameters", x, y)) : (t.fields && (n = Object.keys(t.fields), ("string" == typeof t.fields[n[0]] || e.isArray(t.fields[n[0]])) && e.each(t.fields, function(n, i) {
                                        "string" == typeof i && (i = [i]), t.fields[n] = {
                                            rules: []
                                        }, e.each(i, function(e, i) {
                                            t.fields[n].rules.push({
                                                type: i
                                            })
                                        })
                                    })), y = e.extend(!0, {}, e.fn.form.settings, t), x = e.extend({}, e.fn.form.settings.defaults, y.fields), F.verbose("Extending settings", x, y))
                                } else y = e.fn.form.settings, x = e.fn.form.settings.defaults, F.verbose("Using default form validation", x, y);
                                A = y.namespace, w = y.metadata, C = y.selector, k = y.className, S = y.regExp, T = y.error, E = "module-" + A, D = "." + A, O = j.data(E), F.refresh()
                            },
                            field: function(t) {
                                return F.verbose("Finding field with identifier", t), t = F.escape.string(t), f.filter("#" + t).length > 0 ? f.filter("#" + t) : f.filter('[name="' + t + '"]').length > 0 ? f.filter('[name="' + t + '"]') : f.filter('[name="' + t + '[]"]').length > 0 ? f.filter('[name="' + t + '[]"]') : f.filter("[data-" + w.validate + '="' + t + '"]').length > 0 ? f.filter("[data-" + w.validate + '="' + t + '"]') : e("<input/>")
                            },
                            fields: function(t) {
                                var n = e();
                                return e.each(t, function(e, t) {
                                    n = n.add(F.get.field(t))
                                }), n
                            },
                            validation: function(t) {
                                var n, i;
                                return !!x && (e.each(x, function(e, o) {
                                    i = o.identifier || e, F.get.field(i)[0] == t[0] && (o.identifier = i, n = o)
                                }), n || !1)
                            },
                            value: function(e) {
                                var t, n = [];
                                return n.push(e), t = F.get.values.call(q, n), t[e]
                            },
                            values: function(t) {
                                var n = e.isArray(t) ? F.get.fields(t) : f,
                                    i = {};
                                return n.each(function(t, n) {
                                    var o = e(n),
                                        r = (o.prop("type"), o.prop("name")),
                                        a = o.val(),
                                        s = o.is(C.checkbox),
                                        l = o.is(C.radio),
                                        c = -1 !== r.indexOf("[]"),
                                        u = !!s && o.is(":checked");
                                    r && (c ? (r = r.replace("[]", ""), i[r] || (i[r] = []), s ? u ? i[r].push(a || !0) : i[r].push(!1) : i[r].push(a)) : l ? u && (i[r] = a) : i[r] = s ? !!u && (a || !0) : a)
                                }), i
                            }
                        },
                        has: {
                            field: function(e) {
                                return F.verbose("Checking for existence of a field with identifier", e), e = F.escape.string(e), "string" != typeof e && F.error(T.identifier, e), f.filter("#" + e).length > 0 || f.filter('[name="' + e + '"]').length > 0 || f.filter("[data-" + w.validate + '="' + e + '"]').length > 0
                            }
                        },
                        escape: {
                            string: function(e) {
                                return e = String(e), e.replace(S.escape, "\\$&")
                            }
                        },
                        add: {
                            prompt: function(t, n) {
                                var i = F.get.field(t),
                                    o = i.closest(p),
                                    r = o.children(C.prompt),
                                    a = 0 !== r.length;
                                n = "string" == typeof n ? [n] : n, F.verbose("Adding field error state", t), o.addClass(k.error), y.inline && (a || (r = y.templates.prompt(n), r.appendTo(o)), r.html(n[0]), a ? F.verbose("Inline errors are disabled, no inline error added", t) : y.transition && void 0 !== e.fn.transition && j.transition("is supported") ? (F.verbose("Displaying error with css transition", y.transition), r.transition(y.transition + " in", y.duration)) : (F.verbose("Displaying error with fallback javascript animation"), r.fadeIn(y.duration)))
                            },
                            errors: function(e) {
                                F.debug("Adding form error messages", e), F.set.error(), h.html(y.templates.error(e))
                            }
                        },
                        remove: {
                            prompt: function(t) {
                                var n = F.get.field(t),
                                    i = n.closest(p),
                                    o = i.children(C.prompt);
                                i.removeClass(k.error), y.inline && o.is(":visible") && (F.verbose("Removing prompt for field", t), y.transition && void 0 !== e.fn.transition && j.transition("is supported") ? o.transition(y.transition + " out", y.duration, function() {
                                    o.remove()
                                }) : o.fadeOut(y.duration, function() {
                                    o.remove()
                                }))
                            }
                        },
                        set: {
                            success: function() {
                                j.removeClass(k.error).addClass(k.success)
                            },
                            defaults: function() {
                                f.each(function() {
                                    var t = e(this),
                                        n = t.filter(C.checkbox).length > 0,
                                        i = n ? t.is(":checked") : t.val();
                                    t.data(w.defaultValue, i)
                                })
                            },
                            error: function() {
                                j.removeClass(k.success).addClass(k.error)
                            },
                            value: function(e, t) {
                                var n = {};
                                return n[e] = t, F.set.values.call(q, n)
                            },
                            values: function(t) {
                                e.isEmptyObject(t) || e.each(t, function(t, n) {
                                    var i, o = F.get.field(t),
                                        r = o.parent(),
                                        a = e.isArray(n),
                                        s = r.is(C.uiCheckbox),
                                        l = r.is(C.uiDropdown),
                                        c = o.is(C.radio) && s;
                                    o.length > 0 && (a && s ? (F.verbose("Selecting multiple", n, o), r.checkbox("uncheck"), e.each(n, function(e, t) {
                                        i = o.filter('[value="' + t + '"]'), r = i.parent(), i.length > 0 && r.checkbox("check")
                                    })) : c ? (F.verbose("Selecting radio value", n, o), o.filter('[value="' + n + '"]').parent(C.uiCheckbox).checkbox("check")) : s ? (F.verbose("Setting checkbox value", n, r), !0 === n ? r.checkbox("check") : r.checkbox("uncheck")) : l ? (F.verbose("Setting dropdown value", n, r), r.dropdown("set selected", n)) : (F.verbose("Setting field value", n, o), o.val(n)))
                                })
                            }
                        },
                        validate: {
                            form: function(e, t) {
                                var n = F.get.values();
                                if (N) return !1;
                                if (L = [], F.determine.isValid()) {
                                    if (F.debug("Form has no validation errors, submitting"), F.set.success(), !0 !== t) return y.onSuccess.call(q, e, n)
                                } else if (F.debug("Form has errors"), F.set.error(), y.inline || F.add.errors(L), void 0 !== j.data("moduleApi") && e.stopImmediatePropagation(), !0 !== t) return y.onFailure.call(q, L, n)
                            },
                            field: function(t, n, i) {
                                i = void 0 === i || i, "string" == typeof t && (F.verbose("Validating field", t), n = t, t = x[t]);
                                var o = t.identifier || n,
                                    r = F.get.field(o),
                                    a = !!t.depends && F.get.field(t.depends),
                                    s = !0,
                                    l = [];
                                return t.identifier || (F.debug("Using field name as identifier", o), t.identifier = o), r.prop("disabled") ? (F.debug("Field is disabled. Skipping", o), s = !0) : t.optional && F.is.blank(r) ? (F.debug("Field is optional and blank. Skipping", o), s = !0) : t.depends && F.is.empty(a) ? (F.debug("Field depends on another value that is not present or empty. Skipping", a), s = !0) : void 0 !== t.rules && e.each(t.rules, function(e, n) {
                                    F.has.field(o) && !F.validate.rule(t, n) && (F.debug("Field is invalid", o, n.type), l.push(F.get.prompt(n, t)), s = !1)
                                }), s ? (i && (F.remove.prompt(o, l), y.onValid.call(r)), !0) : (i && (L = L.concat(l), F.add.prompt(o, l), y.onInvalid.call(r, l)), !1)
                            },
                            rule: function(t, n) {
                                var i = F.get.field(t.identifier),
                                    o = (n.type, i.val()),
                                    r = F.get.ancillaryValue(n),
                                    a = F.get.ruleName(n),
                                    s = y.rules[a];
                                return e.isFunction(s) ? (o = void 0 === o || "" === o || null === o ? "" : e.trim(o + ""), s.call(i, o, r)) : void F.error(T.noRule, a)
                            }
                        },
                        setting: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, y, t);
                            else {
                                if (void 0 === n) return y[t];
                                y[t] = n
                            }
                        },
                        internal: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, F, t);
                            else {
                                if (void 0 === n) return F[t];
                                F[t] = n
                            }
                        },
                        debug: function() {
                            !y.silent && y.debug && (y.performance ? F.performance.log(arguments) : (F.debug = Function.prototype.bind.call(console.info, console, y.name + ":"), F.debug.apply(console, arguments)))
                        },
                        verbose: function() {
                            !y.silent && y.verbose && y.debug && (y.performance ? F.performance.log(arguments) : (F.verbose = Function.prototype.bind.call(console.info, console, y.name + ":"), F.verbose.apply(console, arguments)))
                        },
                        error: function() {
                            y.silent || (F.error = Function.prototype.bind.call(console.error, console, y.name + ":"), F.error.apply(console, arguments))
                        },
                        performance: {
                            log: function(e) {
                                var t, n, i;
                                y.performance && (t = (new Date).getTime(), i = a || t, n = t - i, a = t, s.push({
                                    Name: e[0],
                                    Arguments: [].slice.call(e, 1) || "",
                                    Element: q,
                                    "Execution Time": n
                                })), clearTimeout(F.performance.timer), F.performance.timer = setTimeout(F.performance.display, 500)
                            },
                            display: function() {
                                var t = y.name + ":",
                                    n = 0;
                                a = !1, clearTimeout(F.performance.timer), e.each(s, function(e, t) {
                                    n += t["Execution Time"]
                                }), t += " " + n + "ms", r && (t += " '" + r + "'"), o.length > 1 && (t += " (" + o.length + ")"), (void 0 !== console.group || void 0 !== console.table) && s.length > 0 && (console.table || e.each(s, function(e, t) {})), s = []
                            }
                        },
                        invoke: function(t, n, o) {
                            var r, a, s, l = O;
                            return n = n || d, o = q || o, "string" == typeof t && void 0 !== l && (t = t.split(/[\. ]/), r = t.length - 1, e.each(t, function(n, i) {
                                var o = n != r ? i + t[n + 1].charAt(0).toUpperCase() + t[n + 1].slice(1) : t;
                                if (e.isPlainObject(l[o]) && n != r) l = l[o];
                                else {
                                    if (void 0 !== l[o]) return a = l[o], !1;
                                    if (!e.isPlainObject(l[i]) || n == r) return void 0 !== l[i] && (a = l[i], !1);
                                    l = l[i]
                                }
                            })), e.isFunction(a) ? s = a.apply(o, n) : void 0 !== a && (s = a), e.isArray(i) ? i.push(s) : void 0 !== i ? i = [i, s] : void 0 !== s && (i = s), a
                        }
                    }, F.initialize()
                }), void 0 !== i ? i : this
            }, e.fn.form.settings = {
                name: "Form",
                namespace: "form",
                debug: !1,
                verbose: !1,
                performance: !0,
                fields: !1,
                keyboardShortcuts: !0,
                on: "submit",
                inline: !1,
                delay: 200,
                revalidate: !0,
                transition: "scale",
                duration: 200,
                onValid: function() {},
                onInvalid: function() {},
                onSuccess: function() {
                    return !0
                },
                onFailure: function() {
                    return !1
                },
                metadata: {
                    defaultValue: "default",
                    validate: "validate"
                },
                regExp: {
                    htmlID: /^[a-zA-Z][\w:.-]*$/g,
                    bracket: /\[(.*)\]/i,
                    decimal: /^\d+\.?\d*$/,
                    email: /^[a-z0-9!#$%&'*+\/=?^_`{|}~.-]+@[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)*$/i,
                    escape: /[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g,
                    flags: /^\/(.*)\/(.*)?/,
                    integer: /^\-?\d+$/,
                    number: /^\-?\d*(\.\d+)?$/,
                    url: /(https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})/i
                },
                text: {
                    unspecifiedRule: "Please enter a valid value",
                    unspecifiedField: "This field"
                },
                prompt: {
                    empty: "{name} must have a value",
                    checked: "{name} must be checked",
                    email: "{name} must be a valid e-mail",
                    url: "{name} must be a valid url",
                    regExp: "{name} is not formatted correctly",
                    integer: "{name} must be an integer",
                    decimal: "{name} must be a decimal number",
                    number: "{name} must be set to a number",
                    is: '{name} must be "{ruleValue}"',
                    isExactly: '{name} must be exactly "{ruleValue}"',
                    not: '{name} cannot be set to "{ruleValue}"',
                    notExactly: '{name} cannot be set to exactly "{ruleValue}"',
                    contain: '{name} cannot contain "{ruleValue}"',
                    containExactly: '{name} cannot contain exactly "{ruleValue}"',
                    doesntContain: '{name} must contain  "{ruleValue}"',
                    doesntContainExactly: '{name} must contain exactly "{ruleValue}"',
                    minLength: "{name} must be at least {ruleValue} characters",
                    length: "{name} must be at least {ruleValue} characters",
                    exactLength: "{name} must be exactly {ruleValue} characters",
                    maxLength: "{name} cannot be longer than {ruleValue} characters",
                    match: "{name} must match {ruleValue} field",
                    different: "{name} must have a different value than {ruleValue} field",
                    creditCard: "{name} must be a valid credit card number",
                    minCount: "{name} must have at least {ruleValue} choices",
                    exactCount: "{name} must have exactly {ruleValue} choices",
                    maxCount: "{name} must have {ruleValue} or less choices"
                },
                selector: {
                    checkbox: 'input[type="checkbox"], input[type="radio"]',
                    clear: ".clear",
                    field: "input, textarea, select",
                    group: ".field",
                    input: "input",
                    message: ".error.message",
                    prompt: ".prompt.label",
                    radio: 'input[type="radio"]',
                    reset: '.reset:not([type="reset"])',
                    submit: '.submit:not([type="submit"])',
                    uiCheckbox: ".ui.checkbox",
                    uiDropdown: ".ui.dropdown"
                },
                className: {
                    error: "error",
                    label: "ui prompt label",
                    pressed: "down",
                    success: "success"
                },
                error: {
                    identifier: "You must specify a string identifier for each field",
                    method: "The method you called is not defined.",
                    noRule: "There is no rule matching the one you specified",
                    oldSyntax: "Starting in 2.0 forms now only take a single settings object. Validation settings converted to new syntax automatically."
                },
                templates: {
                    error: function(t) {
                        var n = '<ul class="list">';
                        return e.each(t, function(e, t) {
                            n += "<li>" + t + "</li>"
                        }), n += "</ul>", e(n)
                    },
                    prompt: function(t) {
                        return e("<div/>").addClass("ui basic red pointing prompt label").html(t[0])
                    }
                },
                rules: {
                    empty: function(t) {
                        return !(void 0 === t || "" === t || e.isArray(t) && 0 === t.length)
                    },
                    checked: function() {
                        return e(this).filter(":checked").length > 0
                    },
                    email: function(t) {
                        return e.fn.form.settings.regExp.email.test(t)
                    },
                    url: function(t) {
                        return e.fn.form.settings.regExp.url.test(t)
                    },
                    regExp: function(t, n) {
                        if (n instanceof RegExp) return t.match(n);
                        var i, o = n.match(e.fn.form.settings.regExp.flags);
                        return o && (n = o.length >= 2 ? o[1] : n, i = o.length >= 3 ? o[2] : ""), t.match(new RegExp(n, i))
                    },
                    integer: function(t, n) {
                        var i, o, r, a = e.fn.form.settings.regExp.integer;
                        return n && -1 === ["", ".."].indexOf(n) && (-1 == n.indexOf("..") ? a.test(n) && (i = o = n - 0) : (r = n.split("..", 2), a.test(r[0]) && (i = r[0] - 0), a.test(r[1]) && (o = r[1] - 0))), a.test(t) && (void 0 === i || t >= i) && (void 0 === o || t <= o)
                    },
                    decimal: function(t) {
                        return e.fn.form.settings.regExp.decimal.test(t)
                    },
                    number: function(t) {
                        return e.fn.form.settings.regExp.number.test(t)
                    },
                    is: function(e, t) {
                        return t = "string" == typeof t ? t.toLowerCase() : t, (e = "string" == typeof e ? e.toLowerCase() : e) == t
                    },
                    isExactly: function(e, t) {
                        return e == t
                    },
                    not: function(e, t) {
                        return e = "string" == typeof e ? e.toLowerCase() : e, t = "string" == typeof t ? t.toLowerCase() : t, e != t
                    },
                    notExactly: function(e, t) {
                        return e != t
                    },
                    contains: function(t, n) {
                        return n = n.replace(e.fn.form.settings.regExp.escape, "\\$&"), -1 !== t.search(new RegExp(n, "i"))
                    },
                    containsExactly: function(t, n) {
                        return n = n.replace(e.fn.form.settings.regExp.escape, "\\$&"), -1 !== t.search(new RegExp(n))
                    },
                    doesntContain: function(t, n) {
                        return n = n.replace(e.fn.form.settings.regExp.escape, "\\$&"), -1 === t.search(new RegExp(n, "i"))
                    },
                    doesntContainExactly: function(t, n) {
                        return n = n.replace(e.fn.form.settings.regExp.escape, "\\$&"), -1 === t.search(new RegExp(n))
                    },
                    minLength: function(e, t) {
                        return void 0 !== e && e.length >= t
                    },
                    length: function(e, t) {
                        return void 0 !== e && e.length >= t
                    },
                    exactLength: function(e, t) {
                        return void 0 !== e && e.length == t
                    },
                    maxLength: function(e, t) {
                        return void 0 !== e && e.length <= t
                    },
                    match: function(t, n) {
                        var i;
                        return e(this), e('[data-validate="' + n + '"]').length > 0 ? i = e('[data-validate="' + n + '"]').val() : e("#" + n).length > 0 ? i = e("#" + n).val() : e('[name="' + n + '"]').length > 0 ? i = e('[name="' + n + '"]').val() : e('[name="' + n + '[]"]').length > 0 && (i = e('[name="' + n + '[]"]')), void 0 !== i && t.toString() == i.toString()
                    },
                    different: function(t, n) {
                        var i;
                        return e(this), e('[data-validate="' + n + '"]').length > 0 ? i = e('[data-validate="' + n + '"]').val() : e("#" + n).length > 0 ? i = e("#" + n).val() : e('[name="' + n + '"]').length > 0 ? i = e('[name="' + n + '"]').val() : e('[name="' + n + '[]"]').length > 0 && (i = e('[name="' + n + '[]"]')), void 0 !== i && t.toString() !== i.toString()
                    },
                    creditCard: function(t, n) {
                        var i, o, r = {
                                visa: {
                                    pattern: /^4/,
                                    length: [16]
                                },
                                amex: {
                                    pattern: /^3[47]/,
                                    length: [15]
                                },
                                mastercard: {
                                    pattern: /^5[1-5]/,
                                    length: [16]
                                },
                                discover: {
                                    pattern: /^(6011|622(12[6-9]|1[3-9][0-9]|[2-8][0-9]{2}|9[0-1][0-9]|92[0-5]|64[4-9])|65)/,
                                    length: [16]
                                },
                                unionPay: {
                                    pattern: /^(62|88)/,
                                    length: [16, 17, 18, 19]
                                },
                                jcb: {
                                    pattern: /^35(2[89]|[3-8][0-9])/,
                                    length: [16]
                                },
                                maestro: {
                                    pattern: /^(5018|5020|5038|6304|6759|676[1-3])/,
                                    length: [12, 13, 14, 15, 16, 17, 18, 19]
                                },
                                dinersClub: {
                                    pattern: /^(30[0-5]|^36)/,
                                    length: [14]
                                },
                                laser: {
                                    pattern: /^(6304|670[69]|6771)/,
                                    length: [16, 17, 18, 19]
                                },
                                visaElectron: {
                                    pattern: /^(4026|417500|4508|4844|491(3|7))/,
                                    length: [16]
                                }
                            },
                            a = {},
                            s = !1,
                            l = "string" == typeof n && n.split(",");
                        if ("string" == typeof t && 0 !== t.length) {
                            if (t = t.replace(/[\-]/g, ""), l && (e.each(l, function(n, i) {
                                    (o = r[i]) && (a = {
                                        length: -1 !== e.inArray(t.length, o.length),
                                        pattern: -1 !== t.search(o.pattern)
                                    }, a.length && a.pattern && (s = !0))
                                }), !s)) return !1;
                            if (i = {
                                    number: -1 !== e.inArray(t.length, r.unionPay.length),
                                    pattern: -1 !== t.search(r.unionPay.pattern)
                                }, i.number && i.pattern) return !0;
                            for (var c = t.length, u = 0, d = [
                                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                    [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
                                ], f = 0; c--;) f += d[u][parseInt(t.charAt(c), 10)], u ^= 1;
                            return f % 10 == 0 && f > 0
                        }
                    },
                    minCount: function(e, t) {
                        return 0 == t || (1 == t ? "" !== e : e.split(",").length >= t)
                    },
                    exactCount: function(e, t) {
                        return 0 == t ? "" === e : 1 == t ? "" !== e && -1 === e.search(",") : e.split(",").length == t
                    },
                    maxCount: function(e, t) {
                        return 0 != t && (1 == t ? -1 === e.search(",") : e.split(",").length <= t)
                    }
                }
            }
        }(jQuery, window, document),
        function(e, t, n, i) {
            "use strict";
            t = void 0 !== t && t.Math == Math ? t : "undefined" != typeof self && self.Math == Math ? self : Function("return this")(), e.fn.accordion = function(n) {
                var i, o = e(this),
                    r = (new Date).getTime(),
                    a = [],
                    s = arguments[0],
                    l = "string" == typeof s,
                    c = [].slice.call(arguments, 1);
                return t.requestAnimationFrame || t.mozRequestAnimationFrame || t.webkitRequestAnimationFrame || t.msRequestAnimationFrame, o.each(function() {
                    var u, d, f = e.isPlainObject(n) ? e.extend(!0, {}, e.fn.accordion.settings, n) : e.extend({}, e.fn.accordion.settings),
                        p = f.className,
                        h = f.namespace,
                        m = f.selector,
                        g = f.error,
                        v = "." + h,
                        b = "module-" + h,
                        y = o.selector || "",
                        x = e(this),
                        w = x.find(m.title),
                        C = x.find(m.content),
                        k = this,
                        S = x.data(b);
                    d = {
                        initialize: function() {
                            d.debug("Initializing", x), d.bind.events(), f.observeChanges && d.observeChanges(), d.instantiate()
                        },
                        instantiate: function() {
                            S = d, x.data(b, d)
                        },
                        destroy: function() {
                            d.debug("Destroying previous instance", x), x.off(v).removeData(b)
                        },
                        refresh: function() {
                            w = x.find(m.title), C = x.find(m.content)
                        },
                        observeChanges: function() {
                            "MutationObserver" in t && (u = new MutationObserver(function(e) {
                                d.debug("DOM tree modified, updating selector cache"), d.refresh()
                            }), u.observe(k, {
                                childList: !0,
                                subtree: !0
                            }), d.debug("Setting up mutation observer", u))
                        },
                        bind: {
                            events: function() {
                                d.debug("Binding delegated events"), x.on(f.on + v, m.trigger, d.event.click)
                            }
                        },
                        event: {
                            click: function() {
                                d.toggle.call(this)
                            }
                        },
                        toggle: function(t) {
                            var n = void 0 !== t ? "number" == typeof t ? w.eq(t) : e(t).closest(m.title) : e(this).closest(m.title),
                                i = n.next(C),
                                o = i.hasClass(p.animating),
                                r = i.hasClass(p.active),
                                a = r && !o,
                                s = !r && o;
                            d.debug("Toggling visibility of content", n), a || s ? f.collapsible ? d.close.call(n) : d.debug("Cannot close accordion content collapsing is disabled") : d.open.call(n)
                        },
                        open: function(t) {
                            var n = void 0 !== t ? "number" == typeof t ? w.eq(t) : e(t).closest(m.title) : e(this).closest(m.title),
                                i = n.next(C),
                                o = i.hasClass(p.animating);
                            if (i.hasClass(p.active) || o) return void d.debug("Accordion already open, skipping", i);
                            d.debug("Opening accordion content", n), f.onOpening.call(i), f.exclusive && d.closeOthers.call(n), n.addClass(p.active), i.stop(!0, !0).addClass(p.animating), f.animateChildren && (void 0 !== e.fn.transition && x.transition("is supported") ? i.children().transition({
                                animation: "fade in",
                                queue: !1,
                                useFailSafe: !0,
                                debug: f.debug,
                                verbose: f.verbose,
                                duration: f.duration
                            }) : i.children().stop(!0, !0).animate({
                                opacity: 1
                            }, f.duration, d.resetOpacity)), i.slideDown(f.duration, f.easing, function() {
                                i.removeClass(p.animating).addClass(p.active), d.reset.display.call(this), f.onOpen.call(this), f.onChange.call(this)
                            })
                        },
                        close: function(t) {
                            var n = void 0 !== t ? "number" == typeof t ? w.eq(t) : e(t).closest(m.title) : e(this).closest(m.title),
                                i = n.next(C),
                                o = i.hasClass(p.animating),
                                r = i.hasClass(p.active),
                                a = !r && o,
                                s = r && o;
                            !r && !a || s || (d.debug("Closing accordion content", i), f.onClosing.call(i), n.removeClass(p.active), i.stop(!0, !0).addClass(p.animating), f.animateChildren && (void 0 !== e.fn.transition && x.transition("is supported") ? i.children().transition({
                                animation: "fade out",
                                queue: !1,
                                useFailSafe: !0,
                                debug: f.debug,
                                verbose: f.verbose,
                                duration: f.duration
                            }) : i.children().stop(!0, !0).animate({
                                opacity: 0
                            }, f.duration, d.resetOpacity)), i.slideUp(f.duration, f.easing, function() {
                                i.removeClass(p.animating).removeClass(p.active), d.reset.display.call(this), f.onClose.call(this), f.onChange.call(this)
                            }))
                        },
                        closeOthers: function(t) {
                            var n, i, o, r = void 0 !== t ? w.eq(t) : e(this).closest(m.title),
                                a = r.parents(m.content).prev(m.title),
                                s = r.closest(m.accordion),
                                l = m.title + "." + p.active + ":visible",
                                c = m.content + "." + p.active + ":visible";
                            f.closeNested ? (n = s.find(l).not(a), o = n.next(C)) : (n = s.find(l).not(a), i = s.find(c).find(l).not(a), n = n.not(i), o = n.next(C)), n.length > 0 && (d.debug("Exclusive enabled, closing other content", n), n.removeClass(p.active), o.removeClass(p.animating).stop(!0, !0), f.animateChildren && (void 0 !== e.fn.transition && x.transition("is supported") ? o.children().transition({
                                animation: "fade out",
                                useFailSafe: !0,
                                debug: f.debug,
                                verbose: f.verbose,
                                duration: f.duration
                            }) : o.children().stop(!0, !0).animate({
                                opacity: 0
                            }, f.duration, d.resetOpacity)), o.slideUp(f.duration, f.easing, function() {
                                e(this).removeClass(p.active), d.reset.display.call(this)
                            }))
                        },
                        reset: {
                            display: function() {
                                d.verbose("Removing inline display from element", this), e(this).css("display", ""), "" === e(this).attr("style") && e(this).attr("style", "").removeAttr("style")
                            },
                            opacity: function() {
                                d.verbose("Removing inline opacity from element", this), e(this).css("opacity", ""), "" === e(this).attr("style") && e(this).attr("style", "").removeAttr("style")
                            }
                        },
                        setting: function(t, n) {
                            if (d.debug("Changing setting", t, n), e.isPlainObject(t)) e.extend(!0, f, t);
                            else {
                                if (void 0 === n) return f[t];
                                e.isPlainObject(f[t]) ? e.extend(!0, f[t], n) : f[t] = n
                            }
                        },
                        internal: function(t, n) {
                            if (d.debug("Changing internal", t, n), void 0 === n) return d[t];
                            e.isPlainObject(t) ? e.extend(!0, d, t) : d[t] = n
                        },
                        debug: function() {
                            !f.silent && f.debug && (f.performance ? d.performance.log(arguments) : (d.debug = Function.prototype.bind.call(console.info, console, f.name + ":"), d.debug.apply(console, arguments)))
                        },
                        verbose: function() {
                            !f.silent && f.verbose && f.debug && (f.performance ? d.performance.log(arguments) : (d.verbose = Function.prototype.bind.call(console.info, console, f.name + ":"), d.verbose.apply(console, arguments)))
                        },
                        error: function() {
                            f.silent || (d.error = Function.prototype.bind.call(console.error, console, f.name + ":"), d.error.apply(console, arguments))
                        },
                        performance: {
                            log: function(e) {
                                var t, n, i;
                                f.performance && (t = (new Date).getTime(), i = r || t, n = t - i, r = t, a.push({
                                    Name: e[0],
                                    Arguments: [].slice.call(e, 1) || "",
                                    Element: k,
                                    "Execution Time": n
                                })), clearTimeout(d.performance.timer), d.performance.timer = setTimeout(d.performance.display, 500)
                            },
                            display: function() {
                                var t = f.name + ":",
                                    n = 0;
                                r = !1, clearTimeout(d.performance.timer), e.each(a, function(e, t) {
                                    n += t["Execution Time"]
                                }), t += " " + n + "ms", y && (t += " '" + y + "'"), (void 0 !== console.group || void 0 !== console.table) && a.length > 0 && (console.table || e.each(a, function(e, t) {})), a = []
                            }
                        },
                        invoke: function(t, n, o) {
                            var r, a, s, l = S;
                            return n = n || c, o = k || o, "string" == typeof t && void 0 !== l && (t = t.split(/[\. ]/), r = t.length - 1, e.each(t, function(n, i) {
                                var o = n != r ? i + t[n + 1].charAt(0).toUpperCase() + t[n + 1].slice(1) : t;
                                if (e.isPlainObject(l[o]) && n != r) l = l[o];
                                else {
                                    if (void 0 !== l[o]) return a = l[o], !1;
                                    if (!e.isPlainObject(l[i]) || n == r) return void 0 !== l[i] ? (a = l[i], !1) : (d.error(g.method, t), !1);
                                    l = l[i]
                                }
                            })), e.isFunction(a) ? s = a.apply(o, n) : void 0 !== a && (s = a), e.isArray(i) ? i.push(s) : void 0 !== i ? i = [i, s] : void 0 !== s && (i = s), a
                        }
                    }, l ? (void 0 === S && d.initialize(), d.invoke(s)) : (void 0 !== S && S.invoke("destroy"), d.initialize())
                }), void 0 !== i ? i : this
            }, e.fn.accordion.settings = {
                name: "Accordion",
                namespace: "accordion",
                silent: !1,
                debug: !1,
                verbose: !1,
                performance: !0,
                on: "click",
                observeChanges: !0,
                exclusive: !0,
                collapsible: !0,
                closeNested: !1,
                animateChildren: !0,
                duration: 350,
                easing: "easeOutQuad",
                onOpening: function() {},
                onOpen: function() {},
                onClosing: function() {},
                onClose: function() {},
                onChange: function() {},
                error: {
                    method: "The method you called is not defined"
                },
                className: {
                    active: "active",
                    animating: "animating"
                },
                selector: {
                    accordion: ".accordion",
                    title: ".title",
                    trigger: ".title",
                    content: ".content"
                }
            }, e.extend(e.easing, {
                easeOutQuad: function(e, t, n, i, o) {
                    return -i * (t /= o) * (t - 2) + n
                }
            })
        }(jQuery, window, document),
        function(e, t, n, i) {
            "use strict";
            t = void 0 !== t && t.Math == Math ? t : "undefined" != typeof self && self.Math == Math ? self : Function("return this")(), e.fn.checkbox = function(i) {
                var o, r = e(this),
                    a = r.selector || "",
                    s = (new Date).getTime(),
                    l = [],
                    c = arguments[0],
                    u = "string" == typeof c,
                    d = [].slice.call(arguments, 1);
                return r.each(function() {
                    var r, f, p = e.extend(!0, {}, e.fn.checkbox.settings, i),
                        h = p.className,
                        m = p.namespace,
                        g = p.selector,
                        v = p.error,
                        b = "." + m,
                        y = "module-" + m,
                        x = e(this),
                        w = e(this).children(g.label),
                        C = e(this).children(g.input),
                        k = C[0],
                        S = !1,
                        T = !1,
                        A = x.data(y),
                        E = this;
                    f = {
                        initialize: function() {
                            f.verbose("Initializing checkbox", p), f.create.label(), f.bind.events(), f.set.tabbable(), f.hide.input(), f.observeChanges(), f.instantiate(), f.setup()
                        },
                        instantiate: function() {
                            f.verbose("Storing instance of module", f), A = f, x.data(y, f)
                        },
                        destroy: function() {
                            f.verbose("Destroying module"), f.unbind.events(), f.show.input(), x.removeData(y)
                        },
                        fix: {
                            reference: function() {
                                x.is(g.input) && (f.debug("Behavior called on <input> adjusting invoked element"), x = x.closest(g.checkbox), f.refresh())
                            }
                        },
                        setup: function() {
                            f.set.initialLoad(), f.is.indeterminate() ? (f.debug("Initial value is indeterminate"), f.indeterminate()) : f.is.checked() ? (f.debug("Initial value is checked"), f.check()) : (f.debug("Initial value is unchecked"), f.uncheck()), f.remove.initialLoad()
                        },
                        refresh: function() {
                            w = x.children(g.label), C = x.children(g.input), k = C[0]
                        },
                        hide: {
                            input: function() {
                                f.verbose("Modifying <input> z-index to be unselectable"), C.addClass(h.hidden)
                            }
                        },
                        show: {
                            input: function() {
                                f.verbose("Modifying <input> z-index to be selectable"), C.removeClass(h.hidden)
                            }
                        },
                        observeChanges: function() {
                            "MutationObserver" in t && (r = new MutationObserver(function(e) {
                                f.debug("DOM tree modified, updating selector cache"), f.refresh()
                            }), r.observe(E, {
                                childList: !0,
                                subtree: !0
                            }), f.debug("Setting up mutation observer", r))
                        },
                        attachEvents: function(t, n) {
                            var i = e(t);
                            n = e.isFunction(f[n]) ? f[n] : f.toggle, i.length > 0 ? (f.debug("Attaching checkbox events to element", t, n), i.on("click" + b, n)) : f.error(v.notFound)
                        },
                        event: {
                            click: function(t) {
                                var n = e(t.target);
                                return n.is(g.input) ? void f.verbose("Using default check action on initialized checkbox") : n.is(g.link) ? void f.debug("Clicking link inside checkbox, skipping toggle") : (f.toggle(), C.focus(), void t.preventDefault())
                            },
                            keydown: function(e) {
                                var t = e.which,
                                    n = {
                                        enter: 13,
                                        space: 32,
                                        escape: 27
                                    };
                                t == n.escape ? (f.verbose("Escape key pressed blurring field"), C.blur(), T = !0) : e.ctrlKey || t != n.space && t != n.enter ? T = !1 : (f.verbose("Enter/space key pressed, toggling checkbox"), f.toggle(), T = !0)
                            },
                            keyup: function(e) {
                                T && e.preventDefault()
                            }
                        },
                        check: function() {
                            f.should.allowCheck() && (f.debug("Checking checkbox", C), f.set.checked(), f.should.ignoreCallbacks() || (p.onChecked.call(k), p.onChange.call(k)))
                        },
                        uncheck: function() {
                            f.should.allowUncheck() && (f.debug("Unchecking checkbox"), f.set.unchecked(), f.should.ignoreCallbacks() || (p.onUnchecked.call(k), p.onChange.call(k)))
                        },
                        indeterminate: function() {
                            if (f.should.allowIndeterminate()) return void f.debug("Checkbox is already indeterminate");
                            f.debug("Making checkbox indeterminate"), f.set.indeterminate(), f.should.ignoreCallbacks() || (p.onIndeterminate.call(k), p.onChange.call(k))
                        },
                        determinate: function() {
                            if (f.should.allowDeterminate()) return void f.debug("Checkbox is already determinate");
                            f.debug("Making checkbox determinate"), f.set.determinate(), f.should.ignoreCallbacks() || (p.onDeterminate.call(k), p.onChange.call(k))
                        },
                        enable: function() {
                            if (f.is.enabled()) return void f.debug("Checkbox is already enabled");
                            f.debug("Enabling checkbox"), f.set.enabled(), p.onEnable.call(k), p.onEnabled.call(k)
                        },
                        disable: function() {
                            if (f.is.disabled()) return void f.debug("Checkbox is already disabled");
                            f.debug("Disabling checkbox"), f.set.disabled(), p.onDisable.call(k), p.onDisabled.call(k)
                        },
                        get: {
                            radios: function() {
                                var t = f.get.name();
                                return e('input[name="' + t + '"]').closest(g.checkbox)
                            },
                            otherRadios: function() {
                                return f.get.radios().not(x)
                            },
                            name: function() {
                                return C.attr("name")
                            }
                        },
                        is: {
                            initialLoad: function() {
                                return S
                            },
                            radio: function() {
                                return C.hasClass(h.radio) || "radio" == C.attr("type")
                            },
                            indeterminate: function() {
                                return void 0 !== C.prop("indeterminate") && C.prop("indeterminate")
                            },
                            checked: function() {
                                return void 0 !== C.prop("checked") && C.prop("checked")
                            },
                            disabled: function() {
                                return void 0 !== C.prop("disabled") && C.prop("disabled")
                            },
                            enabled: function() {
                                return !f.is.disabled()
                            },
                            determinate: function() {
                                return !f.is.indeterminate()
                            },
                            unchecked: function() {
                                return !f.is.checked()
                            }
                        },
                        should: {
                            allowCheck: function() {
                                return f.is.determinate() && f.is.checked() && !f.should.forceCallbacks() ? (f.debug("Should not allow check, checkbox is already checked"), !1) : !1 !== p.beforeChecked.apply(k) || (f.debug("Should not allow check, beforeChecked cancelled"), !1)
                            },
                            allowUncheck: function() {
                                return f.is.determinate() && f.is.unchecked() && !f.should.forceCallbacks() ? (f.debug("Should not allow uncheck, checkbox is already unchecked"), !1) : !1 !== p.beforeUnchecked.apply(k) || (f.debug("Should not allow uncheck, beforeUnchecked cancelled"), !1)
                            },
                            allowIndeterminate: function() {
                                return f.is.indeterminate() && !f.should.forceCallbacks() ? (f.debug("Should not allow indeterminate, checkbox is already indeterminate"), !1) : !1 !== p.beforeIndeterminate.apply(k) || (f.debug("Should not allow indeterminate, beforeIndeterminate cancelled"), !1)
                            },
                            allowDeterminate: function() {
                                return f.is.determinate() && !f.should.forceCallbacks() ? (f.debug("Should not allow determinate, checkbox is already determinate"), !1) : !1 !== p.beforeDeterminate.apply(k) || (f.debug("Should not allow determinate, beforeDeterminate cancelled"), !1)
                            },
                            forceCallbacks: function() {
                                return f.is.initialLoad() && p.fireOnInit
                            },
                            ignoreCallbacks: function() {
                                return S && !p.fireOnInit
                            }
                        },
                        can: {
                            change: function() {
                                return !(x.hasClass(h.disabled) || x.hasClass(h.readOnly) || C.prop("disabled") || C.prop("readonly"))
                            },
                            uncheck: function() {
                                return "boolean" == typeof p.uncheckable ? p.uncheckable : !f.is.radio()
                            }
                        },
                        set: {
                            initialLoad: function() {
                                S = !0
                            },
                            checked: function() {
                                if (f.verbose("Setting class to checked"), x.removeClass(h.indeterminate).addClass(h.checked), f.is.radio() && f.uncheckOthers(), !f.is.indeterminate() && f.is.checked()) return void f.debug("Input is already checked, skipping input property change");
                                f.verbose("Setting state to checked", k), C.prop("indeterminate", !1).prop("checked", !0), f.trigger.change()
                            },
                            unchecked: function() {
                                if (f.verbose("Removing checked class"), x.removeClass(h.indeterminate).removeClass(h.checked), !f.is.indeterminate() && f.is.unchecked()) return void f.debug("Input is already unchecked");
                                f.debug("Setting state to unchecked"), C.prop("indeterminate", !1).prop("checked", !1), f.trigger.change()
                            },
                            indeterminate: function() {
                                if (f.verbose("Setting class to indeterminate"), x.addClass(h.indeterminate), f.is.indeterminate()) return void f.debug("Input is already indeterminate, skipping input property change");
                                f.debug("Setting state to indeterminate"), C.prop("indeterminate", !0), f.trigger.change()
                            },
                            determinate: function() {
                                if (f.verbose("Removing indeterminate class"), x.removeClass(h.indeterminate), f.is.determinate()) return void f.debug("Input is already determinate, skipping input property change");
                                f.debug("Setting state to determinate"), C.prop("indeterminate", !1)
                            },
                            disabled: function() {
                                if (f.verbose("Setting class to disabled"), x.addClass(h.disabled), f.is.disabled()) return void f.debug("Input is already disabled, skipping input property change");
                                f.debug("Setting state to disabled"), C.prop("disabled", "disabled"), f.trigger.change()
                            },
                            enabled: function() {
                                if (f.verbose("Removing disabled class"), x.removeClass(h.disabled), f.is.enabled()) return void f.debug("Input is already enabled, skipping input property change");
                                f.debug("Setting state to enabled"), C.prop("disabled", !1), f.trigger.change()
                            },
                            tabbable: function() {
                                f.verbose("Adding tabindex to checkbox"), void 0 === C.attr("tabindex") && C.attr("tabindex", 0)
                            }
                        },
                        remove: {
                            initialLoad: function() {
                                S = !1
                            }
                        },
                        trigger: {
                            change: function() {
                                var e = n.createEvent("HTMLEvents"),
                                    t = C[0];
                                t && (f.verbose("Triggering native change event"), e.initEvent("change", !0, !1), t.dispatchEvent(e))
                            }
                        },
                        create: {
                            label: function() {
                                C.prevAll(g.label).length > 0 ? (C.prev(g.label).detach().insertAfter(C), f.debug("Moving existing label", w)) : f.has.label() || (w = e("<label>").insertAfter(C), f.debug("Creating label", w))
                            }
                        },
                        has: {
                            label: function() {
                                return w.length > 0
                            }
                        },
                        bind: {
                            events: function() {
                                f.verbose("Attaching checkbox events"), x.on("click" + b, f.event.click).on("keydown" + b, g.input, f.event.keydown).on("keyup" + b, g.input, f.event.keyup)
                            }
                        },
                        unbind: {
                            events: function() {
                                f.debug("Removing events"), x.off(b)
                            }
                        },
                        uncheckOthers: function() {
                            var e = f.get.otherRadios();
                            f.debug("Unchecking other radios", e), e.removeClass(h.checked)
                        },
                        toggle: function() {
                            if (!f.can.change()) return void(f.is.radio() || f.debug("Checkbox is read-only or disabled, ignoring toggle"));
                            f.is.indeterminate() || f.is.unchecked() ? (f.debug("Currently unchecked"), f.check()) : f.is.checked() && f.can.uncheck() && (f.debug("Currently checked"), f.uncheck())
                        },
                        setting: function(t, n) {
                            if (f.debug("Changing setting", t, n), e.isPlainObject(t)) e.extend(!0, p, t);
                            else {
                                if (void 0 === n) return p[t];
                                e.isPlainObject(p[t]) ? e.extend(!0, p[t], n) : p[t] = n
                            }
                        },
                        internal: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, f, t);
                            else {
                                if (void 0 === n) return f[t];
                                f[t] = n
                            }
                        },
                        debug: function() {
                            !p.silent && p.debug && (p.performance ? f.performance.log(arguments) : (f.debug = Function.prototype.bind.call(console.info, console, p.name + ":"), f.debug.apply(console, arguments)))
                        },
                        verbose: function() {
                            !p.silent && p.verbose && p.debug && (p.performance ? f.performance.log(arguments) : (f.verbose = Function.prototype.bind.call(console.info, console, p.name + ":"), f.verbose.apply(console, arguments)))
                        },
                        error: function() {
                            p.silent || (f.error = Function.prototype.bind.call(console.error, console, p.name + ":"), f.error.apply(console, arguments))
                        },
                        performance: {
                            log: function(e) {
                                var t, n, i;
                                p.performance && (t = (new Date).getTime(), i = s || t, n = t - i, s = t, l.push({
                                    Name: e[0],
                                    Arguments: [].slice.call(e, 1) || "",
                                    Element: E,
                                    "Execution Time": n
                                })), clearTimeout(f.performance.timer), f.performance.timer = setTimeout(f.performance.display, 500)
                            },
                            display: function() {
                                var t = p.name + ":",
                                    n = 0;
                                s = !1, clearTimeout(f.performance.timer), e.each(l, function(e, t) {
                                    n += t["Execution Time"]
                                }), t += " " + n + "ms", a && (t += " '" + a + "'"), (void 0 !== console.group || void 0 !== console.table) && l.length > 0 && (console.table || e.each(l, function(e, t) {})), l = []
                            }
                        },
                        invoke: function(t, n, i) {
                            var r, a, s, l = A;
                            return n = n || d, i = E || i, "string" == typeof t && void 0 !== l && (t = t.split(/[\. ]/), r = t.length - 1, e.each(t, function(n, i) {
                                var o = n != r ? i + t[n + 1].charAt(0).toUpperCase() + t[n + 1].slice(1) : t;
                                if (e.isPlainObject(l[o]) && n != r) l = l[o];
                                else {
                                    if (void 0 !== l[o]) return a = l[o], !1;
                                    if (!e.isPlainObject(l[i]) || n == r) return void 0 !== l[i] ? (a = l[i], !1) : (f.error(v.method, t), !1);
                                    l = l[i]
                                }
                            })), e.isFunction(a) ? s = a.apply(i, n) : void 0 !== a && (s = a), e.isArray(o) ? o.push(s) : void 0 !== o ? o = [o, s] : void 0 !== s && (o = s), a
                        }
                    }, u ? (void 0 === A && f.initialize(), f.invoke(c)) : (void 0 !== A && A.invoke("destroy"), f.initialize())
                }), void 0 !== o ? o : this
            }, e.fn.checkbox.settings = {
                name: "Checkbox",
                namespace: "checkbox",
                silent: !1,
                debug: !1,
                verbose: !0,
                performance: !0,
                uncheckable: "auto",
                fireOnInit: !1,
                onChange: function() {},
                beforeChecked: function() {},
                beforeUnchecked: function() {},
                beforeDeterminate: function() {},
                beforeIndeterminate: function() {},
                onChecked: function() {},
                onUnchecked: function() {},
                onDeterminate: function() {},
                onIndeterminate: function() {},
                onEnable: function() {},
                onDisable: function() {},
                onEnabled: function() {},
                onDisabled: function() {},
                className: {
                    checked: "checked",
                    indeterminate: "indeterminate",
                    disabled: "disabled",
                    hidden: "hidden",
                    radio: "radio",
                    readOnly: "read-only"
                },
                error: {
                    method: "The method you called is not defined"
                },
                selector: {
                    checkbox: ".ui.checkbox",
                    label: "label, .box",
                    input: 'input[type="checkbox"], input[type="radio"]',
                    link: "a[href]"
                }
            }
        }(jQuery, window, document),
        function(e, t, i, o) {
            "use strict";
            t = void 0 !== t && t.Math == Math ? t : "undefined" != typeof self && self.Math == Math ? self : Function("return this")(), e.fn.dimmer = function(t) {
                var o, r = e(this),
                    a = (new Date).getTime(),
                    s = [],
                    l = arguments[0],
                    c = "string" == typeof l,
                    u = [].slice.call(arguments, 1);
                return r.each(function() {
                    var d, f, p, h = e.isPlainObject(t) ? e.extend(!0, {}, e.fn.dimmer.settings, t) : e.extend({}, e.fn.dimmer.settings),
                        m = h.selector,
                        g = h.namespace,
                        v = h.className,
                        b = h.error,
                        y = "." + g,
                        x = "module-" + g,
                        w = r.selector || "",
                        C = "ontouchstart" in i.documentElement ? "touchstart" : "click",
                        k = e(this),
                        S = this,
                        T = k.data(x);
                    p = {
                        preinitialize: function() {
                            p.is.dimmer() ? (f = k.parent(), d = k) : (f = k, d = p.has.dimmer() ? h.dimmerName ? f.find(m.dimmer).filter("." + h.dimmerName) : f.find(m.dimmer) : p.create(), p.set.variation())
                        },
                        initialize: function() {
                            p.debug("Initializing dimmer", h), p.bind.events(), p.set.dimmable(), p.instantiate()
                        },
                        instantiate: function() {
                            p.verbose("Storing instance of module", p), T = p, k.data(x, T)
                        },
                        destroy: function() {
                            p.verbose("Destroying previous module", d), p.unbind.events(), p.remove.variation(), f.off(y)
                        },
                        bind: {
                            events: function() {
                                "hover" == h.on ? f.on("mouseenter" + y, p.show).on("mouseleave" + y, p.hide) : "click" == h.on && f.on(C + y, p.toggle), p.is.page() && (p.debug("Setting as a page dimmer", f), p.set.pageDimmer()), p.is.closable() && (p.verbose("Adding dimmer close event", d), f.on(C + y, m.dimmer, p.event.click))
                            }
                        },
                        unbind: {
                            events: function() {
                                k.removeData(x), f.off(y)
                            }
                        },
                        event: {
                            click: function(t) {
                                p.verbose("Determining if event occured on dimmer", t), (0 === d.find(t.target).length || e(t.target).is(m.content)) && (p.hide(), t.stopImmediatePropagation())
                            }
                        },
                        addContent: function(t) {
                            var n = e(t);
                            p.debug("Add content to dimmer", n), n.parent()[0] !== d[0] && n.detach().appendTo(d)
                        },
                        create: function() {
                            var t = e(h.template.dimmer());
                            return h.dimmerName && (p.debug("Creating named dimmer", h.dimmerName), t.addClass(h.dimmerName)), t.appendTo(f), t
                        },
                        show: function(t) {
                            t = e.isFunction(t) ? t : function() {}, p.debug("Showing dimmer", d, h), p.is.dimmed() && !p.is.animating() || !p.is.enabled() ? p.debug("Dimmer is already shown or disabled") : (p.animate.show(t), h.onShow.call(S), h.onChange.call(S))
                        },
                        hide: function(t) {
                            t = e.isFunction(t) ? t : function() {}, p.is.dimmed() || p.is.animating() ? (p.debug("Hiding dimmer", d), p.animate.hide(t), h.onHide.call(S), h.onChange.call(S)) : p.debug("Dimmer is not visible")
                        },
                        toggle: function() {
                            p.verbose("Toggling dimmer visibility", d), p.is.dimmed() ? p.hide() : p.show()
                        },
                        animate: {
                            show: function(t) {
                                t = e.isFunction(t) ? t : function() {}, h.useCSS && void 0 !== e.fn.transition && d.transition("is supported") ? ("auto" !== h.opacity && p.set.opacity(), d.transition({
                                    animation: h.transition + " in",
                                    queue: !1,
                                    duration: p.get.duration(),
                                    useFailSafe: !0,
                                    onStart: function() {
                                        p.set.dimmed()
                                    },
                                    onComplete: function() {
                                        p.set.active(), t()
                                    }
                                })) : (p.verbose("Showing dimmer animation with javascript"), p.set.dimmed(), "auto" == h.opacity && (h.opacity = .8), d.stop().css({
                                    opacity: 0,
                                    width: "100%",
                                    height: "100%"
                                }).fadeTo(p.get.duration(), h.opacity, function() {
                                    d.removeAttr("style"), p.set.active(), t()
                                }))
                            },
                            hide: function(t) {
                                t = e.isFunction(t) ? t : function() {}, h.useCSS && void 0 !== e.fn.transition && d.transition("is supported") ? (p.verbose("Hiding dimmer with css"), d.transition({
                                    animation: h.transition + " out",
                                    queue: !1,
                                    duration: p.get.duration(),
                                    useFailSafe: !0,
                                    onStart: function() {
                                        p.remove.dimmed()
                                    },
                                    onComplete: function() {
                                        p.remove.active(), t()
                                    }
                                })) : (p.verbose("Hiding dimmer with javascript"), p.remove.dimmed(), d.stop().fadeOut(p.get.duration(), function() {
                                    p.remove.active(), d.removeAttr("style"), t()
                                }))
                            }
                        },
                        get: {
                            dimmer: function() {
                                return d
                            },
                            duration: function() {
                                return "object" == n(h.duration) ? p.is.active() ? h.duration.hide : h.duration.show : h.duration
                            }
                        },
                        has: {
                            dimmer: function() {
                                return h.dimmerName ? k.find(m.dimmer).filter("." + h.dimmerName).length > 0 : k.find(m.dimmer).length > 0
                            }
                        },
                        is: {
                            active: function() {
                                return d.hasClass(v.active)
                            },
                            animating: function() {
                                return d.is(":animated") || d.hasClass(v.animating)
                            },
                            closable: function() {
                                return "auto" == h.closable ? "hover" != h.on : h.closable
                            },
                            dimmer: function() {
                                return k.hasClass(v.dimmer)
                            },
                            dimmable: function() {
                                return k.hasClass(v.dimmable)
                            },
                            dimmed: function() {
                                return f.hasClass(v.dimmed)
                            },
                            disabled: function() {
                                return f.hasClass(v.disabled)
                            },
                            enabled: function() {
                                return !p.is.disabled()
                            },
                            page: function() {
                                return f.is("body")
                            },
                            pageDimmer: function() {
                                return d.hasClass(v.pageDimmer)
                            }
                        },
                        can: {
                            show: function() {
                                return !d.hasClass(v.disabled)
                            }
                        },
                        set: {
                            opacity: function(e) {
                                var t = d.css("background-color"),
                                    n = t.split(","),
                                    i = n && 3 == n.length,
                                    o = n && 4 == n.length;
                                e = 0 === h.opacity ? 0 : h.opacity || e, i || o ? (n[3] = e + ")", t = n.join(",")) : t = "rgba(0, 0, 0, " + e + ")", p.debug("Setting opacity to", e), d.css("background-color", t)
                            },
                            active: function() {
                                d.addClass(v.active)
                            },
                            dimmable: function() {
                                f.addClass(v.dimmable)
                            },
                            dimmed: function() {
                                f.addClass(v.dimmed)
                            },
                            pageDimmer: function() {
                                d.addClass(v.pageDimmer)
                            },
                            disabled: function() {
                                d.addClass(v.disabled)
                            },
                            variation: function(e) {
                                (e = e || h.variation) && d.addClass(e)
                            }
                        },
                        remove: {
                            active: function() {
                                d.removeClass(v.active)
                            },
                            dimmed: function() {
                                f.removeClass(v.dimmed)
                            },
                            disabled: function() {
                                d.removeClass(v.disabled)
                            },
                            variation: function(e) {
                                (e = e || h.variation) && d.removeClass(e)
                            }
                        },
                        setting: function(t, n) {
                            if (p.debug("Changing setting", t, n), e.isPlainObject(t)) e.extend(!0, h, t);
                            else {
                                if (void 0 === n) return h[t];
                                e.isPlainObject(h[t]) ? e.extend(!0, h[t], n) : h[t] = n
                            }
                        },
                        internal: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, p, t);
                            else {
                                if (void 0 === n) return p[t];
                                p[t] = n
                            }
                        },
                        debug: function() {
                            !h.silent && h.debug && (h.performance ? p.performance.log(arguments) : (p.debug = Function.prototype.bind.call(console.info, console, h.name + ":"), p.debug.apply(console, arguments)))
                        },
                        verbose: function() {
                            !h.silent && h.verbose && h.debug && (h.performance ? p.performance.log(arguments) : (p.verbose = Function.prototype.bind.call(console.info, console, h.name + ":"), p.verbose.apply(console, arguments)))
                        },
                        error: function() {
                            h.silent || (p.error = Function.prototype.bind.call(console.error, console, h.name + ":"), p.error.apply(console, arguments))
                        },
                        performance: {
                            log: function(e) {
                                var t, n, i;
                                h.performance && (t = (new Date).getTime(), i = a || t, n = t - i, a = t, s.push({
                                    Name: e[0],
                                    Arguments: [].slice.call(e, 1) || "",
                                    Element: S,
                                    "Execution Time": n
                                })), clearTimeout(p.performance.timer), p.performance.timer = setTimeout(p.performance.display, 500)
                            },
                            display: function() {
                                var t = h.name + ":",
                                    n = 0;
                                a = !1, clearTimeout(p.performance.timer), e.each(s, function(e, t) {
                                    n += t["Execution Time"]
                                }), t += " " + n + "ms", w && (t += " '" + w + "'"), r.length > 1 && (t += " (" + r.length + ")"), (void 0 !== console.group || void 0 !== console.table) && s.length > 0 && (console.table || e.each(s, function(e, t) {})), s = []
                            }
                        },
                        invoke: function(t, n, i) {
                            var r, a, s, l = T;
                            return n = n || u, i = S || i, "string" == typeof t && void 0 !== l && (t = t.split(/[\. ]/), r = t.length - 1, e.each(t, function(n, i) {
                                var o = n != r ? i + t[n + 1].charAt(0).toUpperCase() + t[n + 1].slice(1) : t;
                                if (e.isPlainObject(l[o]) && n != r) l = l[o];
                                else {
                                    if (void 0 !== l[o]) return a = l[o], !1;
                                    if (!e.isPlainObject(l[i]) || n == r) return void 0 !== l[i] ? (a = l[i], !1) : (p.error(b.method, t), !1);
                                    l = l[i]
                                }
                            })), e.isFunction(a) ? s = a.apply(i, n) : void 0 !== a && (s = a), e.isArray(o) ? o.push(s) : void 0 !== o ? o = [o, s] : void 0 !== s && (o = s), a
                        }
                    }, p.preinitialize(), c ? (void 0 === T && p.initialize(), p.invoke(l)) : (void 0 !== T && T.invoke("destroy"), p.initialize())
                }), void 0 !== o ? o : this
            }, e.fn.dimmer.settings = {
                name: "Dimmer",
                namespace: "dimmer",
                silent: !1,
                debug: !1,
                verbose: !1,
                performance: !0,
                dimmerName: !1,
                variation: !1,
                closable: "auto",
                useCSS: !0,
                transition: "fade",
                on: !1,
                opacity: "auto",
                duration: {
                    show: 500,
                    hide: 500
                },
                onChange: function() {},
                onShow: function() {},
                onHide: function() {},
                error: {
                    method: "The method you called is not defined."
                },
                className: {
                    active: "active",
                    animating: "animating",
                    dimmable: "dimmable",
                    dimmed: "dimmed",
                    dimmer: "dimmer",
                    disabled: "disabled",
                    hide: "hide",
                    pageDimmer: "page",
                    show: "show"
                },
                selector: {
                    dimmer: "> .ui.dimmer",
                    content: ".ui.dimmer > .content, .ui.dimmer > .content > .center"
                },
                template: {
                    dimmer: function() {
                        return e("<div />").attr("class", "ui dimmer")
                    }
                }
            }
        }(jQuery, window, document),
        function(e, t, n, i) {
            "use strict";
            t = void 0 !== t && t.Math == Math ? t : "undefined" != typeof self && self.Math == Math ? self : Function("return this")(), e.fn.dropdown = function(i) {
                var o, r = e(this),
                    a = e(n),
                    s = r.selector || "",
                    l = "ontouchstart" in n.documentElement,
                    c = (new Date).getTime(),
                    u = [],
                    d = arguments[0],
                    f = "string" == typeof d,
                    p = [].slice.call(arguments, 1);
                return r.each(function(h) {
                    var m, g, v, b, y, x, w, C, k = e.isPlainObject(i) ? e.extend(!0, {}, e.fn.dropdown.settings, i) : e.extend({}, e.fn.dropdown.settings),
                        S = k.className,
                        T = k.message,
                        A = k.fields,
                        E = k.keys,
                        D = k.metadata,
                        O = k.namespace,
                        F = k.regExp,
                        j = k.selector,
                        q = k.error,
                        L = k.templates,
                        N = "." + O,
                        P = "module-" + O,
                        R = e(this),
                        I = e(k.context),
                        M = R.find(j.text),
                        H = R.find(j.search),
                        z = R.find(j.sizer),
                        $ = R.find(j.input),
                        V = R.find(j.icon),
                        B = R.prev().find(j.text).length > 0 ? R.prev().find(j.text) : R.prev(),
                        W = R.children(j.menu),
                        U = W.find(j.item),
                        _ = !1,
                        X = !1,
                        Q = !1,
                        Y = this,
                        G = R.data(P);
                    C = {
                        initialize: function() {
                            C.debug("Initializing dropdown", k), C.is.alreadySetup() ? C.setup.reference() : (C.setup.layout(), C.refreshData(), C.save.defaults(), C.restore.selected(), C.create.id(), C.bind.events(), C.observeChanges(), C.instantiate())
                        },
                        instantiate: function() {
                            C.verbose("Storing instance of dropdown", C), G = C, R.data(P, C)
                        },
                        destroy: function() {
                            C.verbose("Destroying previous dropdown", R), C.remove.tabbable(), R.off(N).removeData(P), W.off(N), a.off(b), C.disconnect.menuObserver(), C.disconnect.selectObserver()
                        },
                        observeChanges: function() {
                            "MutationObserver" in t && (x = new MutationObserver(C.event.select.mutation), w = new MutationObserver(C.event.menu.mutation), C.debug("Setting up mutation observer", x, w), C.observe.select(), C.observe.menu())
                        },
                        disconnect: {
                            menuObserver: function() {
                                w && w.disconnect()
                            },
                            selectObserver: function() {
                                x && x.disconnect()
                            }
                        },
                        observe: {
                            select: function() {
                                C.has.input() && x.observe($[0], {
                                    childList: !0,
                                    subtree: !0
                                })
                            },
                            menu: function() {
                                C.has.menu() && w.observe(W[0], {
                                    childList: !0,
                                    subtree: !0
                                })
                            }
                        },
                        create: {
                            id: function() {
                                y = (Math.random().toString(16) + "000000000").substr(2, 8), b = "." + y, C.verbose("Creating unique id for element", y)
                            },
                            userChoice: function(t) {
                                var n, i, o;
                                return !!(t = t || C.get.userValues()) && (t = e.isArray(t) ? t : [t], e.each(t, function(t, r) {
                                    !1 === C.get.item(r) && (o = k.templates.addition(C.add.variables(T.addResult, r)), i = e("<div />").html(o).attr("data-" + D.value, r).attr("data-" + D.text, r).addClass(S.addition).addClass(S.item), k.hideAdditions && i.addClass(S.hidden), n = void 0 === n ? i : n.add(i), C.verbose("Creating user choices for value", r, i))
                                }), n)
                            },
                            userLabels: function(t) {
                                var n = C.get.userValues();
                                n && (C.debug("Adding user labels", n), e.each(n, function(e, t) {
                                    C.verbose("Adding custom user value"), C.add.label(t, t)
                                }))
                            },
                            menu: function() {
                                W = e("<div />").addClass(S.menu).appendTo(R)
                            },
                            sizer: function() {
                                z = e("<span />").addClass(S.sizer).insertAfter(H)
                            }
                        },
                        search: function(e) {
                            e = void 0 !== e ? e : C.get.query(), C.verbose("Searching for query", e), C.has.minCharacters(e) ? C.filter(e) : C.hide()
                        },
                        select: {
                            firstUnfiltered: function() {
                                C.verbose("Selecting first non-filtered element"), C.remove.selectedItem(), U.not(j.unselectable).not(j.addition + j.hidden).eq(0).addClass(S.selected)
                            },
                            nextAvailable: function(e) {
                                e = e.eq(0);
                                var t = e.nextAll(j.item).not(j.unselectable).eq(0),
                                    n = e.prevAll(j.item).not(j.unselectable).eq(0);
                                t.length > 0 ? (C.verbose("Moving selection to", t), t.addClass(S.selected)) : (C.verbose("Moving selection to", n), n.addClass(S.selected))
                            }
                        },
                        setup: {
                            api: function() {
                                var e = {
                                    debug: k.debug,
                                    urlData: {
                                        value: C.get.value(),
                                        query: C.get.query()
                                    },
                                    on: !1
                                };
                                C.verbose("First request, initializing API"), R.api(e)
                            },
                            layout: function() {
                                R.is("select") && (C.setup.select(), C.setup.returnedObject()), C.has.menu() || C.create.menu(), C.is.search() && !C.has.search() && (C.verbose("Adding search input"), H = e("<input />").addClass(S.search).prop("autocomplete", "off").insertBefore(M)), C.is.multiple() && C.is.searchSelection() && !C.has.sizer() && C.create.sizer(), k.allowTab && C.set.tabbable()
                            },
                            select: function() {
                                var t = C.get.selectValues();
                                C.debug("Dropdown initialized on a select", t), R.is("select") && ($ = R), $.parent(j.dropdown).length > 0 ? (C.debug("UI dropdown already exists. Creating dropdown menu only"), R = $.closest(j.dropdown), C.has.menu() || C.create.menu(), W = R.children(j.menu), C.setup.menu(t)) : (C.debug("Creating entire dropdown from select"), R = e("<div />").attr("class", $.attr("class")).addClass(S.selection).addClass(S.dropdown).html(L.dropdown(t)).insertBefore($), $.hasClass(S.multiple) && !1 === $.prop("multiple") && (C.error(q.missingMultiple), $.prop("multiple", !0)), $.is("[multiple]") && C.set.multiple(), $.prop("disabled") && (C.debug("Disabling dropdown"), R.addClass(S.disabled)), $.removeAttr("class").detach().prependTo(R)), C.refresh()
                            },
                            menu: function(e) {
                                W.html(L.menu(e, A)), U = W.find(j.item)
                            },
                            reference: function() {
                                C.debug("Dropdown behavior was called on select, replacing with closest dropdown"), R = R.parent(j.dropdown), C.refresh(), C.setup.returnedObject(), f && (G = C, C.invoke(d))
                            },
                            returnedObject: function() {
                                var e = r.slice(0, h),
                                    t = r.slice(h + 1);
                                r = e.add(R).add(t)
                            }
                        },
                        refresh: function() {
                            C.refreshSelectors(), C.refreshData()
                        },
                        refreshItems: function() {
                            U = W.find(j.item)
                        },
                        refreshSelectors: function() {
                            C.verbose("Refreshing selector cache"), M = R.find(j.text), H = R.find(j.search), $ = R.find(j.input), V = R.find(j.icon), B = R.prev().find(j.text).length > 0 ? R.prev().find(j.text) : R.prev(), W = R.children(j.menu), U = W.find(j.item)
                        },
                        refreshData: function() {
                            C.verbose("Refreshing cached metadata"), U.removeData(D.text).removeData(D.value)
                        },
                        clearData: function() {
                            C.verbose("Clearing metadata"), U.removeData(D.text).removeData(D.value), R.removeData(D.defaultText).removeData(D.defaultValue).removeData(D.placeholderText)
                        },
                        toggle: function() {
                            C.verbose("Toggling menu visibility"), C.is.active() ? C.hide() : C.show()
                        },
                        show: function(t) {
                            if (t = e.isFunction(t) ? t : function() {}, !C.can.show() && C.is.remote() && (C.debug("No API results retrieved, searching before show"), C.queryRemote(C.get.query(), C.show)), C.can.show() && !C.is.active()) {
                                if (C.debug("Showing dropdown"), !C.has.message() || C.has.maxSelections() || C.has.allResultsFiltered() || C.remove.message(), C.is.allFiltered()) return !0;
                                !1 !== k.onShow.call(Y) && C.animate.show(function() {
                                    C.can.click() && C.bind.intent(), C.has.menuSearch() && C.focusSearch(), C.set.visible(), t.call(Y)
                                })
                            }
                        },
                        hide: function(t) {
                            t = e.isFunction(t) ? t : function() {}, C.is.active() && (C.debug("Hiding dropdown"), !1 !== k.onHide.call(Y) && C.animate.hide(function() {
                                C.remove.visible(), t.call(Y)
                            }))
                        },
                        hideOthers: function() {
                            C.verbose("Finding other dropdowns to hide"), r.not(R).has(j.menu + "." + S.visible).dropdown("hide")
                        },
                        hideMenu: function() {
                            C.verbose("Hiding menu  instantaneously"), C.remove.active(), C.remove.visible(), W.transition("hide")
                        },
                        hideSubMenus: function() {
                            var e = W.children(j.item).find(j.menu);
                            C.verbose("Hiding sub menus", e), e.transition("hide")
                        },
                        bind: {
                            events: function() {
                                l && C.bind.touchEvents(), C.bind.keyboardEvents(), C.bind.inputEvents(), C.bind.mouseEvents()
                            },
                            touchEvents: function() {
                                C.debug("Touch device detected binding additional touch events"), C.is.searchSelection() || C.is.single() && R.on("touchstart" + N, C.event.test.toggle), W.on("touchstart" + N, j.item, C.event.item.mouseenter)
                            },
                            keyboardEvents: function() {
                                C.verbose("Binding keyboard events"), R.on("keydown" + N, C.event.keydown), C.has.search() && R.on(C.get.inputEvent() + N, j.search, C.event.input), C.is.multiple() && a.on("keydown" + b, C.event.document.keydown)
                            },
                            inputEvents: function() {
                                C.verbose("Binding input change events"), R.on("change" + N, j.input, C.event.change)
                            },
                            mouseEvents: function() {
                                C.verbose("Binding mouse events"), C.is.multiple() && R.on("click" + N, j.label, C.event.label.click).on("click" + N, j.remove, C.event.remove.click), C.is.searchSelection() ? (R.on("mousedown" + N, C.event.mousedown).on("mouseup" + N, C.event.mouseup).on("mousedown" + N, j.menu, C.event.menu.mousedown).on("mouseup" + N, j.menu, C.event.menu.mouseup).on("click" + N, j.icon, C.event.icon.click).on("focus" + N, j.search, C.event.search.focus).on("click" + N, j.search, C.event.search.focus).on("blur" + N, j.search, C.event.search.blur).on("click" + N, j.text, C.event.text.focus), C.is.multiple() && R.on("click" + N, C.event.click)) : ("click" == k.on ? R.on("click" + N, j.icon, C.event.icon.click).on("click" + N, C.event.test.toggle) : "hover" == k.on ? R.on("mouseenter" + N, C.delay.show).on("mouseleave" + N, C.delay.hide) : R.on(k.on + N, C.toggle), R.on("mousedown" + N, C.event.mousedown).on("mouseup" + N, C.event.mouseup).on("focus" + N, C.event.focus), C.has.menuSearch() ? R.on("blur" + N, j.search, C.event.search.blur) : R.on("blur" + N, C.event.blur)), W.on("mouseenter" + N, j.item, C.event.item.mouseenter).on("mouseleave" + N, j.item, C.event.item.mouseleave).on("click" + N, j.item, C.event.item.click)
                            },
                            intent: function() {
                                C.verbose("Binding hide intent event to document"), l && a.on("touchstart" + b, C.event.test.touch).on("touchmove" + b, C.event.test.touch), a.on("click" + b, C.event.test.hide)
                            }
                        },
                        unbind: {
                            intent: function() {
                                C.verbose("Removing hide intent event from document"), l && a.off("touchstart" + b).off("touchmove" + b), a.off("click" + b)
                            }
                        },
                        filter: function(e) {
                            var t = void 0 !== e ? e : C.get.query(),
                                n = function() {
                                    C.is.multiple() && C.filterActive(), C.select.firstUnfiltered(), C.has.allResultsFiltered() ? k.onNoResults.call(Y, t) ? k.allowAdditions ? k.hideAdditions && (C.verbose("User addition with no menu, setting empty style"), C.set.empty(), C.hideMenu()) : (C.verbose("All items filtered, showing message", t), C.add.message(T.noResults)) : (C.verbose("All items filtered, hiding dropdown", t), C.hideMenu()) : (C.remove.empty(), C.remove.message()), k.allowAdditions && C.add.userSuggestion(e), C.is.searchSelection() && C.can.show() && C.is.focusedOnSearch() && C.show()
                                };
                            k.useLabels && C.has.maxSelections() || (k.apiSettings ? C.can.useAPI() ? C.queryRemote(t, function() {
                                k.filterRemoteData && C.filterItems(t), n()
                            }) : C.error(q.noAPI) : (C.filterItems(t), n()))
                        },
                        queryRemote: function(t, n) {
                            var i = {
                                errorDuration: !1,
                                cache: "local",
                                throttle: k.throttle,
                                urlData: {
                                    query: t
                                },
                                onError: function() {
                                    C.add.message(T.serverError), n()
                                },
                                onFailure: function() {
                                    C.add.message(T.serverError), n()
                                },
                                onSuccess: function(e) {
                                    C.remove.message(), C.setup.menu({
                                        values: e[A.remoteValues]
                                    }), n()
                                }
                            };
                            R.api("get request") || C.setup.api(), i = e.extend(!0, {}, i, k.apiSettings), R.api("setting", i).api("query")
                        },
                        filterItems: function(t) {
                            var n = void 0 !== t ? t : C.get.query(),
                                i = null,
                                o = C.escape.string(n),
                                r = new RegExp("^" + o, "igm");
                            C.has.query() && (i = [], C.verbose("Searching for matching values", n), U.each(function() {
                                var t, o, a = e(this);
                                if ("both" == k.match || "text" == k.match) {
                                    if (t = String(C.get.choiceText(a, !1)), -1 !== t.search(r)) return i.push(this), !0;
                                    if ("exact" === k.fullTextSearch && C.exactSearch(n, t)) return i.push(this), !0;
                                    if (!0 === k.fullTextSearch && C.fuzzySearch(n, t)) return i.push(this), !0
                                }
                                if ("both" == k.match || "value" == k.match) {
                                    if (o = String(C.get.choiceValue(a, t)), -1 !== o.search(r)) return i.push(this), !0;
                                    if ("exact" === k.fullTextSearch && C.exactSearch(n, o)) return i.push(this), !0;
                                    if (!0 === k.fullTextSearch && C.fuzzySearch(n, o)) return i.push(this), !0
                                }
                            })), C.debug("Showing only matched items", n), C.remove.filteredItem(), i && U.not(i).addClass(S.filtered)
                        },
                        fuzzySearch: function(e, t) {
                            var n = t.length,
                                i = e.length;
                            if (e = e.toLowerCase(), t = t.toLowerCase(), i > n) return !1;
                            if (i === n) return e === t;
                            e: for (var o = 0, r = 0; o < i; o++) {
                                for (var a = e.charCodeAt(o); r < n;)
                                    if (t.charCodeAt(r++) === a) continue e;
                                return !1
                            }
                            return !0
                        },
                        exactSearch: function(e, t) {
                            return e = e.toLowerCase(), t = t.toLowerCase(), t.indexOf(e) > -1
                        },
                        filterActive: function() {
                            k.useLabels && U.filter("." + S.active).addClass(S.filtered)
                        },
                        focusSearch: function(e) {
                            C.has.search() && !C.is.focusedOnSearch() && (e ? (R.off("focus" + N, j.search), H.focus(), R.on("focus" + N, j.search, C.event.search.focus)) : H.focus())
                        },
                        forceSelection: function() {
                            var e = U.not(S.filtered).filter("." + S.selected).eq(0),
                                t = U.not(S.filtered).filter("." + S.active).eq(0),
                                n = e.length > 0 ? e : t;
                            if (n.length > 0 && !C.is.multiple()) return C.debug("Forcing partial selection to selected item", n), void C.event.item.click.call(n, {}, !0);
                            k.allowAdditions ? (C.set.selected(C.get.query()), C.remove.searchTerm()) : C.remove.searchTerm()
                        },
                        event: {
                            change: function() {
                                Q || (C.debug("Input changed, updating selection"), C.set.selected())
                            },
                            focus: function() {
                                k.showOnFocus && !_ && C.is.hidden() && !g && C.show()
                            },
                            blur: function(e) {
                                g = n.activeElement === this, _ || g || (C.remove.activeLabel(), C.hide())
                            },
                            mousedown: function() {
                                C.is.searchSelection() ? v = !0 : _ = !0
                            },
                            mouseup: function() {
                                C.is.searchSelection() ? v = !1 : _ = !1
                            },
                            click: function(t) {
                                e(t.target).is(R) && (C.is.focusedOnSearch() ? C.show() : C.focusSearch())
                            },
                            search: {
                                focus: function() {
                                    _ = !0, C.is.multiple() && C.remove.activeLabel(), k.showOnFocus && C.search()
                                },
                                blur: function(e) {
                                    g = n.activeElement === this, C.is.searchSelection() && !v && (X || g || (k.forceSelection && C.forceSelection(), C.hide())), v = !1
                                }
                            },
                            icon: {
                                click: function(e) {
                                    C.toggle()
                                }
                            },
                            text: {
                                focus: function(e) {
                                    _ = !0, C.focusSearch()
                                }
                            },
                            input: function(e) {
                                (C.is.multiple() || C.is.searchSelection()) && C.set.filtered(), clearTimeout(C.timer), C.timer = setTimeout(C.search, k.delay.search)
                            },
                            label: {
                                click: function(t) {
                                    var n = e(this),
                                        i = R.find(j.label),
                                        o = i.filter("." + S.active),
                                        r = n.nextAll("." + S.active),
                                        a = n.prevAll("." + S.active),
                                        s = r.length > 0 ? n.nextUntil(r).add(o).add(n) : n.prevUntil(a).add(o).add(n);
                                    t.shiftKey ? (o.removeClass(S.active), s.addClass(S.active)) : t.ctrlKey ? n.toggleClass(S.active) : (o.removeClass(S.active), n.addClass(S.active)), k.onLabelSelect.apply(this, i.filter("." + S.active))
                                }
                            },
                            remove: {
                                click: function() {
                                    var t = e(this).parent();
                                    t.hasClass(S.active) ? C.remove.activeLabels() : C.remove.activeLabels(t)
                                }
                            },
                            test: {
                                toggle: function(e) {
                                    var t = C.is.multiple() ? C.show : C.toggle;
                                    C.is.bubbledLabelClick(e) || C.is.bubbledIconClick(e) || C.determine.eventOnElement(e, t) && e.preventDefault()
                                },
                                touch: function(e) {
                                    C.determine.eventOnElement(e, function() {
                                        "touchstart" == e.type ? C.timer = setTimeout(function() {
                                            C.hide()
                                        }, k.delay.touch) : "touchmove" == e.type && clearTimeout(C.timer)
                                    }), e.stopPropagation()
                                },
                                hide: function(e) {
                                    C.determine.eventInModule(e, C.hide)
                                }
                            },
                            select: {
                                mutation: function(e) {
                                    C.debug("<select> modified, recreating menu"), C.setup.select()
                                }
                            },
                            menu: {
                                mutation: function(t) {
                                    var n = t[0],
                                        i = e(!!n.addedNodes && n.addedNodes[0]),
                                        o = e(!!n.removedNodes && n.removedNodes[0]),
                                        r = i.add(o),
                                        a = r.is(j.addition) || r.closest(j.addition).length > 0,
                                        s = r.is(j.message) || r.closest(j.message).length > 0;
                                    a || s ? (C.debug("Updating item selector cache"), C.refreshItems()) : (C.debug("Menu modified, updating selector cache"), C.refresh())
                                },
                                mousedown: function() {
                                    X = !0
                                },
                                mouseup: function() {
                                    X = !1
                                }
                            },
                            item: {
                                mouseenter: function(t) {
                                    var n = e(t.target),
                                        i = e(this),
                                        o = i.children(j.menu),
                                        r = i.siblings(j.item).children(j.menu),
                                        a = o.length > 0;
                                    !(o.find(n).length > 0) && a && (clearTimeout(C.itemTimer), C.itemTimer = setTimeout(function() {
                                        C.verbose("Showing sub-menu", o), e.each(r, function() {
                                            C.animate.hide(!1, e(this))
                                        }), C.animate.show(!1, o)
                                    }, k.delay.show), t.preventDefault())
                                },
                                mouseleave: function(t) {
                                    var n = e(this).children(j.menu);
                                    n.length > 0 && (clearTimeout(C.itemTimer), C.itemTimer = setTimeout(function() {
                                        C.verbose("Hiding sub-menu", n), C.animate.hide(!1, n)
                                    }, k.delay.hide))
                                },
                                click: function(t, i) {
                                    var o = e(this),
                                        r = e(t ? t.target : ""),
                                        a = o.find(j.menu),
                                        s = C.get.choiceText(o),
                                        l = C.get.choiceValue(o, s),
                                        c = a.length > 0,
                                        u = a.find(r).length > 0;
                                    C.has.menuSearch() && e(n.activeElement).blur(), u || c && !k.allowCategorySelection || (C.is.searchSelection() && (k.allowAdditions && C.remove.userAddition(), C.remove.searchTerm(), C.is.focusedOnSearch() || 1 == i || C.focusSearch(!0)), k.useLabels || (C.remove.filteredItem(), C.set.scrollPosition(o)), C.determine.selectAction.call(this, s, l))
                                }
                            },
                            document: {
                                keydown: function(e) {
                                    var t = e.which;
                                    if (C.is.inObject(t, E)) {
                                        var n = R.find(j.label),
                                            i = n.filter("." + S.active),
                                            o = (i.data(D.value), n.index(i)),
                                            r = n.length,
                                            a = i.length > 0,
                                            s = i.length > 1,
                                            l = 0 === o,
                                            c = o + 1 == r,
                                            u = C.is.searchSelection(),
                                            d = C.is.focusedOnSearch(),
                                            f = C.is.focused(),
                                            p = d && 0 === C.get.caretPosition();
                                        if (u && !a && !d) return;
                                        t == E.leftArrow ? !f && !p || a ? a && (e.shiftKey ? C.verbose("Adding previous label to selection") : (C.verbose("Selecting previous label"), n.removeClass(S.active)), l && !s ? i.addClass(S.active) : i.prev(j.siblingLabel).addClass(S.active).end(), e.preventDefault()) : (C.verbose("Selecting previous label"), n.last().addClass(S.active)) : t == E.rightArrow ? (f && !a && n.first().addClass(S.active), a && (e.shiftKey ? C.verbose("Adding next label to selection") : (C.verbose("Selecting next label"), n.removeClass(S.active)), c ? u ? d ? n.removeClass(S.active) : C.focusSearch() : s ? i.next(j.siblingLabel).addClass(S.active) : i.addClass(S.active) : i.next(j.siblingLabel).addClass(S.active), e.preventDefault())) : t == E.deleteKey || t == E.backspace ? a ? (C.verbose("Removing active labels"), c && u && !d && C.focusSearch(), i.last().next(j.siblingLabel).addClass(S.active), C.remove.activeLabels(i), e.preventDefault()) : p && !a && t == E.backspace && (C.verbose("Removing last label on input backspace"), i = n.last().addClass(S.active), C.remove.activeLabels(i)) : i.removeClass(S.active)
                                    }
                                }
                            },
                            keydown: function(e) {
                                var t = e.which;
                                if (C.is.inObject(t, E)) {
                                    var n, i = U.not(j.unselectable).filter("." + S.selected).eq(0),
                                        o = W.children("." + S.active).eq(0),
                                        r = i.length > 0 ? i : o,
                                        a = r.length > 0 ? r.siblings(":not(." + S.filtered + ")").addBack() : W.children(":not(." + S.filtered + ")"),
                                        s = r.children(j.menu),
                                        l = r.closest(j.menu),
                                        c = l.hasClass(S.visible) || l.hasClass(S.animating) || l.parent(j.menu).length > 0,
                                        u = s.length > 0,
                                        d = r.length > 0,
                                        f = r.not(j.unselectable).length > 0,
                                        p = t == E.delimiter && k.allowAdditions && C.is.multiple();
                                    if (k.allowAdditions && k.hideAdditions && (t == E.enter || p) && f && (C.verbose("Selecting item from keyboard shortcut", r), C.event.item.click.call(r, e), C.is.searchSelection() && C.remove.searchTerm()), C.is.visible()) {
                                        if ((t == E.enter || p) && (t == E.enter && d && u && !k.allowCategorySelection ? (C.verbose("Pressed enter on unselectable category, opening sub menu"), t = E.rightArrow) : f && (C.verbose("Selecting item from keyboard shortcut", r), C.event.item.click.call(r, e), C.is.searchSelection() && C.remove.searchTerm()), e.preventDefault()), d && (t == E.leftArrow && l[0] !== W[0] && (C.verbose("Left key pressed, closing sub-menu"), C.animate.hide(!1, l), r.removeClass(S.selected), l.closest(j.item).addClass(S.selected), e.preventDefault()), t == E.rightArrow && u && (C.verbose("Right key pressed, opening sub-menu"), C.animate.show(!1, s), r.removeClass(S.selected), s.find(j.item).eq(0).addClass(S.selected), e.preventDefault())), t == E.upArrow) {
                                            if (n = d && c ? r.prevAll(j.item + ":not(" + j.unselectable + ")").eq(0) : U.eq(0), a.index(n) < 0) return C.verbose("Up key pressed but reached top of current menu"), void e.preventDefault();
                                            C.verbose("Up key pressed, changing active item"), r.removeClass(S.selected), n.addClass(S.selected), C.set.scrollPosition(n), k.selectOnKeydown && C.is.single() && C.set.selectedItem(n), e.preventDefault()
                                        }
                                        if (t == E.downArrow) {
                                            if (n = d && c ? n = r.nextAll(j.item + ":not(" + j.unselectable + ")").eq(0) : U.eq(0), 0 === n.length) return C.verbose("Down key pressed but reached bottom of current menu"), void e.preventDefault();
                                            C.verbose("Down key pressed, changing active item"), U.removeClass(S.selected), n.addClass(S.selected), C.set.scrollPosition(n), k.selectOnKeydown && C.is.single() && C.set.selectedItem(n), e.preventDefault()
                                        }
                                        t == E.pageUp && (C.scrollPage("up"), e.preventDefault()), t == E.pageDown && (C.scrollPage("down"), e.preventDefault()), t == E.escape && (C.verbose("Escape key pressed, closing dropdown"), C.hide())
                                    } else p && e.preventDefault(), t != E.downArrow || C.is.visible() || (C.verbose("Down key pressed, showing dropdown"), C.select.firstUnfiltered(), C.show(), e.preventDefault())
                                } else C.has.search() || C.set.selectedLetter(String.fromCharCode(t))
                            }
                        },
                        trigger: {
                            change: function() {
                                var e = n.createEvent("HTMLEvents"),
                                    t = $[0];
                                t && (C.verbose("Triggering native change event"), e.initEvent("change", !0, !1), t.dispatchEvent(e))
                            }
                        },
                        determine: {
                            selectAction: function(t, n) {
                                C.verbose("Determining action", k.action), e.isFunction(C.action[k.action]) ? (C.verbose("Triggering preset action", k.action, t, n), C.action[k.action].call(Y, t, n, this)) : e.isFunction(k.action) ? (C.verbose("Triggering user action", k.action, t, n), k.action.call(Y, t, n, this)) : C.error(q.action, k.action)
                            },
                            eventInModule: function(t, i) {
                                var o = e(t.target),
                                    r = o.closest(n.documentElement).length > 0,
                                    a = o.closest(R).length > 0;
                                return i = e.isFunction(i) ? i : function() {}, r && !a ? (C.verbose("Triggering event", i), i(), !0) : (C.verbose("Event occurred in dropdown, canceling callback"), !1)
                            },
                            eventOnElement: function(t, i) {
                                var o = e(t.target),
                                    r = o.closest(j.siblingLabel),
                                    a = n.body.contains(t.target),
                                    s = 0 === R.find(r).length,
                                    l = 0 === o.closest(W).length;
                                return i = e.isFunction(i) ? i : function() {}, a && s && l ? (C.verbose("Triggering event", i), i(), !0) : (C.verbose("Event occurred in dropdown menu, canceling callback"), !1)
                            }
                        },
                        action: {
                            nothing: function() {},
                            activate: function(t, n, i) {
                                if (n = void 0 !== n ? n : t, C.can.activate(e(i))) {
                                    if (C.set.selected(n, e(i)), C.is.multiple() && !C.is.allFiltered()) return;
                                    C.hideAndClear()
                                }
                            },
                            select: function(t, n, i) {
                                if (n = void 0 !== n ? n : t, C.can.activate(e(i))) {
                                    if (C.set.value(n, e(i)), C.is.multiple() && !C.is.allFiltered()) return;
                                    C.hideAndClear()
                                }
                            },
                            combo: function(t, n, i) {
                                n = void 0 !== n ? n : t, C.set.selected(n, e(i)), C.hideAndClear()
                            },
                            hide: function(e, t, n) {
                                C.set.value(t, e), C.hideAndClear()
                            }
                        },
                        get: {
                            id: function() {
                                return y
                            },
                            defaultText: function() {
                                return R.data(D.defaultText)
                            },
                            defaultValue: function() {
                                return R.data(D.defaultValue)
                            },
                            placeholderText: function() {
                                return R.data(D.placeholderText) || ""
                            },
                            text: function() {
                                return M.text()
                            },
                            query: function() {
                                return e.trim(H.val())
                            },
                            searchWidth: function(e) {
                                return e = void 0 !== e ? e : H.val(), z.text(e), Math.ceil(z.width() + 1)
                            },
                            selectionCount: function() {
                                var t = C.get.values();
                                return C.is.multiple() ? e.isArray(t) ? t.length : 0 : "" !== C.get.value() ? 1 : 0
                            },
                            transition: function(e) {
                                return "auto" == k.transition ? C.is.upward(e) ? "slide up" : "slide down" : k.transition
                            },
                            userValues: function() {
                                var t = C.get.values();
                                return !!t && (t = e.isArray(t) ? t : [t], e.grep(t, function(e) {
                                    return !1 === C.get.item(e)
                                }))
                            },
                            uniqueArray: function(t) {
                                return e.grep(t, function(n, i) {
                                    return e.inArray(n, t) === i
                                })
                            },
                            caretPosition: function() {
                                var e, t, i = H.get(0);
                                return "selectionStart" in i ? i.selectionStart : n.selection ? (i.focus(), e = n.selection.createRange(), t = e.text.length, e.moveStart("character", -i.value.length), e.text.length - t) : void 0
                            },
                            value: function() {
                                var t = $.length > 0 ? $.val() : R.data(D.value),
                                    n = e.isArray(t) && 1 === t.length && "" === t[0];
                                return void 0 === t || n ? "" : t
                            },
                            values: function() {
                                var e = C.get.value();
                                return "" === e ? "" : !C.has.selectInput() && C.is.multiple() ? "string" == typeof e ? e.split(k.delimiter) : "" : e
                            },
                            remoteValues: function() {
                                var t = C.get.values(),
                                    n = !1;
                                return t && ("string" == typeof t && (t = [t]), e.each(t, function(e, t) {
                                    var i = C.read.remoteData(t);
                                    C.verbose("Restoring value from session data", i, t), i && (n || (n = {}), n[t] = i)
                                })), n
                            },
                            choiceText: function(t, n) {
                                if (n = void 0 !== n ? n : k.preserveHTML, t) return t.find(j.menu).length > 0 && (C.verbose("Retrieving text of element with sub-menu"), t = t.clone(), t.find(j.menu).remove(), t.find(j.menuIcon).remove()), void 0 !== t.data(D.text) ? t.data(D.text) : n ? e.trim(t.html()) : e.trim(t.text())
                            },
                            choiceValue: function(t, n) {
                                return n = n || C.get.choiceText(t), !!t && (void 0 !== t.data(D.value) ? String(t.data(D.value)) : "string" == typeof n ? e.trim(n.toLowerCase()) : String(n))
                            },
                            inputEvent: function() {
                                var e = H[0];
                                return !!e && (void 0 !== e.oninput ? "input" : void 0 !== e.onpropertychange ? "propertychange" : "keyup")
                            },
                            selectValues: function() {
                                var t = {};
                                return t.values = [], R.find("option").each(function() {
                                    var n = e(this),
                                        i = n.html(),
                                        o = n.attr("disabled"),
                                        r = void 0 !== n.attr("value") ? n.attr("value") : i;
                                    "auto" === k.placeholder && "" === r ? t.placeholder = i : t.values.push({
                                        name: i,
                                        value: r,
                                        disabled: o
                                    })
                                }), k.placeholder && "auto" !== k.placeholder && (C.debug("Setting placeholder value to", k.placeholder), t.placeholder = k.placeholder), k.sortSelect ? (t.values.sort(function(e, t) {
                                    return e.name > t.name ? 1 : -1
                                }), C.debug("Retrieved and sorted values from select", t)) : C.debug("Retrieved values from select", t), t
                            },
                            activeItem: function() {
                                return U.filter("." + S.active)
                            },
                            selectedItem: function() {
                                var e = U.not(j.unselectable).filter("." + S.selected);
                                return e.length > 0 ? e : U.eq(0)
                            },
                            itemWithAdditions: function(e) {
                                var t = C.get.item(e),
                                    n = C.create.userChoice(e);
                                return n && n.length > 0 && (t = t.length > 0 ? t.add(n) : n), t
                            },
                            item: function(t, n) {
                                var i, o, r = !1;
                                return t = void 0 !== t ? t : void 0 !== C.get.values() ? C.get.values() : C.get.text(), i = o ? t.length > 0 : void 0 !== t && null !== t, o = C.is.multiple() && e.isArray(t), n = "" === t || 0 === t || n || !1, i && U.each(function() {
                                    var i = e(this),
                                        a = C.get.choiceText(i),
                                        s = C.get.choiceValue(i, a);
                                    if (null !== s && void 0 !== s)
                                        if (o) - 1 === e.inArray(String(s), t) && -1 === e.inArray(a, t) || (r = r ? r.add(i) : i);
                                        else if (n) {
                                        if (C.verbose("Ambiguous dropdown value using strict type check", i, t), s === t || a === t) return r = i, !0
                                    } else if (String(s) == String(t) || a == t) return C.verbose("Found select item by value", s, t), r = i, !0
                                }), r
                            }
                        },
                        check: {
                            maxSelections: function(e) {
                                return !k.maxSelections || (e = void 0 !== e ? e : C.get.selectionCount(), e >= k.maxSelections ? (C.debug("Maximum selection count reached"), k.useLabels && (U.addClass(S.filtered), C.add.message(T.maxSelections)), !0) : (C.verbose("No longer at maximum selection count"), C.remove.message(), C.remove.filteredItem(), C.is.searchSelection() && C.filterItems(), !1))
                            }
                        },
                        restore: {
                            defaults: function() {
                                C.clear(), C.restore.defaultText(), C.restore.defaultValue()
                            },
                            defaultText: function() {
                                var e = C.get.defaultText();
                                e === C.get.placeholderText ? (C.debug("Restoring default placeholder text", e), C.set.placeholderText(e)) : (C.debug("Restoring default text", e), C.set.text(e))
                            },
                            placeholderText: function() {
                                C.set.placeholderText()
                            },
                            defaultValue: function() {
                                var e = C.get.defaultValue();
                                void 0 !== e && (C.debug("Restoring default value", e), "" !== e ? (C.set.value(e), C.set.selected()) : (C.remove.activeItem(), C.remove.selectedItem()))
                            },
                            labels: function() {
                                k.allowAdditions && (k.useLabels || (C.error(q.labels), k.useLabels = !0), C.debug("Restoring selected values"), C.create.userLabels()), C.check.maxSelections()
                            },
                            selected: function() {
                                C.restore.values(), C.is.multiple() ? (C.debug("Restoring previously selected values and labels"), C.restore.labels()) : C.debug("Restoring previously selected values")
                            },
                            values: function() {
                                C.set.initialLoad(), k.apiSettings && k.saveRemoteData && C.get.remoteValues() ? C.restore.remoteValues() : C.set.selected(), C.remove.initialLoad()
                            },
                            remoteValues: function() {
                                var t = C.get.remoteValues();
                                C.debug("Recreating selected from session data", t), t && (C.is.single() ? e.each(t, function(e, t) {
                                    C.set.text(t)
                                }) : e.each(t, function(e, t) {
                                    C.add.label(e, t)
                                }))
                            }
                        },
                        read: {
                            remoteData: function(e) {
                                var n;
                                return void 0 === t.Storage ? void C.error(q.noStorage) : void 0 !== (n = sessionStorage.getItem(e)) && n
                            }
                        },
                        save: {
                            defaults: function() {
                                C.save.defaultText(), C.save.placeholderText(), C.save.defaultValue()
                            },
                            defaultValue: function() {
                                var e = C.get.value();
                                C.verbose("Saving default value as", e), R.data(D.defaultValue, e)
                            },
                            defaultText: function() {
                                var e = C.get.text();
                                C.verbose("Saving default text as", e), R.data(D.defaultText, e)
                            },
                            placeholderText: function() {
                                var e;
                                !1 !== k.placeholder && M.hasClass(S.placeholder) && (e = C.get.text(), C.verbose("Saving placeholder text as", e), R.data(D.placeholderText, e))
                            },
                            remoteData: function(e, n) {
                                if (void 0 === t.Storage) return void C.error(q.noStorage);
                                C.verbose("Saving remote data to session storage", n, e), sessionStorage.setItem(n, e)
                            }
                        },
                        clear: function() {
                            C.is.multiple() && k.useLabels ? C.remove.labels() : (C.remove.activeItem(), C.remove.selectedItem()), C.set.placeholderText(), C.clearValue()
                        },
                        clearValue: function() {
                            C.set.value("")
                        },
                        scrollPage: function(e, t) {
                            var n, i, o, r = t || C.get.selectedItem(),
                                a = r.closest(j.menu),
                                s = a.outerHeight(),
                                l = a.scrollTop(),
                                c = U.eq(0).outerHeight(),
                                u = Math.floor(s / c),
                                d = (a.prop("scrollHeight"), "up" == e ? l - c * u : l + c * u),
                                f = U.not(j.unselectable);
                            o = "up" == e ? f.index(r) - u : f.index(r) + u, n = "up" == e ? o >= 0 : o < f.length, i = n ? f.eq(o) : "up" == e ? f.first() : f.last(), i.length > 0 && (C.debug("Scrolling page", e, i), r.removeClass(S.selected), i.addClass(S.selected), k.selectOnKeydown && C.is.single() && C.set.selectedItem(i), a.scrollTop(d))
                        },
                        set: {
                            filtered: function() {
                                var e = C.is.multiple(),
                                    t = C.is.searchSelection(),
                                    n = e && t,
                                    i = t ? C.get.query() : "",
                                    o = "string" == typeof i && i.length > 0,
                                    r = C.get.searchWidth(),
                                    a = "" !== i;
                                e && o && (C.verbose("Adjusting input width", r, k.glyphWidth), H.css("width", r)), o || n && a ? (C.verbose("Hiding placeholder text"), M.addClass(S.filtered)) : (!e || n && !a) && (C.verbose("Showing placeholder text"), M.removeClass(S.filtered))
                            },
                            empty: function() {
                                R.addClass(S.empty)
                            },
                            loading: function() {
                                R.addClass(S.loading)
                            },
                            placeholderText: function(e) {
                                e = e || C.get.placeholderText(), C.debug("Setting placeholder text", e), C.set.text(e), M.addClass(S.placeholder)
                            },
                            tabbable: function() {
                                C.is.searchSelection() ? (C.debug("Added tabindex to searchable dropdown"), H.val("").attr("tabindex", 0), W.attr("tabindex", -1)) : (C.debug("Added tabindex to dropdown"), void 0 === R.attr("tabindex") && (R.attr("tabindex", 0), W.attr("tabindex", -1)))
                            },
                            initialLoad: function() {
                                C.verbose("Setting initial load"), m = !0
                            },
                            activeItem: function(e) {
                                k.allowAdditions && e.filter(j.addition).length > 0 ? e.addClass(S.filtered) : e.addClass(S.active)
                            },
                            partialSearch: function(e) {
                                var t = C.get.query().length;
                                H.val(e.substr(0, t))
                            },
                            scrollPosition: function(e, t) {
                                var n, i, o, r, a, s, l, c, u;
                                e = e || C.get.selectedItem(), n = e.closest(j.menu), i = e && e.length > 0, t = void 0 !== t && t, e && n.length > 0 && i && (r = e.position().top, n.addClass(S.loading), s = n.scrollTop(), a = n.offset().top, r = e.offset().top, o = s - a + r, t || (l = n.height(), u = s + l < o + 5, c = o - 5 < s), C.debug("Scrolling to active item", o), (t || c || u) && n.scrollTop(o), n.removeClass(S.loading))
                            },
                            text: function(e) {
                                "select" !== k.action && ("combo" == k.action ? (C.debug("Changing combo button text", e, B), k.preserveHTML ? B.html(e) : B.text(e)) : (e !== C.get.placeholderText() && M.removeClass(S.placeholder), C.debug("Changing text", e, M), M.removeClass(S.filtered), k.preserveHTML ? M.html(e) : M.text(e)))
                            },
                            selectedItem: function(e) {
                                var t = C.get.choiceValue(e),
                                    n = C.get.choiceText(e, !1),
                                    i = C.get.choiceText(e, !0);
                                C.debug("Setting user selection to item", e), C.remove.activeItem(), C.set.partialSearch(n), C.set.activeItem(e), C.set.selected(t, e), C.set.text(i)
                            },
                            selectedLetter: function(t) {
                                var n, i = U.filter("." + S.selected),
                                    o = i.length > 0 && C.has.firstLetter(i, t),
                                    r = !1;
                                o && (n = i.nextAll(U).eq(0), C.has.firstLetter(n, t) && (r = n)), r || U.each(function() {
                                    if (C.has.firstLetter(e(this), t)) return r = e(this), !1
                                }), r && (C.verbose("Scrolling to next value with letter", t), C.set.scrollPosition(r), i.removeClass(S.selected), r.addClass(S.selected), k.selectOnKeydown && C.is.single() && C.set.selectedItem(r))
                            },
                            direction: function(e) {
                                "auto" == k.direction ? C.is.onScreen(e) ? C.remove.upward(e) : C.set.upward(e) : "upward" == k.direction && C.set.upward(e)
                            },
                            upward: function(e) {
                                (e || R).addClass(S.upward)
                            },
                            value: function(e, t, n) {
                                var i = C.escape.value(e),
                                    o = $.length > 0,
                                    r = (C.has.value(e), C.get.values()),
                                    a = void 0 !== e ? String(e) : e;
                                if (o) {
                                    if (!k.allowReselection && a == r && (C.verbose("Skipping value update already same value", e, r), !C.is.initialLoad())) return;
                                    C.is.single() && C.has.selectInput() && C.can.extendSelect() && (C.debug("Adding user option", e), C.add.optionValue(e)), C.debug("Updating input value", i, r), Q = !0, $.val(i), !1 === k.fireOnInit && C.is.initialLoad() ? C.debug("Input native change event ignored on initial load") : C.trigger.change(), Q = !1
                                } else C.verbose("Storing value in metadata", i, $), i !== r && R.data(D.value, a);
                                !1 === k.fireOnInit && C.is.initialLoad() ? C.verbose("No callback on initial load", k.onChange) : k.onChange.call(Y, e, t, n)
                            },
                            active: function() {
                                R.addClass(S.active)
                            },
                            multiple: function() {
                                R.addClass(S.multiple)
                            },
                            visible: function() {
                                R.addClass(S.visible)
                            },
                            exactly: function(e, t) {
                                C.debug("Setting selected to exact values"), C.clear(), C.set.selected(e, t)
                            },
                            selected: function(t, n) {
                                var i = C.is.multiple();
                                (n = k.allowAdditions ? n || C.get.itemWithAdditions(t) : n || C.get.item(t)) && (C.debug("Setting selected menu item to", n), C.is.multiple() && C.remove.searchWidth(), C.is.single() ? (C.remove.activeItem(), C.remove.selectedItem()) : k.useLabels && C.remove.selectedItem(), n.each(function() {
                                    var t = e(this),
                                        o = C.get.choiceText(t),
                                        r = C.get.choiceValue(t, o),
                                        a = t.hasClass(S.filtered),
                                        s = t.hasClass(S.active),
                                        l = t.hasClass(S.addition),
                                        c = i && 1 == n.length;
                                    i ? !s || l ? (k.apiSettings && k.saveRemoteData && C.save.remoteData(o, r), k.useLabels ? (C.add.value(r, o, t), C.add.label(r, o, c), C.set.activeItem(t), C.filterActive(), C.select.nextAvailable(n)) : (C.add.value(r, o, t), C.set.text(C.add.variables(T.count)), C.set.activeItem(t))) : a || (C.debug("Selected active value, removing label"), C.remove.selected(r)) : (k.apiSettings && k.saveRemoteData && C.save.remoteData(o, r), C.set.text(o), C.set.value(r, o, t), t.addClass(S.active).addClass(S.selected))
                                }))
                            }
                        },
                        add: {
                            label: function(t, n, i) {
                                var o, r = C.is.searchSelection() ? H : M,
                                    a = C.escape.value(t);
                                if (o = e("<a />").addClass(S.label).attr("data-" + D.value, a).html(L.label(a, n)), o = k.onLabelCreate.call(o, a, n), C.has.label(t)) return void C.debug("Label already exists, skipping", a);
                                k.label.variation && o.addClass(k.label.variation), !0 === i ? (C.debug("Animating in label", o), o.addClass(S.hidden).insertBefore(r).transition(k.label.transition, k.label.duration)) : (C.debug("Adding selection label", o), o.insertBefore(r))
                            },
                            message: function(t) {
                                var n = W.children(j.message),
                                    i = k.templates.message(C.add.variables(t));
                                n.length > 0 ? n.html(i) : n = e("<div/>").html(i).addClass(S.message).appendTo(W)
                            },
                            optionValue: function(t) {
                                var n = C.escape.value(t);
                                $.find('option[value="' + C.escape.string(n) + '"]').length > 0 || (C.disconnect.selectObserver(), C.is.single() && (C.verbose("Removing previous user addition"), $.find("option." + S.addition).remove()), e("<option/>").prop("value", n).addClass(S.addition).html(t).appendTo($), C.verbose("Adding user addition as an <option>", t), C.observe.select())
                            },
                            userSuggestion: function(e) {
                                var t, n = W.children(j.addition),
                                    i = C.get.item(e),
                                    o = i && i.not(j.addition).length,
                                    r = n.length > 0;
                                if (!k.useLabels || !C.has.maxSelections()) {
                                    if ("" === e || o) return void n.remove();
                                    r ? (n.data(D.value, e).data(D.text, e).attr("data-" + D.value, e).attr("data-" + D.text, e).removeClass(S.filtered), k.hideAdditions || (t = k.templates.addition(C.add.variables(T.addResult, e)), n.html(t)), C.verbose("Replacing user suggestion with new value", n)) : (n = C.create.userChoice(e), n.prependTo(W), C.verbose("Adding item choice to menu corresponding with user choice addition", n)), k.hideAdditions && !C.is.allFiltered() || n.addClass(S.selected).siblings().removeClass(S.selected), C.refreshItems()
                                }
                            },
                            variables: function(e, t) {
                                var n, i, o = -1 !== e.search("{count}"),
                                    r = -1 !== e.search("{maxCount}"),
                                    a = -1 !== e.search("{term}");
                                return C.verbose("Adding templated variables to message", e), o && (n = C.get.selectionCount(), e = e.replace("{count}", n)), r && (n = C.get.selectionCount(), e = e.replace("{maxCount}", k.maxSelections)), a && (i = t || C.get.query(), e = e.replace("{term}", i)), e
                            },
                            value: function(t, n, i) {
                                var o, r = C.get.values();
                                if ("" === t) return void C.debug("Cannot select blank values from multiselect");
                                e.isArray(r) ? (o = r.concat([t]), o = C.get.uniqueArray(o)) : o = [t], C.has.selectInput() ? C.can.extendSelect() && (C.debug("Adding value to select", t, o, $), C.add.optionValue(t)) : (o = o.join(k.delimiter), C.debug("Setting hidden input to delimited value", o, $)), !1 === k.fireOnInit && C.is.initialLoad() ? C.verbose("Skipping onadd callback on initial load", k.onAdd) : k.onAdd.call(Y, t, n, i), C.set.value(o, t, n, i), C.check.maxSelections()
                            }
                        },
                        remove: {
                            active: function() {
                                R.removeClass(S.active)
                            },
                            activeLabel: function() {
                                R.find(j.label).removeClass(S.active)
                            },
                            empty: function() {
                                R.removeClass(S.empty)
                            },
                            loading: function() {
                                R.removeClass(S.loading)
                            },
                            initialLoad: function() {
                                m = !1
                            },
                            upward: function(e) {
                                (e || R).removeClass(S.upward)
                            },
                            visible: function() {
                                R.removeClass(S.visible)
                            },
                            activeItem: function() {
                                U.removeClass(S.active)
                            },
                            filteredItem: function() {
                                k.useLabels && C.has.maxSelections() || (k.useLabels && C.is.multiple() ? U.not("." + S.active).removeClass(S.filtered) : U.removeClass(S.filtered), C.remove.empty())
                            },
                            optionValue: function(e) {
                                var t = C.escape.value(e),
                                    n = $.find('option[value="' + C.escape.string(t) + '"]');
                                n.length > 0 && n.hasClass(S.addition) && (x && (x.disconnect(), C.verbose("Temporarily disconnecting mutation observer")), n.remove(), C.verbose("Removing user addition as an <option>", t), x && x.observe($[0], {
                                    childList: !0,
                                    subtree: !0
                                }))
                            },
                            message: function() {
                                W.children(j.message).remove()
                            },
                            searchWidth: function() {
                                H.css("width", "")
                            },
                            searchTerm: function() {
                                C.verbose("Cleared search term"), H.val(""), C.set.filtered()
                            },
                            userAddition: function() {
                                U.filter(j.addition).remove()
                            },
                            selected: function(t, n) {
                                if (!(n = k.allowAdditions ? n || C.get.itemWithAdditions(t) : n || C.get.item(t))) return !1;
                                n.each(function() {
                                    var t = e(this),
                                        n = C.get.choiceText(t),
                                        i = C.get.choiceValue(t, n);
                                    C.is.multiple() ? k.useLabels ? (C.remove.value(i, n, t), C.remove.label(i)) : (C.remove.value(i, n, t), 0 === C.get.selectionCount() ? C.set.placeholderText() : C.set.text(C.add.variables(T.count))) : C.remove.value(i, n, t), t.removeClass(S.filtered).removeClass(S.active), k.useLabels && t.removeClass(S.selected)
                                })
                            },
                            selectedItem: function() {
                                U.removeClass(S.selected)
                            },
                            value: function(e, t, n) {
                                var i, o = C.get.values();
                                C.has.selectInput() ? (C.verbose("Input is <select> removing selected option", e), i = C.remove.arrayValue(e, o), C.remove.optionValue(e)) : (C.verbose("Removing from delimited values", e), i = C.remove.arrayValue(e, o), i = i.join(k.delimiter)), !1 === k.fireOnInit && C.is.initialLoad() ? C.verbose("No callback on initial load", k.onRemove) : k.onRemove.call(Y, e, t, n), C.set.value(i, t, n), C.check.maxSelections()
                            },
                            arrayValue: function(t, n) {
                                return e.isArray(n) || (n = [n]), n = e.grep(n, function(e) {
                                    return t != e
                                }), C.verbose("Removed value from delimited string", t, n), n
                            },
                            label: function(e, t) {
                                var n = R.find(j.label),
                                    i = n.filter("[data-" + D.value + '="' + C.escape.string(e) + '"]');
                                C.verbose("Removing label", i), i.remove()
                            },
                            activeLabels: function(e) {
                                e = e || R.find(j.label).filter("." + S.active), C.verbose("Removing active label selections", e), C.remove.labels(e)
                            },
                            labels: function(t) {
                                t = t || R.find(j.label), C.verbose("Removing labels", t), t.each(function() {
                                    var t = e(this),
                                        n = t.data(D.value),
                                        i = void 0 !== n ? String(n) : n,
                                        o = C.is.userValue(i);
                                    if (!1 === k.onLabelRemove.call(t, n)) return void C.debug("Label remove callback cancelled removal");
                                    C.remove.message(), o ? (C.remove.value(i), C.remove.label(i)) : C.remove.selected(i)
                                })
                            },
                            tabbable: function() {
                                C.is.searchSelection() ? (C.debug("Searchable dropdown initialized"), H.removeAttr("tabindex"), W.removeAttr("tabindex")) : (C.debug("Simple selection dropdown initialized"), R.removeAttr("tabindex"), W.removeAttr("tabindex"))
                            }
                        },
                        has: {
                            menuSearch: function() {
                                return C.has.search() && H.closest(W).length > 0
                            },
                            search: function() {
                                return H.length > 0
                            },
                            sizer: function() {
                                return z.length > 0
                            },
                            selectInput: function() {
                                return $.is("select")
                            },
                            minCharacters: function(e) {
                                return !k.minCharacters || (e = void 0 !== e ? String(e) : String(C.get.query()), e.length >= k.minCharacters)
                            },
                            firstLetter: function(e, t) {
                                var n, i;
                                return !(!e || 0 === e.length || "string" != typeof t) && (n = C.get.choiceText(e, !1), t = t.toLowerCase(), i = String(n).charAt(0).toLowerCase(), t == i)
                            },
                            input: function() {
                                return $.length > 0
                            },
                            items: function() {
                                return U.length > 0
                            },
                            menu: function() {
                                return W.length > 0
                            },
                            message: function() {
                                return 0 !== W.children(j.message).length
                            },
                            label: function(e) {
                                var t = C.escape.value(e);
                                return R.find(j.label).filter("[data-" + D.value + '="' + C.escape.string(t) + '"]').length > 0
                            },
                            maxSelections: function() {
                                return k.maxSelections && C.get.selectionCount() >= k.maxSelections
                            },
                            allResultsFiltered: function() {
                                var e = U.not(j.addition);
                                return e.filter(j.unselectable).length === e.length
                            },
                            userSuggestion: function() {
                                return W.children(j.addition).length > 0
                            },
                            query: function() {
                                return "" !== C.get.query()
                            },
                            value: function(t) {
                                var n = C.get.values();
                                return !!(e.isArray(n) ? n && -1 !== e.inArray(t, n) : n == t)
                            }
                        },
                        is: {
                            active: function() {
                                return R.hasClass(S.active)
                            },
                            bubbledLabelClick: function(t) {
                                return e(t.target).is("select, input") && R.closest("label").length > 0
                            },
                            bubbledIconClick: function(t) {
                                return e(t.target).closest(V).length > 0
                            },
                            alreadySetup: function() {
                                return R.is("select") && R.parent(j.dropdown).length > 0 && 0 === R.prev().length
                            },
                            animating: function(e) {
                                return e ? e.transition && e.transition("is animating") : W.transition && W.transition("is animating")
                            },
                            disabled: function() {
                                return R.hasClass(S.disabled)
                            },
                            focused: function() {
                                return n.activeElement === R[0]
                            },
                            focusedOnSearch: function() {
                                return n.activeElement === H[0]
                            },
                            allFiltered: function() {
                                return (C.is.multiple() || C.has.search()) && !(0 == k.hideAdditions && C.has.userSuggestion()) && !C.has.message() && C.has.allResultsFiltered()
                            },
                            hidden: function(e) {
                                return !C.is.visible(e)
                            },
                            initialLoad: function() {
                                return m
                            },
                            onScreen: function(e) {
                                var t, n = e || W,
                                    i = !0,
                                    o = {};
                                return n.addClass(S.loading), t = {
                                    context: {
                                        scrollTop: I.scrollTop(),
                                        height: I.outerHeight()
                                    },
                                    menu: {
                                        offset: n.offset(),
                                        height: n.outerHeight()
                                    }
                                }, C.is.verticallyScrollableContext() && (t.menu.offset.top += t.context.scrollTop), o = {
                                    above: t.context.scrollTop <= t.menu.offset.top - t.menu.height,
                                    below: t.context.scrollTop + t.context.height >= t.menu.offset.top + t.menu.height
                                }, o.below ? (C.verbose("Dropdown can fit in context downward", o), i = !0) : o.below || o.above ? (C.verbose("Dropdown cannot fit below, opening upward", o), i = !1) : (C.verbose("Dropdown cannot fit in either direction, favoring downward", o), i = !0), n.removeClass(S.loading), i
                            },
                            inObject: function(t, n) {
                                var i = !1;
                                return e.each(n, function(e, n) {
                                    if (n == t) return i = !0, !0
                                }), i
                            },
                            multiple: function() {
                                return R.hasClass(S.multiple)
                            },
                            remote: function() {
                                return k.apiSettings && C.can.useAPI()
                            },
                            single: function() {
                                return !C.is.multiple()
                            },
                            selectMutation: function(t) {
                                var n = !1;
                                return e.each(t, function(t, i) {
                                    if (i.target && e(i.target).is("select")) return n = !0, !0
                                }), n
                            },
                            search: function() {
                                return R.hasClass(S.search)
                            },
                            searchSelection: function() {
                                return C.has.search() && 1 === H.parent(j.dropdown).length
                            },
                            selection: function() {
                                return R.hasClass(S.selection)
                            },
                            userValue: function(t) {
                                return -1 !== e.inArray(t, C.get.userValues())
                            },
                            upward: function(e) {
                                return (e || R).hasClass(S.upward)
                            },
                            visible: function(e) {
                                return e ? e.hasClass(S.visible) : W.hasClass(S.visible)
                            },
                            verticallyScrollableContext: function() {
                                var e = I.get(0) !== t && I.css("overflow-y");
                                return "auto" == e || "scroll" == e
                            }
                        },
                        can: {
                            activate: function(e) {
                                return !!k.useLabels || !C.has.maxSelections() || !(!C.has.maxSelections() || !e.hasClass(S.active))
                            },
                            click: function() {
                                return l || "click" == k.on
                            },
                            extendSelect: function() {
                                return k.allowAdditions || k.apiSettings
                            },
                            show: function() {
                                return !C.is.disabled() && (C.has.items() || C.has.message())
                            },
                            useAPI: function() {
                                return void 0 !== e.fn.api
                            }
                        },
                        animate: {
                            show: function(t, n) {
                                var i, o = n || W,
                                    r = n ? function() {} : function() {
                                        C.hideSubMenus(), C.hideOthers(), C.set.active()
                                    };
                                t = e.isFunction(t) ? t : function() {}, C.verbose("Doing menu show animation", o), C.set.direction(n), i = C.get.transition(n), C.is.selection() && C.set.scrollPosition(C.get.selectedItem(), !0), (C.is.hidden(o) || C.is.animating(o)) && ("none" == i ? (r(), o.transition("show"), t.call(Y)) : void 0 !== e.fn.transition && R.transition("is supported") ? o.transition({
                                    animation: i + " in",
                                    debug: k.debug,
                                    verbose: k.verbose,
                                    duration: k.duration,
                                    queue: !0,
                                    onStart: r,
                                    onComplete: function() {
                                        t.call(Y)
                                    }
                                }) : C.error(q.noTransition, i))
                            },
                            hide: function(t, n) {
                                var i = n || W,
                                    o = (k.duration, n ? function() {} : function() {
                                        C.can.click() && C.unbind.intent(), C.remove.active()
                                    }),
                                    r = C.get.transition(n);
                                t = e.isFunction(t) ? t : function() {}, (C.is.visible(i) || C.is.animating(i)) && (C.verbose("Doing menu hide animation", i), "none" == r ? (o(), i.transition("hide"), t.call(Y)) : void 0 !== e.fn.transition && R.transition("is supported") ? i.transition({
                                    animation: r + " out",
                                    duration: k.duration,
                                    debug: k.debug,
                                    verbose: k.verbose,
                                    queue: !0,
                                    onStart: o,
                                    onComplete: function() {
                                        "auto" == k.direction && C.remove.upward(n), t.call(Y)
                                    }
                                }) : C.error(q.transition))
                            }
                        },
                        hideAndClear: function() {
                            C.remove.searchTerm(), C.has.maxSelections() || (C.has.search() ? C.hide(function() {
                                C.remove.filteredItem()
                            }) : C.hide())
                        },
                        delay: {
                            show: function() {
                                C.verbose("Delaying show event to ensure user intent"), clearTimeout(C.timer), C.timer = setTimeout(C.show, k.delay.show)
                            },
                            hide: function() {
                                C.verbose("Delaying hide event to ensure user intent"), clearTimeout(C.timer), C.timer = setTimeout(C.hide, k.delay.hide)
                            }
                        },
                        escape: {
                            value: function(t) {
                                var n = e.isArray(t),
                                    i = "string" == typeof t,
                                    o = !i && !n,
                                    r = i && -1 !== t.search(F.quote),
                                    a = [];
                                return o || !r ? t : (C.debug("Encoding quote values for use in select", t), n ? (e.each(t, function(e, t) {
                                    a.push(t.replace(F.quote, "&quot;"))
                                }), a) : t.replace(F.quote, "&quot;"))
                            },
                            string: function(e) {
                                return e = String(e), e.replace(F.escape, "\\$&")
                            }
                        },
                        setting: function(t, n) {
                            if (C.debug("Changing setting", t, n), e.isPlainObject(t)) e.extend(!0, k, t);
                            else {
                                if (void 0 === n) return k[t];
                                e.isPlainObject(k[t]) ? e.extend(!0, k[t], n) : k[t] = n
                            }
                        },
                        internal: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, C, t);
                            else {
                                if (void 0 === n) return C[t];
                                C[t] = n
                            }
                        },
                        debug: function() {
                            !k.silent && k.debug && (k.performance ? C.performance.log(arguments) : (C.debug = Function.prototype.bind.call(console.info, console, k.name + ":"), C.debug.apply(console, arguments)))
                        },
                        verbose: function() {
                            !k.silent && k.verbose && k.debug && (k.performance ? C.performance.log(arguments) : (C.verbose = Function.prototype.bind.call(console.info, console, k.name + ":"), C.verbose.apply(console, arguments)))
                        },
                        error: function() {
                            k.silent || (C.error = Function.prototype.bind.call(console.error, console, k.name + ":"), C.error.apply(console, arguments))
                        },
                        performance: {
                            log: function(e) {
                                var t, n, i;
                                k.performance && (t = (new Date).getTime(), i = c || t, n = t - i, c = t, u.push({
                                    Name: e[0],
                                    Arguments: [].slice.call(e, 1) || "",
                                    Element: Y,
                                    "Execution Time": n
                                })), clearTimeout(C.performance.timer), C.performance.timer = setTimeout(C.performance.display, 500)
                            },
                            display: function() {
                                var t = k.name + ":",
                                    n = 0;
                                c = !1, clearTimeout(C.performance.timer), e.each(u, function(e, t) {
                                    n += t["Execution Time"]
                                }), t += " " + n + "ms", s && (t += " '" + s + "'"), (void 0 !== console.group || void 0 !== console.table) && u.length > 0 && (console.table || e.each(u, function(e, t) {})), u = []
                            }
                        },
                        invoke: function(t, n, i) {
                            var r, a, s, l = G;
                            return n = n || p, i = Y || i, "string" == typeof t && void 0 !== l && (t = t.split(/[\. ]/), r = t.length - 1, e.each(t, function(n, i) {
                                var o = n != r ? i + t[n + 1].charAt(0).toUpperCase() + t[n + 1].slice(1) : t;
                                if (e.isPlainObject(l[o]) && n != r) l = l[o];
                                else {
                                    if (void 0 !== l[o]) return a = l[o], !1;
                                    if (!e.isPlainObject(l[i]) || n == r) return void 0 !== l[i] ? (a = l[i], !1) : (C.error(q.method, t), !1);
                                    l = l[i]
                                }
                            })), e.isFunction(a) ? s = a.apply(i, n) : void 0 !== a && (s = a), e.isArray(o) ? o.push(s) : void 0 !== o ? o = [o, s] : void 0 !== s && (o = s), a
                        }
                    }, f ? (void 0 === G && C.initialize(), C.invoke(d)) : (void 0 !== G && G.invoke("destroy"), C.initialize())
                }), void 0 !== o ? o : r
            }, e.fn.dropdown.settings = {
                silent: !1,
                debug: !1,
                verbose: !1,
                performance: !0,
                on: "click",
                action: "activate",
                apiSettings: !1,
                selectOnKeydown: !0,
                minCharacters: 0,
                filterRemoteData: !1,
                saveRemoteData: !0,
                throttle: 200,
                context: t,
                direction: "auto",
                keepOnScreen: !0,
                match: "both",
                fullTextSearch: !1,
                placeholder: "auto",
                preserveHTML: !0,
                sortSelect: !1,
                forceSelection: !0,
                allowAdditions: !1,
                hideAdditions: !0,
                maxSelections: !1,
                useLabels: !0,
                delimiter: ",",
                showOnFocus: !0,
                allowReselection: !1,
                allowTab: !0,
                allowCategorySelection: !1,
                fireOnInit: !1,
                transition: "auto",
                duration: 200,
                glyphWidth: 1.037,
                label: {
                    transition: "scale",
                    duration: 200,
                    variation: !1
                },
                delay: {
                    hide: 300,
                    show: 200,
                    search: 20,
                    touch: 50
                },
                onChange: function(e, t, n) {},
                onAdd: function(e, t, n) {},
                onRemove: function(e, t, n) {},
                onLabelSelect: function(e) {},
                onLabelCreate: function(t, n) {
                    return e(this)
                },
                onLabelRemove: function(e) {
                    return !0
                },
                onNoResults: function(e) {
                    return !0
                },
                onShow: function() {},
                onHide: function() {},
                name: "Dropdown",
                namespace: "dropdown",
                message: {
                    addResult: "Add <b>{term}</b>",
                    count: "{count} selected",
                    maxSelections: "Max {maxCount} selections",
                    noResults: "No results found.",
                    serverError: "There was an error contacting the server"
                },
                error: {
                    action: "You called a dropdown action that was not defined",
                    alreadySetup: "Once a select has been initialized behaviors must be called on the created ui dropdown",
                    labels: "Allowing user additions currently requires the use of labels.",
                    missingMultiple: "<select> requires multiple property to be set to correctly preserve multiple values",
                    method: "The method you called is not defined.",
                    noAPI: "The API module is required to load resources remotely",
                    noStorage: "Saving remote data requires session storage",
                    noTransition: "This module requires ui transitions <https://github.com/Semantic-Org/UI-Transition>"
                },
                regExp: {
                    escape: /[-[\]{}()*+?.,\\^$|#\s]/g,
                    quote: /"/g
                },
                metadata: {
                    defaultText: "defaultText",
                    defaultValue: "defaultValue",
                    placeholderText: "placeholder",
                    text: "text",
                    value: "value"
                },
                fields: {
                    remoteValues: "results",
                    values: "values",
                    disabled: "disabled",
                    name: "name",
                    value: "value",
                    text: "text"
                },
                keys: {
                    backspace: 8,
                    delimiter: 188,
                    deleteKey: 46,
                    enter: 13,
                    escape: 27,
                    pageUp: 33,
                    pageDown: 34,
                    leftArrow: 37,
                    upArrow: 38,
                    rightArrow: 39,
                    downArrow: 40
                },
                selector: {
                    addition: ".addition",
                    dropdown: ".ui.dropdown",
                    hidden: ".hidden",
                    icon: "> .dropdown.icon",
                    input: '> input[type="hidden"], > select',
                    item: ".item",
                    label: "> .label",
                    remove: "> .label > .delete.icon",
                    siblingLabel: ".label",
                    menu: ".menu",
                    message: ".message",
                    menuIcon: ".dropdown.icon",
                    search: "input.search, .menu > .search > input, .menu input.search",
                    sizer: "> input.sizer",
                    text: "> .text:not(.icon)",
                    unselectable: ".disabled, .filtered"
                },
                className: {
                    active: "active",
                    addition: "addition",
                    animating: "animating",
                    disabled: "disabled",
                    empty: "empty",
                    dropdown: "ui dropdown",
                    filtered: "filtered",
                    hidden: "hidden transition",
                    item: "item",
                    label: "ui label",
                    loading: "loading",
                    menu: "menu",
                    message: "message",
                    multiple: "multiple",
                    placeholder: "default",
                    sizer: "sizer",
                    search: "search",
                    selected: "selected",
                    selection: "selection",
                    upward: "upward",
                    visible: "visible"
                }
            }, e.fn.dropdown.settings.templates = {
                dropdown: function(t) {
                    var n = t.placeholder || !1,
                        i = (t.values, "");
                    return i += '<i class="dropdown icon"></i>', t.placeholder ? i += '<div class="default text">' + n + "</div>" : i += '<div class="text"></div>', i += '<div class="menu">', e.each(t.values, function(e, t) {
                        i += t.disabled ? '<div class="disabled item" data-value="' + t.value + '">' + t.name + "</div>" : '<div class="item" data-value="' + t.value + '">' + t.name + "</div>"
                    }), i += "</div>"
                },
                menu: function(t, n) {
                    var i = t[n.values] || {},
                        o = "";
                    return e.each(i, function(e, t) {
                        var i = t[n.text] ? 'data-text="' + t[n.text] + '"' : "",
                            r = t[n.disabled] ? "disabled " : "";
                        o += '<div class="' + r + 'item" data-value="' + t[n.value] + '"' + i + ">", o += t[n.name], o += "</div>"
                    }), o
                },
                label: function(e, t) {
                    return t + '<i class="delete icon"></i>'
                },
                message: function(e) {
                    return e
                },
                addition: function(e) {
                    return e
                }
            }
        }(jQuery, window, document),
        function(e, t, n, i) {
            "use strict";
            t = void 0 !== t && t.Math == Math ? t : "undefined" != typeof self && self.Math == Math ? self : Function("return this")(), e.fn.modal = function(i) {
                var o, r = e(this),
                    a = e(t),
                    s = e(n),
                    l = e("body"),
                    c = r.selector || "",
                    u = (new Date).getTime(),
                    d = [],
                    f = arguments[0],
                    p = "string" == typeof f,
                    h = [].slice.call(arguments, 1),
                    m = t.requestAnimationFrame || t.mozRequestAnimationFrame || t.webkitRequestAnimationFrame || t.msRequestAnimationFrame || function(e) {
                        setTimeout(e, 0)
                    };
                return r.each(function() {
                    var r, g, v, b, y, x, w, C, k, S = e.isPlainObject(i) ? e.extend(!0, {}, e.fn.modal.settings, i) : e.extend({}, e.fn.modal.settings),
                        T = S.selector,
                        A = S.className,
                        E = S.namespace,
                        D = S.error,
                        O = "." + E,
                        F = "module-" + E,
                        j = e(this),
                        q = e(S.context),
                        L = j.find(T.close),
                        N = this,
                        P = j.data(F),
                        R = !1;
                    k = {
                        initialize: function() {
                            k.verbose("Initializing dimmer", q), k.create.id(), k.create.dimmer(), k.refreshModals(), k.bind.events(), S.observeChanges && k.observeChanges(), k.instantiate()
                        },
                        instantiate: function() {
                            k.verbose("Storing instance of modal"), P = k, j.data(F, P)
                        },
                        create: {
                            dimmer: function() {
                                var t = {
                                        debug: S.debug,
                                        dimmerName: "modals",
                                        duration: {
                                            show: S.duration,
                                            hide: S.duration
                                        }
                                    },
                                    n = e.extend(!0, t, S.dimmerSettings);
                                if (S.inverted && (n.variation = void 0 !== n.variation ? n.variation + " inverted" : "inverted"), void 0 === e.fn.dimmer) return void k.error(D.dimmer);
                                k.debug("Creating dimmer with settings", n), b = q.dimmer(n), S.detachable ? (k.verbose("Modal is detachable, moving content into dimmer"), b.dimmer("add content", j)) : k.set.undetached(), S.blurring && b.addClass(A.blurring), y = b.dimmer("get dimmer")
                            },
                            id: function() {
                                w = (Math.random().toString(16) + "000000000").substr(2, 8), x = "." + w, k.verbose("Creating unique id for element", w)
                            }
                        },
                        destroy: function() {
                            k.verbose("Destroying previous modal"), j.removeData(F).off(O), a.off(x), y.off(x), L.off(O), q.dimmer("destroy")
                        },
                        observeChanges: function() {
                            "MutationObserver" in t && (C = new MutationObserver(function(e) {
                                k.debug("DOM tree modified, refreshing"), k.refresh()
                            }), C.observe(N, {
                                childList: !0,
                                subtree: !0
                            }), k.debug("Setting up mutation observer", C))
                        },
                        refresh: function() {
                            k.remove.scrolling(), k.cacheSizes(), k.set.screenHeight(), k.set.type(), k.set.position()
                        },
                        refreshModals: function() {
                            g = j.siblings(T.modal), r = g.add(j)
                        },
                        attachEvents: function(t, n) {
                            var i = e(t);
                            n = e.isFunction(k[n]) ? k[n] : k.toggle, i.length > 0 ? (k.debug("Attaching modal events to element", t, n), i.off(O).on("click" + O, n)) : k.error(D.notFound, t)
                        },
                        bind: {
                            events: function() {
                                k.verbose("Attaching events"), j.on("click" + O, T.close, k.event.close).on("click" + O, T.approve, k.event.approve).on("click" + O, T.deny, k.event.deny), a.on("resize" + x, k.event.resize)
                            }
                        },
                        get: {
                            id: function() {
                                return (Math.random().toString(16) + "000000000").substr(2, 8)
                            }
                        },
                        event: {
                            approve: function() {
                                if (R || !1 === S.onApprove.call(N, e(this))) return void k.verbose("Approve callback returned false cancelling hide");
                                R = !0, k.hide(function() {
                                    R = !1
                                })
                            },
                            deny: function() {
                                if (R || !1 === S.onDeny.call(N, e(this))) return void k.verbose("Deny callback returned false cancelling hide");
                                R = !0, k.hide(function() {
                                    R = !1
                                })
                            },
                            close: function() {
                                k.hide()
                            },
                            click: function(t) {
                                var i = e(t.target),
                                    o = i.closest(T.modal).length > 0,
                                    r = e.contains(n.documentElement, t.target);
                                !o && r && (k.debug("Dimmer clicked, hiding all modals"), k.is.active() && (k.remove.clickaway(), S.allowMultiple ? k.hide() : k.hideAll()))
                            },
                            debounce: function(e, t) {
                                clearTimeout(k.timer), k.timer = setTimeout(e, t)
                            },
                            keyboard: function(e) {
                                27 == e.which && (S.closable ? (k.debug("Escape key pressed hiding modal"), k.hide()) : k.debug("Escape key pressed, but closable is set to false"), e.preventDefault())
                            },
                            resize: function() {
                                b.dimmer("is active") && m(k.refresh)
                            }
                        },
                        toggle: function() {
                            k.is.active() || k.is.animating() ? k.hide() : k.show()
                        },
                        show: function(t) {
                            t = e.isFunction(t) ? t : function() {}, k.refreshModals(), k.showModal(t)
                        },
                        hide: function(t) {
                            t = e.isFunction(t) ? t : function() {}, k.refreshModals(), k.hideModal(t)
                        },
                        showModal: function(t) {
                            t = e.isFunction(t) ? t : function() {}, k.is.animating() || !k.is.active() ? (k.showDimmer(), k.cacheSizes(), k.set.position(), k.set.screenHeight(), k.set.type(), k.set.clickaway(), !S.allowMultiple && k.others.active() ? k.hideOthers(k.showModal) : (S.onShow.call(N), S.transition && void 0 !== e.fn.transition && j.transition("is supported") ? (k.debug("Showing modal with css animations"), j.transition({
                                debug: S.debug,
                                animation: S.transition + " in",
                                queue: S.queue,
                                duration: S.duration,
                                useFailSafe: !0,
                                onComplete: function() {
                                    S.onVisible.apply(N), S.keyboardShortcuts && k.add.keyboardShortcuts(), k.save.focus(), k.set.active(), S.autofocus && k.set.autofocus(), t()
                                }
                            })) : k.error(D.noTransition))) : k.debug("Modal is already visible")
                        },
                        hideModal: function(t, n) {
                            if (t = e.isFunction(t) ? t : function() {}, k.debug("Hiding modal"), !1 === S.onHide.call(N, e(this))) return void k.verbose("Hide callback returned false cancelling hide");
                            (k.is.animating() || k.is.active()) && (S.transition && void 0 !== e.fn.transition && j.transition("is supported") ? (k.remove.active(), j.transition({
                                debug: S.debug,
                                animation: S.transition + " out",
                                queue: S.queue,
                                duration: S.duration,
                                useFailSafe: !0,
                                onStart: function() {
                                    k.others.active() || n || k.hideDimmer(), S.keyboardShortcuts && k.remove.keyboardShortcuts()
                                },
                                onComplete: function() {
                                    S.onHidden.call(N), k.restore.focus(), t()
                                }
                            })) : k.error(D.noTransition))
                        },
                        showDimmer: function() {
                            b.dimmer("is animating") || !b.dimmer("is active") ? (k.debug("Showing dimmer"), b.dimmer("show")) : k.debug("Dimmer already visible")
                        },
                        hideDimmer: function() {
                            if (!b.dimmer("is animating") && !b.dimmer("is active")) return void k.debug("Dimmer is not visible cannot hide");
                            b.dimmer("hide", function() {
                                k.remove.clickaway(), k.remove.screenHeight()
                            })
                        },
                        hideAll: function(t) {
                            var n = r.filter("." + A.active + ", ." + A.animating);
                            t = e.isFunction(t) ? t : function() {}, n.length > 0 && (k.debug("Hiding all visible modals"), k.hideDimmer(), n.modal("hide modal", t))
                        },
                        hideOthers: function(t) {
                            var n = g.filter("." + A.active + ", ." + A.animating);
                            t = e.isFunction(t) ? t : function() {}, n.length > 0 && (k.debug("Hiding other modals", g), n.modal("hide modal", t, !0))
                        },
                        others: {
                            active: function() {
                                return g.filter("." + A.active).length > 0
                            },
                            animating: function() {
                                return g.filter("." + A.animating).length > 0
                            }
                        },
                        add: {
                            keyboardShortcuts: function() {
                                k.verbose("Adding keyboard shortcuts"), s.on("keyup" + O, k.event.keyboard)
                            }
                        },
                        save: {
                            focus: function() {
                                v = e(n.activeElement).blur()
                            }
                        },
                        restore: {
                            focus: function() {
                                v && v.length > 0 && v.focus()
                            }
                        },
                        remove: {
                            active: function() {
                                j.removeClass(A.active)
                            },
                            clickaway: function() {
                                S.closable && y.off("click" + x)
                            },
                            bodyStyle: function() {
                                "" === l.attr("style") && (k.verbose("Removing style attribute"), l.removeAttr("style"))
                            },
                            screenHeight: function() {
                                k.debug("Removing page height"), l.css("height", "")
                            },
                            keyboardShortcuts: function() {
                                k.verbose("Removing keyboard shortcuts"), s.off("keyup" + O)
                            },
                            scrolling: function() {
                                b.removeClass(A.scrolling), j.removeClass(A.scrolling)
                            }
                        },
                        cacheSizes: function() {
                            var i = j.outerHeight();
                            void 0 !== k.cache && 0 === i || (k.cache = {
                                pageHeight: e(n).outerHeight(),
                                height: i + S.offset,
                                contextHeight: "body" == S.context ? e(t).height() : b.height()
                            }), k.debug("Caching modal and container sizes", k.cache)
                        },
                        can: {
                            fit: function() {
                                return k.cache.height + 2 * S.padding < k.cache.contextHeight
                            }
                        },
                        is: {
                            active: function() {
                                return j.hasClass(A.active)
                            },
                            animating: function() {
                                return j.transition("is supported") ? j.transition("is animating") : j.is(":visible")
                            },
                            scrolling: function() {
                                return b.hasClass(A.scrolling)
                            },
                            modernBrowser: function() {
                                return !(t.ActiveXObject || "ActiveXObject" in t)
                            }
                        },
                        set: {
                            autofocus: function() {
                                var e = j.find("[tabindex], :input").filter(":visible"),
                                    t = e.filter("[autofocus]"),
                                    n = t.length > 0 ? t.first() : e.first();
                                n.length > 0 && n.focus()
                            },
                            clickaway: function() {
                                S.closable && y.on("click" + x, k.event.click)
                            },
                            screenHeight: function() {
                                k.can.fit() ? l.css("height", "") : (k.debug("Modal is taller than page content, resizing page height"), l.css("height", k.cache.height + 2 * S.padding))
                            },
                            active: function() {
                                j.addClass(A.active)
                            },
                            scrolling: function() {
                                b.addClass(A.scrolling), j.addClass(A.scrolling)
                            },
                            type: function() {
                                k.can.fit() ? (k.verbose("Modal fits on screen"), k.others.active() || k.others.animating() || k.remove.scrolling()) : (k.verbose("Modal cannot fit on screen setting to scrolling"), k.set.scrolling())
                            },
                            position: function() {
                                k.verbose("Centering modal on page", k.cache), k.can.fit() ? j.css({
                                    top: "",
                                    marginTop: -k.cache.height / 2
                                }) : j.css({
                                    marginTop: "",
                                    top: s.scrollTop()
                                })
                            },
                            undetached: function() {
                                b.addClass(A.undetached)
                            }
                        },
                        setting: function(t, n) {
                            if (k.debug("Changing setting", t, n), e.isPlainObject(t)) e.extend(!0, S, t);
                            else {
                                if (void 0 === n) return S[t];
                                e.isPlainObject(S[t]) ? e.extend(!0, S[t], n) : S[t] = n
                            }
                        },
                        internal: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, k, t);
                            else {
                                if (void 0 === n) return k[t];
                                k[t] = n
                            }
                        },
                        debug: function() {
                            !S.silent && S.debug && (S.performance ? k.performance.log(arguments) : (k.debug = Function.prototype.bind.call(console.info, console, S.name + ":"), k.debug.apply(console, arguments)))
                        },
                        verbose: function() {
                            !S.silent && S.verbose && S.debug && (S.performance ? k.performance.log(arguments) : (k.verbose = Function.prototype.bind.call(console.info, console, S.name + ":"), k.verbose.apply(console, arguments)))
                        },
                        error: function() {
                            S.silent || (k.error = Function.prototype.bind.call(console.error, console, S.name + ":"), k.error.apply(console, arguments))
                        },
                        performance: {
                            log: function(e) {
                                var t, n, i;
                                S.performance && (t = (new Date).getTime(), i = u || t, n = t - i, u = t, d.push({
                                    Name: e[0],
                                    Arguments: [].slice.call(e, 1) || "",
                                    Element: N,
                                    "Execution Time": n
                                })), clearTimeout(k.performance.timer), k.performance.timer = setTimeout(k.performance.display, 500)
                            },
                            display: function() {
                                var t = S.name + ":",
                                    n = 0;
                                u = !1, clearTimeout(k.performance.timer), e.each(d, function(e, t) {
                                    n += t["Execution Time"]
                                }), t += " " + n + "ms", c && (t += " '" + c + "'"), (void 0 !== console.group || void 0 !== console.table) && d.length > 0 && (console.table || e.each(d, function(e, t) {})), d = []
                            }
                        },
                        invoke: function(t, n, i) {
                            var r, a, s, l = P;
                            return n = n || h, i = N || i, "string" == typeof t && void 0 !== l && (t = t.split(/[\. ]/), r = t.length - 1, e.each(t, function(n, i) {
                                var o = n != r ? i + t[n + 1].charAt(0).toUpperCase() + t[n + 1].slice(1) : t;
                                if (e.isPlainObject(l[o]) && n != r) l = l[o];
                                else {
                                    if (void 0 !== l[o]) return a = l[o], !1;
                                    if (!e.isPlainObject(l[i]) || n == r) return void 0 !== l[i] && (a = l[i], !1);
                                    l = l[i]
                                }
                            })), e.isFunction(a) ? s = a.apply(i, n) : void 0 !== a && (s = a), e.isArray(o) ? o.push(s) : void 0 !== o ? o = [o, s] : void 0 !== s && (o = s), a
                        }
                    }, p ? (void 0 === P && k.initialize(), k.invoke(f)) : (void 0 !== P && P.invoke("destroy"), k.initialize())
                }), void 0 !== o ? o : this
            }, e.fn.modal.settings = {
                name: "Modal",
                namespace: "modal",
                silent: !1,
                debug: !1,
                verbose: !1,
                performance: !0,
                observeChanges: !1,
                allowMultiple: !1,
                detachable: !0,
                closable: !0,
                autofocus: !0,
                inverted: !1,
                blurring: !1,
                dimmerSettings: {
                    closable: !1,
                    useCSS: !0
                },
                keyboardShortcuts: !0,
                context: "body",
                queue: !1,
                duration: 500,
                offset: 0,
                transition: "scale",
                padding: 50,
                onShow: function() {},
                onVisible: function() {},
                onHide: function() {
                    return !0
                },
                onHidden: function() {},
                onApprove: function() {
                    return !0
                },
                onDeny: function() {
                    return !0
                },
                selector: {
                    close: "> .close",
                    approve: ".actions .positive, .actions .approve, .actions .ok",
                    deny: ".actions .negative, .actions .deny, .actions .cancel",
                    modal: ".ui.modal"
                },
                error: {
                    dimmer: "UI Dimmer, a required component is not included in this page",
                    method: "The method you called is not defined.",
                    notFound: "The element you specified could not be found"
                },
                className: {
                    active: "active",
                    animating: "animating",
                    blurring: "blurring",
                    scrolling: "scrolling",
                    undetached: "undetached"
                }
            }
        }(jQuery, window, document),
        function(e, t, i, o) {
            "use strict";
            t = void 0 !== t && t.Math == Math ? t : "undefined" != typeof self && self.Math == Math ? self : Function("return this")(), e.fn.popup = function(o) {
                var r, a = e(this),
                    s = e(i),
                    l = e(t),
                    c = e("body"),
                    u = a.selector || "",
                    d = (new Date).getTime(),
                    f = [],
                    p = arguments[0],
                    h = "string" == typeof p,
                    m = [].slice.call(arguments, 1);
                return a.each(function() {
                    var a, g, v, b, y, x, w = e.isPlainObject(o) ? e.extend(!0, {}, e.fn.popup.settings, o) : e.extend({}, e.fn.popup.settings),
                        C = w.selector,
                        k = w.className,
                        S = w.error,
                        T = w.metadata,
                        A = w.namespace,
                        E = "." + w.namespace,
                        D = "module-" + A,
                        O = e(this),
                        F = e(w.context),
                        j = e(w.scrollContext),
                        q = e(w.boundary),
                        L = w.target ? e(w.target) : O,
                        N = 0,
                        P = !1,
                        R = !1,
                        I = this,
                        M = O.data(D);
                    x = {
                        initialize: function() {
                            x.debug("Initializing", O), x.createID(), x.bind.events(), !x.exists() && w.preserve && x.create(), w.observeChanges && x.observeChanges(), x.instantiate()
                        },
                        instantiate: function() {
                            x.verbose("Storing instance", x), M = x, O.data(D, M)
                        },
                        observeChanges: function() {
                            "MutationObserver" in t && (v = new MutationObserver(x.event.documentChanged), v.observe(i, {
                                childList: !0,
                                subtree: !0
                            }), x.debug("Setting up mutation observer", v))
                        },
                        refresh: function() {
                            w.popup ? a = e(w.popup).eq(0) : w.inline && (a = L.nextAll(C.popup).eq(0), w.popup = a), w.popup ? (a.addClass(k.loading), g = x.get.offsetParent(), a.removeClass(k.loading), w.movePopup && x.has.popup() && x.get.offsetParent(a)[0] !== g[0] && (x.debug("Moving popup to the same offset parent as activating element"), a.detach().appendTo(g))) : g = w.inline ? x.get.offsetParent(L) : x.has.popup() ? x.get.offsetParent(a) : c, g.is("html") && g[0] !== c[0] && (x.debug("Setting page as offset parent"), g = c), x.get.variation() && x.set.variation()
                        },
                        reposition: function() {
                            x.refresh(), x.set.position()
                        },
                        destroy: function() {
                            x.debug("Destroying previous module"), v && v.disconnect(), a && !w.preserve && x.removePopup(), clearTimeout(x.hideTimer), clearTimeout(x.showTimer), x.unbind.close(), x.unbind.events(), O.removeData(D)
                        },
                        event: {
                            start: function(t) {
                                var n = e.isPlainObject(w.delay) ? w.delay.show : w.delay;
                                clearTimeout(x.hideTimer), R || (x.showTimer = setTimeout(x.show, n))
                            },
                            end: function() {
                                var t = e.isPlainObject(w.delay) ? w.delay.hide : w.delay;
                                clearTimeout(x.showTimer), x.hideTimer = setTimeout(x.hide, t)
                            },
                            touchstart: function(e) {
                                R = !0, x.show()
                            },
                            resize: function() {
                                x.is.visible() && x.set.position()
                            },
                            documentChanged: function(t) {
                                [].forEach.call(t, function(t) {
                                    t.removedNodes && [].forEach.call(t.removedNodes, function(t) {
                                        (t == I || e(t).find(I).length > 0) && (x.debug("Element removed from DOM, tearing down events"), x.destroy())
                                    })
                                })
                            },
                            hideGracefully: function(t) {
                                var n = e(t.target),
                                    o = e.contains(i.documentElement, t.target),
                                    r = n.closest(C.popup).length > 0;
                                t && !r && o ? (x.debug("Click occurred outside popup hiding popup"), x.hide()) : x.debug("Click was inside popup, keeping popup open")
                            }
                        },
                        create: function() {
                            var t = x.get.html(),
                                n = x.get.title(),
                                i = x.get.content();
                            t || i || n ? (x.debug("Creating pop-up html"), t || (t = w.templates.popup({
                                title: n,
                                content: i
                            })), a = e("<div/>").addClass(k.popup).data(T.activator, O).html(t), w.inline ? (x.verbose("Inserting popup element inline", a), a.insertAfter(O)) : (x.verbose("Appending popup element to body", a), a.appendTo(F)), x.refresh(), x.set.variation(), w.hoverable && x.bind.popup(), w.onCreate.call(a, I)) : 0 !== L.next(C.popup).length ? (x.verbose("Pre-existing popup found"), w.inline = !0, w.popup = L.next(C.popup).data(T.activator, O), x.refresh(), w.hoverable && x.bind.popup()) : w.popup ? (e(w.popup).data(T.activator, O), x.verbose("Used popup specified in settings"), x.refresh(), w.hoverable && x.bind.popup()) : x.debug("No content specified skipping display", I)
                        },
                        createID: function() {
                            y = (Math.random().toString(16) + "000000000").substr(2, 8), b = "." + y, x.verbose("Creating unique id for element", y)
                        },
                        toggle: function() {
                            x.debug("Toggling pop-up"), x.is.hidden() ? (x.debug("Popup is hidden, showing pop-up"), x.unbind.close(), x.show()) : (x.debug("Popup is visible, hiding pop-up"), x.hide())
                        },
                        show: function(e) {
                            if (e = e || function() {}, x.debug("Showing pop-up", w.transition), x.is.hidden() && (!x.is.active() || !x.is.dropdown())) {
                                if (x.exists() || x.create(), !1 === w.onShow.call(a, I)) return void x.debug("onShow callback returned false, cancelling popup animation");
                                w.preserve || w.popup || x.refresh(), a && x.set.position() && (x.save.conditions(), w.exclusive && x.hideAll(), x.animate.show(e))
                            }
                        },
                        hide: function(e) {
                            if (e = e || function() {}, x.is.visible() || x.is.animating()) {
                                if (!1 === w.onHide.call(a, I)) return void x.debug("onHide callback returned false, cancelling popup animation");
                                x.remove.visible(), x.unbind.close(), x.restore.conditions(), x.animate.hide(e)
                            }
                        },
                        hideAll: function() {
                            e(C.popup).filter("." + k.visible).each(function() {
                                e(this).data(T.activator).popup("hide")
                            })
                        },
                        exists: function() {
                            return !!a && (w.inline || w.popup ? x.has.popup() : a.closest(F).length >= 1)
                        },
                        removePopup: function() {
                            x.has.popup() && !w.popup && (x.debug("Removing popup", a), a.remove(), a = void 0, w.onRemove.call(a, I))
                        },
                        save: {
                            conditions: function() {
                                x.cache = {
                                    title: O.attr("title")
                                }, x.cache.title && O.removeAttr("title"), x.verbose("Saving original attributes", x.cache.title)
                            }
                        },
                        restore: {
                            conditions: function() {
                                return x.cache && x.cache.title && (O.attr("title", x.cache.title), x.verbose("Restoring original attributes", x.cache.title)), !0
                            }
                        },
                        supports: {
                            svg: function() {
                                return void 0 === ("undefined" == typeof SVGGraphicsElement ? "undefined" : n(SVGGraphicsElement))
                            }
                        },
                        animate: {
                            show: function(t) {
                                t = e.isFunction(t) ? t : function() {}, w.transition && void 0 !== e.fn.transition && O.transition("is supported") ? (x.set.visible(), a.transition({
                                    animation: w.transition + " in",
                                    queue: !1,
                                    debug: w.debug,
                                    verbose: w.verbose,
                                    duration: w.duration,
                                    onComplete: function() {
                                        x.bind.close(), t.call(a, I), w.onVisible.call(a, I)
                                    }
                                })) : x.error(S.noTransition)
                            },
                            hide: function(t) {
                                if (t = e.isFunction(t) ? t : function() {}, x.debug("Hiding pop-up"), !1 === w.onHide.call(a, I)) return void x.debug("onHide callback returned false, cancelling popup animation");
                                w.transition && void 0 !== e.fn.transition && O.transition("is supported") ? a.transition({
                                    animation: w.transition + " out",
                                    queue: !1,
                                    duration: w.duration,
                                    debug: w.debug,
                                    verbose: w.verbose,
                                    onComplete: function() {
                                        x.reset(), t.call(a, I), w.onHidden.call(a, I)
                                    }
                                }) : x.error(S.noTransition)
                            }
                        },
                        change: {
                            content: function(e) {
                                a.html(e)
                            }
                        },
                        get: {
                            html: function() {
                                return O.removeData(T.html), O.data(T.html) || w.html
                            },
                            title: function() {
                                return O.removeData(T.title), O.data(T.title) || w.title
                            },
                            content: function() {
                                return O.removeData(T.content), O.data(T.content) || O.attr("title") || w.content
                            },
                            variation: function() {
                                return O.removeData(T.variation), O.data(T.variation) || w.variation
                            },
                            popup: function() {
                                return a
                            },
                            popupOffset: function() {
                                return a.offset()
                            },
                            calculations: function() {
                                var e, n = L[0],
                                    i = q[0] == t,
                                    o = w.inline || w.popup && w.movePopup ? L.position() : L.offset(),
                                    r = i ? {
                                        top: 0,
                                        left: 0
                                    } : q.offset(),
                                    s = {},
                                    c = i ? {
                                        top: l.scrollTop(),
                                        left: l.scrollLeft()
                                    } : {
                                        top: 0,
                                        left: 0
                                    };
                                return s = {
                                    target: {
                                        element: L[0],
                                        width: L.outerWidth(),
                                        height: L.outerHeight(),
                                        top: o.top,
                                        left: o.left,
                                        margin: {}
                                    },
                                    popup: {
                                        width: a.outerWidth(),
                                        height: a.outerHeight()
                                    },
                                    parent: {
                                        width: g.outerWidth(),
                                        height: g.outerHeight()
                                    },
                                    screen: {
                                        top: r.top,
                                        left: r.left,
                                        scroll: {
                                            top: c.top,
                                            left: c.left
                                        },
                                        width: q.width(),
                                        height: q.height()
                                    }
                                }, w.setFluidWidth && x.is.fluid() && (s.container = {
                                    width: a.parent().outerWidth()
                                }, s.popup.width = s.container.width), s.target.margin.top = w.inline ? parseInt(t.getComputedStyle(n).getPropertyValue("margin-top"), 10) : 0, s.target.margin.left = w.inline ? x.is.rtl() ? parseInt(t.getComputedStyle(n).getPropertyValue("margin-right"), 10) : parseInt(t.getComputedStyle(n).getPropertyValue("margin-left"), 10) : 0, e = s.screen, s.boundary = {
                                    top: e.top + e.scroll.top,
                                    bottom: e.top + e.scroll.top + e.height,
                                    left: e.left + e.scroll.left,
                                    right: e.left + e.scroll.left + e.width
                                }, s
                            },
                            id: function() {
                                return y
                            },
                            startEvent: function() {
                                return "hover" == w.on ? "mouseenter" : "focus" == w.on && "focus"
                            },
                            scrollEvent: function() {
                                return "scroll"
                            },
                            endEvent: function() {
                                return "hover" == w.on ? "mouseleave" : "focus" == w.on && "blur"
                            },
                            distanceFromBoundary: function(e, t) {
                                var n, i, o = {};
                                return t = t || x.get.calculations(), n = t.popup, i = t.boundary, e && (o = {
                                    top: e.top - i.top,
                                    left: e.left - i.left,
                                    right: i.right - (e.left + n.width),
                                    bottom: i.bottom - (e.top + n.height)
                                }, x.verbose("Distance from boundaries determined", e, o)), o
                            },
                            offsetParent: function(t) {
                                var n = void 0 !== t ? t[0] : O[0],
                                    i = n.parentNode,
                                    o = e(i);
                                if (i)
                                    for (var r = "none" === o.css("transform"), a = "static" === o.css("position"), s = o.is("html"); i && !s && a && r;) i = i.parentNode, o = e(i), r = "none" === o.css("transform"), a = "static" === o.css("position"), s = o.is("html");
                                return o && o.length > 0 ? o : e()
                            },
                            positions: function() {
                                return {
                                    "top left": !1,
                                    "top center": !1,
                                    "top right": !1,
                                    "bottom left": !1,
                                    "bottom center": !1,
                                    "bottom right": !1,
                                    "left center": !1,
                                    "right center": !1
                                }
                            },
                            nextPosition: function(e) {
                                var t = e.split(" "),
                                    n = t[0],
                                    i = t[1],
                                    o = {
                                        top: "bottom",
                                        bottom: "top",
                                        left: "right",
                                        right: "left"
                                    },
                                    r = {
                                        left: "center",
                                        center: "right",
                                        right: "left"
                                    },
                                    a = {
                                        "top left": "top center",
                                        "top center": "top right",
                                        "top right": "right center",
                                        "right center": "bottom right",
                                        "bottom right": "bottom center",
                                        "bottom center": "bottom left",
                                        "bottom left": "left center",
                                        "left center": "top left"
                                    },
                                    s = "top" == n || "bottom" == n,
                                    l = !1,
                                    c = !1,
                                    u = !1;
                                return P || (x.verbose("All available positions available"), P = x.get.positions()), x.debug("Recording last position tried", e), P[e] = !0, "opposite" === w.prefer && (u = [o[n], i], u = u.join(" "), l = !0 === P[u], x.debug("Trying opposite strategy", u)), "adjacent" === w.prefer && s && (u = [n, r[i]], u = u.join(" "), c = !0 === P[u], x.debug("Trying adjacent strategy", u)), (c || l) && (x.debug("Using backup position", u), u = a[e]), u
                            }
                        },
                        set: {
                            position: function(e, t) {
                                if (0 === L.length || 0 === a.length) return void x.error(S.notFound);
                                var n, i, o, r, s, l, c, u;
                                if (t = t || x.get.calculations(), e = e || O.data(T.position) || w.position, n = O.data(T.offset) || w.offset, i = w.distanceAway, o = t.target, r = t.popup, s = t.parent, 0 === o.width && 0 === o.height && !x.is.svg(o.element)) return x.debug("Popup target is hidden, no action taken"), !1;
                                switch (w.inline && (x.debug("Adding margin to calculation", o.margin), "left center" == e || "right center" == e ? (n += o.margin.top, i += -o.margin.left) : "top left" == e || "top center" == e || "top right" == e ? (n += o.margin.left, i -= o.margin.top) : (n += o.margin.left, i += o.margin.top)), x.debug("Determining popup position from calculations", e, t), x.is.rtl() && (e = e.replace(/left|right/g, function(e) {
                                    return "left" == e ? "right" : "left"
                                }), x.debug("RTL: Popup position updated", e)), N == w.maxSearchDepth && "string" == typeof w.lastResort && (e = w.lastResort), e) {
                                    case "top left":
                                        l = {
                                            top: "auto",
                                            bottom: s.height - o.top + i,
                                            left: o.left + n,
                                            right: "auto"
                                        };
                                        break;
                                    case "top center":
                                        l = {
                                            bottom: s.height - o.top + i,
                                            left: o.left + o.width / 2 - r.width / 2 + n,
                                            top: "auto",
                                            right: "auto"
                                        };
                                        break;
                                    case "top right":
                                        l = {
                                            bottom: s.height - o.top + i,
                                            right: s.width - o.left - o.width - n,
                                            top: "auto",
                                            left: "auto"
                                        };
                                        break;
                                    case "left center":
                                        l = {
                                            top: o.top + o.height / 2 - r.height / 2 + n,
                                            right: s.width - o.left + i,
                                            left: "auto",
                                            bottom: "auto"
                                        };
                                        break;
                                    case "right center":
                                        l = {
                                            top: o.top + o.height / 2 - r.height / 2 + n,
                                            left: o.left + o.width + i,
                                            bottom: "auto",
                                            right: "auto"
                                        };
                                        break;
                                    case "bottom left":
                                        l = {
                                            top: o.top + o.height + i,
                                            left: o.left + n,
                                            bottom: "auto",
                                            right: "auto"
                                        };
                                        break;
                                    case "bottom center":
                                        l = {
                                            top: o.top + o.height + i,
                                            left: o.left + o.width / 2 - r.width / 2 + n,
                                            bottom: "auto",
                                            right: "auto"
                                        };
                                        break;
                                    case "bottom right":
                                        l = {
                                            top: o.top + o.height + i,
                                            right: s.width - o.left - o.width - n,
                                            left: "auto",
                                            bottom: "auto"
                                        }
                                }
                                if (void 0 === l && x.error(S.invalidPosition, e), x.debug("Calculated popup positioning values", l), a.css(l).removeClass(k.position).addClass(e).addClass(k.loading), c = x.get.popupOffset(), u = x.get.distanceFromBoundary(c, t), x.is.offstage(u, e)) {
                                    if (x.debug("Position is outside viewport", e), N < w.maxSearchDepth) return N++, e = x.get.nextPosition(e), x.debug("Trying new position", e), !!a && x.set.position(e, t);
                                    if (!w.lastResort) return x.debug("Popup could not find a position to display", a), x.error(S.cannotPlace, I), x.remove.attempts(), x.remove.loading(), x.reset(), w.onUnplaceable.call(a, I), !1;
                                    x.debug("No position found, showing with last position")
                                }
                                return x.debug("Position is on stage", e), x.remove.attempts(), x.remove.loading(), w.setFluidWidth && x.is.fluid() && x.set.fluidWidth(t), !0
                            },
                            fluidWidth: function(e) {
                                e = e || x.get.calculations(), x.debug("Automatically setting element width to parent width", e.parent.width), a.css("width", e.container.width)
                            },
                            variation: function(e) {
                                (e = e || x.get.variation()) && x.has.popup() && (x.verbose("Adding variation to popup", e), a.addClass(e))
                            },
                            visible: function() {
                                O.addClass(k.visible)
                            }
                        },
                        remove: {
                            loading: function() {
                                a.removeClass(k.loading)
                            },
                            variation: function(e) {
                                (e = e || x.get.variation()) && (x.verbose("Removing variation", e), a.removeClass(e))
                            },
                            visible: function() {
                                O.removeClass(k.visible)
                            },
                            attempts: function() {
                                x.verbose("Resetting all searched positions"), N = 0, P = !1
                            }
                        },
                        bind: {
                            events: function() {
                                x.debug("Binding popup events to module"), "click" == w.on && O.on("click" + E, x.toggle), "hover" == w.on && O.on("touchstart" + E, x.event.touchstart), x.get.startEvent() && O.on(x.get.startEvent() + E, x.event.start).on(x.get.endEvent() + E, x.event.end), w.target && x.debug("Target set to element", L), l.on("resize" + b, x.event.resize)
                            },
                            popup: function() {
                                x.verbose("Allowing hover events on popup to prevent closing"), a && x.has.popup() && a.on("mouseenter" + E, x.event.start).on("mouseleave" + E, x.event.end)
                            },
                            close: function() {
                                (!0 === w.hideOnScroll || "auto" == w.hideOnScroll && "click" != w.on) && j.one(x.get.scrollEvent() + b, x.event.hideGracefully), "hover" == w.on && R && (x.verbose("Binding popup close event to document"), s.on("touchstart" + b, function(e) {
                                    x.verbose("Touched away from popup"), x.event.hideGracefully.call(I, e)
                                })), "click" == w.on && w.closable && (x.verbose("Binding popup close event to document"), s.on("click" + b, function(e) {
                                    x.verbose("Clicked away from popup"), x.event.hideGracefully.call(I, e)
                                }))
                            }
                        },
                        unbind: {
                            events: function() {
                                l.off(b), O.off(E)
                            },
                            close: function() {
                                s.off(b), j.off(b)
                            }
                        },
                        has: {
                            popup: function() {
                                return a && a.length > 0
                            }
                        },
                        is: {
                            offstage: function(t, n) {
                                var i = [];
                                return e.each(t, function(e, t) {
                                    t < -w.jitter && (x.debug("Position exceeds allowable distance from edge", e, t, n), i.push(e))
                                }), i.length > 0
                            },
                            svg: function(e) {
                                return x.supports.svg() && e instanceof SVGGraphicsElement
                            },
                            active: function() {
                                return O.hasClass(k.active)
                            },
                            animating: function() {
                                return void 0 !== a && a.hasClass(k.animating)
                            },
                            fluid: function() {
                                return void 0 !== a && a.hasClass(k.fluid)
                            },
                            visible: function() {
                                return void 0 !== a && a.hasClass(k.visible)
                            },
                            dropdown: function() {
                                return O.hasClass(k.dropdown)
                            },
                            hidden: function() {
                                return !x.is.visible()
                            },
                            rtl: function() {
                                return "rtl" == O.css("direction")
                            }
                        },
                        reset: function() {
                            x.remove.visible(), w.preserve ? void 0 !== e.fn.transition && a.transition("remove transition") : x.removePopup()
                        },
                        setting: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, w, t);
                            else {
                                if (void 0 === n) return w[t];
                                w[t] = n
                            }
                        },
                        internal: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, x, t);
                            else {
                                if (void 0 === n) return x[t];
                                x[t] = n
                            }
                        },
                        debug: function() {
                            !w.silent && w.debug && (w.performance ? x.performance.log(arguments) : (x.debug = Function.prototype.bind.call(console.info, console, w.name + ":"), x.debug.apply(console, arguments)))
                        },
                        verbose: function() {
                            !w.silent && w.verbose && w.debug && (w.performance ? x.performance.log(arguments) : (x.verbose = Function.prototype.bind.call(console.info, console, w.name + ":"), x.verbose.apply(console, arguments)))
                        },
                        error: function() {
                            w.silent || (x.error = Function.prototype.bind.call(console.error, console, w.name + ":"), x.error.apply(console, arguments))
                        },
                        performance: {
                            log: function(e) {
                                var t, n, i;
                                w.performance && (t = (new Date).getTime(), i = d || t, n = t - i, d = t, f.push({
                                    Name: e[0],
                                    Arguments: [].slice.call(e, 1) || "",
                                    Element: I,
                                    "Execution Time": n
                                })), clearTimeout(x.performance.timer), x.performance.timer = setTimeout(x.performance.display, 500)
                            },
                            display: function() {
                                var t = w.name + ":",
                                    n = 0;
                                d = !1, clearTimeout(x.performance.timer), e.each(f, function(e, t) {
                                    n += t["Execution Time"]
                                }), t += " " + n + "ms", u && (t += " '" + u + "'"), (void 0 !== console.group || void 0 !== console.table) && f.length > 0 && (console.table || e.each(f, function(e, t) {})), f = []
                            }
                        },
                        invoke: function(t, n, i) {
                            var o, a, s, l = M;
                            return n = n || m, i = I || i, "string" == typeof t && void 0 !== l && (t = t.split(/[\. ]/), o = t.length - 1, e.each(t, function(n, i) {
                                var r = n != o ? i + t[n + 1].charAt(0).toUpperCase() + t[n + 1].slice(1) : t;
                                if (e.isPlainObject(l[r]) && n != o) l = l[r];
                                else {
                                    if (void 0 !== l[r]) return a = l[r], !1;
                                    if (!e.isPlainObject(l[i]) || n == o) return void 0 !== l[i] && (a = l[i], !1);
                                    l = l[i]
                                }
                            })), e.isFunction(a) ? s = a.apply(i, n) : void 0 !== a && (s = a), e.isArray(r) ? r.push(s) : void 0 !== r ? r = [r, s] : void 0 !== s && (r = s), a
                        }
                    }, h ? (void 0 === M && x.initialize(), x.invoke(p)) : (void 0 !== M && M.invoke("destroy"), x.initialize())
                }), void 0 !== r ? r : this
            }, e.fn.popup.settings = {
                name: "Popup",
                silent: !1,
                debug: !1,
                verbose: !1,
                performance: !0,
                namespace: "popup",
                observeChanges: !0,
                onCreate: function() {},
                onRemove: function() {},
                onShow: function() {},
                onVisible: function() {},
                onHide: function() {},
                onUnplaceable: function() {},
                onHidden: function() {},
                on: "hover",
                boundary: t,
                addTouchEvents: !0,
                position: "top left",
                variation: "",
                movePopup: !0,
                target: !1,
                popup: !1,
                inline: !1,
                preserve: !1,
                hoverable: !1,
                content: !1,
                html: !1,
                title: !1,
                closable: !0,
                hideOnScroll: "auto",
                exclusive: !1,
                context: "body",
                scrollContext: t,
                prefer: "opposite",
                lastResort: !1,
                delay: {
                    show: 50,
                    hide: 70
                },
                setFluidWidth: !0,
                duration: 200,
                transition: "scale",
                distanceAway: 0,
                jitter: 2,
                offset: 0,
                maxSearchDepth: 15,
                error: {
                    invalidPosition: "The position you specified is not a valid position",
                    cannotPlace: "Popup does not fit within the boundaries of the viewport",
                    method: "The method you called is not defined.",
                    noTransition: "This module requires ui transitions <https://github.com/Semantic-Org/UI-Transition>",
                    notFound: "The target or popup you specified does not exist on the page"
                },
                metadata: {
                    activator: "activator",
                    content: "content",
                    html: "html",
                    offset: "offset",
                    position: "position",
                    title: "title",
                    variation: "variation"
                },
                className: {
                    active: "active",
                    animating: "animating",
                    dropdown: "dropdown",
                    fluid: "fluid",
                    loading: "loading",
                    popup: "ui popup",
                    position: "top left center bottom right",
                    visible: "visible"
                },
                selector: {
                    popup: ".ui.popup"
                },
                templates: {
                    escape: function(e) {
                        var t = /[&<>"'`]/g,
                            n = /[&<>"'`]/,
                            i = {
                                "&": "&amp;",
                                "<": "&lt;",
                                ">": "&gt;",
                                '"': "&quot;",
                                "'": "&#x27;",
                                "`": "&#x60;"
                            },
                            o = function(e) {
                                return i[e]
                            };
                        return n.test(e) ? e.replace(t, o) : e
                    },
                    popup: function(t) {
                        var i = "",
                            o = e.fn.popup.settings.templates.escape;
                        return void 0 !== (void 0 === t ? "undefined" : n(t)) && (void 0 !== n(t.title) && t.title && (t.title = o(t.title), i += '<div class="header">' + t.title + "</div>"), void 0 !== n(t.content) && t.content && (t.content = o(t.content), i += '<div class="content">' + t.content + "</div>")), i
                    }
                }
            }
        }(jQuery, window, document),
        function(e, t, n, i) {
            "use strict";
            t = void 0 !== t && t.Math == Math ? t : "undefined" != typeof self && self.Math == Math ? self : Function("return this")(), e.fn.sidebar = function(i) {
                var o, r = e(this),
                    a = e(t),
                    s = e(n),
                    l = e("html"),
                    c = e("head"),
                    u = r.selector || "",
                    d = (new Date).getTime(),
                    f = [],
                    p = arguments[0],
                    h = "string" == typeof p,
                    m = [].slice.call(arguments, 1),
                    g = t.requestAnimationFrame || t.mozRequestAnimationFrame || t.webkitRequestAnimationFrame || t.msRequestAnimationFrame || function(e) {
                        setTimeout(e, 0)
                    };
                return r.each(function() {
                    var r, v, b, y, x, w, C = e.isPlainObject(i) ? e.extend(!0, {}, e.fn.sidebar.settings, i) : e.extend({}, e.fn.sidebar.settings),
                        k = C.selector,
                        S = C.className,
                        T = C.namespace,
                        A = C.regExp,
                        E = C.error,
                        D = "." + T,
                        O = "module-" + T,
                        F = e(this),
                        j = e(C.context),
                        q = F.children(k.sidebar),
                        L = j.children(k.fixed),
                        N = j.children(k.pusher),
                        P = this,
                        R = F.data(O);
                    w = {
                        initialize: function() {
                            w.debug("Initializing sidebar", i), w.create.id(), x = w.get.transitionEvent(), w.is.ios() && w.set.ios(), C.delaySetup ? g(w.setup.layout) : w.setup.layout(), g(function() {
                                w.setup.cache()
                            }), w.instantiate()
                        },
                        instantiate: function() {
                            w.verbose("Storing instance of module", w), R = w, F.data(O, w)
                        },
                        create: {
                            id: function() {
                                b = (Math.random().toString(16) + "000000000").substr(2, 8), v = "." + b, w.verbose("Creating unique id for element", b)
                            }
                        },
                        destroy: function() {
                            w.verbose("Destroying previous module for", F), F.off(D).removeData(O), w.is.ios() && w.remove.ios(), j.off(v), a.off(v), s.off(v)
                        },
                        event: {
                            clickaway: function(e) {
                                var t = N.find(e.target).length > 0 || N.is(e.target),
                                    n = j.is(e.target);
                                t && (w.verbose("User clicked on dimmed page"), w.hide()), n && (w.verbose("User clicked on dimmable context (scaled out page)"), w.hide())
                            },
                            touch: function(e) {},
                            containScroll: function(e) {
                                P.scrollTop <= 0 && (P.scrollTop = 1), P.scrollTop + P.offsetHeight >= P.scrollHeight && (P.scrollTop = P.scrollHeight - P.offsetHeight - 1)
                            },
                            scroll: function(t) {
                                0 === e(t.target).closest(k.sidebar).length && t.preventDefault()
                            }
                        },
                        bind: {
                            clickaway: function() {
                                w.verbose("Adding clickaway events to context", j), C.closable && j.on("click" + v, w.event.clickaway).on("touchend" + v, w.event.clickaway)
                            },
                            scrollLock: function() {
                                C.scrollLock && (w.debug("Disabling page scroll"), a.on("DOMMouseScroll" + v, w.event.scroll)), w.verbose("Adding events to contain sidebar scroll"), s.on("touchmove" + v, w.event.touch), F.on("scroll" + D, w.event.containScroll)
                            }
                        },
                        unbind: {
                            clickaway: function() {
                                w.verbose("Removing clickaway events from context", j), j.off(v)
                            },
                            scrollLock: function() {
                                w.verbose("Removing scroll lock from page"), s.off(v), a.off(v), F.off("scroll" + D)
                            }
                        },
                        add: {
                            inlineCSS: function() {
                                var t, n = w.cache.width || F.outerWidth(),
                                    i = w.cache.height || F.outerHeight(),
                                    o = w.is.rtl(),
                                    a = w.get.direction(),
                                    s = {
                                        left: n,
                                        right: -n,
                                        top: i,
                                        bottom: -i
                                    };
                                o && (w.verbose("RTL detected, flipping widths"), s.left = -n, s.right = n), t = "<style>", "left" === a || "right" === a ? (w.debug("Adding CSS rules for animation distance", n), t += " .ui.visible." + a + ".sidebar ~ .fixed, .ui.visible." + a + ".sidebar ~ .pusher {   -webkit-transform: translate3d(" + s[a] + "px, 0, 0);           transform: translate3d(" + s[a] + "px, 0, 0); }") : "top" !== a && "bottom" != a || (t += " .ui.visible." + a + ".sidebar ~ .fixed, .ui.visible." + a + ".sidebar ~ .pusher {   -webkit-transform: translate3d(0, " + s[a] + "px, 0);           transform: translate3d(0, " + s[a] + "px, 0); }"), w.is.ie() && ("left" === a || "right" === a ? (w.debug("Adding CSS rules for animation distance", n), t += " body.pushable > .ui.visible." + a + ".sidebar ~ .pusher:after {   -webkit-transform: translate3d(" + s[a] + "px, 0, 0);           transform: translate3d(" + s[a] + "px, 0, 0); }") : "top" !== a && "bottom" != a || (t += " body.pushable > .ui.visible." + a + ".sidebar ~ .pusher:after {   -webkit-transform: translate3d(0, " + s[a] + "px, 0);           transform: translate3d(0, " + s[a] + "px, 0); }"), t += " body.pushable > .ui.visible.left.sidebar ~ .ui.visible.right.sidebar ~ .pusher:after, body.pushable > .ui.visible.right.sidebar ~ .ui.visible.left.sidebar ~ .pusher:after {   -webkit-transform: translate3d(0px, 0, 0);           transform: translate3d(0px, 0, 0); }"), t += "</style>", r = e(t).appendTo(c), w.debug("Adding sizing css to head", r)
                            }
                        },
                        refresh: function() {
                            w.verbose("Refreshing selector cache"), j = e(C.context), q = j.children(k.sidebar), N = j.children(k.pusher), L = j.children(k.fixed), w.clear.cache()
                        },
                        refreshSidebars: function() {
                            w.verbose("Refreshing other sidebars"), q = j.children(k.sidebar)
                        },
                        repaint: function() {
                            w.verbose("Forcing repaint event"), P.style.display = "none", P.offsetHeight, P.scrollTop = P.scrollTop, P.style.display = ""
                        },
                        setup: {
                            cache: function() {
                                w.cache = {
                                    width: F.outerWidth(),
                                    height: F.outerHeight(),
                                    rtl: "rtl" == F.css("direction")
                                }
                            },
                            layout: function() {
                                0 === j.children(k.pusher).length && (w.debug("Adding wrapper element for sidebar"), w.error(E.pusher), N = e('<div class="pusher" />'), j.children().not(k.omitted).not(q).wrapAll(N), w.refresh()), 0 !== F.nextAll(k.pusher).length && F.nextAll(k.pusher)[0] === N[0] || (w.debug("Moved sidebar to correct parent element"), w.error(E.movedSidebar, P), F.detach().prependTo(j), w.refresh()), w.clear.cache(), w.set.pushable(), w.set.direction()
                            }
                        },
                        attachEvents: function(t, n) {
                            var i = e(t);
                            n = e.isFunction(w[n]) ? w[n] : w.toggle, i.length > 0 ? (w.debug("Attaching sidebar events to element", t, n), i.on("click" + D, n)) : w.error(E.notFound, t)
                        },
                        show: function(t) {
                            if (t = e.isFunction(t) ? t : function() {}, w.is.hidden()) {
                                if (w.refreshSidebars(), C.overlay && (w.error(E.overlay), C.transition = "overlay"), w.refresh(), w.othersActive())
                                    if (w.debug("Other sidebars currently visible"), C.exclusive) {
                                        if ("overlay" != C.transition) return void w.hideOthers(w.show);
                                        w.hideOthers()
                                    } else C.transition = "overlay";
                                w.pushPage(function() {
                                    t.call(P), C.onShow.call(P)
                                }), C.onChange.call(P), C.onVisible.call(P)
                            } else w.debug("Sidebar is already visible")
                        },
                        hide: function(t) {
                            t = e.isFunction(t) ? t : function() {}, (w.is.visible() || w.is.animating()) && (w.debug("Hiding sidebar", t), w.refreshSidebars(), w.pullPage(function() {
                                t.call(P), C.onHidden.call(P)
                            }), C.onChange.call(P), C.onHide.call(P))
                        },
                        othersAnimating: function() {
                            return q.not(F).filter("." + S.animating).length > 0
                        },
                        othersVisible: function() {
                            return q.not(F).filter("." + S.visible).length > 0
                        },
                        othersActive: function() {
                            return w.othersVisible() || w.othersAnimating()
                        },
                        hideOthers: function(e) {
                            var t = q.not(F).filter("." + S.visible),
                                n = t.length,
                                i = 0;
                            e = e || function() {}, t.sidebar("hide", function() {
                                ++i == n && e()
                            })
                        },
                        toggle: function() {
                            w.verbose("Determining toggled direction"), w.is.hidden() ? w.show() : w.hide()
                        },
                        pushPage: function(t) {
                            var n, i, o, r = w.get.transition(),
                                a = "overlay" === r || w.othersActive() ? F : N;
                            t = e.isFunction(t) ? t : function() {}, "scale down" == C.transition && w.scrollToTop(), w.set.transition(r), w.repaint(), n = function() {
                                w.bind.clickaway(), w.add.inlineCSS(), w.set.animating(), w.set.visible()
                            }, i = function() {
                                w.set.dimmed()
                            }, o = function(e) {
                                e.target == a[0] && (a.off(x + v, o), w.remove.animating(), w.bind.scrollLock(), t.call(P))
                            }, a.off(x + v), a.on(x + v, o), g(n), C.dimPage && !w.othersVisible() && g(i)
                        },
                        pullPage: function(t) {
                            var n, i, o = w.get.transition(),
                                r = "overlay" == o || w.othersActive() ? F : N;
                            t = e.isFunction(t) ? t : function() {}, w.verbose("Removing context push state", w.get.direction()), w.unbind.clickaway(), w.unbind.scrollLock(), n = function() {
                                w.set.transition(o), w.set.animating(), w.remove.visible(), C.dimPage && !w.othersVisible() && N.removeClass(S.dimmed)
                            }, i = function(e) {
                                e.target == r[0] && (r.off(x + v, i), w.remove.animating(), w.remove.transition(), w.remove.inlineCSS(), ("scale down" == o || C.returnScroll && w.is.mobile()) && w.scrollBack(), t.call(P))
                            }, r.off(x + v), r.on(x + v, i), g(n)
                        },
                        scrollToTop: function() {
                            w.verbose("Scrolling to top of page to avoid animation issues"), y = e(t).scrollTop(), F.scrollTop(0), t.scrollTo(0, 0)
                        },
                        scrollBack: function() {
                            w.verbose("Scrolling back to original page position"), t.scrollTo(0, y)
                        },
                        clear: {
                            cache: function() {
                                w.verbose("Clearing cached dimensions"), w.cache = {}
                            }
                        },
                        set: {
                            ios: function() {
                                l.addClass(S.ios)
                            },
                            pushed: function() {
                                j.addClass(S.pushed)
                            },
                            pushable: function() {
                                j.addClass(S.pushable)
                            },
                            dimmed: function() {
                                N.addClass(S.dimmed)
                            },
                            active: function() {
                                F.addClass(S.active)
                            },
                            animating: function() {
                                F.addClass(S.animating)
                            },
                            transition: function(e) {
                                e = e || w.get.transition(), F.addClass(e)
                            },
                            direction: function(e) {
                                e = e || w.get.direction(), F.addClass(S[e])
                            },
                            visible: function() {
                                F.addClass(S.visible)
                            },
                            overlay: function() {
                                F.addClass(S.overlay)
                            }
                        },
                        remove: {
                            inlineCSS: function() {
                                w.debug("Removing inline css styles", r), r && r.length > 0 && r.remove()
                            },
                            ios: function() {
                                l.removeClass(S.ios)
                            },
                            pushed: function() {
                                j.removeClass(S.pushed)
                            },
                            pushable: function() {
                                j.removeClass(S.pushable)
                            },
                            active: function() {
                                F.removeClass(S.active)
                            },
                            animating: function() {
                                F.removeClass(S.animating)
                            },
                            transition: function(e) {
                                e = e || w.get.transition(), F.removeClass(e)
                            },
                            direction: function(e) {
                                e = e || w.get.direction(), F.removeClass(S[e])
                            },
                            visible: function() {
                                F.removeClass(S.visible)
                            },
                            overlay: function() {
                                F.removeClass(S.overlay)
                            }
                        },
                        get: {
                            direction: function() {
                                return F.hasClass(S.top) ? S.top : F.hasClass(S.right) ? S.right : F.hasClass(S.bottom) ? S.bottom : S.left
                            },
                            transition: function() {
                                var e, t = w.get.direction();
                                return e = w.is.mobile() ? "auto" == C.mobileTransition ? C.defaultTransition.mobile[t] : C.mobileTransition : "auto" == C.transition ? C.defaultTransition.computer[t] : C.transition, w.verbose("Determined transition", e), e
                            },
                            transitionEvent: function() {
                                var e, t = n.createElement("element"),
                                    i = {
                                        transition: "transitionend",
                                        OTransition: "oTransitionEnd",
                                        MozTransition: "transitionend",
                                        WebkitTransition: "webkitTransitionEnd"
                                    };
                                for (e in i)
                                    if (void 0 !== t.style[e]) return i[e]
                            }
                        },
                        is: {
                            ie: function() {
                                var e = !t.ActiveXObject && "ActiveXObject" in t,
                                    n = "ActiveXObject" in t;
                                return e || n
                            },
                            ios: function() {
                                var e = navigator.userAgent,
                                    t = e.match(A.ios),
                                    n = e.match(A.mobileChrome);
                                return !(!t || n || (w.verbose("Browser was found to be iOS", e), 0))
                            },
                            mobile: function() {
                                var e = navigator.userAgent;
                                return e.match(A.mobile) ? (w.verbose("Browser was found to be mobile", e), !0) : (w.verbose("Browser is not mobile, using regular transition", e), !1)
                            },
                            hidden: function() {
                                return !w.is.visible()
                            },
                            visible: function() {
                                return F.hasClass(S.visible)
                            },
                            open: function() {
                                return w.is.visible()
                            },
                            closed: function() {
                                return w.is.hidden()
                            },
                            vertical: function() {
                                return F.hasClass(S.top)
                            },
                            animating: function() {
                                return j.hasClass(S.animating)
                            },
                            rtl: function() {
                                return void 0 === w.cache.rtl && (w.cache.rtl = "rtl" == F.css("direction")), w.cache.rtl
                            }
                        },
                        setting: function(t, n) {
                            if (w.debug("Changing setting", t, n), e.isPlainObject(t)) e.extend(!0, C, t);
                            else {
                                if (void 0 === n) return C[t];
                                e.isPlainObject(C[t]) ? e.extend(!0, C[t], n) : C[t] = n
                            }
                        },
                        internal: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, w, t);
                            else {
                                if (void 0 === n) return w[t];
                                w[t] = n
                            }
                        },
                        debug: function() {
                            !C.silent && C.debug && (C.performance ? w.performance.log(arguments) : (w.debug = Function.prototype.bind.call(console.info, console, C.name + ":"), w.debug.apply(console, arguments)))
                        },
                        verbose: function() {
                            !C.silent && C.verbose && C.debug && (C.performance ? w.performance.log(arguments) : (w.verbose = Function.prototype.bind.call(console.info, console, C.name + ":"), w.verbose.apply(console, arguments)))
                        },
                        error: function() {
                            C.silent || (w.error = Function.prototype.bind.call(console.error, console, C.name + ":"), w.error.apply(console, arguments))
                        },
                        performance: {
                            log: function(e) {
                                var t, n, i;
                                C.performance && (t = (new Date).getTime(), i = d || t, n = t - i, d = t, f.push({
                                    Name: e[0],
                                    Arguments: [].slice.call(e, 1) || "",
                                    Element: P,
                                    "Execution Time": n
                                })), clearTimeout(w.performance.timer), w.performance.timer = setTimeout(w.performance.display, 500)
                            },
                            display: function() {
                                var t = C.name + ":",
                                    n = 0;
                                d = !1, clearTimeout(w.performance.timer), e.each(f, function(e, t) {
                                    n += t["Execution Time"]
                                }), t += " " + n + "ms", u && (t += " '" + u + "'"), (void 0 !== console.group || void 0 !== console.table) && f.length > 0 && (console.table || e.each(f, function(e, t) {})), f = []
                            }
                        },
                        invoke: function(t, n, i) {
                            var r, a, s, l = R;
                            return n = n || m, i = P || i, "string" == typeof t && void 0 !== l && (t = t.split(/[\. ]/), r = t.length - 1, e.each(t, function(n, i) {
                                var o = n != r ? i + t[n + 1].charAt(0).toUpperCase() + t[n + 1].slice(1) : t;
                                if (e.isPlainObject(l[o]) && n != r) l = l[o];
                                else {
                                    if (void 0 !== l[o]) return a = l[o], !1;
                                    if (!e.isPlainObject(l[i]) || n == r) return void 0 !== l[i] ? (a = l[i], !1) : (w.error(E.method, t), !1);
                                    l = l[i]
                                }
                            })), e.isFunction(a) ? s = a.apply(i, n) : void 0 !== a && (s = a), e.isArray(o) ? o.push(s) : void 0 !== o ? o = [o, s] : void 0 !== s && (o = s), a
                        }
                    }, h ? (void 0 === R && w.initialize(), w.invoke(p)) : (void 0 !== R && w.invoke("destroy"), w.initialize())
                }), void 0 !== o ? o : this
            }, e.fn.sidebar.settings = {
                name: "Sidebar",
                namespace: "sidebar",
                silent: !1,
                debug: !1,
                verbose: !1,
                performance: !0,
                transition: "auto",
                mobileTransition: "auto",
                defaultTransition: {
                    computer: {
                        left: "uncover",
                        right: "uncover",
                        top: "overlay",
                        bottom: "overlay"
                    },
                    mobile: {
                        left: "uncover",
                        right: "uncover",
                        top: "overlay",
                        bottom: "overlay"
                    }
                },
                context: "body",
                exclusive: !1,
                closable: !0,
                dimPage: !0,
                scrollLock: !1,
                returnScroll: !1,
                delaySetup: !1,
                duration: 500,
                onChange: function() {},
                onShow: function() {},
                onHide: function() {},
                onHidden: function() {},
                onVisible: function() {},
                className: {
                    active: "active",
                    animating: "animating",
                    dimmed: "dimmed",
                    ios: "ios",
                    pushable: "pushable",
                    pushed: "pushed",
                    right: "right",
                    top: "top",
                    left: "left",
                    bottom: "bottom",
                    visible: "visible"
                },
                selector: {
                    fixed: ".fixed",
                    omitted: "script, link, style, .ui.modal, .ui.dimmer, .ui.nag, .ui.fixed",
                    pusher: ".pusher",
                    sidebar: ".ui.sidebar"
                },
                regExp: {
                    ios: /(iPad|iPhone|iPod)/g,
                    mobileChrome: /(CriOS)/g,
                    mobile: /Mobile|iP(hone|od|ad)|Android|BlackBerry|IEMobile|Kindle|NetFront|Silk-Accelerated|(hpw|web)OS|Fennec|Minimo|Opera M(obi|ini)|Blazer|Dolfin|Dolphin|Skyfire|Zune/g
                },
                error: {
                    method: "The method you called is not defined.",
                    pusher: "Had to add pusher element. For optimal performance make sure body content is inside a pusher element",
                    movedSidebar: "Had to move sidebar. For optimal performance make sure sidebar and pusher are direct children of your body tag",
                    overlay: "The overlay setting is no longer supported, use animation: overlay",
                    notFound: "There were no elements that matched the specified selector"
                }
            }
        }(jQuery, window, document),
        function(e, t, n, i) {
            "use strict";
            t = void 0 !== t && t.Math == Math ? t : "undefined" != typeof self && self.Math == Math ? self : Function("return this")(), e.fn.sticky = function(i) {
                var o, r = e(this),
                    a = r.selector || "",
                    s = (new Date).getTime(),
                    l = [],
                    c = arguments[0],
                    u = "string" == typeof c,
                    d = [].slice.call(arguments, 1);
                return r.each(function() {
                    var r, f, p, h, m, g = e.isPlainObject(i) ? e.extend(!0, {}, e.fn.sticky.settings, i) : e.extend({}, e.fn.sticky.settings),
                        v = g.className,
                        b = g.namespace,
                        y = g.error,
                        x = "." + b,
                        w = "module-" + b,
                        C = e(this),
                        k = e(t),
                        S = e(g.scrollContext),
                        T = (C.selector, C.data(w)),
                        A = t.requestAnimationFrame || t.mozRequestAnimationFrame || t.webkitRequestAnimationFrame || t.msRequestAnimationFrame || function(e) {
                            setTimeout(e, 0)
                        },
                        E = this;
                    m = {
                        initialize: function() {
                            m.determineContainer(), m.determineContext(), m.verbose("Initializing sticky", g, r), m.save.positions(), m.checkErrors(), m.bind.events(), g.observeChanges && m.observeChanges(), m.instantiate()
                        },
                        instantiate: function() {
                            m.verbose("Storing instance of module", m), T = m, C.data(w, m)
                        },
                        destroy: function() {
                            m.verbose("Destroying previous instance"), m.reset(), p && p.disconnect(), h && h.disconnect(), k.off("load" + x, m.event.load).off("resize" + x, m.event.resize), S.off("scrollchange" + x, m.event.scrollchange), C.removeData(w)
                        },
                        observeChanges: function() {
                            "MutationObserver" in t && (p = new MutationObserver(m.event.documentChanged), h = new MutationObserver(m.event.changed), p.observe(n, {
                                childList: !0,
                                subtree: !0
                            }), h.observe(E, {
                                childList: !0,
                                subtree: !0
                            }), h.observe(f[0], {
                                childList: !0,
                                subtree: !0
                            }), m.debug("Setting up mutation observer", h))
                        },
                        determineContainer: function() {
                            r = g.container ? e(g.container) : C.offsetParent()
                        },
                        determineContext: function() {
                            if (f = g.context ? e(g.context) : r, 0 === f.length) return void m.error(y.invalidContext, g.context, C)
                        },
                        checkErrors: function() {
                            if (m.is.hidden() && m.error(y.visible, C), m.cache.element.height > m.cache.context.height) return m.reset(), void m.error(y.elementSize, C)
                        },
                        bind: {
                            events: function() {
                                k.on("load" + x, m.event.load).on("resize" + x, m.event.resize), S.off("scroll" + x).on("scroll" + x, m.event.scroll).on("scrollchange" + x, m.event.scrollchange)
                            }
                        },
                        event: {
                            changed: function(e) {
                                clearTimeout(m.timer), m.timer = setTimeout(function() {
                                    m.verbose("DOM tree modified, updating sticky menu", e), m.refresh()
                                }, 100)
                            },
                            documentChanged: function(t) {
                                [].forEach.call(t, function(t) {
                                    t.removedNodes && [].forEach.call(t.removedNodes, function(t) {
                                        (t == E || e(t).find(E).length > 0) && (m.debug("Element removed from DOM, tearing down events"), m.destroy())
                                    })
                                })
                            },
                            load: function() {
                                m.verbose("Page contents finished loading"), A(m.refresh)
                            },
                            resize: function() {
                                m.verbose("Window resized"), A(m.refresh)
                            },
                            scroll: function() {
                                A(function() {
                                    S.triggerHandler("scrollchange" + x, S.scrollTop())
                                })
                            },
                            scrollchange: function(e, t) {
                                m.stick(t), g.onScroll.call(E)
                            }
                        },
                        refresh: function(e) {
                            m.reset(), g.context || m.determineContext(), e && m.determineContainer(), m.save.positions(), m.stick(), g.onReposition.call(E)
                        },
                        supports: {
                            sticky: function() {
                                var t = e("<div/>");
                                return t[0], t.addClass(v.supported), t.css("position").match("sticky")
                            }
                        },
                        save: {
                            lastScroll: function(e) {
                                m.lastScroll = e
                            },
                            elementScroll: function(e) {
                                m.elementScroll = e
                            },
                            positions: function() {
                                var e = {
                                        height: S.height()
                                    },
                                    t = {
                                        margin: {
                                            top: parseInt(C.css("margin-top"), 10),
                                            bottom: parseInt(C.css("margin-bottom"), 10)
                                        },
                                        offset: C.offset(),
                                        width: C.outerWidth(),
                                        height: C.outerHeight()
                                    },
                                    n = {
                                        offset: f.offset(),
                                        height: f.outerHeight()
                                    };
                                r.outerHeight(), m.is.standardScroll() || (m.debug("Non-standard scroll. Removing scroll offset from element offset"), e.top = S.scrollTop(), e.left = S.scrollLeft(), t.offset.top += e.top, n.offset.top += e.top, t.offset.left += e.left, n.offset.left += e.left), m.cache = {
                                    fits: t.height < e.height,
                                    scrollContext: {
                                        height: e.height
                                    },
                                    element: {
                                        margin: t.margin,
                                        top: t.offset.top - t.margin.top,
                                        left: t.offset.left,
                                        width: t.width,
                                        height: t.height,
                                        bottom: t.offset.top + t.height
                                    },
                                    context: {
                                        top: n.offset.top,
                                        height: n.height,
                                        bottom: n.offset.top + n.height
                                    }
                                }, m.set.containerSize(), m.set.size(), m.stick(), m.debug("Caching element positions", m.cache)
                            }
                        },
                        get: {
                            direction: function(e) {
                                var t = "down";
                                return e = e || S.scrollTop(), void 0 !== m.lastScroll && (m.lastScroll < e ? t = "down" : m.lastScroll > e && (t = "up")), t
                            },
                            scrollChange: function(e) {
                                return e = e || S.scrollTop(), m.lastScroll ? e - m.lastScroll : 0
                            },
                            currentElementScroll: function() {
                                return m.elementScroll ? m.elementScroll : m.is.top() ? Math.abs(parseInt(C.css("top"), 10)) || 0 : Math.abs(parseInt(C.css("bottom"), 10)) || 0
                            },
                            elementScroll: function(e) {
                                e = e || S.scrollTop();
                                var t = m.cache.element,
                                    n = m.cache.scrollContext,
                                    i = m.get.scrollChange(e),
                                    o = t.height - n.height + g.offset,
                                    r = m.get.currentElementScroll(),
                                    a = r + i;
                                return r = m.cache.fits || a < 0 ? 0 : a > o ? o : a
                            }
                        },
                        remove: {
                            lastScroll: function() {
                                delete m.lastScroll
                            },
                            elementScroll: function(e) {
                                delete m.elementScroll
                            },
                            offset: function() {
                                C.css("margin-top", "")
                            }
                        },
                        set: {
                            offset: function() {
                                m.verbose("Setting offset on element", g.offset), C.css("margin-top", g.offset)
                            },
                            containerSize: function() {
                                var e = r.get(0).tagName;
                                "HTML" === e || "body" == e ? m.determineContainer() : Math.abs(r.outerHeight() - m.cache.context.height) > g.jitter && (m.debug("Context has padding, specifying exact height for container", m.cache.context.height), r.css({
                                    height: m.cache.context.height
                                }))
                            },
                            minimumSize: function() {
                                var e = m.cache.element;
                                r.css("min-height", e.height)
                            },
                            scroll: function(e) {
                                m.debug("Setting scroll on element", e), m.elementScroll != e && (m.is.top() && C.css("bottom", "").css("top", -e), m.is.bottom() && C.css("top", "").css("bottom", e))
                            },
                            size: function() {
                                0 !== m.cache.element.height && 0 !== m.cache.element.width && (E.style.setProperty("width", m.cache.element.width + "px", "important"), E.style.setProperty("height", m.cache.element.height + "px", "important"))
                            }
                        },
                        is: {
                            standardScroll: function() {
                                return S[0] == t
                            },
                            top: function() {
                                return C.hasClass(v.top)
                            },
                            bottom: function() {
                                return C.hasClass(v.bottom)
                            },
                            initialPosition: function() {
                                return !m.is.fixed() && !m.is.bound()
                            },
                            hidden: function() {
                                return !C.is(":visible")
                            },
                            bound: function() {
                                return C.hasClass(v.bound)
                            },
                            fixed: function() {
                                return C.hasClass(v.fixed)
                            }
                        },
                        stick: function(e) {
                            var t = e || S.scrollTop(),
                                n = m.cache,
                                i = n.fits,
                                o = n.element,
                                r = n.scrollContext,
                                a = n.context,
                                s = m.is.bottom() && g.pushing ? g.bottomOffset : g.offset,
                                e = {
                                    top: t + s,
                                    bottom: t + s + r.height
                                },
                                l = (m.get.direction(e.top), i ? 0 : m.get.elementScroll(e.top)),
                                c = !i;
                            0 !== o.height && (m.is.initialPosition() ? e.top >= a.bottom ? (m.debug("Initial element position is bottom of container"), m.bindBottom()) : e.top > o.top && (o.height + e.top - l >= a.bottom ? (m.debug("Initial element position is bottom of container"), m.bindBottom()) : (m.debug("Initial element position is fixed"), m.fixTop())) : m.is.fixed() ? m.is.top() ? e.top <= o.top ? (m.debug("Fixed element reached top of container"), m.setInitialPosition()) : o.height + e.top - l >= a.bottom ? (m.debug("Fixed element reached bottom of container"), m.bindBottom()) : c && (m.set.scroll(l), m.save.lastScroll(e.top), m.save.elementScroll(l)) : m.is.bottom() && (e.bottom - o.height <= o.top ? (m.debug("Bottom fixed rail has reached top of container"), m.setInitialPosition()) : e.bottom >= a.bottom ? (m.debug("Bottom fixed rail has reached bottom of container"), m.bindBottom()) : c && (m.set.scroll(l), m.save.lastScroll(e.top), m.save.elementScroll(l))) : m.is.bottom() && (e.top <= o.top ? (m.debug("Jumped from bottom fixed to top fixed, most likely used home/end button"), m.setInitialPosition()) : g.pushing ? m.is.bound() && e.bottom <= a.bottom && (m.debug("Fixing bottom attached element to bottom of browser."), m.fixBottom()) : m.is.bound() && e.top <= a.bottom - o.height && (m.debug("Fixing bottom attached element to top of browser."), m.fixTop())))
                        },
                        bindTop: function() {
                            m.debug("Binding element to top of parent container"), m.remove.offset(), C.css({
                                left: "",
                                top: "",
                                marginBottom: ""
                            }).removeClass(v.fixed).removeClass(v.bottom).addClass(v.bound).addClass(v.top), g.onTop.call(E), g.onUnstick.call(E)
                        },
                        bindBottom: function() {
                            m.debug("Binding element to bottom of parent container"), m.remove.offset(), C.css({
                                left: "",
                                top: ""
                            }).removeClass(v.fixed).removeClass(v.top).addClass(v.bound).addClass(v.bottom), g.onBottom.call(E), g.onUnstick.call(E)
                        },
                        setInitialPosition: function() {
                            m.debug("Returning to initial position"), m.unfix(), m.unbind()
                        },
                        fixTop: function() {
                            m.debug("Fixing element to top of page"), m.set.minimumSize(), m.set.offset(), C.css({
                                left: m.cache.element.left,
                                bottom: "",
                                marginBottom: ""
                            }).removeClass(v.bound).removeClass(v.bottom).addClass(v.fixed).addClass(v.top), g.onStick.call(E)
                        },
                        fixBottom: function() {
                            m.debug("Sticking element to bottom of page"), m.set.minimumSize(), m.set.offset(), C.css({
                                left: m.cache.element.left,
                                bottom: "",
                                marginBottom: ""
                            }).removeClass(v.bound).removeClass(v.top).addClass(v.fixed).addClass(v.bottom), g.onStick.call(E)
                        },
                        unbind: function() {
                            m.is.bound() && (m.debug("Removing container bound position on element"), m.remove.offset(), C.removeClass(v.bound).removeClass(v.top).removeClass(v.bottom))
                        },
                        unfix: function() {
                            m.is.fixed() && (m.debug("Removing fixed position on element"), m.remove.offset(), C.removeClass(v.fixed).removeClass(v.top).removeClass(v.bottom), g.onUnstick.call(E))
                        },
                        reset: function() {
                            m.debug("Resetting elements position"), m.unbind(), m.unfix(), m.resetCSS(), m.remove.offset(), m.remove.lastScroll()
                        },
                        resetCSS: function() {
                            C.css({
                                width: "",
                                height: ""
                            }), r.css({
                                height: ""
                            })
                        },
                        setting: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, g, t);
                            else {
                                if (void 0 === n) return g[t];
                                g[t] = n
                            }
                        },
                        internal: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, m, t);
                            else {
                                if (void 0 === n) return m[t];
                                m[t] = n
                            }
                        },
                        debug: function() {
                            !g.silent && g.debug && (g.performance ? m.performance.log(arguments) : (m.debug = Function.prototype.bind.call(console.info, console, g.name + ":"), m.debug.apply(console, arguments)))
                        },
                        verbose: function() {
                            !g.silent && g.verbose && g.debug && (g.performance ? m.performance.log(arguments) : (m.verbose = Function.prototype.bind.call(console.info, console, g.name + ":"), m.verbose.apply(console, arguments)))
                        },
                        error: function() {
                            g.silent || (m.error = Function.prototype.bind.call(console.error, console, g.name + ":"), m.error.apply(console, arguments))
                        },
                        performance: {
                            log: function(e) {
                                var t, n, i;
                                g.performance && (t = (new Date).getTime(), i = s || t, n = t - i, s = t, l.push({
                                    Name: e[0],
                                    Arguments: [].slice.call(e, 1) || "",
                                    Element: E,
                                    "Execution Time": n
                                })), clearTimeout(m.performance.timer), m.performance.timer = setTimeout(m.performance.display, 0)
                            },
                            display: function() {
                                var t = g.name + ":",
                                    n = 0;
                                s = !1, clearTimeout(m.performance.timer), e.each(l, function(e, t) {
                                    n += t["Execution Time"]
                                }), t += " " + n + "ms", a && (t += " '" + a + "'"), (void 0 !== console.group || void 0 !== console.table) && l.length > 0 && (console.table || e.each(l, function(e, t) {})), l = []
                            }
                        },
                        invoke: function(t, n, i) {
                            var r, a, s, l = T;
                            return n = n || d, i = E || i, "string" == typeof t && void 0 !== l && (t = t.split(/[\. ]/), r = t.length - 1, e.each(t, function(n, i) {
                                var o = n != r ? i + t[n + 1].charAt(0).toUpperCase() + t[n + 1].slice(1) : t;
                                if (e.isPlainObject(l[o]) && n != r) l = l[o];
                                else {
                                    if (void 0 !== l[o]) return a = l[o], !1;
                                    if (!e.isPlainObject(l[i]) || n == r) return void 0 !== l[i] && (a = l[i], !1);
                                    l = l[i]
                                }
                            })), e.isFunction(a) ? s = a.apply(i, n) : void 0 !== a && (s = a), e.isArray(o) ? o.push(s) : void 0 !== o ? o = [o, s] : void 0 !== s && (o = s), a
                        }
                    }, u ? (void 0 === T && m.initialize(), m.invoke(c)) : (void 0 !== T && T.invoke("destroy"), m.initialize())
                }), void 0 !== o ? o : this
            }, e.fn.sticky.settings = {
                name: "Sticky",
                namespace: "sticky",
                silent: !1,
                debug: !1,
                verbose: !0,
                performance: !0,
                pushing: !1,
                context: !1,
                container: !1,
                scrollContext: t,
                offset: 0,
                bottomOffset: 0,
                jitter: 5,
                observeChanges: !1,
                onReposition: function() {},
                onScroll: function() {},
                onStick: function() {},
                onUnstick: function() {},
                onTop: function() {},
                onBottom: function() {},
                error: {
                    container: "Sticky element must be inside a relative container",
                    visible: "Element is hidden, you must call refresh after element becomes visible. Use silent setting to surpress this warning in production.",
                    method: "The method you called is not defined.",
                    invalidContext: "Context specified does not exist",
                    elementSize: "Sticky element is larger than its container, cannot create sticky."
                },
                className: {
                    bound: "bound",
                    fixed: "fixed",
                    supported: "native",
                    top: "top",
                    bottom: "bottom"
                }
            }
        }(jQuery, window, document),
        function(e, t, i, o) {
            "use strict";
            t = void 0 !== t && t.Math == Math ? t : "undefined" != typeof self && self.Math == Math ? self : Function("return this")(), e.fn.transition = function() {
                var o, r = e(this),
                    a = r.selector || "",
                    s = (new Date).getTime(),
                    l = [],
                    c = arguments,
                    u = c[0],
                    d = [].slice.call(arguments, 1),
                    f = "string" == typeof u;
                return t.requestAnimationFrame || t.mozRequestAnimationFrame || t.webkitRequestAnimationFrame || t.msRequestAnimationFrame, r.each(function(t) {
                    var p, h, m, g, v, b, y, x, w, C = e(this),
                        k = this;
                    w = {
                        initialize: function() {
                            p = w.get.settings.apply(k, c), g = p.className, m = p.error, v = p.metadata, x = "." + p.namespace, y = "module-" + p.namespace, h = C.data(y) || w, b = w.get.animationEndEvent(), f && (f = w.invoke(u)), !1 === f && (w.verbose("Converted arguments into settings object", p), p.interval ? w.delay(p.animate) : w.animate(), w.instantiate())
                        },
                        instantiate: function() {
                            w.verbose("Storing instance of module", w), h = w, C.data(y, h)
                        },
                        destroy: function() {
                            w.verbose("Destroying previous module for", k), C.removeData(y)
                        },
                        refresh: function() {
                            w.verbose("Refreshing display type on next animation"), delete w.displayType
                        },
                        forceRepaint: function() {
                            w.verbose("Forcing element repaint");
                            var e = C.parent(),
                                t = C.next();
                            0 === t.length ? C.detach().appendTo(e) : C.detach().insertBefore(t)
                        },
                        repaint: function() {
                            w.verbose("Repainting element"), k.offsetWidth
                        },
                        delay: function(e) {
                            var n, i, o = w.get.animationDirection();
                            o || (o = w.can.transition() ? w.get.direction() : "static"), e = void 0 !== e ? e : p.interval, n = "auto" == p.reverse && o == g.outward, i = n || 1 == p.reverse ? (r.length - t) * p.interval : t * p.interval, w.debug("Delaying animation by", i), setTimeout(w.animate, i)
                        },
                        animate: function(e) {
                            if (p = e || p, !w.is.supported()) return w.error(m.support), !1;
                            if (w.debug("Preparing animation", p.animation), w.is.animating()) {
                                if (p.queue) return !p.allowRepeats && w.has.direction() && w.is.occurring() && !0 !== w.queuing ? w.debug("Animation is currently occurring, preventing queueing same animation", p.animation) : w.queue(p.animation), !1;
                                if (!p.allowRepeats && w.is.occurring()) return w.debug("Animation is already occurring, will not execute repeated animation", p.animation), !1;
                                w.debug("New animation started, completing previous early", p.animation), h.complete()
                            }
                            w.can.animate() ? w.set.animating(p.animation) : w.error(m.noAnimation, p.animation, k)
                        },
                        reset: function() {
                            w.debug("Resetting animation to beginning conditions"), w.remove.animationCallbacks(), w.restore.conditions(), w.remove.animating()
                        },
                        queue: function(e) {
                            w.debug("Queueing animation of", e), w.queuing = !0, C.one(b + ".queue" + x, function() {
                                w.queuing = !1, w.repaint(), w.animate.apply(this, p)
                            })
                        },
                        complete: function(e) {
                            w.debug("Animation complete", p.animation), w.remove.completeCallback(), w.remove.failSafe(), w.is.looping() || (w.is.outward() ? (w.verbose("Animation is outward, hiding element"), w.restore.conditions(), w.hide()) : w.is.inward() ? (w.verbose("Animation is outward, showing element"), w.restore.conditions(), w.show()) : (w.verbose("Static animation completed"), w.restore.conditions(), p.onComplete.call(k)))
                        },
                        force: {
                            visible: function() {
                                var e = C.attr("style"),
                                    t = w.get.userStyle(),
                                    n = w.get.displayType(),
                                    i = t + "display: " + n + " !important;",
                                    o = C.css("display"),
                                    r = void 0 === e || "" === e;
                                o !== n ? (w.verbose("Overriding default display to show element", n), C.attr("style", i)) : r && C.removeAttr("style")
                            },
                            hidden: function() {
                                var e = C.attr("style"),
                                    t = C.css("display"),
                                    n = void 0 === e || "" === e;
                                "none" === t || w.is.hidden() ? n && C.removeAttr("style") : (w.verbose("Overriding default display to hide element"), C.css("display", "none"))
                            }
                        },
                        has: {
                            direction: function(t) {
                                var n = !1;
                                return t = t || p.animation, "string" == typeof t && (t = t.split(" "), e.each(t, function(e, t) {
                                    t !== g.inward && t !== g.outward || (n = !0)
                                })), n
                            },
                            inlineDisplay: function() {
                                var t = C.attr("style") || "";
                                return e.isArray(t.match(/display.*?;/, ""))
                            }
                        },
                        set: {
                            animating: function(e) {
                                var t;
                                w.remove.completeCallback(), e = e || p.animation, t = w.get.animationClass(e), w.save.animation(t), w.force.visible(), w.remove.hidden(), w.remove.direction(), w.start.animation(t)
                            },
                            duration: function(e, t) {
                                t = t || p.duration, ((t = "number" == typeof t ? t + "ms" : t) || 0 === t) && (w.verbose("Setting animation duration", t), C.css({
                                    "animation-duration": t
                                }))
                            },
                            direction: function(e) {
                                e = e || w.get.direction(), e == g.inward ? w.set.inward() : w.set.outward()
                            },
                            looping: function() {
                                w.debug("Transition set to loop"), C.addClass(g.looping)
                            },
                            hidden: function() {
                                C.addClass(g.transition).addClass(g.hidden)
                            },
                            inward: function() {
                                w.debug("Setting direction to inward"), C.removeClass(g.outward).addClass(g.inward)
                            },
                            outward: function() {
                                w.debug("Setting direction to outward"), C.removeClass(g.inward).addClass(g.outward)
                            },
                            visible: function() {
                                C.addClass(g.transition).addClass(g.visible)
                            }
                        },
                        start: {
                            animation: function(e) {
                                e = e || w.get.animationClass(), w.debug("Starting tween", e), C.addClass(e).one(b + ".complete" + x, w.complete), p.useFailSafe && w.add.failSafe(), w.set.duration(p.duration), p.onStart.call(k)
                            }
                        },
                        save: {
                            animation: function(e) {
                                w.cache || (w.cache = {}), w.cache.animation = e
                            },
                            displayType: function(e) {
                                "none" !== e && C.data(v.displayType, e)
                            },
                            transitionExists: function(t, n) {
                                e.fn.transition.exists[t] = n, w.verbose("Saving existence of transition", t, n)
                            }
                        },
                        restore: {
                            conditions: function() {
                                var e = w.get.currentAnimation();
                                e && (C.removeClass(e), w.verbose("Removing animation class", w.cache)), w.remove.duration()
                            }
                        },
                        add: {
                            failSafe: function() {
                                var e = w.get.duration();
                                w.timer = setTimeout(function() {
                                    C.triggerHandler(b)
                                }, e + p.failSafeDelay), w.verbose("Adding fail safe timer", w.timer)
                            }
                        },
                        remove: {
                            animating: function() {
                                C.removeClass(g.animating)
                            },
                            animationCallbacks: function() {
                                w.remove.queueCallback(), w.remove.completeCallback()
                            },
                            queueCallback: function() {
                                C.off(".queue" + x)
                            },
                            completeCallback: function() {
                                C.off(".complete" + x)
                            },
                            display: function() {
                                C.css("display", "")
                            },
                            direction: function() {
                                C.removeClass(g.inward).removeClass(g.outward)
                            },
                            duration: function() {
                                C.css("animation-duration", "")
                            },
                            failSafe: function() {
                                w.verbose("Removing fail safe timer", w.timer), w.timer && clearTimeout(w.timer)
                            },
                            hidden: function() {
                                C.removeClass(g.hidden)
                            },
                            visible: function() {
                                C.removeClass(g.visible)
                            },
                            looping: function() {
                                w.debug("Transitions are no longer looping"), w.is.looping() && (w.reset(), C.removeClass(g.looping))
                            },
                            transition: function() {
                                C.removeClass(g.visible).removeClass(g.hidden)
                            }
                        },
                        get: {
                            settings: function(t, i, o) {
                                return "object" == (void 0 === t ? "undefined" : n(t)) ? e.extend(!0, {}, e.fn.transition.settings, t) : "function" == typeof o ? e.extend({}, e.fn.transition.settings, {
                                    animation: t,
                                    onComplete: o,
                                    duration: i
                                }) : "string" == typeof i || "number" == typeof i ? e.extend({}, e.fn.transition.settings, {
                                    animation: t,
                                    duration: i
                                }) : "object" == (void 0 === i ? "undefined" : n(i)) ? e.extend({}, e.fn.transition.settings, i, {
                                    animation: t
                                }) : "function" == typeof i ? e.extend({}, e.fn.transition.settings, {
                                    animation: t,
                                    onComplete: i
                                }) : e.extend({}, e.fn.transition.settings, {
                                    animation: t
                                })
                            },
                            animationClass: function(e) {
                                var t = e || p.animation,
                                    n = w.can.transition() && !w.has.direction() ? w.get.direction() + " " : "";
                                return g.animating + " " + g.transition + " " + n + t
                            },
                            currentAnimation: function() {
                                return !(!w.cache || void 0 === w.cache.animation) && w.cache.animation
                            },
                            currentDirection: function() {
                                return w.is.inward() ? g.inward : g.outward
                            },
                            direction: function() {
                                return w.is.hidden() || !w.is.visible() ? g.inward : g.outward
                            },
                            animationDirection: function(t) {
                                var n;
                                return t = t || p.animation, "string" == typeof t && (t = t.split(" "), e.each(t, function(e, t) {
                                    t === g.inward ? n = g.inward : t === g.outward && (n = g.outward)
                                })), n || !1
                            },
                            duration: function(e) {
                                return e = e || p.duration, !1 === e && (e = C.css("animation-duration") || 0), "string" == typeof e ? e.indexOf("ms") > -1 ? parseFloat(e) : 1e3 * parseFloat(e) : e
                            },
                            displayType: function(e) {
                                return e = void 0 === e || e, p.displayType ? p.displayType : (e && void 0 === C.data(v.displayType) && w.can.transition(!0), C.data(v.displayType))
                            },
                            userStyle: function(e) {
                                return e = e || C.attr("style") || "", e.replace(/display.*?;/, "")
                            },
                            transitionExists: function(t) {
                                return e.fn.transition.exists[t]
                            },
                            animationStartEvent: function() {
                                var e, t = i.createElement("div"),
                                    n = {
                                        animation: "animationstart",
                                        OAnimation: "oAnimationStart",
                                        MozAnimation: "mozAnimationStart",
                                        WebkitAnimation: "webkitAnimationStart"
                                    };
                                for (e in n)
                                    if (void 0 !== t.style[e]) return n[e];
                                return !1
                            },
                            animationEndEvent: function() {
                                var e, t = i.createElement("div"),
                                    n = {
                                        animation: "animationend",
                                        OAnimation: "oAnimationEnd",
                                        MozAnimation: "mozAnimationEnd",
                                        WebkitAnimation: "webkitAnimationEnd"
                                    };
                                for (e in n)
                                    if (void 0 !== t.style[e]) return n[e];
                                return !1
                            }
                        },
                        can: {
                            transition: function(t) {
                                var n, i, o, r, a, s, l = p.animation,
                                    c = w.get.transitionExists(l),
                                    u = w.get.displayType(!1);
                                if (void 0 === c || t) {
                                    if (w.verbose("Determining whether animation exists"), n = C.attr("class"), i = C.prop("tagName"), o = e("<" + i + " />").addClass(n).insertAfter(C), r = o.addClass(l).removeClass(g.inward).removeClass(g.outward).addClass(g.animating).addClass(g.transition).css("animationName"), a = o.addClass(g.inward).css("animationName"), u || (u = o.attr("class", n).removeAttr("style").removeClass(g.hidden).removeClass(g.visible).show().css("display"), w.verbose("Determining final display state", u), w.save.displayType(u)), o.remove(), r != a) w.debug("Direction exists for animation", l), s = !0;
                                    else {
                                        if ("none" == r || !r) return void w.debug("No animation defined in css", l);
                                        w.debug("Static animation found", l, u), s = !1
                                    }
                                    w.save.transitionExists(l, s)
                                }
                                return void 0 !== c ? c : s
                            },
                            animate: function() {
                                return void 0 !== w.can.transition()
                            }
                        },
                        is: {
                            animating: function() {
                                return C.hasClass(g.animating)
                            },
                            inward: function() {
                                return C.hasClass(g.inward)
                            },
                            outward: function() {
                                return C.hasClass(g.outward)
                            },
                            looping: function() {
                                return C.hasClass(g.looping)
                            },
                            occurring: function(e) {
                                return e = e || p.animation, e = "." + e.replace(" ", "."), C.filter(e).length > 0
                            },
                            visible: function() {
                                return C.is(":visible")
                            },
                            hidden: function() {
                                return "hidden" === C.css("visibility")
                            },
                            supported: function() {
                                return !1 !== b
                            }
                        },
                        hide: function() {
                            w.verbose("Hiding element"), w.is.animating() && w.reset(), k.blur(), w.remove.display(), w.remove.visible(), w.set.hidden(), w.force.hidden(), p.onHide.call(k), p.onComplete.call(k)
                        },
                        show: function(e) {
                            w.verbose("Showing element", e), w.remove.hidden(), w.set.visible(), w.force.visible(), p.onShow.call(k), p.onComplete.call(k)
                        },
                        toggle: function() {
                            w.is.visible() ? w.hide() : w.show()
                        },
                        stop: function() {
                            w.debug("Stopping current animation"), C.triggerHandler(b)
                        },
                        stopAll: function() {
                            w.debug("Stopping all animation"), w.remove.queueCallback(), C.triggerHandler(b)
                        },
                        clear: {
                            queue: function() {
                                w.debug("Clearing animation queue"), w.remove.queueCallback()
                            }
                        },
                        enable: function() {
                            w.verbose("Starting animation"), C.removeClass(g.disabled)
                        },
                        disable: function() {
                            w.debug("Stopping animation"), C.addClass(g.disabled)
                        },
                        setting: function(t, n) {
                            if (w.debug("Changing setting", t, n), e.isPlainObject(t)) e.extend(!0, p, t);
                            else {
                                if (void 0 === n) return p[t];
                                e.isPlainObject(p[t]) ? e.extend(!0, p[t], n) : p[t] = n
                            }
                        },
                        internal: function(t, n) {
                            if (e.isPlainObject(t)) e.extend(!0, w, t);
                            else {
                                if (void 0 === n) return w[t];
                                w[t] = n
                            }
                        },
                        debug: function() {
                            !p.silent && p.debug && (p.performance ? w.performance.log(arguments) : (w.debug = Function.prototype.bind.call(console.info, console, p.name + ":"), w.debug.apply(console, arguments)))
                        },
                        verbose: function() {
                            !p.silent && p.verbose && p.debug && (p.performance ? w.performance.log(arguments) : (w.verbose = Function.prototype.bind.call(console.info, console, p.name + ":"), w.verbose.apply(console, arguments)))
                        },
                        error: function() {
                            p.silent || (w.error = Function.prototype.bind.call(console.error, console, p.name + ":"), w.error.apply(console, arguments))
                        },
                        performance: {
                            log: function(e) {
                                var t, n, i;
                                p.performance && (t = (new Date).getTime(), i = s || t, n = t - i, s = t, l.push({
                                    Name: e[0],
                                    Arguments: [].slice.call(e, 1) || "",
                                    Element: k,
                                    "Execution Time": n
                                })), clearTimeout(w.performance.timer), w.performance.timer = setTimeout(w.performance.display, 500)
                            },
                            display: function() {
                                var t = p.name + ":",
                                    n = 0;
                                s = !1, clearTimeout(w.performance.timer), e.each(l, function(e, t) {
                                    n += t["Execution Time"]
                                }), t += " " + n + "ms", a && (t += " '" + a + "'"), r.length > 1 && (t += " (" + r.length + ")"), (void 0 !== console.group || void 0 !== console.table) && l.length > 0 && (console.table || e.each(l, function(e, t) {})), l = []
                            }
                        },
                        invoke: function(t, n, i) {
                            var r, a, s, l = h;
                            return n = n || d, i = k || i, "string" == typeof t && void 0 !== l && (t = t.split(/[\. ]/), r = t.length - 1, e.each(t, function(n, i) {
                                var o = n != r ? i + t[n + 1].charAt(0).toUpperCase() + t[n + 1].slice(1) : t;
                                if (e.isPlainObject(l[o]) && n != r) l = l[o];
                                else {
                                    if (void 0 !== l[o]) return a = l[o], !1;
                                    if (!e.isPlainObject(l[i]) || n == r) return void 0 !== l[i] && (a = l[i], !1);
                                    l = l[i]
                                }
                            })), e.isFunction(a) ? s = a.apply(i, n) : void 0 !== a && (s = a), e.isArray(o) ? o.push(s) : void 0 !== o ? o = [o, s] : void 0 !== s && (o = s), void 0 !== a && a
                        }
                    }, w.initialize()
                }), void 0 !== o ? o : this
            }, e.fn.transition.exists = {}, e.fn.transition.settings = {
                name: "Transition",
                silent: !1,
                debug: !1,
                verbose: !1,
                performance: !0,
                namespace: "transition",
                interval: 0,
                reverse: "auto",
                onStart: function() {},
                onComplete: function() {},
                onShow: function() {},
                onHide: function() {},
                useFailSafe: !0,
                failSafeDelay: 100,
                allowRepeats: !1,
                displayType: !1,
                animation: "fade",
                duration: !1,
                queue: !0,
                metadata: {
                    displayType: "display"
                },
                className: {
                    animating: "animating",
                    disabled: "disabled",
                    hidden: "hidden",
                    inward: "in",
                    loading: "loading",
                    looping: "looping",
                    outward: "out",
                    transition: "transition",
                    visible: "visible"
                },
                error: {
                    noAnimation: "Element is no longer attached to DOM. Unable to animate.  Use silent setting to surpress this warning in production.",
                    repeated: "That animation is already occurring, cancelling repeated animation",
                    method: "The method you called is not defined",
                    support: "This browser does not support CSS animations"
                }
            }
        }(jQuery, window, document)
    },
    "sV/x": function(e, t, n) {
        n("WRGp"), n("OQde")
    },
    xZZD: function(e, t) {}
});