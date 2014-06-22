PostBoy
=======

Simple distributed emailing system.

Usually websites send emails directly in a request.
Sometime I tried to use as emailing daemon "ssmtp".
I was shocked when I tried to send ten mails from django.
This was about half a minute (about 3 seconds per letter), and my request was processed long.

This system will be save your response time because your letters will be added to queue and delivered as soon as possible.
If you have more then one server, you will have load balancing and guarantee of delivering for your mailings.

For working the Postboy needed running and configure RabbitMQ AMQP daemon.
This may used as cluster or single server instance.
For delivering will be used any localhost MTA.

Installation
++++++++++++

Quick installation the system in the Ubuntu server.
Install the Postboy:

    pip install postboy

Then install a rabbitmq and any MTA (I recommend install postfix):

    apt-get install postfix rabbitmq-server

Choose local domain and other


Run the worker:
    
    /usr/bin/postboy --debug

Also you may set any options:

    $ postboy --help
    Usage: postboy [options]

    Options:
      -h, --help            show this help message and exit
      -H ADDRESS, --host=ADDRESS
                            Broker host
      -p PORT, --port=PORT  Broker port
      -t SECONDS, --timeout=SECONDS
                            Getting task timeout
      --smtp-host=ADDRESS   SMTP server
      --debug               A lot of logging messages
      --broker=HOST         Rabbitmq host
      --broker-port=PORT    Rabbitmq port
      --broker-channel=CHANNEL
                            Rabbitmq channel
      --max-retries=NUMBER  Maximum number of retries sending messages


Using
+++++
Then try to use it in your code:

    >>> from postboy import Email, BrokerHandler
    >>> broker = BrokerHandler()
    >>> email = Email(sender='info@test.name', recipient='user@localhost', subject='Test')
    >>> broker.store(email.dumps())
    1 # <= return task id
