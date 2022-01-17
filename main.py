from decouple import config
from datetime import date

import praw
import pprint
import logging
import csv

logging.basicConfig(level=logging.INFO)

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
          a list of the top 10 posts of the week (praw.models.Submission)

    """

    logging.info("Getting data for " + subreddit + "...")

    sub = reddit.subreddit(subreddit)

    num_subscribers = sub.subscribers

    top_weekly = sub.top("week", limit=20)

    return dict([('subscribers', num_subscribers), ('posts', top_weekly)])


def weight_sub_posts(subreddit_data):
    """

    Weights the posts in a subreddit by engagement

    Parameters
    ----------
    subreddit_data (dict): contains data about the subreddit 

    Returns
    ----------
    list: a list of weighted posts (praw.models.Submission)
    """

    logging.info("Weighing posts in subreddit ...")

    weighted_list = []

    subscribers = subreddit_data.get('subscribers')

    for post in subreddit_data.get('posts'):

        post.weight = post.num_comments / subscribers

        weighted_list.append(post)

    return weighted_list


def main():

    top_posts = [
        *weight_sub_posts(get_sub_data("bitcoin")),
        *weight_sub_posts(get_sub_data("ethereum")),
        *weight_sub_posts(get_sub_data("solana")),
        *weight_sub_posts(get_sub_data("stellar")),
        *weight_sub_posts(get_sub_data("cryptocurrency")),
        *weight_sub_posts(get_sub_data("cryptocurrencies")),
        *weight_sub_posts(get_sub_data("defi")),
        *weight_sub_posts(get_sub_data("web3"))
    ]

    top_posts.sort(key=lambda post: post.weight, reverse=True)

    top_10_posts = top_posts[0:20]

    filename = f'top_20_weekly_{date.today().strftime("%Y_%m_%d")}.csv'

    columns = ['Weight', 'URL', 'Title', 'Comments', 'Type', 'Body']

    with open(filename, "w") as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=columns)

        csvwriter.writeheader()

        logging.info("Writing to file ...")

        for post in top_10_posts:

            post_type = "Text Post" if post.is_self else "Link Post"

            body = post.selftext if post.is_self else "N/A"

            contents = dict(Weight=post.weight,
                            URL=post.url,
                            Title=post.title,
                            Comments=post.num_comments,
                            Type=post_type,
                            Body=body)

            csvwriter.writerow(contents)


if __name__ == "__main__":
    main()