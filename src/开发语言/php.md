1. 数组操作函数
2. 字符串操作函数（数组和字符串的函数是最常问的，非常多，一定不要记混了）
3. 指针和引用区别
4. 堆和栈的区别
5. == ===区别
6. PHP的垃圾回收机制
7. zval结构
8. 防sql注入
9. 跨域问题
10. 长链接和长轮询


* 1.php数组函数常见的那些?并说出使用方法 (array_merge、in_array的作用)
// 遍历数组
list();  //不是真正的函数，而是PHP的语言结构，用于给一组变量赋值，仅能用于索引数组
foreach();  //返回数组当前元素的键值对，并将指针移动到下一个元素位置
while(); //可配合list或each使用：while(list($key, $value) = each($arr)){each $key, $value; }
//数组内部指针控制
current();  //读取指针位置的内容
key();      //读取当前指针指向内容的索引值
next();     //将数组中的内部指针指向下一单元
prev();     //将数组内部指针倒回一位
end();      //将数组内部指针指向最后一个元素
reset();    //将目前指针指向第一个索引位置
//数组键值操作函数
array_values($arr);       //获得数组的值
array_keys($arr);         //获得数组的键名
array_flip($arr);         //数组中的值与键名互换（如果有重复前面的会被后面的覆盖）
array_search('PHP',$arr); //检索给定的值，加true则是严格类型检查
array_reverse($arr);      //将数组中的元素翻转(前后顺序)
in_array("apple", $arr);  //在数组中检索apple
array_key_exists("apple", $arr); // 检索给定的键名是否存在数组中
array_count_values($arr);        // 统计数组中所有值出现的次数
array_unique($arr);              // 删除数组中重复的值
//数组回调函数
array_filter(); //使用回调函数过滤数组中的元素，如果回调返回true则当前的元素被包含到返回数组中
array_walk();   //回调函数处理数组，自定义函数要有两个参数，本函数第三个参数可以作为回调第三个参数返回
array_map();    //可以处理多个数组，每个数组的长度应该相同，传入数组的个数和回调函数参数个数应该一致
//数组的分段和填充
array_slice($arr, 0, 3);    //将数组中的一段取出，此函数忽略键名（数组的分段）
array_splice($arr, 0, 3，array("black","maroon"));    //将数组中的一段取出，返回的序列从原数组中删除
array_chunk($arr, 3, TRUE);   //将一个数组分割成多个，TRUE为保留原数组的键名（分割多个数组）
//数组与栈，列队
array_push($arr, "apple", "pear");    //将一个或多个元素压入数组栈的末尾（入栈），返回入栈元素的个数
array_pop($arr);    // 将数组栈的最后一个元素弹出（出栈）
array_shift($arr);   //数组中第一个元素移出并返回（长度减1，其他元素向前移动一位，数字键名改为从零计数，文字键名不变）
array_unshift($arr,"a",array(1,2));  //在数组的开头插入一个或多个元素
//数组的排序
sort($arr);      //由小到大，忽略键名
rsort($arr);     //由大到小，忽略键名
asort($arr);     //由小到大，保留键名
arsort($arr);    //由大到小，保留键名
ksort($arr);     //按照键名正序排序
krsort($arr);    //按照键名逆序排序
//数组的计算
array_sum($arr);   //对数组内部的所有元素做求和运算（数组元素的求和）
array_merge($arr1, $arr2); //合并两个或多个（相同字符串键名，后面覆盖前面，相同的数字键名，后面的附加到后面）
array_diff($arr1, $arr2);       //返回差集结果数组
array_diff_assoc($arr1, $arr2, $arr3);  //返回差集结果数组，键名也做比较
array_intersect($arr1, $arr2);  //返回交集结果数组
array_intersect_assoc($arr1, $arr2);   //返回交集结果数组，键名也做比较
//其他的数组函数
array_unique($arr);   //移除数组中重复的值，新的数组中会保留原始的键名
shuffle($arr);        // 将数组的顺序打乱
* 2.PHP中几个输出函数echo，print()，print_r()，sprintf()，var_dump()的区别
    * echo：是语句不是函数，没有返回值，可输出多个变量值，不需要圆括号。不能输出数组和对象，只能打印简单类型(如int,string)。
    * print：是语句不是函数，有返回值 1 ，只能输出一个变量，不需要圆括号。不能输出数组和对象，只能打印简单类型(如int,string)。
    * print_r：是函数，可以打印复合类型，例如：stirng、int、float、array、object等，输出array时会用结构表示，而且可以通过print_r($str,true)来使print_r不输出而返回print_r处理后的值
    * printf：是函数，有返回值，返回值是打印内容的长度，把文字格式化以后输出（参看C语言）
    * sprintf：是函数，跟printf相似，但不打印，而是返回格式化后的文字（该函数把格式化的字符串写写入一个变量中，而不是输出来），其    他的与printf一样。
    * var_dump()：函数，输出变量的内容、类型或字符串的内容、类型、长度。常用来调试。
