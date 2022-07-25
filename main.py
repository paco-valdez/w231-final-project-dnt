from time import sleep

import click

from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


def read_file(fin):
    content = None
    with open(fin, "r") as f_in:
        content = f_in.readlines()
    return content

def add_protocol(url):
    if url.startswith('http://') or url.startswith('https://'):
        return url
    return f'https://{url}'

def add_endslash(url):
    if url.endswith('/'):
        return url
    return f'{url}/'

def count_cookies(url, dnt=False):
    profile_path = 'default.profile'
    options = Options()
    options.set_preference('profile', profile_path)
    options.set_preference("javascript.enabled", True)
    options.set_preference("privacy.trackingprotection.enabled", dnt)
    driver = webdriver.Firefox(options=options)

    driver.get(url)

    sleep(5)

    for request in driver.requests:
        if request.url == url:
            print(request.headers)

    # driver.find_element(By.ID, 'truste-show-consent').click()
    # sleep(2)
    # driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'truste_popframe'))
    # sleep(2)
    # element = driver.find_element(By.CLASS_NAME, 'rejectAll')
    # driver.execute_script("arguments[0].scrollIntoView();", element)
    # element.click()
    # sleep(2)
    # driver.switch_to.default_content()

    cookies = driver.get_cookies()
    for cookie in cookies:
        print(cookie)

    n_cookies = len(cookies)
    print(n_cookies)
    driver.close()
    return n_cookies


@click.command()
@click.argument('filepath', type=click.Path(exists=True))
@click.argument('out_file', type=click.Path())
def cookies(filepath, out_file):

    rows = read_file(filepath)
    fp = open(out_file, 'w')
    fp.write('url,n_cookies,n_cookes_dnt\n')
    fp.close()
    for row in rows:
        row = row.split(',')
        if row:
            url = row[1].strip().replace('\n', '')
            url = add_protocol(url)
            url = add_endslash(url)
            n = -1  # invalid
            dnt_n = -1  # invalid
            try:
                n = count_cookies(url, dnt=False)
                dnt_n = count_cookies(url, dnt=True)
            except:
                pass
            line = f'{url},{n},{dnt_n}'
            print(line)
            fp = open(out_file, 'a')
            fp.write(f'{line}\n')
            fp.close()


if __name__ == '__main__':
    cookies()
