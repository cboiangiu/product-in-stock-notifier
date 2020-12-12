# phone_alert

## Overview

TODO: Add overview

## iOS

Link: https://www.icloud.com/shortcuts/7b72bfe7be8b4f88b60f6b42e16353da

~~In the `/ios` directory you will find a Shortcuts file named `product_in_stock.shortcut`.~~

_Apparently importing shortcut files is not yet supported, so I have shared a link for the shortcut via iCloud. The file is still left in `/ios` if apple eventually fixes this. Also, I have left screenshots of the shortcut actions in `/ios/media` if you want te recreate it yourself._

__Note__: The first version of the shortcut added an alarm and timer upon receiving the IN STOCK email. Unfortunately apple does not support running automations on email triggers automaticaly (it just sends a notification to run the shortcut). Therefore, this new version of the shortcut only opens the browser with the product link and also copies it to the clipboard.

### Instructions

First, make sure to allow Untrusted shortcuts from iPhone Settings app -> Shortcuts.

Click the link above to add the shortcut or recreate it yourself. 

When adding the shortcut, make sure to replace the product and store name in `Notify: Product - Store` in the `When I run:` section. Press `Add Untrusted Shortcut` at the bottom. 

Answer the import questions in the `Configure This Shortcut` section.  

Go to `Automation` tab and create a new `Personal Automation`. For the trigger, select email. For sender, select the address added during `setup.py` in `EMAILER_EMAIL`. For the subject, the format should be `Example Product Name:Example Store Name - IN STOCK` depending on the name of the product and the store. For the recipient, enter the PUSH enabled email added during `setup.py` in `EMAILS_TO_NOTIFY` (you can use your @icloud address if you have it added in you Mail app).

In the action section select `Add Action` and choose `Run Shortcut` and choose the imported/created shortcut.

Press `Next` button in the top right and `Done`.

That's all.

__Note__: If you have defined multiple products in the python script, create a shortcut and automation for each one (import shortcut, answer questions, create automation).

## Android

Haven't researched how to do a similar thing on Android. Tasker might be a good start, idk. PR's welcome!
