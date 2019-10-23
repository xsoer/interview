* 基本数据类型？
    * Undefined、Null、Boolean、Number、String、ECMAScript 2015 新增:Symbol(创建后独一无二且不可变的数据类型 )
* 介绍js有哪些内置对象？
    * Object 是 JavaScript 中所有对象的父对象
    * 数据封装类对象：Object、Array、Boolean、Number 和 String
    * 其他对象：Function、Arguments、Math、Date、RegExp、Error
* null，undefined 的区别？
    * null         表示一个对象是“没有值”的值，也就是值为“空”；
    * undefined     表示一个变量声明了没有初始化(赋值)；
    * undefined不是一个有效的JSON，而null是；
    * undefined的类型(typeof)是undefined；
    * null的类型(typeof)是object；
    * Javascript将未赋值的变量默认值设为undefined；
    * Javascript从来不会将变量设为null。它是用来让程序员表明某个用var声明的变量时没有值的。
    *  注意：
        * 在验证null时，一定要使用　=== ，因为 == 无法分别 null 和　undefined
        * null == undefined // true
        * null === undefined // false
* 使用 typeof bar === "object" 判断 bar 是不是一个对象有神马潜在的弊端？如何避免这种弊端？
//使用 typeof 的弊端是显而易见的(这种弊端同使用 instanceof)：
let obj = {};
let arr = [];
console.log(typeof obj === 'object');  //true
console.log(typeof arr === 'object');  //true
console.log(typeof null === 'object');  //true
//从上面的输出结果可知，typeof bar === "object" 并不能准确判断 bar 就是一个 Object。可以通过 Object.prototype.toString.call(bar) === "[object Object]" 来避免这种弊端：
let obj = {};
let arr = [];
console.log(Object.prototype.toString.call(obj));  //[object Object]
console.log(Object.prototype.toString.call(arr));  //[object Array]
console.log(Object.prototype.toString.call(null));  //[object Null]
//而 [] === false 是返回 false 的。
*
- #### JavaScript有几种类型的值？，你能画一下他们的内存图吗？
  * 栈：原始数据类型（Undefined，Null，Boolean，Number、String）
  * 堆：引用数据类型（对象、数组和函数）
  * 两种类型的区别是：存储位置不同；
     - 原始数据类型直接存储在栈(stack)中的简单数据段，占据空间小、大小固定，属于被频繁使用数据，所以放入栈中存储；
     - 引用数据类型存储在堆(heap)中的对象,占据空间大、大小不固定。如果存储在栈中，将会影响程序运行的性能；引用数据类型在栈中存储了指针，该指针指向堆中该实体的起始地址。当解释器寻找引用值时，会首先检索其在栈中的地址，取得地址后从堆中获得实体
- #### 如何将字符串转化为数字，例如'12.3b'?
  * parseFloat('12.3b');
  * 正则表达式，'12.3b'.match(/(\d)+(\.)?(\d)+/g)[0] * 1, 但是这个不太靠谱，提供一种思路而已。
  * 如何验证非空
- #### 定时器
- #### 异步与同步请求如何实现？
- #### 什么是window对象? 什么是document对象?
  * window对象是指浏览器打开的窗口。
  * document对象是Documentd对象（HTML 文档对象）的一个只读引用，window对象的一个属性。
- #### cookie 和session 的区别？
  * 1.cookie数据存放在客户的浏览器上，session数据放在服务器上。
  * 2.cookie不是很安全，别人可以分析存放在本地的COOKIE并进行COOKIE欺骗。考虑到安全应当使用session。
  * 3.session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能。考虑到减轻服务器性能方面，应当使用COOKIE。
  * 4.单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie。
  * 5.所以个人建议：将登陆信息等重要信息存放为SESSION;其他信息如果需要保留，可以放在COOKIE中
