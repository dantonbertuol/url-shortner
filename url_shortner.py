import pyshorteners as short


class UrlShortner:
    def __init__(self, url):
        self.url = url
        self.shortner = short.Shortener()

    def shorter_url(self) -> str:
        try:
            short_url = self.shortner.tinyurl.short(self.url)
        except Exception as e:
            short_url = e
        return short_url


if __name__ == "__main__":
    while True:
        link = input('Your link: ')
        shortner = UrlShortner(link)

        short_link = shortner.shorter_url()

        print("Your short link:", short_link)

        retry = input('Do you want to try another link? [Y/n]\n> ')

        if retry.upper() == 'N':
            break
        elif retry.upper() == 'Y':
            continue
