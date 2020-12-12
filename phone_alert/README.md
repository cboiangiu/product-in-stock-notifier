# phone_alert

## Overview

TODO: Add overview

## iOS

TODO: Add product_in_stock.shortcut in /ios

In the `/ios` directory you will find a Shortcuts file named `product_in_stock.shortcut`.

Send that file to your ios device and import the shortcut to your Shortcuts app. During the import you will be asked to answer some questions regarding the shortcut's configuration (product url and product name). After answering the questions the shortcut will be added.

Next, go to the automations section in the shortcuts app and create a new Personal Automation. For the trigger select Email and configure the Sender as you defined it during the `setup.py` phase. For the subject, the format should be `Example Product Name:Example Store Name - IN STOCK` depending on the name of the product and the store. For the action of the automation select Run Shortcut and select the previously created shortcut.

If you have defined multiple products in the python script, create a shortcut and automation for each one (import shortcut, answer questions, create automation). If creating multiple shortcuts, make sure to rename them after import so that each gets a unique name that can be used then for each automation when selected in Run Shortcut.

## Android

Haven't researched how to do a similar thing on Android. Tasker might be a good start, idk.
