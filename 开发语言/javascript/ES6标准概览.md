# ES6标准概览

- 作者：codehackfox@gmail.com
- 时间：2019-03-10 19:58:51

> ## 0x00、变量

> 新增两个关键字：let、const

- let与var的区别

  - 作用域不同()
  - 变量是否可以提升不

- contst：只读不可改，声明即赋值 其所声明的对象的属性是可以改变的。

>## 0x01、箭头函数

>## 0x02、字符串

- 模版字符串(``)
- 新增几个方法

```javascript
'my string'.startsWith('my'); //true
'my string'.endsWith('my'); // false
'my string'.includes('str'); // true
'my '.repeat(3); // 'my my my '
```

>## 0x03、数组

> Array 对象增加了一些新的静态方法，Array 原型上也增加了一些新方法

- from 从类数组和可遍历对象中创建 Array 的实例
- find 返回回调返回 true 的第一个元素。

```javascript
[9, 2, 10, 8].find(n => n === 10) // 10
```

- findIndex 返回回调函数返回 true的第一个元素的下标。

```javascript
[5, 1, 10, 8].findIndex(n => n === 10) // 2
```

- fill 用所给参数"覆盖"数组的元素。

```javascript
[0, 0, 0].fill(7) // [7, 7, 7]
[0, 0, 0, 0, 0].fill(7, 1, 3) // [0, 7, 7, 7, 0]
```

>## 0x04、新增Map和Set结构

>## 0x05、Math新增几个方法

- Math.sign 返回数字的符号，结果为 1、-1 或 0。
- Math.trunc 返回无小数位的数字
- Math.cbrt 返回数字的立方根。

```javascript
Math.sign(5); // 1
Math.sign(-9); // -1

Math.trunc(5.9); // 5
Math.trunc(5.123); // 5

Math.cbrt(64); // 4
```

>## 0x06、扩展运算符(...)

```javascript
let values = [1, 2, 4];
let some = [...values, 8]; // [1, 2, 4, 8]
let more = [...values, 8, ...values]; // [1, 2, 4, 8, 1, 2, 4]

// ES5 equivalent:
let values = [1, 2, 4];
// Iterate, push, sweat, repeat...
// Iterate, push, sweat, repeat...
```

扩展语法在传参数调用函数时也非常有用

```javascript
let values = [1, 2, 4];

doSomething(...values);

function doSomething(x, y, z) {
   // x = 1, y = 2, z = 4
}

// ES5 equivalent:
doSomething.apply(null, values);
```

>## 0x07、解构赋值

```javascript
let [x, y] = [1, 2]; // x = 1, y = 2

// ES5 equivalent:
var arr = [1, 2];
var x = arr[0];
var y = arr[1];

//使用这个语法，可以一次性给多个变量赋值。一个很好的附加用处是可以很简单地交换变量值：
let x = 1,
    y = 2;

[x, y] = [y, x]; // x = 2, y = 1
//解构也可以用于对象。注意对象中必须存在对应的键：
let obj = {x: 1, y: 2};
let {x, y} = obj; // x = 1, y = 2
//你也可以使用该机制来修改变量名：
let obj = {x: 1, y: 2};
let {x: a, y: b} = obj; // a = 1, b = 2
//另一个有趣的模式是模拟多个返回值：
function doSomething() {
   return [1, 2]
}

let [x, y] = doSomething(); // x = 1, y = 2
//解构可以用来为参数对象赋默认值。通过对象字面量，可以模拟命名参数：
function doSomething({y = 1, z = 0}) {
   console.log(y, z);
}
doSomething({y: 2});
```

>## 0x08、参数

```javascript
//可以设置默认参数
function doSomething(x, y = 2) {
   return x * y;
}

doSomething(5); // 10
doSomething(5, undefined); // 10
doSomething(5, 3); // 15
//看起来很简洁，对吧？ 我肯定你之前在 ES5 中曾经需要给某些参数赋默认值：
function doSomething(x, y) {
   y = y === undefined ? 2 : y;
   return x * y;
}
```

>## 0x09、模块

```javascript
类的创建围绕 class 和 constructor 关键词。以下是个简短的示例：
class Vehicle {
   constructor(name) {
      this.name = name;
      this.kind = 'vehicle';
   }
   getName() {
      return this.name;
   }
}

// Create an instance
let myVehicle = new Vehicle('rocky');
```

注意类的定义不是一般的对象，因此，类的成员间没有逗号。 创造一个类的对象时，需要使用 new 关键词。继承一个基类时，使用 extends：

```javascript
class Car extends Vehicle {
   constructor(name) {
      super(name);
      this.kind = 'car'
   }
}

let myCar = new Car('bumpy');

myCar.getName(); // 'bumpy'
myCar instanceof Car; // true
myCar instanceof Vehicle; //true
```

从衍生类中，你可以使用从任何构造函数或方法中使用 super 来获取它的基类：

> 使用 super() 调用父类构造函数。 调用其它成员，举个例子，使用 super.getName() 。

>## 0x10、记号

> 记号是一个新的原生数据类型，像 Number 和 String 一样。你可以使用记号为对象属性创建唯一标识或创建唯一的常量。

```javascript
const MY_CONSTANT = Symbol();

let obj = {};
obj[MY_CONSTANT] = 1;

//记号与 const 配合很合适，因为它们都有不可改变的特性。
const CHINESE = Symbol();
const ENGLISH = Symbol();
const SPANISH = Symbol();

switch(language) {
   case CHINESE:
      //
      break;
   case ENGLISH:
      //
      break;
   case SPANISH:
      //
      break;
   default:
      //
      break;
}
//你可以为 symbol 添加描述。虽然不可以通过描述获取 symbol，但是可用于代码调试。
const CONST_1 = Symbol('my symbol');
const CONST_2 = Symbol('my symbol');

typeof CONST_1 === 'symbol'; // true

CONST_1 === CONST_2; // false
```