* 3.不用新变量直接交换现有两个变量的值
// 1
 list($a, $b) = array($b, $a);
//2
$a = $a . $b;
$b = strlen( $b );
$b = substr( $a, 0, (strlen($a) – $b ) );
$a = substr( $a, strlen($b) );
//3
$a = $b.','.$a ;
$a = explode(',', $a);
$b = $a[1];
$a = $a[0];
//这个是当两个数都是数字的时候:
$a = $a + $b;
$b = $a – $b;
$a = $a – $b;
//借助数组
$a = array($a,$b);
$b = $a[0];
$a = $a[1];
* 4.写个函数来解决多线程同时读写一个文件的问题。
<?php
     $fp = fopen("/tmp/lock.txt","w+");
     if(flock($fp, LOCK_EX)){// 进行排它型锁定
         fwrite($fp,"Write something here\n");
         flock($fp, LOCK_UN);// 释放锁定
     }else{
         echo "Couldn't lock the file !";
     }
     fclose($fp);
* 5.禁掉cookie的session使用方案，设置session过期的方法，对应函数
    * 通过 url 传值，把session id附加到url上（缺点：整个站点中不能有纯静态页面，因为纯静态页面session id 将无法继续传到下一页面）
    * 通过隐藏表单，把session id 放到表单的隐藏文本框中同表单一块提交过去（缺点：不适用<a>标签这种直接跳转的非表单的情况）
    * 直接配置php.ini文件,将php.ini文件里的session.use_trans_sid= 0设为1,（好像在win上不支持）
    * 用文件、数据库等形式保存Session ID，在跨页过程中手动调用
//第一种  setcookie() 直接用setcookie设置session id的生命周期。
$lifetime=60; //保存1分钟
session_start();
setcookie(session_name(), session_id(), time()+$lifetime, "/");
//第二种  session_set_cookie_params()
$lifetime=60;//保存1分钟
session_set_cookie_params($lifetime);
session_start();
session_regenerate_id(true);
//其中session_regenerate_id();方法用于改变当前session_id的值，并保留session中数组的值。参数默认为 false,如果设置为true则改变session_id的值，并清空当前session数组。
* 6.php获取文件内容的方法，对应的函数
    * file_get_contents得到文件的内容（可以以get和post的方式获取），整个文件读入一个字符串中
    * 用fopen打开url, 以get方式获取内容（借助fgets()函数）
    * 用fsockopen函数打开url（可以以get和post的方式获取），以get方式获取完整的数据，包括header和body
    * 使用curl库获取内容，使用curl库之前，需要查看php.ini，查看是否已经打开了curl扩展
