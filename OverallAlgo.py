'''

;; DB set up

Entries objects... 
- id
- date
- time
- tweet
- tweet setiment value (can be null)
- weather value or description (based off weather api decison)=NULL

---------
algorithm -- collect tweets

# start algorith on cerry picked "nice" day or "bad" day

# decide what kind of weather it is (EVERY x hours)

    # while < X hours
        # steaming api -- collect tweet
        # findSentiment(tweet)
        # saveToDB(date, time, tweet, tweet sentiment, weather value)

    # break after some amount of time

--------
algorithm -- find weatherments

# run algo

# loop through DB

    # update dictinary {date:   ,
                        weatherValue:   ,
                        sentiment:
                       }

# once dictionary complete, create graph for every weather type and show the range of sentiment values
# maybe find an average value and compare them all?
'''