- #### cookie、sessionStorage、localStorage区别？
    * cookie是网站为了标示用户身份而储存在用户本地终端（Client Side）上的数据（通常经过加密）。
    * cookie数据始终在同源的http请求中携带（即使不需要），记会在浏览器和服务器间来回传递。
    *sessionStorage和localStorage不会自动把数据发给服务器，仅在本地保存。
    * 存储大小：
      cookie数据大小不能超过4k。
      sessionStorage和localStorage 虽然也有存储大小的限制，但比cookie大得多，可以达到5M或更大。
    * 有期时间：
      localStorage 存储持久数据，浏览器关闭后数据不丢失除非主动删除数据；
      sessionStorage 数据在当前浏览器窗口关闭后自动删除。
      cookie 设置的cookie过期时间之前一直有效，即使窗口或浏览器关闭
- #### 请解释一下 JavaScript 的同源策略。
  * 概念:同源策略是客户端脚本（尤其是Javascript）的重要的安全度量标准。它最早出自Netscape Navigator2.0，其目的是防止某个文档或脚本从多个不同源装载。
  * 这里的同源策略指的是：协议，域名，端口相同，同源策略是一种安全协议。
  * 指一段脚本只能读取来自同一来源的窗口和文档的属性。
- #### 如何判断在数组中是否存在
  indexOf
- #### 如何判断一个对象是否属于某个类？
  * 使用instanceof
- #### for in和for of的区别
- #### 数组转字符串(join)；字符串转数组(split(''))
- #### 你有用过哪些前端性能优化的方法？
  *(1） 减少http请求次数：CSS Sprites, JS、CSS源码压缩、图片大小控制合适；网页Gzip，CDN托管，data缓存 ，图片服务器。
  *（2） 前端模板 JS+数据，减少由于HTML标签导致的带宽浪费，前端用变量保存AJAX请求结果，每次操作本地变量，不用请求，减少请求次数
  *（3） 用innerHTML代替DOM操作，减少DOM操作次数，优化javascript性能。
  *（4） 当需要设置的样式很多时设置className而不是直接操作style。
  *（5） 少用全局变量、缓存DOM节点查找的结果。减少IO读取操作。
  *（6） 避免使用CSS Expression（css表达式)又称Dynamic properties(动态属性)。
  *（7） 图片预加载，将样式表放在顶部，将脚本放在底部 加上时间戳。
  *（8） 避免在页面的主体布局中使用table，table要等其中的内容完全下载之后才会显示出来，显示比div+css布局慢。
  * 对普通的网站有一个统一的思路，就是尽量向前端优化、减少数据库操作、减少磁盘IO。向前端优化指的是，在不影响功能和体验的情况下，能在浏览器执行的不要在服务端执行，能在缓存服务器上直接返回的不要到应用服务器，程序能直接取得的结果不要到外部取得，本机内能取得的数据不要到远程取，内存能取到的不要到磁盘取，缓存中有的不要去数据库查询。减少数据库操作指减少更新次数、缓存结果减少查询次数、将数据库执行的操作尽可能的让你的程序完成（例如join查询），减少磁盘IO指尽量不使用文件系统作为缓存、减少读写文件次数等。程序优化永远要优化慢的部分，换语言是无法“优化”的。
- #### jQuery 的属性拷贝(extend)的实现原理是什么，如何实现深拷贝？
- #### js延迟加载的方式有哪些？
  *  defer和async、动态创建DOM方式（用得最多）、按需异步载入js
- #### axios有哪些方法、参数？
- #### ajax请求头部携带cookie
```
import axios from 'axios'
axios.defaults.withCredentials=true;//让ajax携带cookie
Vue.prototype.$axios = axios;
```

## react
- #### React 中 Element 与 Component 的区别是？
- #### React 中 refs 的作用是什么？
  * Refs 是 React 提供给我们的安全访问 DOM 元素或者某个组件实例的句柄。我们可以为元素添加ref属性然后在回调函数中接受该元素在 DOM 树中的句柄，该值会作为回调函数的第一个参数返回：
