from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!


<a href="https://www.accuweather.com/en/us/arlington-va/22201/weather-forecast/331250" class="aw-widget-legal">
<!--
By accessing and/or using this code snippet, you agree to AccuWeather’s terms and conditions (in English) which can be found at https://www.accuweather.com/en/free-weather-widgets/terms and AccuWeather’s Privacy Statement (in English) which can be found at https://www.accuweather.com/en/privacy.
-->
</a><div id="awcc1532187822421" class="aw-widget-current"  data-locationkey="331250" data-unit="f" data-language="en-us" data-useip="false" data-uid="awcc1532187822421"></div><script type="text/javascript" src="https://oap.accuweather.com/launch.js"></script>"

if __name__ == "__main__":
    application.run()
