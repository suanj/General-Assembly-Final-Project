from youtube_statistics import YTstats

API_KEY = "AIzaSyCvOo6y0w2cnaTCuprKd1lpZkIVAplN8AU"
channel_id = "UCxLzfLcNEtXsOSE_ysUTnXQ"

yt = YTstats(API_KEY, channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()