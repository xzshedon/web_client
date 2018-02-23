##### Web_Client 轻量级的python+selenium Web 测试框架

- Unittest + PageObject + HtmlTestRunner

- log + report + screenshot

###### 目录结构
- config：配置文件

- framework：主要的逻辑文件
    - 包括POM基类base_page：定义对web页面的各种操作
    - 浏览器选择器：选择启动什么浏览器，并返回一个driver
    - log内容配置：命令执行log，保存在test_reports下，以脚本运行时间戳为文件名
    - HTMLTestRunner：测试报告模板（开源）
    
- pageobjects：进行PageObject分类，以系统或模块为文件夹名字，并以页面作为page

- test_report：存放log + report + screenshot

- testsuites：每个页面的测试用例

- tools：存放webdriver，Win用户请按照目录下的readme，按需下载，Linux请更改browser_engine的配置


##### For FUN.
