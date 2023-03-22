#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:52:18 2023

@author: paulin
"""
from pyppeteer import launch

browser = launch()
page = browser.newPage()
page.goto('https://www.google.com/maps/@47.7299647,-121.1342003,13.18z')
page.screenshot({'path': 'mapgrab.png'})

dimensions = page.evaluate('''() => {
    return {
        width: document.documentElement.clientWidth,
        height: document.documentElement.clientHeight,
        deviceScaleFactor: window.devicePixelRatio,
    }
}''')

print(dimensions)
# >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
browser.close()