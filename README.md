# Plover-TCIM : an Traditional Chinese Steno System

This plugin is a Plover steno system plugin, please refer to the site to download [Plover](https://github.com/openstenoproject/plover) first if you haven't do so. 

## [Changelog](https://github.com/Quisette/TC_steno/blob/master/Changelog.md)

## Install 

This plugin has yet to be uploaded to Plover's plugin manager, so users should install it manually using CLI method:

`git clone https://github.com/Quisette/plover-TCIM.git `

`plover -s plover_plugins install -e ./ `

After installation, please install the dictionary files and head to [plover_next_stroke](https://github.com/Kaoffie/plover_next_stroke) to install the next storke suggestion plugin in order to get full experience.

## [Theory Intorduction](https://github.com/Quisette/TC_steno/blob/master/Theory%20Introduction.md)



# 千鳥詞注： Plover 中文速錄輸入法

此Plugin為使用於速錄機及速錄鍵盤之輸入法，須配合開源速錄軟體 [Plover](https://github.com/openstenoproject/plover) 使用。

## [Changelog](https://github.com/Quisette/TC_steno/blob/master/Changelog.md)

## 安裝方法

法ㄧ：使用 Plover Plugin Manager 下載（尚未開放）

法二：CLI 方式下載：

`git clone https://github.com/Quisette/plover-TCIM.git `

`plover -s plover_plugins install -e ./ `

安裝完成後，請至[plover_next_stroke](https://github.com/Kaoffie/plover_next_stroke)安裝此Plugin（選字目錄）、重新開啟 Plover 並安裝字典。

## 理論說明

詳見[理論說明](https://github.com/Quisette/TC_steno/blob/master/Theory%20Introduction.md)

## 開發中功能

1. ~~選字功能（編號/倉頡選字）=> 須由另一選字 Plugin 處理（待開發）~~ 詳見 [plover_next_stroke](https://github.com/Kaoffie/plover_next_stroke)
2. ~~額外的詞典管理器(可快速生成index, conflict, main 三個檔案)~~
3. ~~拼音字根式字典及輸入法~~=>已為主要開發系統
4. 聲符簡碼表
5. ~~鍵盤指令(Enter, Del, etc.)~~
6. ~~常用標點符號~~

