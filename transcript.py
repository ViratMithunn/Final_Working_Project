from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(url):
    video_id = url.replace('https://www.youtube.com/watch?v=', '')
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    output = ''
    for x in transcript:
        sentence = x['text']
        output += f'{sentence}\n'
    return output
