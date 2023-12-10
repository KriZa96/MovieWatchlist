def get_youtube_video_id(link):
    id = ""
    for index in range(len(link)-1, -1, -1):
        if link[index] == "=":
            id += link[index+1:]
    return id


def youtube_link(link):
    start = ""
    movie_id = get_youtube_video_id(link)
    for index in range(len(link)-1, -1, -1):
        if link[index] == "/":
            start += f'{link[:index-1]}/embed/{movie_id}'
            return start
