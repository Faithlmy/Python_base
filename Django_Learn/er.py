#!/usr/bin/env python3
# coding: utf-8
import os, django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superops.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainpro.settings")
django.setup()

#
# def collectasset():
#     from assets.AssetApi import Asset
#     obj = Asset()
#     info_list = obj.collect_all_minions()
#     obj.save_info(info_list)
#
#
# if __name__ == "__main__":
#     collectasset()