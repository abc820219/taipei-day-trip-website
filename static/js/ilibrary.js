// 分析需要功能
// 降低難度chrome能跑就好
// 可以鍊式調用
// console.log封裝 $log
// XMLHttpRequest 封裝 $ajax
// html操作封裝   html removeChild append  prepend
// 事件綁定封裝   on
// input封裝      val
// css操作封裝    add remove toggle
// 分析構造函式寫法
// Jquery.prototype = {
//     // 構造函式
//     init: function (selector) {
//         let doms = document.querySelectorAll(selector)
//         let that = this
//         doms.forEach((dom, i) => {
//             that[i] = dom
//         })
// that.css = function (str) {
//     if (!doms.length) return
//     if (doms.length === 1) {
//         doms[0].classList.add(str)
//         return
//     }
//     doms.forEach(dom => {
//         dom.classList.add(str)
//     })
// }
// }
// }
;(function () {
    // log開不開
    let logIsOpen = true
    // 創建一Iquery個函式
    // 畫面
    let Iquery = function (selector) {
        // 返回函式prototype上的class實例
        let result = new Iquery.prototype.Init(selector)
        return result
    }
    // 把Iquery函式放置window全局中
    window.$ = window.Iquery = Iquery
    window.$log = function (message) {
        if (!logIsOpen) return
        window.console.log(message)
    }
    //  畫面功能封裝
    Iquery.prototype.Init = class Init {
        constructor(selector) {
            this.doms = document.querySelectorAll(selector)
            this.length = this.doms.length
            this.doms.forEach((element, i) => {
                this[i] = element
            })
            this.parse = new DOMParser()
        }
        each(fn) {
            this.doms.forEach((dom, i) => {
                fn(dom, i)
            })
        }
        // html區域
        // innerHTML
        html(str) {
            if (!this.doms.length) return
            if (this.doms.length === 1) {
                this.doms[0].innerHTML = str
                return
            }
            this.doms.forEach((dom) => {
                dom.innerHTML(str)
            })
        }
        // removeChild
        removeChild() {
            if (!this.doms.length) return
            if (this.doms.length === 1) {
                this.doms[0].parentNode.removeChild(this.doms[0])
                return
            }
            this.doms.forEach((dom) => {
                this.doms[0].parentNode.removeChild(dom)
            })
        }
        // appenChild
        append(domNode) {
            if (!this.doms.length) return
            domNode = this.parse.parseFromString(domNode, 'text/html')
            domNode = domNode.body.firstChild
            if (this.doms.length === 1) {
                this.doms[0].appendChild(domNode)
                return
            }
            this.doms.forEach((dom) => {
                dom.appendChild(domNode)
            })
        }
        // prepend
        prepend(dom) {
            if (!this.doms.length) return
            domNode = this.parse.parseFromString(domNode, 'text/html')
            domNode = domNode.body.firstChild
            if (this.doms.length === 1) {
                this.doms[0].prepend(dom)
                return
            }
            this.doms.forEach((dom) => {
                dom.prepend(dom)
            })
        }
        // 事件區域
        // addEventListener
        on(event, func) {
            // console.log(this.doms)
            if (!this.doms.length) return
            if (this.doms.length === 1) {
                this.doms[0].addEventListener(event, func)
                return
            }
            this.doms.forEach((dom) => {
                dom.addEventListener(event, func)
            })
        }
        // input
        // inputDom.value
        val(value) {
            if (!this.doms.length) return
            if (this.doms.length === 1) {
                if (value) {
                    return this.doms[0].value = value
                }
                return this.doms[0].value
            }
        }
        width() {
            if (!this.doms.length) return
            if (this.doms.length === 1) {
                return this.doms[0].offsetWidth
            }
        }
        // css樣式區域
        style(str) {
            if (!this.doms.length) return
            if (this.doms.length === 1) {
                this.doms[0].style[str.split(':')[0]] = str.split(':')[1]
                return
            }
            this.doms.forEach((dom) => {
                dom.style[str.split(':')[0]] = str.split(':')[1]
            })
        }
        // classList.add
        add(str) {
            if (!this.doms.length) return
            if (this.doms.length === 1) {
                this.doms[0].classList.add(str)
                return
            }
            this.doms.forEach((dom) => {
                dom.classList.add(str)
            })
        }
        // classList.remove
        remove(str) {
            if (!this.doms.length) return
            if (this.doms.length === 1) {
                this.doms[0].classList.remove(str)
                return
            }
            this.doms.forEach((dom) => {
                dom.classList.remove(str)
            })
        }
        // classList.toggle
        toggle(str) {
            if (!this.doms.length) return
            if (this.doms.length === 1) {
                this.doms[0].classList.toggle(str)
                return
            }
            this.doms.forEach((dom) => {
                dom.classList.toggle(str)
            })
        }
    }
    // api封裝
    // get / post
    Iquery.prototype.Ajax = class Ajax {
        constructor() {}
        get(url) {
            return new Promise((resolve, reject) => {
                let xhr = new XMLHttpRequest()
                xhr.open('GET', url, true)
                xhr.send()
                xhr.onload = function () {
                    let res = {
                        data: JSON.parse(this.responseText),
                    }
                    resolve(res)
                }
                xhr.onerror = function () {
                    let res = {
                        data: JSON.parse(this.responseText),
                    }
                    reject(res)
                }
                xhr.e
            })
        }
    }
    window.$ajax = new Iquery.prototype.Ajax()
})()
