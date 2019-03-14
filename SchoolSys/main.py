#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pac_menu import Menu_Manager
'初始化一个Menu的菜单对象实例'
menu = Menu_Manager.Menu()
'调用菜单实例的显示菜单函数'
menu.show_summary_menu()
'调用菜单实例的选择菜单函数，让用户选择对应的菜单进行系统的管理'
menu.select_summary_menu()
summary_menu = menu.get_summary_menu()
'根据用户的选择，显示对应的子菜单'
menu.show_sbu_menu(summary_menu)