* 7.php魔术方法与魔术常量
    * 类方法：
        * 1、__construct();
            * 说明：具有构造函数的类会在每次创建新对象时先调用此方法，适合在使用对象之前做一些初始化工作。如果子类中定义了构造函数则不会隐式调用其父类的构造函数。要执行父类的构造函数，需要在子类的构造函数中调用 parent::__construct()。如果子类没有定义构造函数则会如同一个普通的类方法一样从父类继承。
        * 2、__destruct();
            * 说明：析构函数会在到某个对象的所有引用都被删除或者当对象被显式销毁时执行。
    * 方法重载：
        * 3、__call();
            * 说明：在对象中调用一个不可访问方法时，__call(); 方法会被调用。
        * 4、__callStatic();
            * 说明：用静态方式中调用一个不可访问方法时，__callStatic(); 方法会被调用。
    * 属性重载：(只对类中私有受保护的成员属性有效)
        * 5、__get();
            * 说明：读取不可访问属性的值时，__get() 会被调用。
        * 6、__set();
            * 说明：在给不可访问属性赋值时，__set() 会被调用。
        * 7、__isset();
            * 说明：当对不可访问属性调用 isset() 或 empty() 时，__isset() 会被调用。
        * 8、__unset();
            * 说明：当对不可访问属性调用 unset() 时，__unset() 会被调用。
    * 序列化相关：
        * 9、__sleep();
            * 说明：序列化时调用，serialize() 函数会检查类中是否存在该魔术方法。如果存在，该方法会先被调用，然后才执行序列化操作。
        *  10、__wakeup();
            * 说明：unserialize() 会检查是否存在一个 __wakeup() 方法。如果存在，则会先调用该方法，用在反序列化操作中，例如重新建立数据库连接，或执行其它初始化操作
    * 操作类和对象方法：
        * 11、__toString();
            * 说明：方法用于一个类被当成字符串时调用，例如把一个类当做字符串进行输出
        * 12、__invoke()；
            * 说明：当尝试以调用函数的方式调用一个对象时，__invoke() 方法会被自动调用。
        * 13、__set_state()；
            * 说明：当调用 var_export() 导出类时，此静态 方法会被调用。 本方法的唯一参数是一个数组
        * 14、__clone();
            * 说明：当复制完成时，如果定义了 __clone() 方法，则新创建的对象（复制生成的对象）中的 __clone() 方法会被调用，可用于修改属性的值。
        * 15、__autoload();
            * 说明：该方法可以自动实例化需要的类。当程序要用一个类但没有被实例化时，改方法在指定路径下查找和该类名称相同的文件。否则报错。
        * 16 __debugInfo();
            * 说明：php5.6增加的特性，var_dump()一个类时触发，返回一个包含对象属性的数组
    * 常量：
        * __LINK__      //文件中的当前行号。
        * __FILE__       //文件的完整路径和文件名。如果用在被包含文件中，则返回被包含的文件名。
        * __DIR__       //文件所在的目录。如果用在被包括文件中，则返回被包括的文件所在的目录，它等价于 dirname(__FILE__)。
        * __FUNCTION__       //函数名称。自 PHP 5 起本常量返回该函数被定义时的名字（区分大小写）。在 PHP 4 中该值总是小写字母的。
        *  __CLASS__              //类的名称。自 PHP 5 起本常量返回该类被定义时的名字（区分大小写）。在 PHP 4 中该值总是小写字母的。
        *  __METHOD__         //类的方法名（PHP 5.0.0 新加）。返回该方法被定义时的名字（区分大小写）。
        *  __NAMESPACE__   //当前命名空间的名称（大小写敏感）。这个常量是在编译时定义的（PHP 5.3.0 新增)
* 8.PHP 如何获取客户端的IP地址
    * 用$_SERVER获取的IP地址有什么问题？
    * $_SERVER['REMOTE_ADDR'] ;   通过全局数组来获得
    * getenv('REMOTE_ADDR') ; 通过环境变量来获得
    * 当客户机使用代理的时候获取不到真实的IP地址
