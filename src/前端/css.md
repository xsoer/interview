CSS
* display:none和visibility:hidden的区别？
    * display:none 隐藏对应的元素，在文档布局中不再给它分配空间，它各边的元素会合拢，就当他从来不存在。
    * visibility:hidden 隐藏对应的元素，但是在文档布局中仍保留原来的空间。
*  CSS中link 和@import的区别是？
    *  (1) link属于HTML标签，而@import是CSS提供
    *  (2) 页面被加载的时，link会同时被加载，而@import被引用的CSS会等到引用它的CSS文件被加载完再加载;
    * (3) import只在IE5以上才能识别，而link是HTML标签，无兼容问题;
    * (4) link方式的样式的权重 高于@import的权重.
* CSS 选择符有哪些？哪些属性可以继承？优先级算法如何计算？ CSS3新增伪类有那些？
    * 选择符
        * 1.id选择器（ # myid）
        * 2.类选择器（.myclassname）
        * 3.标签选择器（div, h1, p）
        * 4.相邻选择器（h1 + p）
        * 5.子选择器（ul > li）
        * 6.后代选择器（li a）
        * 7.通配符选择器（ * ）
        * 8.属性选择器（a[rel = "external"]）
        * 9.伪类选择器（a: hover, li:nth-child）
    * 优先级原则
        * 优先级就近原则，同权重情况下样式定义最近者为准;
        * 载入样式以最后载入的定位为准;
    * 优先级为:
        * 同权重: 内联样式表（标签内部）> 嵌入样式表（当前文件中）> 外部样式表（外部文件中）。
        * !important > id > class > tag
        * important 比 内联优先级高
    * 可继承的样式： font-size font-family color, UL LI DL DD DT;
    * 不可继承的样式：border padding margin width height
* display有哪些值？说明他们的作用。
    * block     块类型。默认宽度为父元素宽度，可设置宽高，换行显示。
    * none     缺省值。象行内元素类型一样显示。
    * inline     行内元素类型。默认宽度为内容宽度，不可设置宽高，同行显示。
    *  inline-block 默认宽度为内容宽度，可以设置宽高，同行显示。
    * list-item     象块类型元素一样显示，并添加样式列表标记。
    * table     此元素会作为块级表格来显示。
    * inherit     规定应该从父元素继承 display 属性的值。
