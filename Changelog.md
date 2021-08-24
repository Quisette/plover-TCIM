# Changelog

## Pre-release 0.1.0 | 2021.8.18

* ### Changing to Alphabet-based roots and abandoning Zhuyin-based roots and dictionary files

  Owing to the issue of Microsoft Excel having difficulty dealing with the Unicode ㄯ(U+312F) and Windows system's not showing this code, in order to enhance the compatibility of the system to all users, The main dictionary code has recompiled to alphabet-based (Pinyin-based) format, and the Zhuyin-based root input method has abandoned from now. 
  However, **It is still strongly recommended that learners study with the format of Zhuyin**, since the dictionary file has compiled based on Zhuyin, and using Pinyin to comprehend it might have some issues when it comes to some words.
  **The base theorem of Zhuyin has not changed at all**, but in order to lessen the difficulty of editing a massive amount of dictionary entries, Alphabet-based format has less chance to make errors. 

* ### Word selecting  system has developed with some bugs , but fixible by implementing other indicators

  The numeral word selecting index has successfully developed, which can deal with up to around 20 entries by far [(in our combined dictionary)](https://github.com/Quisette/TC_steno/tree/master/Pinyin%20Version/dictionaries). 
  However, some of the dictionary index entries is unable to use, which involves the plover system's root-reading methods, and it seems to be unfixable solely by the plugin.
  Nevertheless. these word-selecting issues can be used by implementing other word-selecting indexes such as Cangjie roots, which has been planned to be developed. 

## Pre-release 0.1.1 | 2021.8.24

* ### The word-selection plugin has developed

* ### The hinderance of number has been fixed


# 版本更新

## Pre-release 0.1.0 | 2021.8.18

* ### 字典以及編碼更改為字母式字根，並暫停注音式字根之開發

  由於 Microsoft Excel 在編輯字典清單時無法辨識 Unicode ㄯ(U+312F) 導致選字列表出現錯誤，以及Microsoft Windows 無法顯示此字元，為增加系統間的兼容性，在此版本之後全面採用字母式字根，同時也暫停注音式字根及字典的開發。
  但**這個決定並非表示系統將全面改為漢語拼音模式**。注音與漢語拼音間仍有部分不規則之問題，且繁體中文與簡體中文採用拼音不盡相同，因此**學習者應仍然採用注音符號為學習此系統之媒介**。

* ### 選字系統已完成初步開發，選單部分錯誤可由採用其他選字系統避免

  以數字編碼的選字系統已開發完成並且可使用，請[更新字典檔案並詳讀README.md](https://github.com/Quisette/TC_steno/tree/master/Pinyin Version/dictionaries)。

  選字系統目前可支援20餘個詞同時選用，但某些編號是無法使用的。詳細的編碼與數字輸入規則，將會在[理論說明](https://github.com/Quisette/TC_steno/blob/master/Theory%20Introduction.md)講解。

  * 不可使用的詞條編碼是：11,21,22,31,32,33...

  這個錯誤牽涉到Plover本身對字根排列順序解讀的方式，可能無法在Plugin層面解決。不過若使用其他編碼方式(如取倉頡首碼)此問題便可解決。
  倉頡首碼的字典Index也預計在最近開發，敬請期待。

  