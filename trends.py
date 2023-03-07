
import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()

#get today's treniding topics
#trendingtoday = pytrend.today_searches(pn='US');
#trendingtoday.head(20);

#print(trendingtoday)

# Get Google Top Charts
#df = pytrend.top_charts(2020, hl='en-US', tz=300, geo='GLOBAL');
#df.head();
#print (df)

#Get todays trending
df = pytrend.trending_searches()
df.head()
arr= df.values
print(arr) #Array con todos los trends
print(arr[12][0]); #Elemento 1

# Set the keyword you want to search for
keyword = arr[12][0]

# Build the payload
pytrend.build_payload(kw_list=[keyword])

# Get related queries
related_queries = pytrend.related_queries()[keyword]['top']

# Print the most searched titles for the keyword
print("Most searched titles for", keyword)
for title in related_queries['query']:
    print(title)