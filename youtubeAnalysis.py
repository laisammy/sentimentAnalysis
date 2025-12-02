from youtube_comment_downloader import YoutubeCommentDownloader

video_id = "x1wQ3lNJf3c"  # IMPORTANT: Only the ID, not full URL

downloader = YoutubeCommentDownloader()

comments = downloader.get_comments(
    video_id,
    sort_by=0,     # 0 = Top comments, 1 = Newest
    sleep=.1       # reduce rate-limit issues
)

fileName = "comments_" + video_id + ".txt"

count = 0
max_comments = 50

for c in comments:
    with open(fileName, "w", encoding="utf-8") as f:
        for c in comments:
            text = c["text"].replace("\n", " ")   # remove multiline breaks
            f.write(text + "\n")
            if count >= max_comments:
                break
