from flask import Flask, render_template, request,redirect, url_for, session
from flask import jsonify
import pickle
import numpy as np
import pandas as pd
import nltk
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
stemmer = SnowballStemmer(language="english")
import random
import tensorflow
import tflearn
nltk.download('punkt')
nltk.download('stopwords') 
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english')) 
import time
import datetime


data = pickle.load(open("data_dict.p","rb"))
words = pickle.load(open("words.p","rb"))
labels = pickle.load(open("labels.p","rb"))
training = pickle.load(open("training.p","rb"))
output = pickle.load(open("output.p","rb"))

history = []

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 20)
net = tflearn.fully_connected(net, 20)
net = tflearn.fully_connected(net, 20)
net = tflearn.fully_connected(net, 20)
net = tflearn.fully_connected(net, len(output[0]), activation ="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)
model.load("my_model.tflearn")


def bag_of_words(s, words):
    bag = [0 for i in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    
    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i]=(1)
    
    return np.array(bag)

bot_stats = pd.DataFrame(columns = ["ID","Int Nr","Sent_Score","user_input","not_und","bot_reply","time","minutes"])
minu = []
counter = 1
positive = 0
negative = 0
under = 0
n_under = 0
interactions = 0

website = Flask(__name__)

@website.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        inp = request.form["inp"]
        anwser = chat(inp)
        if anwser != "Chat ended":
            history.append("You: "+inp)
            history.append("Chatty: "+anwser)
        if anwser == "Chat ended":
            return redirect(url_for("index"))
        return render_template("home.html",anwser=anwser, history=history)
    return render_template("home.html")

def chat(inp):
    global counter
    global history
    global interactions
    while True:
        scores = sid.polarity_scores(inp)
        inpu=inp
        inp = inp.split()
        inp = [stemmer.stem(i) for i in inp]
        inp = ' '.join(inp)
        if inp.lower() == "clear":
            history = []
            counter += 1
            return "Chat ended"
        elif scores["compound"] > -0.4:
            results = model.predict([bag_of_words(inp, words)])[0]
            results_index = np.argmax(results)
            tag = labels[results_index]

            if results[results_index] > 0.7:
                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg['responses']
                        und = False
                        resp = random.choice(responses)
                interactions +=1
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                minu = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').minute
                update_bot_stats(counter,interactions, scores["compound"], inpu, und, resp,timestamp,minu)
                visual(scores["compound"],und,interactions)
                return resp
            elif (results[results_index] < 0.7) and (results[results_index] > 0.6):
                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg['responses']
                        und = True
                        resp = random.choice(responses)
                interactions +=1
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                minu = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').minute
                update_bot_stats(counter,interactions, scores["compound"], inpu, und, resp,timestamp,minu)
                visual(scores["compound"],und,interactions)
                return "I am not sure if I understood correctly, but I believe you are referring to the following: "+resp
            else:
                resp = "I am so sorry, I did not understand your question. Please try again or ask a different question"
                und = True
                interactions +=1
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                minu = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').minute
                update_bot_stats(counter,interactions, scores["compound"], inpu, und, resp,timestamp,minu)
                visual(scores["compound"],und,interactions)
                return "I am so sorry, I did not understand your question. Please try again or ask a different question"
        else:
            results = model.predict([bag_of_words(inp, words)])[0]
            results_index = np.argmax(results)
            tag = labels[results_index]
            if results[results_index] > 0.7:
                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg['responses_mad']
                        und = False
                        resp = random.choice(responses)
                interactions +=1
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                minu = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').minute
                update_bot_stats(counter,interactions, scores["compound"], inpu, und, resp,timestamp,minu)
                visual(scores["compound"],und,interactions)
                return  resp
            elif (results[results_index] < 0.7) and (results[results_index] > 0.6):
                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg['responses_mad']
                        resp = random.choice(responses)
                        und = True
                interactions +=1
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                minu = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').minute
                update_bot_stats(counter,interactions, scores["compound"], inpu, und, resp,timestamp,minu)
                visual(scores["compound"],und,interactions)
                return "I am not sure if I understood correctly, but I believe you are referring to the following: "+resp
            else:
                resp = "I am so sorry, I did not understand your question. Please try again or ask a different question"
                und = True
                interactions +=1
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                minu = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').minute
                update_bot_stats(counter,interactions, scores["compound"], inpu, und, resp,timestamp,minu)
                visual(scores["compound"],und,interactions)
                return "I am so sorry, I did not understand your question. Please try again or ask a different question"
    


def update_bot_stats(ID,inter, sent_score,user_input,not_und, bot_reply, timer,minu):
    global bot_stats
    new_row = {"ID": ID,"Int Nr":inter, "Sent_Score": sent_score, "user_input": user_input, "not_und": not_und, "bot_reply": bot_reply,"time":timer,"minutes":minu}
    new_row=pd.DataFrame([new_row])
    bot_stats = pd.concat([bot_stats, new_row],axis=0)

def visual(sent_score,X, interact):
    global positive
    global negative
    global under
    global n_under
    global bot_stats
    if sent_score > -0.4:
        positive += 1
    else:
        negative += 1
    if X == True:
        n_under += 1
    else:
        under += 1
    

    fig, (ax1, ax2) = plt.subplots(1,2)
    ax1.bar(['positive','negative'], [positive, negative],color=['#2EB430', '#BD270D'])
    ax1.set_title("Positive/Neutral vs Negative")
    ax2.bar(['Understood','Not understood'], [under, n_under],color=['#3B8642', '#B65843'])
    ax2.set_title("Understood vs Not Understood")
    fig.subplots_adjust(wspace=0.2,hspace=0.2)

    plot_name = f"static/my_plot_{time.time()}.png"
    plt.savefig(plot_name)

    fig2, ax3 = plt.subplots()
    ax3.plot(bot_stats['minutes'].unique(),[bot_stats[bot_stats['minutes']==a]['Int Nr'].count() for a in bot_stats['minutes'].unique()], color = '#485049')
    ax3.set_title("Nr of interactions per minute")
    plt.xlabel('Time (minutes)')
    plt.ylabel('Nr interactions')
    plt.show()
    plot_name2 = f"static/my_plot2_{time.time()}.png"
    fig2.savefig(plot_name2)
    plt.close()
    return plot_name, plot_name2


@website.route("/analytics")
def analytics():
    plot_url, plot_name2 = visual(0.0,0.0,0.0)
    random_number = random.randint(1, 1000000)
    return render_template("analytics.html", data=bot_stats.to_html(),plot_url=plot_url,plot_name2=plot_name2, random=random_number)


@website.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        password = request.form["pass"]
        if user == 'santos.123' and password == "12345":
           print("Login successful!")
           time.sleep(2)
           return redirect("/analytics") 
    return render_template("login.html")

if __name__ == "__main__":
    website.run(port = 8000, debug = True)

