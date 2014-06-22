PostBoy
=======

Simple distributed emailing system.

Installation
++++++++++++

        pip install postboy

Using
+++++

    /usr/bin/postboy --debug

Then try to use it.

    >>> from postboy import Email, BrokerHandler
    >>> broker = BrokerHandler()
    >>> email = Email(sender='info@test.name', recipient='user@localhost', subject='Test')
    >>> broker.store(email.dumps())
    1 # <= return task id
