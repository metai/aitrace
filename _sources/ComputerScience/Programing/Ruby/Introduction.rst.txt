.. _Section-IntroductionRubyProgramingComputerScience:

引言
=====================


什么是Ruby
---------------





库包管理
----------------

gem 和 bundle. Gem是一个管理Ruby库和程序的标准包，它通过Ruby Gem（如 http://rubygems.org/）源来查找、安装、升级和卸载软件包，非常的便捷。


bundle 不仅用来安装 gem，更重要的是还负责计算出不同 gem 的依赖版本，最终生成 Gemfile.lock 文件，该文件记录了确切的 gem 名称和版本号，以及他们所依赖的 gem 的名称和版本号。

第一次运行 bundle install 时自动生成 Gemfile.lock 文件。
以后每次运行 bundle install 时,如果 Gemfile 中的条目不变 bundle 就不会再次计算 gem 依赖版本号，直接根据 Gemfile.lock 检查和安装 gem。
如果出现依赖冲突时可以通过 bundle update 更新 Gemfile.lock。
