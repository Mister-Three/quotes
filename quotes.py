import random
import time

quotes = [
    '“All our dreams can come true, if we have the courage to pursue them.” – Walt Disney',
    '“The secret of getting ahead is getting started.” – Mark Twain',
    '“I’ve missed more than 9,000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed. I’ve failed over and over and over again in my life and that is why I succeed.” – Michael Jordan',
    '“Don’t limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve.” – Mary Kay Ash',
    '“The best time to plant a tree was 20 years ago. The second best time is now.” – Chinese Proverb',
    '“It’s hard to beat a person who never gives up.” – Babe Ruth',
    '“I wake up every morning and think to myself, ‘how far can I push this company in the next 24 hours.’” – Leah Busque',
    '“If people are doubting how far you can go, go so far that you can’t hear them anymore.” – Michele Ruiz',
    '“We need to accept that we won’t always make the right decisions, that we’ll screw up royally sometimes – understanding that failure is not the opposite of success, it’s part of success.” – Arianna Huffington',
    '“Write it. Shoot it. Publish it. Crochet it, sauté it, whatever. MAKE.” – Joss Whedon',
    '“You’ve gotta dance like there’s nobody watching, love like you’ll never be hurt, sing like there’s nobody listening, and live like it’s heaven on earth.” ― William W. Purkey',
    '“Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten.”― Neil Gaiman',
    '“Everything you can imagine is real.”― Pablo Picasso',
    '“When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.” ― Helen Keller',
    '“Do one thing every day that scares you.”― Eleanor Roosevelt',
    '“It’s no use going back to yesterday, because I was a different person then.”― Lewis Carroll',
    '“Smart people learn from everything and everyone, average people from their experiences, stupid people already have all the answers.” – Socrates',
    '“You’re off to great places, today is your day. Your mountain is waiting, so get on your way.” - Dr. Seuss',
    '“You always pass failure on the way to success.” - Mickey Rooney',
    '"I have the simplest tastes. I am always satisfied with the best" -Oscar Wilde',
]
nice_messages = [
    'You are awesome',
    'You are loved',
    'You are an amazing person',
    'People want to be around you',
    'You are very smart',
    '<3'
    'People wish they could be as cool as you',
    'People can\'t argue with such an awesome person like you.',
    'You\'re special',
    'Out of 7 billion people, you are unique.',
    'Take care of those that take care of you, and you\'ll see how much your life will change.',
    'Nothing is impossible when you have the right person by your side.',
    'Friendship is something you can\'t buy or sell. It\'s priceless therefore you have to take care of it and make sure your friends are happy. Each and every day.',
    '',
]

print("Hello <3")
time.sleep(1)
while True:
    ask = input("What type of uplifting sentence do you want today? A quote, or a nice message? \n")
    if ask == 'quote':
        print(random.choice(quotes))
        time.sleep(2)
    if ask == 'nice messages':
        print(random.choice(nice_messages))
        time.sleep(2)
    if ask == 'nice message':
        print(random.choice(nice_messages))
        time.sleep(2)
    if ask == 'quotes':
        print(random.choice(quotes))
        time.sleep(2)
