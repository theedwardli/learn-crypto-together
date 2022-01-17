from decouple import config

import praw

# Authenticate with your Reddit credentials
reddit = praw.Reddit(client_id=config('clientID'),
                     client_secret=config('clientSecret'),
                     user_agent=config('userAgent'))


def get_sub_data(subreddit):
    """
    
    Retrives information about a specific subreddit

    Parameters
    ----------
    subreddit (str): the name of the subreddit

    Returns
    ----------
    dict: a dict that contains the number of subscribers and 
          a list of the top 10 posts of the week (praw.Model.Submission)

    """

    sub = reddit.subreddit(subreddit)

    num_subscribers = sub.subscribers

    top_weekly = sub.top("week", limit=10)

    return dict([('subscribers', num_subscribers), ('posts', top_weekly)])


def rank_posts(list_of_subreddit_dicts):

    # TODO


def main():

    bitcoin = get_sub_data("bitcoin")
    ethereum = get_sub_data("ethereum")
    solana = get_sub_data("solana")
    stellar = get_sub_data("stellar")
    cryptocurrency = get_sub_data("cryptocurrency")
    cryptocurrencies = get_sub_data("cryptocurrencies")
    defi = get_sub_data("defi")
    web3 = get_sub_data("web3")




if __name__ == "__main__":
    main()