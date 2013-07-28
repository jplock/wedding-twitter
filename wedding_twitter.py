#!/usr/bin/env python

import datetime
import time

import twitter

TWITTER_USERNAME = 'jplock'
TWITTER_PASSWORD = 'REPLACE_ME'
TWITTER_TAG = ' #plocknet'

START_TIME = datetime.datetime(2010, 5, 15, 13, 0, 0)
#START_TIME = datetime.datetime(2010, 5, 12, 17, 0, 0)

MESSAGES = {}
MESSAGES[0] = "Oh boy, here we go...%s"
MESSAGES[1] = "Where is the exit? KIDDING!%s"
MESSAGES[5] = "Walking down the aisle...%s"
MESSAGES[10] = "Did @KennedyX8 just let one rip? It was probably SlimShady666.%s"
MESSAGES[15] = "Modern Warfare 2 is calling @GMBowman04's name right about now.%s"
MESSAGES[20] = "Isn't there some sort of handyman project @edelend should be working on?%s"
MESSAGES[24] = "Where is Phil Jr?%s"
MESSAGES[25] = "Hopefully this makes it into @vsundqvist's newspaper!%s"
MESSAGES[26] = "Let's see how well @cmunick has been setting up the reception!%s"
MESSAGES[27] = "I bet @ckulchar is waxing the GTO right about now.%s"
MESSAGES[28] = "The only thing that could make this day better would be @pdidds and @ginapsu's bruschetta bread!%s"
MESSAGES[29] = ".@natefoo and @rcoraor: don't look now but I think Sofia is crawling down the aisle!%s"
MESSAGES[30] = "To the delight of @Bacon and @susotchka, every item on the reception menu has bacon on/in it. KIDDING!%s"
MESSAGES[31] = "Wings 2: Aces High is calling @Viper9181's name right about now.%s"
MESSAGES[32] = "If you want to see rickster really move, have @maggiesapovchak spill some ice water on him. :)%s"
MESSAGES[33] = "Too bad Rocky didn't make an appearance with @LuisValbuena.%s"
MESSAGES[34] = "Coming soon, @JoeDaley1 co-owner/co-founder/bartender of the Cousin's Daley!%s"
MESSAGES[35] = "I married @lilmisskrisdee! Let's get this party started!%s"


def main():
    """Main execution function."""

    api = twitter.Api(username=TWITTER_USERNAME, password=TWITTER_PASSWORD)

    print 'START %s' % START_TIME

    while True:
        current_time = datetime.datetime.now()
        diff = current_time - START_TIME
        delta_seconds = diff.days * 86400 + diff.seconds
        delta_minutes = delta_seconds / 60

        print 'TIME %s [%dm:%ds]' % (current_time, delta_minutes, delta_seconds)

        for offset in sorted(MESSAGES.keys()):
            if offset <= delta_minutes:
                try:
                    message = MESSAGES.pop(offset)
                except KeyError:
                    print 'ERROR offset=%d not found in MESSAGES' % offset

                message = message % TWITTER_TAG
                num_chars = len(message)

                if num_chars > 140:
                    print 'ERROR "%s" is %d characters.' % (message, num_chars)
                    continue

                status = 'FAIL'
                ret = 0
                try:
                    ret = api.PostUpdate(message)
                except twitter.TwitterError:
                    # ignore exceptions
                    pass

                if ret:
                    status = 'OK'

                print '  %s <- %d tweet: "%s"' % (status, offset, message)

        if not MESSAGES:
            break
        print '...sleeping for 15 seconds...'
        time.sleep(15)

    print 'END %s' % current_time

if __name__ == '__main__':
    main()
