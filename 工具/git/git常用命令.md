---
author: "hackfox"
date: 2016-12-24 19:08:57
title: "Git常用命令"
categories:
  - Development
tags:
  - git
comments: false
toc: true
draft: false
---

- ``git init``                  #git 初始化仓库
- ``git clone remote_url``      #git 克隆远程库
- ``git add *`` #git 添加所有文件
- ``git commit -m "批注"``      #git 提交
- ``git push <remoteName> <localName>``                 #git推送至远程
- ``git remote add origin <server>``    #远程没有创建仓库，将本地推送到远程仓库
- ``git checkout -b branch_name``   #创建分支，并切换到分支
- ``git checkout master``       #切换到主分支
- ``git branch -d <branch_name>``     #删除分支
- ``git pull <remoteName> <localName>``    #将本地仓库更新至最新
- ``git merge branch_name``    #将其他分支合并到本地主分支
- ``git diff <sourch_branch> <target_branch>``     #比对分支
- ``git tag <tag_name>``   #创建标签
- ``git show``     #
- ``git status``   #查看当前状态
- ``git fetch``    #合并
- ``git config --list``    #查看配置信息
- ``git rm <file_name>``   #删除文件
- ``git mv <old_name> <new_name>``     #重命名文件
- ``git log``      #查看日志
- ``git rebase HEAD <file_name>``  #重置
- ``git remote -v``    #查看远程仓库
- ``git remote rm <file_name>``    #删除远程仓库
- ``git branch``   #查看本地分支
- ``git branch -r``    #查看远程分支
- ``git branch <branch_name>`` #创建本地分支
- ``git config --global user.name NEWNAME``    #修改用户名
- ``git config --global user.email NEWEMAIL``  #修改用户邮箱
