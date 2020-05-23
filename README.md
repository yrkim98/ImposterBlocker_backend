# Impostor Blocker
## Project Overview
Hello! We're team **Imposter Blocker**. We're here with our new solution to fight online phishing.

**96%** of global cybercrime attacks can be attributed to phishing, yet there exists no viable solution to accurately fight phishing. These attacks cost the world **$6 trillion annually**, consequentially increasing brand erosion and reducing online channel adoption. We want to help enterprises counter phishing attacks to minimize financial losses and regain brand trust.

## Our Solution
We've created a detection algorithm that can accurately determine suspect phishing sites. Through our unique use of computer vision to detect logos and related brand content, paired with HTML classification, we provide clients with accurate and reliable detection scores. **We will help you secure your online presence!**


## Members

| Team Member | Position | Contact Info |
|--|--|--|
| ![enter image description here](https://i.imgur.com/LOBf6hf.jpg) <div>Saurav Kharb| <li>Product Design <li>Backend Dev.  | skharb@uw.edu
![Brian- ImposterBlocker](https://i.imgur.com/loWdGjv.png)<div>Brian Kim | <li>Computer Vision <li> Backend Dev.| yrkim98@uw.edu |
![Anushka- ImposterBlocker](https://i.imgur.com/YADRrmj.jpg)<div>Anushka Raheja | <li> UX Designer <li> Frontend Dev. | araheja@uw.edu
<div>Pranita Mantravadi | <li> Product Manager <li> Frontend Dev. | pranitam@uw.edu


<div>
<div>

# New User Guide

Welcome to Imposter Blocker! We're happy to have you.
When prompted, create a new user account by clicking **Sign Up** and **Log In** to your account.

## Profile Setup
Once logged in, the first order of business is setting up your credentials. This is important for our algorithms to work properly. You can do so by clicking the **Your Credentials** tab.
![Credentials Tab](https://i.imgur.com/pRFpx0z.png)
Once here, you should add all of your company domains by clicking the **+** button below **Company Domains**, and all company logos by clicking the **+** button below **Logo/Images**. Once uploaded, these will automatically save, and you are ready to test suspect sites.

## Testing Suspect Sites
You can test for phishing sites by using our URL input box on the **Home** page.
![Home](https://i.imgur.com/V8ze4Su.png)

 1. Enter a URL you wish to test in the provided input field.
 2. Click **Submit**.
 3. Wait for website to be scraped and analyzed. (This may take a while!)

## Interpreting Results
![Results Screen](https://i.imgur.com/ZzLwCKx.png)
You interpret the scores as follows:

 - <u>HTML Score</u>: The *HTML score*, based on scraping the HTML tags in the website and looking for common fishing patterns. Also analyzes the URL of your suspect site, seeing if they may be trying to impersonate your brand's URL.
 - <u> Logo score </u>: The *Logo Score*, is how confident our computer vision algorithm thinks your brand's logo may be on the suspect site. Suspect sites will usually have your logo, or a similarly copied logo.
 - <u> Blue Score </u>: The *Blur Score*, is how much blur, or other artifacts of copying images is present on the images on the suspect site. Suspect sites will usually have a higher blur score on the images on their page.
 **For all scores: The higher the score, the more likely it is a phishing site.**
 **100: Algorithm is sure this is a phishing site**
 **0: Algorithm is sure that this is NOT a phishing site**

# Future Direction

As of now, we hope to keep our project up and running after capstone ends. However, we do want to be mindful of the costs we are going to incur. For the purposes of the class, we will ensure that none of our personal billing information is being used for any Imposter Blocker service on the web or offline. We would also be working on a resource document to collect all the knowledge we’ve been able to gather over the past two quarters. This will be helpful for onboarding any newcomers to the team, as well as existing Capstone members. Our landing page and web services will remain functional but only accessible by protected individuals, so as to ensure public access and account creation on our web application are temporarily not possible. Finally, we will work on code maintenance and ease-of-reading so future developers inheriting the legacy code will have a structured guide to navigate through the codebase. We are optimistic for what Impostor Blocker’s future holds and hope to make great strides in our goals.
