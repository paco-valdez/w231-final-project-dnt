# Measuring Do Not Track (DNT) signals effectiveness - Python Script.

There are multiple tools used to test web applications; most of them emulate the signals sent by browsers and try to capture the behavior of the websites when responding to scripted actions. Selenium is somewhat different than most of these tools. It uses real browsers to make the requests and connects to the backend services of the browsers to monitor the behavior of a website given a set of actions.


## Methodology Description
A limitation of Selenium is that by design, it does not gives access to the HTTP headers, making it impossible to be certain that the DNT header was sent. Selenium-wire is an extension built on top of Selenium that allows the monitoring of the headers sent to websites. With this script, a request for the top 100 websites is made. First without the DNT header enabled, then with the DNT header enabled. Then the number of cookies stored in both scenarios is counted. It has a try-catch clause to keep counting even if a request failed for any reason.

There are a few limitations with this methodology, if consent popups were implemented correctly, there would be no difference between requests made with the DNT header and requests made without it. The websites shouldn’t store anything until the user has given consent, but as mentioned before, many websites store cookies even before the user has given consent. It could be argued that if a user sent its preferences over the headers, there would be no need to store anything or even show a consent popup.

Another variation of this study could have been to count the cookies from every combination of the presence of the DNT header and accepting or rejecting cookies. This methodology is more manual intensive since it would require custom scripting to adapt the algorithm to every website surveyed.


## Usage

Help
```
python main.py --help
```

Usage
```
python main.py [INPUT FILE] [OUTPUT FILE]
```

Run test file
```
python main.py test.csv test_report.csv
```
