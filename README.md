# ```Scrape-Telegram-Users```

## Telegram script to scrape users from Telegram groups

## Requirements
### ** Prerequisites

``
* Python 3.6+
* Telegram API Id and API hash
* Telethon
* QRCode
* python-decouple
``
### Additional Requirements
``
- Password=put your password here if you enable two-step verification
- phone_number=put your phone number here.

> Note that phone_number and password are variables that needs to be placed inside the `.env` file separated by new line and they will be used when creating a new session.
 

## Usage

``
* after finished setting up your environment 

- Run `myadd.py` and this will add all the scraped members to your group make sure to replace this line  
       `if a.title=="Telegram_Testing":
            channel.append(a)`

        replace `Telegram_Testing` with your own Telegram group name.   

``

> 
-----------------------------------------
-----------------------------------------
> Author: Abinet Tesfu.

-----------------------------------------
-----------------------------------------

> You can find me on [Telegram](https://t.me/Abinet_tes) or [Github](github.com/Abinet508).