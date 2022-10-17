import tweepy


consumer_key = "" #REDACTED
consumer_secret = "" #REDACTED
access_token = "" #REDACTED
access_token_secret = "" #REDACTED


client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# Create Tweet
sonum = input("Sisesta tweet: ")

response = client.create_tweet(text=sonum)

print(f"https://twitter.com/user/status/{response.data['id']}")
