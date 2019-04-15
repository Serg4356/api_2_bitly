import requests
import os
import sys
from dotenv import load_dotenv
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='''
                    Program creates short bitly link
                    if url inputted by user is not shortified yet,
                    and returns counts of redirects if url is already added
                    '''
    )
    parser.add_argument(
        'link',
        help='Enter your short bitly link or long url')
    return parser


def get_bitlink(token, long_url):
	url = 'https://api-ssl.bitly.com/v4/bitlinks'
	payload = {
            "long_url": long_url
	}
	headers = {
            'Authorization': 'Bearer {}'.format(token),
	}
	response = requests.post(
		url,
		json=payload,
		headers=headers
		)
	return response


def get_bitlink_redirect_count(token, bitlink):
	url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(bitlink)
	headers = {
            'Authorization': 'Bearer {}'.format(token),
	}
	params = {
            'unit': 'day',
            'units': -1,
	}
	response = requests.get(
		url,
		params=params,
		headers=headers
		)
	return response


def is_bitlink(token, link):
  url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(link)
  headers = {'Authorization': 'Bearer {}'.format(token)}
  response = requests.get(url, headers=headers)
  return response.ok


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TOKEN')
    parser = create_parser()
    users_link = parser.parse_args().link
    if is_bitlink(token, users_link):
      print('Redirects count is: {}'.format(
        get_bitlink_redirect_count(
          token,
          users_link
          ).json()['total_clicks']
        ))
    else:
      try:
        response = get_bitlink(token, users_link)
        response.raise_for_status()
        print('Short link: {}'.format(response.json()['link']))
      except requests.exceptions.HTTPError:
        print('WARNING!\n{}'.format(response.json()['message']))
