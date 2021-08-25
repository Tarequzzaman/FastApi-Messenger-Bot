Facebook Messenger FastAPI

Create environments with Python3.7

Install reqiments


  ```
    pip install -r requirements.txt
  ```

Convert `env.example` to `.env` and fullfill the  variables 
<br><br>
`FB_APP_SECRET`=<br>
`FB_VERIFY_TOKEN`=<br>
`FB_PAGE_ACCESS_TOKEN`=<br>


for collecting this three variable you have  to follow the boelow steps

1. Visit a facebook page 
2. Visit https://developers.facebook.com/apps/?show_reminder=true
3. If you don't have account on developers facebook then create account 
4. Create an new app on https://developers.facebook.com/apps/?show_reminder=true
4. `FB_APP_SECRET` is find to `Dashboard`->`Setting`->`Basic` (App Secret)
5. Click on products then setup `Messenger`
6. You got `FB_PAGE_ACCESS_TOKEN`   from -><br>
     Go to `Access Tokens` section and click on the `Add or remove page` then click on `Generate Token` Button copy this token. 
7. `FB_VERIFY_TOKEN` is a random token more than 8 char
8. You collected all three variable required for you project


Run this project using: 

```
uvicorn app.main:app --reload
```

Finally we run this project. But for testing the bot we need to add callback url to messenger app setting Webhooks section. One problem arise hare. For callback url you need a secure url like `https`.


You need to download Ngrok from   here: https://ngrok.com/download

Go to the downloaded folder using teminal and type:
```
./ngrok http 8000
```

It will generate 2 links one is http and another one is https. Just copy the https link.   


Now we are ready with our https secure url. Go to the app deshboard  `Messenger` ->`Setting` ->`Webhook` and add the `Callback URL` as 

```
https link from ngrok/webhook
```
example: 
```
https://6a42d3b4.ngrok.io/webhook
```

`Verify Token` is the same of `FB_VERIFY_TOKEN`

then click on `Varify and Save` 

Now you can send message from your messener to your facebook page inbox