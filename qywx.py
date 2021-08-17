#coding=ANSI
from playwright.sync_api import Playwright, sync_playwright
import ddddocr
from PIL import ImageGrab

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to 
    page.goto("http://ehall.hpu.edu.cn/infoplus/form/XSMRJKSB/start")

    # Click [placeholder="请输入账号"]
    page.click("[placeholder=\"请输入账号\"]")

    # Fill [placeholder="请输入账号"]
    page.fill("[placeholder=\"请输入账号\"]", "311922010508")

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "V075410V")

    box = (1233, 537, 1353, 570)
    img = ImageGrab.grab(box)
    img.save('E:\\v.png')

    ocr = ddddocr.DdddOcr()
    with open('E:\\v.png', 'rb') as f:
        img_bytes = f.read()
    r = ocr.classification(img_bytes)
    r=str(int(r[0])+int(r[2]))

    # Click [placeholder="请输入验证码"]
    page.click("[placeholder=\"请输入验证码\"]")
    # Fill [placeholder="请输入验证码"]
    page.fill("[placeholder=\"请输入验证码\"]", r)

    # Click input:has-text("登录")
    # with page.expect_navigation(url="https://ehall.hpu.edu.cn/infoplus/form/27878259/render"):
    with page.expect_navigation():
        page.click("input:has-text(\"登录\")")
    # assert page.url == "https://ehall.hpu.edu.cn/infoplus/form/XSMRJKSB/start"

    # Click #infoplus_view_1518_0 >> text=提交
    page.click("//body[1]/div[4]/form[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/ul[1]/li[1]/a[1]/nobr[1]")

    # Click text=确认
    page.click("//button[contains(text(),'确认')]")

    # Click text=确定
    # with page.expect_navigation(url="https://ehall.hpu.edu.cn/infoplus/form/27878259/render"):
    with page.expect_navigation():
        page.click("text=确定")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
