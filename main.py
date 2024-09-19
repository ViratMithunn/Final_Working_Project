from transcript import get_transcript
from gpt import check_facts

def main():
    video_url = 'https://www.youtube.com/watch?v=B6Pc6YRgDqo'
    print(f"Fetching transcript for: {video_url}")
    transcript = get_transcript(video_url)
    print("Transcript fetched.")
    print("Checking facts...")
    result = check_facts(transcript)
    print("Fact-checking result:")
    print(result)

if __name__ == "__main__":
    main()
