from appium.webdriver import Remote
import time,telebot,pytesseract 
from PIL import Image 
TOKEN = "7586753756:AAGYIRR-GlpPH1y2grfHifY2nVe_r3ODbD0"
def send_message_to_telegram(message):
    bot = telebot.TeleBot(TOKEN)
    CHAT_ID = 5681806139
    bot.send_message(chat_id=CHAT_ID, text=message)
username = "tlaryan_P10ps8"
access_key = "eqBzgQyMAvFpKc8tyzox"
app_id = "04114f5bee5aadb67f305e2ac2bf6fe3ba81e941"
desired_caps = {
    'platformName': 'Android',
    'device': 'Samsung Galaxy S23',
    'os_version': '13',
    'app': 'bs://' + app_id,
    'browserstack.user': username,
    'browserstack.key': access_key,
    'noReset': True,
    'fullReset': False,
}
try:
    Game = Remote('https://hub-cloud.browserstack.com/wd/hub', desired_caps)
    time.sleep(10)    
    # Example Action
    Game.tap([(500, 1000)], 1000)
    time.sleep(5)
    print("Tapped on position (500, 1000)")
    # Capture Screenshot and Analyze
    screenshot_path = "game_screen.png"
    Game.save_screenshot(screenshot_path)
    text = pytesseract.image_to_string(Image.open(screenshot_path))
    print("Detected text:", text)
    # Send Result to Telegram
    send_message_to_telegram(f"Automation completed successfully! Detected text: {text}")
except Exception as e:
    #send_message_to_telegram(f"Error: {str(e)}")
    print(f"Error: {str(e)}")
finally:
    if 'Game' in locals() and Game is not None:
        Game.quit()

