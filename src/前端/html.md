HTML
* DOM操作——怎样添加、移除、移动、复制、创建和查找节点。
    *   1）创建新节点
        * createDocumentFragment() //创建一个DOM
        * createElement() //创建一个具体的
        * createTextNode() //创建一个文本节点
    *   2）添加、移除、替换、插入
        * appendChild()
        * removeChild()
        * replaceChild()
        * insertBefore() //并没有insertAfter()
    * 3）查找
        * getElementsByTagName() //通过标签名
        * getElementsByName() //通过元素的Name属性的值(IE容错能力较强，会得到一个数组，其中包括id等于name值的)
        * getElementById() //通过元素Id，唯一性
