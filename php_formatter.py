#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime, sublime_plugin
import os

class PhpFormatterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # projectパスの取り方はこれでいいのか？
        #projectDir = self.view.window().folders()[0]

        pluginPath = sublime.packages_path() + "\\User\\php_formatter\\"
        tempPath = os.environ.get('TEMP', '')
        if tempPath == "":
            sublime.message_dialog(u"環境変数[TEMP]が取得できません。")
            return

        #print(self.view.file_name())
        phpCBPath = pluginPath + "phpCB.bat"
        #phpCBPath = pluginPath + "hoge.bat"
        # 半角スペースを含むのでダブルコーテーションで囲む
        phpCBPath = '"' + phpCBPath + '"'

        phpCBPath = phpCBPath + " " + self.view.file_name()
        print(phpCBPath)
        os.system(phpCBPath)

        # sublime.packages_path() + "User\php_formater.bat"
        #print(sublime.packages_path())

