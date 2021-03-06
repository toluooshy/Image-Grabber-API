from bs4 import BeautifulSoup
import requests

website = 'https://www.olin.edu'


class ImageScraper:
    def __init__(self, url):
        self.url = url
        self.html = ""
        self.images = []

    def get_html(self):
        """
        This function gets the raw html code from the website defined in self.url

        Takes: self
        Use: defines self.html
        Returns: self.html
        """
        try:
            self.html = BeautifulSoup(requests.get(self.url).content, 'lxml')
            return self.html
        except TypeError:
            print(
                "This function needs an object of the type 'string' to be passed into it to work.")

    def get_images(self):
        """
        This function gets the image src urls from the raw html defined in self.html

        Takes: self
        Use: defines self.images
        Returns: self.images
        """
        imgs = self.html.find_all('img')
        for img in imgs:
            try:
                if len(img['src']) > 0:
                    src = str(img['src']).replace(
                        't_lazy/', '').replace('e_pixelate/', '')
                    if src[0:6] == '//cdn.':
                        self.images.append(
                            ['https://' + src[2:], img['alt']])
                    if src[0:4] == '//i.':
                        self.images.append(
                            ['https://' + src[2:], img['alt']])
                    elif src[0:2] == '//':
                        self.images.append(
                            [str(self.url + '/' + src[2:]).replace('http://', 'https://'), img['alt']])
                    elif src[0:1] == '/':
                        self.images.append(
                            [str(self.url + '/' + src[1:]).replace('http://', 'https://'), img['alt']])
                    else:
                        self.images.append([str(src).replace(
                            'http://', 'https://'), img['alt']])
            except KeyError:
                pass
        return self.images


if __name__ == "__main__":
    urlimage = ImageScraper(website)
    urlimage.get_html()
    # print(urlimage.get_images())
