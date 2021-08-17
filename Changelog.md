# Changelog

## Pre-release 0.1.0 | 2021.8.18

* ### Changing to Alphabet-based roots and abandoning Zhuyin-based roots and dictionary files

  Owing to the issue of Microsoft Excel having difficulty dealing with the Unicode ㄯ(U+312F), The main dictionary code has recompiled to alphabet-based (Pinyin-based) format, and the Zhuyin-based root input method has abandoned from now. 
  However, **It is still strongly recommended that learners study with the format of Zhuyin**, since the dictionary file has compiled based on Zhuyin, and using Pinyin to comprehend it might have some issues when it comes to some words.
  **The base theorem of Zhuyin has not changed at all**, but in order to lessen the difficulty of editing a massive amount of dictionaries, Alphabet-based format has less chance to make errors. 

* ### Word selecting  system has developed with some bugs , but fixible by implementing other indicators

  The word selecting index has successfully developed, which can deal with up to 10 entries. 
  However, some of the dictionary index entries has contained more than 10 entries, which cannot be used by now. 
  The main reason causing this might be the plover system's word root read list, which seems to be unfixable solely by the plugin.
  Nevertheless. these word-selecting issues can be used by implementing Cangjie roots to indicate words, which has been planned to be developed. 

  