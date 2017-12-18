# Import与from...import的区别与用法
1. 当模块test.py中没有类，只有方法add，此方法实现传入的数字+1功能
<p>(1)如果使用import导入：import  test</p>
> 调用方法：test.add(1)
<p>(2)使果用form...import导入：from  test  import  *</p>
> 调用方法：add(1)
2. 当模块test.py中有类，类名为cal，类中有方法add，此方法实现传入数字+1功能
<p>(1)如果使用import导入：import  test</p>

> 调用方法：test.cal().add(1)

<p>(2)如果使用from...import导入：from  test  import  *</p>

> 调用方法：cal().add(1)
