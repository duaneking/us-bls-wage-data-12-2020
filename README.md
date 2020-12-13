# us-bls-wage-data-12-2020

YOU HAVE BEEN WARNED.

Before you read anything else: I need you to understand that this data is a SINGLE updated RESULT SUMMARY of a very complicated process that the government uses to collect wage data as PART of the prevailing wage calculation done MULTIPLE TIMES A YEAR to ensure that people who immigrate into the USA are presented with and maintain to get a fair wage compared to current citizens as part of that experience of being an American.

This means the data has no value past 6/2021, because the US BLS will have given you updates via a new OWL dump. No, this does not obligate me to update this at that time, and overly rude requests I do so will be ignored if I don't feel like trolling back in self defense instead.

So no, its not exact. This data is NOT what your coworker or Boss is making exactly. It's a time based average/mean/median (We do not know which). So It should not be taken as Absolute Truth. It does not represent "the right wage", it represents a calculated wage that the US BLS considers fair.  The open market probably disagrees. 

In fact, the USBLS themselves stated that these numbers are TOO LOW to be accurate or valid for wage determination (They want wages for immigrants to go up to be more fair) and can not be used for the amount the person makes when asking for a visa for them at that rate, etc. 

In all cases, consider these numbers to be too LOW to be fully accurate.. but consider them to be a good way to tell if your getting underpaid.

Again: These are a LOWER BOUND NOT A RATE HR SHOULD OFFER.  If HR needs a rate to offer, these rates are too low. Start there.

I wanted to know this data because I had been told I was asking for too much, and I wanted to know what that "honest and fair wage" actually was.

I was open to the idea that I was wrong in what I wanted. I realized maybe I was just getting more pay than others, possibly because I did better work.  I wanted to know the truth, so I did this to find the average rates for my industries in my area for this part of 2020 as I consider the 2021 too far in the future to know but its clear the USBLS wants rates at a set rate for that time and isn't scared to try to manipulate the public into making it happen by saying so.. so thankfully I have that experience andcan understand whats going on.  These rates are a request for the future, an anchor for the past.

In the end, I was surprised to find the person telling me I was asking for too much was not only wrong, they were actually trying to take advantage of me and lying to my face based on this data.

As a result, I feel like its important others have access to this same data, so that they can also defend themselves from abuse or being taken advantage of by being as informed as the federal BLS will allow them to be based on the data I was able to extract from the public data dump.

Due to this, and as these numbers are used to calculate fairness in regards to human rights by the US BLS, these metrics are considered to be TOO LOW for some roles to be legal as a wage in some regulated industries, and as a result, I question even releasing them to the public out of fear that these HOURLY RATES will be abused, but the fed did so, and who am I to judge peoples ability to understand that the hourly wage rates presented here do not reflect actual wage trends, are a bad generalization of an entire country over a period of months, some that have not happened, etc, and are thus considered too low in all cases to be fair based on that data from the government themselves.

# What is this?
This is a a Federal Bureau of Labor Statistics wage data from the BLS for the 4th quarter of 2020, cleaned up and made importable into a PostgreSQL DB so I could run some queries and understand the differences in wages between CA and WA state for typical roles.

It contains the original dump CSV files from the FED, as well as PostgrSQL Import files generated for both raw full import and schema based dumps... because I had to do it the hard way so why not give you the opportunity as well?

# So I could see what people make?
Kinda.  The wage data the US BLS gives out is always incomplete and always edited to ensure the correct desired political bias of the people in power.   Its not going to be 100% accurate because part of the US BLS's job is to manipulate wage data as a proxy to control the economy. Its what they exist to do, in part. But also keep in mind that rates will be lower than market here because high wages can both be a good thing and a bad thing for the government so they want prices to be generally lower and stable.  As a result, these numbers for higher paid roles should best be considered conservative when they are available.  And in most cases, you will find the Fed doesn't want you to know and just removed it.

# So what are these 'NOPE' fields in the exports? I want to know the rate you are hiding from me, where do I get it!?!

I'm not hiding anything; After all why would I go through all this trouble?

If the field you want says 'NOPE' it was an entry that the Fed BLS actively censored or removed, or at least it was not included in the data I was allowed to download.

I use the 'Nope' dummy value to show this. Its custom and easy to see as distinct from a NULL or empty value, and calls it out in the export as missing. Its also the same length string as NULL, and I find it funny.

That is the government saying 'Nope', not me. I want the data as much as you do. I just don't have it. Sorry. No, I will not go out and get it because I can't (or I don't want to, take your pick).  This was a personal project that I now consider to be finished as I got what I wanted out of it: A gut check.

# The wage for my area seems slightly low, why is that?
If you only one or two people with a specific hard to find for the area title, that areas data is going to be wild due to the averages.  Look at the area.  Is it known for that type of worker? In general, if there are less companies who need that sort of worker, and the work can not be done remote, wages will be lower due to lower company demand.  It doesn't mean that the same skills are suddenly worth less, it simply means the same skills are not as in demand in that area. Consider the highest wage between two different areas to be an indication of relative demand.

# What is the status of this project?
This is a one time data dump.  It will NOT be Updated or worked on from this point on.  It only exists in its current state. It will never be updated.  It should never be considered correct as the numbers are known to be too low. I'm making my one git-push and then I'm done.

