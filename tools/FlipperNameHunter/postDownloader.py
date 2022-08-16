import requests
from datetime import datetime
import traceback
import time
import json
import sys

username = ""  # put the username you want to download in the quotes
subreddit = "flipperzero"  # put the subreddit you want to download in the quotes
# leave either one blank to download an entire user's or subreddit's history
# or fill in both to download a specific users history from a specific subreddit

filter_string = None
if username == "" and subreddit == "":
	print("Fill in either username or subreddit")
	sys.exit(0)
elif username == "" and subreddit != "":
	filter_string = f"subreddit={subreddit}"
elif username != "" and subreddit == "":
	filter_string = f"author={username}"
else:
	filter_string = f"author={username}&subreddit={subreddit}"

url = "https://api.pushshift.io/reddit/{}/search?limit=1000&sort=desc&{}&before="

start_time = datetime.utcnow()


def downloadFromUrl(filename, object_type):
	print(f"Saving {object_type}s to {filename}")

	count = 0
	handle = open(filename, 'w')
	previous_epoch = int(start_time.timestamp())
	while True:
		new_url = url.format(object_type, filter_string)+str(previous_epoch)
		json_text = requests.get(new_url, headers={'User-Agent': "Post downloader by /u/Watchful1"})
		time.sleep(1)  # pushshift has a rate limit, if we send requests too fast it will start returning error messages
		try:
			json_data = json_text.json()
		except json.decoder.JSONDecodeError:
			time.sleep(1)
			continue

		if 'data' not in json_data:
			break
		objects = json_data['data']
		if len(objects) == 0:
			break

		for object in objects:
			previous_epoch = object['created_utc'] - 1
			count += 1
			if object_type == 'comment':
				try:
					handle.write(str(object['score']))
					handle.write(" : ")
					handle.write(datetime.fromtimestamp(object['created_utc']).strftime("%Y-%m-%d"))
					handle.write("\n")
					handle.write(object['body'].encode(encoding='ascii', errors='ignore').decode())
					handle.write("\n-------------------------------\n")
				except Exception as err:
					print(f"Couldn't print comment: https://www.reddit.com{object['permalink']}")
					print(traceback.format_exc())
			elif object_type == 'submission':
				if object['is_self']:
					if 'selftext' not in object:
						continue
					try:
						handle.write(str(object['score']))
						handle.write(" : ")
						handle.write(datetime.fromtimestamp(object['created_utc']).strftime("%Y-%m-%d"))
						handle.write("\n")
						handle.write(object['selftext'].encode(encoding='ascii', errors='ignore').decode())
						handle.write("\n-------------------------------\n")
					except Exception as err:
						print(f"Couldn't print post: {object['url']}")
						print(traceback.format_exc())

		print("Saved {} {}s through {}".format(count, object_type, datetime.fromtimestamp(previous_epoch).strftime("%Y-%m-%d")))

	print(f"Saved {count} {object_type}s")
	handle.close()


downloadFromUrl("posts.txt", "submission")
downloadFromUrl("comments.txt", "comment")
