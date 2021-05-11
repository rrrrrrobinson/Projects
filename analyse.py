
# take in an opinionated string and we want to output whether or not this is a bad day or good day or okay day
# we can run it 10 time and see what it is and compare it to what the current day is like 

# essentially how it would work is whenever the token from this string is found in a tweet we have already used then it 
# would make a probablity just like niave bais does





# model 

# (, type of day) for training
# we want new entry to input a tweet string and then output a day

#1
#string tweet => sentiment 
#classify({sentiment}) => what kinda day

Setinment - (pos&>.7, pos>.5, PosElse, neg&>.7, neg>.5, negElse, 1.0&neutral) | daytype - (good, bad, okay)

pos|neg|neutral|weathertype
pos&>.7, negElse, nutral, "good"



{neg:.5}, bad
{pos:.7}, good
{neg:.3}, okay



#2
#classify({string tweet}) => what kinda day
{neg.2},bad
