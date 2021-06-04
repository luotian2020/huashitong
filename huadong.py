#下滑滚动
import time

def scroll(driver):
    js="return action=document.body.scrollHeight"
    height=0
    newheight=driver.execute_script(js)
    while height<newheight:
        for i in range(height,newheight,100):
            driver.execute_script('window.scrollTo(0,{})'.format(i))
            time.sleep(0.5)
        height=newheight
        time.sleep(2)
        newheight=driver.execute_script(js)
