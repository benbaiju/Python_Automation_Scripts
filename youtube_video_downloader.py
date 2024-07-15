import yt_dlp

def download_youtube_video(url):
    ydl_opts = {}

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', None)
            video_views = info_dict.get('view_count', None)
            
            print("Title:", video_title)
            print("Views:", video_views)
            print("Download complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    if url.strip():
        download_youtube_video(url)
    else:
        print("Invalid URL. Please enter a valid YouTube URL.")