- #### createElement 与 cloneElement 的区别是什么？
  * createElement 函数是 JSX 编译之后使用的创建 React Element 的函数，而 cloneElement 则是用于复制某个元素并传入新的 Props。
- #### 组件的生命周期有哪些？
  * 组件的声明周期有三种阶段，一种是初始化阶段（Mounting），一种是更新阶段（Updating）最后一种是析构阶段（Unmounting）。而这两个阶段的声明周期函数都是相似且有一一对应的关系的
- #### 什么时候使用 Class Component 而非 Functional Component?
  * 如果你的组件有state或者使用了生命周期函数，那么请使用Class component。 否则，使用Functional component。
- 什么是keys 而且为什么他们很重要
  * Keys负责帮助React跟踪列表中哪些元素被改变/添加/移除。

## vue
- ####1.请谈谈Vue中的MVVM模式
  * MVVM全称是Model-View-ViewModel
  * Vue是以数据为驱动的，Vue自身将DOM和数据进行绑定，一旦创建绑定，DOM和数据将保持同步，每当数据发生变化，DOM会跟着变化。 ViewModel是Vue的核心，它是Vue的一个实例。Vue实例时作用域某个HTML元素上的这个HTML元素可以是body，也可以是某个id所指代的元素。
  * DOMListeners和DataBindings是实现双向绑定的关键。DOMListeners监听页面所有View层DOM元素的变化，当发生变化，Model层的数据随之变化；DataBindings监听Model层的数据，当数据发生变化，View层的DOM元素随之变化。
- ####2.v-show和v-if指令的共同点和不同点?
  * v-show指令是通过修改元素的displayCSS属性让其显示或者隐藏
  * v-if指令是直接销毁和重建DOM达到让元素显示和隐藏的效果
- ####3.如何让CSS只在当前组件中起作用?
  * 将当前组件的``<style>``修改为``<style scoped>``
- ####4.Vue中引入组件的步骤?
  * 1.采用ES6的import ... from ...语法或CommonJS的require()方法引入组件
  * 2.对组件进行注册,代码如下
  * 3.使用组件<my-component></my-component>
```js
// 注册
Vue.component('my-component', {
  template: '<div>A custom component!</div>'
})
```

- #### 组件间如何传递值或调用
- ####5.在Vue中使用插件的步骤
  * 采用ES6的import ... from ...语法或CommonJS的require()方法引入插件
  * 使用全局方法Vue.use( plugin )使用插件,可以传入一个选项对象Vue.use(MyPlugin, { someOption: true })
- ####6.请列举出3个Vue中常用的生命周期钩子函数?
  * created: 实例已经创建完成之后调用,在这一步,实例已经完成数据观测, 属性和方法的运算, watch/event事件回调. 然而, 挂载阶段还没有开始, $el属性目前还不可见
  * mounted:  el被新创建的 vm.$el 替换，并挂载到实例上去之后调用该钩子。如果 root 实例挂载了一个文档内元素，当 mounted 被调用时 vm.$el 也在文档内。
  * activated: keep-alive组件激活时调用
- ####7.请简述下Vuex的原理和使用方法
  * 数据单向流动
  * 一个应用可以看作是由上面三部分组成: View, Actions,State,数据的流动也是从View => Actions => State =>View 以此达到数据的单向流动.但是项目较大的, 组件嵌套过多的时候, 多组件共享同一个State会在数据传递时出现很多问题.Vuex就是为了解决这些问题而产生的.
  * Vuex可以被看作项目中所有组件的数据中心,我们将所有组件中共享的State抽离出来,任何组件都可以访问和操作我们的数据中心.

  * 上图可以很好的说明Vuex的组成,一个实例化的Vuex.Store由state, mutations和actions三个属性组成:
    - state中保存着共有数据
    - 改变state中的数据有且只有通过mutations中的方法,且mutations中的方法必须是同步的
    - 如果要写异步的方法,需要些在actions中, 并通过commit到mutations中进行state中数据的更改.
