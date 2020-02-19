from threading import Thread

from utils.download import download
from utils import get_logger
from scraper import scraper, text_list, visited, subdomains, wordFreq, output_fifty_most_common_words
import time

class Worker(Thread):
    def __init__(self, worker_id, config, frontier):
        self.logger = get_logger(f"Worker-{worker_id}", "Worker")
        self.config = config
        self.frontier = frontier
        super().__init__(daemon=True)
        
    def run(self):
        while True:
            tbd_url = self.frontier.get_tbd_url()
            if not tbd_url:
                from scraper import longestPageURL
                self.logger.info("Frontier is empty. Stopping Crawler.")
                print("Question 1. Total number of unique pages: ", len(visited))
                print("Question 2. The longest page is ", longestPageURL)
                print("Question 3. The  50 most commmon words are: ")
                output_fifty_most_common_words(wordFreq)

                print("Question 4. Total number of subdomains:, ", len(subdomains))
                print("Subdomain list and number of pages in each: ")
                for i,j in sorted(subdomains.items()):
                    print(i, ":", j)
                break
            resp = download(tbd_url, self.config, self.logger)
            self.logger.info(
                f"Downloaded {tbd_url}, status <{resp.status}>, "
                f"using cache {self.config.cache_server}.")
            scraped_urls = scraper(tbd_url, resp)
            for scraped_url in scraped_urls:
                self.frontier.add_url(scraped_url)
            self.frontier.mark_url_complete(tbd_url)
            time.sleep(self.config.time_delay)
