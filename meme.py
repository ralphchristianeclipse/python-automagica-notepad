from automagica import *
import os
import json
import requests
from multiprocessing.dummy import Pool

targetMeme = "Dexter-Chemistry"

browser = ChromeBrowser()


def getElements(url):
    browser.get(url)

    topText = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/input	')
    bottomText = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/input')

    englishRadioButton = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div[3]/label[1]/img')

    generateButton = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div[4]/a')

    return [topText, bottomText, englishRadioButton, generateButton]


def generateMeme(meme, top, bottom):
    topText, bottomText, englishRadioButton, generateButton = getElements(
        f"https://memegenerator.net/{meme}/caption")

    topText.send_keys(top)

    bottomText.send_keys(bottom)

    englishRadioButton.click()
    generateButton.click()
    Wait(2)
    image = browser.find_element_by_xpath(
        '/html/body/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/img')
    return image.get_attribute("src")


def downloadImage(url):
    filename = url.split('/')[-1]
    print(filename, url)

    r = requests.get(url)
    with open(f"./images/{filename}", 'wb') as outfile:
        outfile.write(r.content)


def downloadImagesInParallel(images):
    return Pool(os.cpu_count()).map(downloadImage, images)


memes = []

with open('memes.json') as jsonFd:
    memes = json.load(jsonFd)

images = [generateMeme(targetMeme, *meme.values()) for meme in memes]

downloadImagesInParallel(images)
browser.close()
