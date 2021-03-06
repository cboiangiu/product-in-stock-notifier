# product-in-stock-notifier

Get notified when a product comes back in stock.

## Overview

TODO: Add overview

Created using python 3.8.

Tested on RaspberryPi 3 with RaspberryPi OS.

## Prerequisites

An [ExpressVPN](https://www.expressvpn.com) subscription and account key.

## Before you run

```
$ python setup.py
```

__Important__: If you intend to use `phone_alert`, make sure that emails added to `EMAILS_TO_NOTIFY` support PUSH (example: @icloud addresses for iOS). 

You can get latest .deb package from https://www.expressvpn.com/support/vpn-setup/app-for-linux/#download if the provided one does not work.

## How to run

```
$ cd notifier
$ python main.py
```

## Get alerts on your phone

Read [phone_alert](phone_alert/README.md) docs to learn how to create alerts for your phone, such as alarms, when receiving IN STOCK emails.

## To be added

- Implement the use of free proxies for page data requests
- Audio alerts for RaspberryPi via aux speaker
- Android `phone_alert`
