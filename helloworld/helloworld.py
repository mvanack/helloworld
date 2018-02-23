#!/usr/bin/env python


def helloworld(name=None, popcorn=None, countdown=None):

    # print greeting
    if not name:
        print("hello world")
    else:
        print("hello {}".format(name))
        # Print movie and popcorn call
    if popcorn:
        print("Movie")

    if countdown:
        if countdown <= 0:
            print("Showtime!")
        else:
            print("Get your popcorn!")
