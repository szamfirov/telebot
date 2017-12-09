# telebot

### Description

A really simple and secure Telegram bot.

### Requirements

Please keep the following things in mind:

* You would need to [create your own bot](https://core.telegram.org/bots#creating-a-new-bot) to make use of this project (or you can use an existing one if you already have it).
* The bot can be contacted only by specific users, which adds an extra layer of protection in case someone tries to do something nasty. So you need to know your Telegram user ID (you can check [@userinfobot](https://telegram.me/userinfobot)) in order to use the functionalities.
* At the time of writing this, I used `Python3.6` to install/deploy this bad boy, so make sure you have this installed on the machine you want to run it.

### Quick Start

You will need a Python3.6 virtual environment.
```sh
$ pip install virtualenv
$ virtualenv -p $(which python3.6) ~/venvs/telebot
$ source ~/venvs/telebot/bin/activate
```

Or if you're using `pyenv`, you can do something like this:
```sh
$ pyenv install 3.6.3
$ pyenv virtualenv 3.6.3 telebot
```

Once you are all set, you can install telebot, add a few settings and run it with gunicorn:
```sh
$ pip install -e .
$ pip install gunicorn
$ cp settings.ini.dist settings.ini
$ gunicorn --paste settings.ini
```

### Deployment

You may want to check this thing in action. The easiest solution is local deployment. First you need a configuration file:
```sh
$ cp settings.ini.dist settings.ini
```
Make sure you add the necessary information in the configuration file and make all the changes you like. After this is done, you need an HTTP server to run this on. In this example I'm using [Gunicorn](http://gunicorn.org/)

```sh
$ pip install gunicorn
$ gunicorn --paste settings.ini
```

It will start listening on port `5556` where it accepts traffic. A good idea might be to put it behind nginx and enable SSL. Once you have a public URL you can configure [webhooks](https://core.telegram.org/bots/api#setwebhook) for the Telegram bot so it can receive the latest updates via an outgoing webhook.

---

Another possible way of deploying is using the Free-Tier of AWS to test it out and see how the bot works. The deployment is quite easy and it's done with the help of [Zappa](https://github.com/Miserlou/Zappa).

You can go through the quick start guide there, but it's as easy as:
```sh
$ pip install zappa
$ zappa init
$ zappa deploy
```

and on the plus side - you'll run this thing server-less style! ;)

