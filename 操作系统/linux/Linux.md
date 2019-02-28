Linux

>进程
1.分为三类：交互式进程、批处理进程、守护进程
2.守护进程：最活跃、在后台运行
3.父进程与子进程
    1)父进程总结，子进程跟着总结；反之不然
4.工具：ps,kill,pgrep,top
5.状态：R-运行，S-睡眠，Z-僵尸http://www.jianshu.com/p/a146a8d383d4

>awk使用
1.其中单引号中的被大括号括着的就是awk的语句，注意，其只能被单引号包含。
2.其中的$1..$n表示第几例。注：$0表示整个行。
    如：shell>awk '{print $1, $4}' netstat.txt
3.格式化输出，如：shell>awk '{printf "%-8s %-8s %-8s %-18s %-22s %-15s\n",$1,$2,$3,$4,$5,$6}' netstat.txt
4.过滤记录，第三列为0且第六列为listen,如：shell>awk '$3==0 && $6=="LISTEN" ' netstat.txt,
    #其中：“==”为比较运算符。其他比较运算符：!=, >, <, >=, <=
    e.g：shell>awk ' $3>0 {print $0}' netstat.txt
    #如果我们需要表头的话，我们可以引入内建变量NR：
         shell>awk '$3==0 && $6=="LISTEN" || NR==1 ' netstat.txt
    #再加上格式化输出：
         shell>awk '$3==0 && $6=="LISTEN" || NR==1 {printf "%-20s %-20s %s\n",$4,$5,$6}' netstat.txt
5.内建变量
    $0	当前记录（这个变量中存放着整个行的内容）
    $1~$n	当前记录的第n个字段，字段间由FS分隔
    FS	输入字段分隔符 默认是空格或Tab
    NF	当前记录中的字段个数，就是有多少列
    NR	已经读出的记录数，就是行号，从1开始，如果有多个文件话，这个值也是不断累加中。
    FNR	当前记录数，与NR不同的是，这个值会是各个文件自己的行号
    RS	输入的记录分隔符， 默认为换行符
    OFS	输出字段分隔符， 默认也是空格
    ORS	输出的记录分隔符，默认为换行符
    FILENAME	当前输入文件的名字
e.g.
#如果要输出行号
    shell>awk '$3==0 && $6=="ESTABLISHED" || NR==1 {printf "%02s %s %-20s %-20s %s\n",NR, FNR, $4,$5,$6}' netstat.txt
6.指定分割符
    shell>awk  'BEGIN{FS=":"} {print $1,$3,$6}' /etc/passwd
    shell>awk  -F: '{print $1,$3,$6}' /etc/passwd   #-F的意思就是指定分隔符,指定多个分隔符 -F '[;:]'
    shell>awk  -F: '{print $1,$3,$6}' OFS="\t" /etc/passwd  #以\t作为分隔符输出
7.字符串匹配
    1) ~ 表示模式开始。/ /中是模式。这就是一个正则表达式的匹配。
        shell>awk '$6 ~ /FIN/ || NR==1 {print NR,$4,$5,$6}' OFS="\t" netstat.txt
        shell>awk '$6 ~ /WAIT/ || NR==1 {print NR,$4,$5,$6}' OFS="\t" netstat.txt
        shell>awk '/LISTEN/' netstat.txt
    2)使用 “/FIN|TIME/” 来匹配 FIN 或者 TIME
        shell>awk '$6 ~ /FIN|TIME/ || NR==1 {print NR,$4,$5,$6}' OFS="\t" netstat.txt
    3)模式取反 ! ~ //
        shell>awk '$6 !~ /WAIT/ || NR==1 {print NR,$4,$5,$6}' OFS="\t" netstat.txt
        shell>awk '!/WAIT/' netstat.txt
8.拆分文件
    shell>  awk 'NR!=1{if($6 ~ /TIME|ESTABLISHED/) print > "1.txt";
            else if($6 ~ /LISTEN/) print > "2.txt";
            else print > "3.txt" }' netstat.txt
    ps:R!=1表示不处理表头
9.统计
    统计各个connection状态
        shell>awk 'NR!=1{a[$6]++;} END {for (i in a) print i ", " a[i];}' netstat.txt
    每个用户的进程的占了多少内存
        shell>ps aux | awk 'NR!=1{a[$1]+=$6;} END { for(i in a) print i ", " a[i]"KB";}'
10.awk脚本
    1)  BEGIN{ 这里面放的是执行前的语句 }
        END {这里面放的是处理完所有的行后要执行的语句 }
        {这里面放的是处理每一行时要执行的语句}
e.g.
#从file文件中找出长度大于80的行
    shell>awk 'length>80' file
#按连接数查看客户端IP
    shell>netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr
#打印99乘法表
    shell>seq 9 | sed 'H;g' | awk -v RS='' '{for(i=1;i<=NF;i++)printf("%dx%d=%d%s", i, NR, i*NR, i==NR?"\n":"\t")}'
