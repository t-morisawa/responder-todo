"""
form dataを扱うクラス
本アプリはform dataとcontrollerを共通のライブラリで扱っているのでcontrollerに統一しても良さそう
"""
from dataclasses import dataclass
from typing import List
from entity import Checklist


def checklist_from_form(media):
    # mediaは1はじまりなのに対しchecklistは0始まりなので各要素を1ずつずらす
    checklist = media.get_list('riyu')
    return Checklist(list(map(lambda i: int(i)-1, checklist)))