* 9.写一个函数，可以遍历文件夹下的所有文件和文件夹。
 function get_dir_info($path){
   $handle = opendir($path);//打开目录返回句柄
   while(($content = readdir($handle))!== false){
       $new_dir = $path . DIRECTORY_SEPARATOR . $content;
       if($content == '..' || $content == '.'){
          continue;
       }
       if(is_dir($new_dir)){
           echo “
目录：".$new_dir . ‘
';
           get_dir_info($new_dir);
       }else{
           echo "文件：".$path.':'.$content .'';
       }
   }
}
get_dir_info($dir);
* 10.PHP缓存技术有哪些?
    *  全页面静态化缓存，也就是将页面全部生成html静态页面，用户访问时直接访问的静态页面，而不会去走php服务器解析的流程
    * 页面部分缓存，将一个页面中不经常变的部分进行静态缓存，而经常变化的块不缓存，最后组装在一起显示
    * 数据缓存，通过一个id进行请求的数据,将数据缓存到一个php文件中,id和文件是对应的,下次通过这个id进行请求时 直接读php文件
    * 查询缓存，和数据缓存差不多,根据查询语句进行缓存;
    * 常用的缓存技术有：redis和memcache
* 11.strlen()与mb_strlen的作用与区别
    * 在PHP中，strlen与mb_strlen是求字符串长度的函数
    * PHP内置的字符串长度函数strlen无法正确处理中文字符串，它得到的只是字符串所占的字节数。对于GB2312的中文编码，strlen得到的值是汉字个数的2倍，而对于UTF-8编码的中文，就是3倍（在 UTF-8编码下，一个汉字占3个字节）。
    * 采用mb_strlen函数可以较好地解决这个问题。mb_strlen的用法和strlen类似，只不过它有第二个可选参数用于指定字符编码。例如得到UTF-8的字符串
    * str长度，可以用mbstrlen(str,'UTF-8')。如果省略第二个参数，则会使用PHP的内部编码。内部编码可以通过 mb_internal_encoding()函数得到。
    * 需要注意的是，mb_strlen并不是PHP核心函数，使用前需要确保在php.ini中加载了php_mbstring.dll，即保“extension=php_mbstring.dll”这一行存在并且没有被注释掉，否则会出现未定义函 数的问题。
* 12.写一个函数，尽可能高效的从一个标准url中取出扩展名
$arr = parse_url('http://www.sina.com.cn/abc/de/fg.php?id=1');
result=pathinfo(arr['path']);
var_dump($arr);
var_dump($result['extension']);
* 13.php.ini 中safe mod关闭 影响哪些函数和参数，至少写6个？
move_uploaded_file()     exec()    system()   passthru()   popen()   fopen()  mkdir()    rmdir()  rename()                     unlink()  copy()      chgrp()    chown()   chmod()     touch()  symlink()    link()  parse_ini_file()
set_time_limit()  max_execution_time mail()
* 14.isset() 、empty()与is_null的区别
    * 当变量未定义时，is_null() 和“参数本身”是不允许作为参数判断的，会报Notice警告错误；
    * empty , isset首先都会检查变量是否存在，然后对变量值进行检测。而is_null 和 “参数本身”只是直接检查变量值，是否为null，因此如果变量未定义就会出现错误！
    * isset()：仅当null和未定义，返回false；
    * empty()：""、0、"0"、NULL、FALSE、array(),未定义，均返回true；
    * is_null()：仅判断是否为null，未定义报警告；
    * 变量本身作为参数，与empty()一致，但接受未定义变量时，报警告；
