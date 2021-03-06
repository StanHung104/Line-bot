from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('nbmyidt6LUb1WgS7cMTcwBLt3m3EHdrVafsyFzcwYnI7dwL/ejnnfMMxpwtkw1iNwkSVhgyTWmctLMoHTu7M9DNLtk70fnVWS5lKEAw8JoY687ddetEezbd0+WpYt4/c9e2LGGltH/1fs42RdfUnjgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2c39ed006388b510651a7d6f50701766')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我這邊正常，你要不要再試一次'

    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='2',
            sticker_id='23'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    if msg in ['hi', 'Hi', '你好', '您好', '安安', 'HI']:
        r = '嗨'
    elif msg in ['吃飯', '你吃飯了嗎?', '吃飯了嗎']:
        r = '你要請客嗎?'
    elif msg in ['你是誰', '你是誰?', '?', 'who are you']:
        r = '您好，我是Stan建置的機器人'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))

#上傳圖片
    sticker_message = StickerSendMessage(
    package_id='1',
    sticker_id='1')


if __name__ == "__main__":
    app.run()