* 15.MVC是什么，有什么优缺点
    *  MVC的优点
        * （1） 可以为一个模型在运行时同时建立和使用多个视图。变化-传播机制可以确保所有相关的视图及时得到模型数据变化，从而使所有关联的视图和控制器做到行为
        * （2） 视图与控制器的可接插性，允许更换视图和控制器对象，而且可以根据需求动态的打开或关闭、甚至在运行期间进行对象
        * （3） 模型的可移植性。因为模型是独立于视图的，所以可以把一个模型独立地移植到新的平台工作。需要做的只是在新平台上对视图和控制器进行新的
        * （4） 潜在的框架结构。可以基于此模型建立应用程序框架，不仅仅是用在设计界面的设计中。
    * 2、 MVC的不足之
        * （1） 增加了系统结构和实现的复杂性。对于简单的界面，严格遵循MVC，使模型、视图与控制器分离，会增加结构的复杂性，并可能产生过多的更新操作，降低运行
        * （2） 视图与控制器间的过于紧密的连接。视图与控制器是相互分离，但确实联系紧密的部件，视图没有控制器的存在，其应用是很有限的，反之亦然，这样就妨碍了他们的独立重用。
        * （3） 视图对模型数据的低效率访问。依据模型操作接口的不同，视图可能需要多次调用才能获得足够的显示数据。对未变化数据的不必要的频繁访问，也将损害操作性能。
        * （4） 目前，一般高级的界面工具或构造器不支持MVC模式。改造这些工具以适应MVC需要和建立分离的部件的代价是很高的，从而造成使用MVC的困难。
* 16.session与cookie的联系和区别（运行机制），session共享问题解决方案
    * 区别与联系：
        * 使用session_start()调用session，服务器端在生成session文件的同时生成session ID哈希值和默认值为PHPSESSID的session name，并向客户端发送变量为PHPSESSID(session name)(默认)值为一个128位的哈希值。服务器端将通过该cookie与客户端进行交互，session变量的值经php内部系列化后保存在服务器 机器上的文本文件中，和客户端的变量名默认情况下为PHPSESSID的coolie进行对应交互，即服务器自动发送了http 头:header(‘Set-Cookie: session_name()=session_id(); path=/’);即setcookie(session_name(),session_id());当从该页跳转到的新页面并调用 session_start()后,PHP将检查与给定ID相关联的服务器端存贮的session数据，如果没找到则新建一个数据集。
    * 共享方案：
        * 使用数据库保存session， 使用数据库来保存session，就算服务器宕机了也没事，session照样在。
            * 问题：程序需要定制；每次请求都进行数据库读写开销不小，另外数据库是一个单点，可以做数据库的hash来解 决这个问题。
        * 使用 memcached来保存session， 这种方式跟数据库类似，内存存取性能比数据库好很多。
            * 问题：程序需要定制，增加 了工作量；存入memcached中的数据都需要序列化，效率较低，断电或者重启电脑容易丢失数据；
        * 通过加密的cookie，在A服务器上登录，在用户的浏览器上添加加密的cookie，当用户访问B服务器时，检查有无Session，如果没有，就检验 Cookie是否有效，Cookie有效的话就在B服务器上重建session。简单，高效， 服务器的压力减小了，因为session数据不存在服务器磁盘上。根本就不会出现session读取不到的问题。
        * 问题：网络请求占用很多。每次请求时，客户端都要通过cookie发送session数据给服务器，session中数据不能太多，浏览器对cookie 的大
        * 小存在限制。不适合高访问量的情况，因为高访问量的情况下。
* 17.PHP支持多继承吗？为什么？
    * 不支持。PHP类只能继承一个父类，并用关键字“extended”标识。
* 18.include和require 分别返回什么错误级别
    * include会系统警告并继续执行
    * require会发出系统警告但是会引致致命错误令脚本终止运行
* 19.防sql注入方法
function post_check($post){
  if(!get_magic_quotes_gpc()){//  判断magic_quotes_gpc是否为打开
      $post = addslashes($post);//  进行magic_quotes_gpc没有打开的情况对提交数据的过滤
  }
  $post = str_replace("_","\_",  $post);// 把 '_'过滤掉
  $post = str_replace("%","\%",  $post);// 把 '%'过滤掉
  $post = nl2br($post);//  回车转换
  $post = htmlspecialchars($post);//  html标记转换
  return $post;
}
* 20. php连接mysql数据库的几种方式及区别
    * mysql:面向过程
    * mysqli:面向对象
    * pdo:可移植性高


* 1.php数组函数常见的那些?并说出使用方法 (array_merge、in_array的作用)
* 2.PHP中几个输出函数echo，print()，print_r()，sprintf()，var_dump()的区别
* 3.不用新变量直接交换现有两个变量的值
* 4.写个函数来解决多线程同时读写一个文件的问题。
* 5.禁掉cookie的session使用方案，设置session过期的方法，对应函数
* 6.php获取文件内容的方法，对应的函数
* 7.php魔术方法与魔术常量
* 8.PHP 如何获取客户端的IP地址
* 9.写一个函数，可以遍历文件夹下的所有文件和文件夹。
* 10.PHP缓存技术有哪些?
* 11.strlen()与mb_strlen的作用与区别
* 12.写一个函数，尽可能高效的从一个标准url中取出扩展名
* 13.php.ini 中safe mod关闭 影响哪些函数和参数，至少写6个？
* 14.isset() 、empty()与is_null的区别
* 15.MVC是什么，有什么优缺点
* 16.session与cookie的联系和区别（运行机制），session共享问题解决方案
* 17.PHP支持多继承吗？为什么？
* 18.include和require 分别返回什么错误级别
* 19.防sql注入方法
* 20. php连接mysql数据库的几种方式及区别
* * 3.场景公司表和投资事件表同步轮次方法：如果投资事件的轮次大与公司轮次也修改公司轮次，否则不修改
* * 4.数据版本化
* * 5.php空对象在json_encode和json_decode之后会称为空数组
* * 6.foreach循环不会修改数组的值，只有加&符才会同步修改
* * 7.cookie和session的区别，post和get区别
* * 8.设置或生成cookie的方法有几种，cookie的参数有几个，分别是什么
* * 9.Php里魔术方法有哪些，分别作用是什么
* * 写一个函数把一个数组进行倒序排列
* * Php里的数组是如何实现的？
* * 把一个二叉树按行输出
* * Php如何发送一个请求
* * Php如何发送头请求
* * 如何修改或配置虚拟ip
* * 请求返回的状态码代表什么意义？（301.302.401，501等）
* * 如何防止攻击，例如用ajax提交如何保证其安全性
* * Linux下查看磁盘的命令
*     * df -h
*     * du -sh *
* * Php里的use是干什么的
* * Php写出一个单例模型
* * 数据库优化，需要注意些什么
* * 大流量网站优化
* * 书写匹配url正则表达式
* * 冒泡排序或二分查找
* * 数据库存储引擎有哪些，各有什么特点
* * 数据库三范式是什么，实际使用是什么场景
* * GD库是什么，可以做什么
* * 时间函数获取，获得前一天的时间，获取两个时间差
* * php扩展使用过哪些？各有什么特点
* * 大表如何拆分
* * 如何预防sql注入、xss攻击
* * error_report()是做什么的
* * 写一个求阶乘函数
* * 在js中.和#的区别
* * html中position是做什么的
* * 如何防止中文乱码
* * linux常用命令有哪些，都是做什么的
* * 数据库缓存如何做，redis，memcache等
* * char和varchar有什么区别，用哪种字段查询效率更高，为什么
* * POP3、SMTP、HTTP、DNS、FTP都是什么
* * 对于MVC的理解
* * print，echo，print_r有什么区别
* * 如何学习积累知识的，未来几年的职业规划
* * 用过的版本控制器有哪些，有哪些命令
* * 封装，继承，多态是什么
* * 静态方法是否可以继承
* * 框架路由机制什么
* * 进程状态
* * 谈谈自己最有代表性的一个项目，遇到哪些问题，以及如何解决的
* * 如何捕获异常
* * 如何控制发布后代码错误不被抛出
* * 生成环境和开发环境有什么不同
* * 一个错误码不想被抛出，而是可以拦截并且做邮件或短信通知
* * 如何获取3.1415926这个浮点型的前三位
