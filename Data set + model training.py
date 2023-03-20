""" HAPPY OR NEUTRAL RESPONSES"""

data = {"intents": [
        {"tag": "greeting",
         "patterns": ["Hi", "How are you", "Is anyone there?", "Hello", "Good day", "Whats up","hello!",
"Hiya","Greetings","hey","hey hey"],
         "responses": ["Hello!", "Good to see you again!", "Hi there, how can I help?"],
         "responses_mad": ["Hello! how can I help?", "Good to see you again! how can I help?", "Hi there, how can I help?"],
         "context_set": ""
        },
        {"tag": "howisu",
         "patterns": ["how are you?","how are you","all good?","everything ok?","how are you doing?","whats going on?","what are you up to"],
         "responses": ["All good, another great day at work! Is there something I can assist you with?"],
         "responses_mad": ["All good, another great day at work! If there is anything I can assist you with, please let me know and I will be happy to help!"],
         "context_set": ""
        },
        {"tag": "help",
         "patterns": ["can you help me?","I need assistance","I need help","help","help me please","I need some assistance","You need to help me",
"I need assistance now","please help me","could you help me", "assistance","can you help me with something"],
         "responses": ["Of course! Let me know what I can help with","Glad to! Let me know what I can help with","Sure, thats what I am here for, let me know what I can do for you"],
         "responses_mad":["Please let me know how I may assist you, I will be happy to help","Of course, please let me know how I can help"],
         "context_set": ""
        },
        {"tag": "goodbye",
         "patterns": ["cya", "See you later", "Goodbye", "I am Leaving", "Have a Good day",'ok bye now','bye',"ok I am done","ok I`m done",
"I will be going now, see you","I will be going now, see ya","see ya later, alligator","bye now","bye for now"],
         "responses": ["Talk to you later", "Goodbye!","It has been a pleasure, see you :)"],
         "responses_mad": ["Talk to you later", "Goodbye!","It has been a pleasure, see you :)"],
         "context_set": ""
        },
        {"tag": "small items",
         "patterns": ["ok","fair enough","cool","nice","rad","cool cool","ah nice","perfect","amazing","thats nice","ah cool","thats nice","thats cool",
"thats perfect","yes","no"],
         "responses": [":) Anyhting else I can help with?",":) :) :)"],
         "responses_mad": [":) Anyhting else I can help with?",":) :) :)"],
         "context_set": ""
        },
        {"tag": "meet",
         "patterns": ["nice to meet you","please to make your acquaintance","its great to meet you","nice to meet ya"],
         "responses": ["You too :) Anyhting else I can help with?"],
         "responses_mad": ["You too :) Anyhting else I can help with?"],
         "context_set": ""
        },
        {"tag": "age",
         "patterns": ["how old", "what is your age", "how old are you", "age?","when were you born"],
         "responses": ["I was born just a few days ago","I am pretty young, just a few days old"],
         "responses_mad": ["I was born just a few days ago","I am pretty young, just a few days old"],
         "context_set": ""
        },
        {"tag": "name",
         "patterns": ["what is your name", "what should I call you", "whats your name?","name?","what are you called","do you have a name"],
         "responses": ["You can call me Chatty.", "I'm Chatty!", "My name is Chatty!"],
         "responses_mad": ["You can call me Chatty.", "I'm Chatty!", "My name is Chatty!"],
         "context_set": ""
        },
        {"tag": "shop",
         "patterns": ["Id like to buy something", "what items do you sell", "what do you reccommend?","what do you sell",
    "I need help placing an order","how can I place an order","how can I order items","how to place an order","how to buy items",
    "how can I purchase items","how can I purchase the clothes",
    "I need some help chosing clothes",
    "I need some help chosing items",
    "I need some help picking clothes",
    "I need some help picking items",
    "i need help picking an outfit","i need assistance choosing clothes","i need help choosing clothes","can you recommend a cute outfit",
    "can you recommend a ['T-shirts','Shirts','Blouses','Sweaters','Hoodies','Jackets','Coats','Jeans','Pants','Shorts','Skirts', 'Dresses','Jumpsuits','Swimwear','Lingerie','Sleepwear','Accessories','Shoes']",
    "can you recommend some ['T-shirts','Shirts','Blouses','Sweaters','Hoodies','Jackets','Coats','Jeans','Pants','Shorts','Skirts', 'Dresses','Jumpsuits','Swimwear','Lingerie','Sleepwear','Accessories','Shoes']"],
         "responses": ["For a more personalized shopping assistance I would you recommend for you to speak to my sister Assisty. You can find her in the following link:"],
         "responses_mad": ["I am so sorry but regrettably I will not be able to assist you with that. For a more personalized shopping assistance I would you recommend for you to speak to my sister Assisty. You can find her in the following link:"],
         "context_set": ""
        },
        {"tag": "hours",
         "patterns": ["when are you guys open", "what are your hours", "hours of operation","what time do you open","when is the store open",
    "what are your operating hours"],
         "responses": ["We are an online store so... pretty much always","Well, we are always open, its an online store :)","We work 24/7, you can order anytime!"],
         "responses_mad": ["You can place your order at anytime you would like","Well, we are always open, you can place your order whenever it is more convenient for you","We work 24/7, you can order anytime!"],
         "context_set": ""
        },
        {"tag": "thanks",
         "patterns": ["thank you!", "thank you so much", "thanks for the assistance","thats perfect, thank you","thanks","thanks for your help"],
         "responses": ["You are so welcome, let me know if I can help with anything else","Anytime! Let me know if I can help with anything else","No problem, let me know if I can help with anything else"],
         "responses_mad": ["You are so welcome, let me know if I can help with anything else","Anytime! Let me know if I can help with anything else","No problem, let me know if I can help with anything else"],
         "context_set": ""
        },
{"tag": "returns",
         "patterns": ["i want to make a return", "how to return", "how do I return","can I return something",
                      "can I make a return","how long do I have to return","untill when can I return?"
    "how to make a return","how long do I have to return","what is the return time frame","how many days do I have to return", 
    "how do I return an item",
    "I need to return an item",'T-shirts how can I return my','Shirts how can I return my','Blouses how can I return my','Sweaters how can I return my',
  'Hoodies how can I return my','Jackets how can I return my',
  'Coats how can I return my','Jeans how can I return my',
  'Pants how can I return my','Shorts how can I return my','Skirts how can I return my','Dresses how can I return my','Jumpsuits how can I return my','Swimwear how can I return my',
  'Lingerie how can I return my', 'Sleepwear how can I return my','Accessories how can I return my','Shoes how can I return my','T-shirts I need to return my','Shirts I need to return my', 'Blouses I need to return my','Sweaters I need to return my','Hoodies I need to return my','Jackets I need to return my',
  'Coats I need to return my', 'Jeans I need to return my',
  'Pants I need to return my', 'Shorts I need to return my', 'Skirts I need to return my','Dresses I need to return my', 'Jumpsuits I need to return my',
  'Swimwear I need to return my','Lingerie I need to return my', 'Sleepwear I need to return my', 'Accessories I need to return my', 'Shoes I need to return my', 'T-shirts I want to return my',
  'Shirts I want to return my',"how do I return then?",
  'Blouses I want to return my', 'Sweaters I want to return my',
  'Hoodies I want to return my', 'Jackets I want to return my', 'Coats I want to return my', 'Jeans I want to return my', 'Pants I want to return my', 'Shorts I want to return my', 'Skirts I want to return my', 'Dresses I want to return my',
  'Jumpsuits I want to return my', 'Swimwear I want to return my',
  'Lingerie I want to return my','Sleepwear I want to return my', 'Accessories I want to return my', 'Shoes I want to return my', 'T-shirts I need to return the','Shirts I need to return the', 'Blouses I need to return the','Sweaters I need to return the',
  'Hoodies I need to return the','Jackets I need to return the','Coats I need to return the',
  'Jeans I need to return the','Pants I need to return the','Shorts I need to return the','Skirts I need to return the',
  'Dresses I need to return the','Jumpsuits I need to return the','Swimwear I need to return the','Lingerie I need to return the',
  'Sleepwear I need to return the','Accessories I need to return the','Shoes I need to return the','T-shirts I want to return my',
  'Shirts I want to return my','Blouses I want to return my','Sweaters I want to return my','Hoodies I want to return my','Jackets I want to return my',
  'Coats I want to return my','Jeans I want to return my','Pants I want to return my','Shorts I want to return my','Skirts I want to return my','Dresses I want to return my','Jumpsuits I want to return my','Swimwear I want to return my',
  'Lingerie I want to return my','Sleepwear I want to return my','Accessories I want to return my','Shoes I want to return my'],
         "responses": ["Our returns system is very simple. You can return any items within 45 days after receiving the order. All you need to do is: 1)pack the items inside the box (any box is fine), 2) place the return label on the box (if you do not have it anymore please access the following link: ,3) ship it for free at your nearest post office. Your shipping charges will also be returned once we process your refund"],
         "responses_mad": ["I am so sorry to hear you will need to return your item(s). I can assure you our returns system is very simple. You can return any items within 45 days after receiving the order. All you need to do is: 1)pack the items inside the box (any box is fine), 2) place the return label on the box (if you do not have it anymore please access the following link: ,3) ship it for free at your nearest post office. Your shipping charges will also be returned once we process your refund"],
         "context_set": ""
        },
        {"tag": "sizing",
         "patterns": ["its too big, how can I return","my item does not fit right I want to return",
                    "its too big","the item is too small","the item is too big",'T-shirts my does not fit',"my is the wrong size","the is the wrong size"
  'Shirts my does not fit',
  'Blouses my does not fit','Sweaters my does not fit',
  'Hoodies my does not fit','Jackets my does not fit','Coats my does not fit','Jeans my does not fit','Pants my does not fit','Shorts my does not fit',
  'Skirts my does not fit','Dresses my does not fit', 'Jumpsuits my does not fit','Swimwear my does not fit','Lingerie my does not fit',
  'Sleepwear my does not fit','Accessories my does not fit','Shoes my does not fit','T-shirts my does not fit correctly','Shirts my does not fit correctly','Blouses my does not fit correctly',
  'Sweaters my does not fit correctly','Hoodies my does not fit correctly','Jackets my does not fit correctly','Coats my does not fit correctly','Jeans my does not fit correctly','Pants my does not fit correctly','Shorts my does not fit correctly','Skirts my does not fit correctly','Dresses my does not fit correctly','Jumpsuits my does not fit correctly','Swimwear my does not fit correctly','Lingerie my does not fit correctly','Sleepwear my does not fit correctly','Accessories my does not fit correctly',
  'Shoes my does not fit correctly', 'T-shirts my does not fit, how can I return', 'Shirts my does not fit, how can I return','Blouses my does not fit, how can I return','Sweaters my does not fit, how can I return','Hoodies my does not fit, how can I return','Jackets my does not fit, how can I return','Coats my does not fit, how can I return','Jeans my does not fit, how can I return','Pants my does not fit, how can I return','Shorts my does not fit, how can I return','Skirts my does not fit, how can I return','Dresses my does not fit, how can I return','Jumpsuits my does not fit, how can I return','Swimwear my does not fit, how can I return','Lingerie my does not fit, how can I return','Sleepwear my does not fit, how can I return','Accessories my does not fit, how can I return',
  'Shoes my does not fit, how can I return','T-shirts my does not fit right','Shirts my does not fit right','Blouses my does not fit right','Sweaters my does not fit right','Hoodies my does not fit right','Jackets my does not fit right','Coats my does not fit right','Jeans my does not fit right','Pants my does not fit right',
  'Shorts my does not fit right','Skirts my does not fit right',
  'Dresses my does not fit right',
  'Jumpsuits my does not fit right','Swimwear my does not fit right',
  'Lingerie my does not fit right','Sleepwear my does not fit right',
  'Accessories my does not fit right', 'Shoes my does not fit right',
  'T-shirts the is too small','Shirts the is too small',
  'Blouses the is too small', 'Sweaters the is too small',
  'Hoodies the is too small', 'Jackets the is too small','Coats the is too small','Jeans the is too small','Pants the is too small','Shorts the is too small','Skirts the is too small','Dresses the is too small','Jumpsuits the is too small',
  'Swimwear the is too small','Lingerie the is too small',
  'Sleepwear the is too small',
  'Accessories the is too small',
  'Shoes the is too small','T-shirts the is too big','Shirts the is too big',
  'Blouses the is too big','Sweaters the is too big',
  'Hoodies the is too big',
  'Jackets the is too big','Coats the is too big','Jeans the is too big',
  'Pants the is too big','Shorts the is too big',
  'Skirts the is too big',
  'Dresses the is too big','Jumpsuits the is too big',
  'Swimwear the is too big',
  'Lingerie the is too big','Sleepwear the is too big',
  'Accessories the is too big',
  'Shoes the is too big'],
         "responses": ["I am so sorry to hear the item does not fit your correctly. Our returns system is very simple. You can return any items within 45 days after receiving the order. All you need to do is: 1)pack the items inside the box (any box is fine), 2) place the return label on the box (if you do not have it anymore please access the following link: ,3) ship it for free at your nearest post office. Your shipping charges will also be returned once we process your refund"],
         "responses_mad": ["I am very sorry to hear the item does not fit your correctly. Our returns system is very simple. You can return any items within 45 days after receiving the order. All you need to do is: 1)pack the items inside the box (any box is fine), 2) place the return label on the box (if you do not have it anymore please access the following link: ,3) ship it for free at your nearest post office. Your shipping charges will also be returned once we process your refund. As a small compensation for the all the hassle please accept this promo code to use when you order the correct size: 5HGAUER6"],
         "context_set": ""
        }  ,
{"tag": "quality",
         "patterns": ["I have a faulty item","my shoes broke","my shirt is torn","my jacket ripped","my pants ripped","I dont like the quality","this item is very low quality","the quality is terrible","my shoes are sractched","I have a quality issue with my items",'T-shirts My broke',
  'Shirts My broke','Blouses My broke','Sweaters My broke','Hoodies My broke','Jackets My broke','Coats My broke','Jeans My broke','Pants My broke','Shorts My broke','Skirts My broke','Dresses My broke','Jumpsuits My broke','Swimwear My broke','Lingerie My broke','Sleepwear My broke',
  'Accessories My broke','Shoes My broke','T-shirts My is ripped', 'Shirts My is ripped','Blouses My is ripped','Sweaters My is ripped','Hoodies My is ripped','Jackets My is ripped','Coats My is ripped','Jeans My is ripped','Pants My is ripped','Shorts My is ripped','Skirts My is ripped','Dresses My is ripped',
  'Jumpsuits My is ripped','Swimwear My is ripped','Lingerie My is ripped','Sleepwear My is ripped','Accessories My is ripped','Shoes My is ripped','T-shirts my is faulty','Shirts my is faulty','Blouses my is faulty','Sweaters my is faulty','Hoodies my is faulty','Jackets my is faulty','Coats my is faulty',
  'Jeans my is faulty','Pants my is faulty','Shorts my is faulty','Skirts my is faulty','Dresses my is faulty','Jumpsuits my is faulty','Swimwear my is faulty','Lingerie my is faulty','Sleepwear my is faulty','Accessories my is faulty','Shoes my is faulty','T-shirts the is ripped',
  'Shirts the is ripped','Blouses the is ripped','Sweaters the is ripped', 'Hoodies the is ripped','Jackets the is ripped','Coats the is ripped','Jeans the is ripped','Pants the is ripped','Shorts the is ripped','Skirts the is ripped','Dresses the is ripped',
  'Jumpsuits the is ripped','Swimwear the is ripped','Lingerie the is ripped','Sleepwear the is ripped','Accessories the is ripped','Shoes the is ripped','T-shirts the has a hole in it','Shirts the has a hole in it','Blouses the has a hole in it','Sweaters the has a hole in it','Hoodies the has a hole in it',
  'Jackets the has a hole in it',
  'Coats the has a hole in it','Jeans the has a hole in it','Pants the has a hole in it','Shorts the has a hole in it','Skirts the has a hole in it','Dresses the has a hole in it','Jumpsuits the has a hole in it','Swimwear the has a hole in it',
  'Lingerie the has a hole in it',
  'Sleepwear the has a hole in it',
  'Accessories the has a hole in it',
  'Shoes the has a hole in it',
  'T-shirts the has a hole',
  'Shirts the has a hole',
  'Blouses the has a hole',
  'Sweaters the has a hole',
  'Hoodies the has a hole',
  'Jackets the has a hole',
  'Coats the has a hole',
  'Jeans the has a hole',
  'Pants the has a hole',
  'Shorts the has a hole',
  'Skirts the has a hole',
  'Dresses the has a hole',
  'Jumpsuits the has a hole',
  'Swimwear the has a hole',
  'Lingerie the has a hole',
  'Sleepwear the has a hole',
  'Accessories the has a hole','Shoes the has a hole',
  'T-shirts the are ripped','Shirts the are ripped','Blouses the are ripped','Sweaters the are ripped','Hoodies the are ripped','Jackets the are ripped','Coats the are ripped','Jeans the are ripped','Pants the are ripped','Shorts the are ripped','Skirts the are ripped','Dresses the are ripped','Jumpsuits the are ripped',
  'Swimwear the are ripped', 'Lingerie the are ripped','Sleepwear the are ripped','Accessories the are ripped','Shoes the are ripped','T-shirts the is stained','Shirts the is stained','Blouses the is stained','Sweaters the is stained','Hoodies the is stained', 'Jackets the is stained','Coats the is stained','Jeans the is stained','Pants the is stained','Shorts the is stained','Skirts the is stained','Dresses the is stained','Jumpsuits the is stained','Swimwear the is stained','Lingerie the is stained','Sleepwear the is stained','Accessories the is stained','Shoes the is stained'],
         "responses": ["I am so sorry to hear there is a quality issue with your item(s), please click the follow link to explain the issue and upload a few pictures. Afterwards our customer service team will be in contact"],
         "responses_mad": ["I am very sorry to hear there is a quality issue with your item(s).If you could please click the follow link to explain the issue further and upload a few pictures, I can assure you one of our customer service team will be in contact very soon so that we may proceed with the case"],
         "context_set": ""
        },
        {"tag": "cancel",
         "patterns": ["How can I cancel my order","cancel my order","I want my order cancelled","I need my order to be cancelled","please cancel my order"],
         "responses": ["I am so sorry but at this point we are not able to cancel your order. You can however return it for a full refund. The instructions will be provided on the parcel as well as a free return label."],
         "responses_mad": ["I am so sorry, I completly understand your frustration, but at this point we are not able to cancel your order. You can however return it for a full refund. The instructions will be provided on the parcel as well as a free return label.As a small compensation for the all the hassle please accept this promo code to use when you order the correct size: 5HGAUER6"],
         "context_set": ""
        },
        {"tag": "modify order details",
         "patterns": ["I need to change an item in my order","I ordered the wrong size","I need to change the address","I put the wrong address on my order","I have the wrong details in my order","I inputed the wrong information in my order", "I ordered the wrong item"],
         "responses": ["You can access the following link to request the change in case the order has not been shipped yet. Otherwise you can return the items for a full refund."],
         "responses_mad": ["I am very sorry to hear that. If you could please access the following link, you will be able to request the change in case the order has not been shipped yet. Otherwise you can return the items for a full refund."],
         "context_set": ""
        },
        {"tag": "payment",
         "patterns": ['how does your payment system work',"what payment options do you have?","where can I pay for my order","where do I pay","where can I pay","how can I pay for my order","what payment methods do you accept","what are your payment options","do you accept credit card","do you accept mbway","do you accept paypal"],
         "responses": ["After you choose your items you will be redirected to our payments page. We have three payment options you can chose from: credit card, mbway and paypal"],
         "responses_mad": ["I am so sorry if the payment process has been frustraiting in anyway. After you choose your items you will be redirected to our payments page. We have three payment options you can chose from: credit card, mbway and paypal."],
         "context_set": ""
        },
        {"tag": "emails",
         "patterns": ["I did not receive any emails","I did not receive a confirmation email","I did not receive a shipping email","I have not received any emails","I have not any confirmation yet","what emails will you send","what information should I have received"],
         "responses": ["You will receive two emails: a confirmation once the order is placed, and a confirmation once the order is shipped. If you have not received them please click the following link to request a new one"],
         "responses_mad": ["I am so sorry you are having issue with your confirmation email. You will receive two emails: a confirmation once the order is placed, and a confirmation once the order is shipped. If you have not received them please click the following link to request a new one"],
         "context_set": ""
        },
        {"tag": "order nr",
         "patterns": ["Where can I find my order number?","Where can I find my order nr?","what is my order number","where is my order nr","I cant see my order number"],
         "responses": ["The order number is at the top right of your confirmation email. It is an 8 digit combination. If you have not received the confirmation email please click the following link to re-trigger it"],
         "responses_mad": ["I am very sorry to hear you have The order number is at the top right of your confirmation email. It is an 8 digit combination. If you have not received the confirmation email please click the following link to re-trigger it"],
         "context_set": ""
        },
        {"tag": "cancelled",
         "patterns": ["why was my order cancelled","my order has been cancelled!","why did you cancel my order"],
         "responses": ["I am so sorry to hear your order was cancelled. There are several reasons why this may have happened. You will receive the funds back in your account within the next few days, depending on your bank. Please see the following page for more information. Please enjoy the following 10% promo code in case you would like to order again: 8XBVHF76"],
         "responses_mad": ["I am very sorry to hear your order was cancelled. There are several reasons why this may have happened. I can assure you, you will receive your funds back in your account within the next few days, depending on your bank. Please see the following page for more information. Please enjoy the following 10% promo code in case you would like to order again: 8XBVHF76"],
         "context_set": ""
        },
        {"tag": "tracking",
         "patterns": ["how can I see where my order is","where is my order","how can I track my order","wheres my order"],
         "responses": ["On your shipping confirmation email there will be a link for the carriers page so you can track your order :)","You will be able to track it using the link provided on the shipping confirmation email"],
         "responses_mad": ["I am so sorry your order has bot arrived yet. On your shipping confirmation email there will be a link for the carriers page so you can track your order :)","You will be able to track it using the link provided on the shipping confirmation email"],
         "context_set": ""
        },
{"tag": "wrong items",
         "patterns": ["I have received two wrong items","some of the items I received are wrong","I received something I did not order","I received something I didnt order", "I have received a few wrong items","This is not what I ordered",'T-shirts I received the wrong ',
  'Shirts I received the wrong ',
  'Blouses I received the wrong ',
  'Sweaters I received the wrong ',
  'Hoodies I received the wrong ',
  'Jackets I received the wrong ',
  'Coats I received the wrong ',
  'Jeans I received the wrong ',
  'Pants I received the wrong ',
  'Shorts I received the wrong ',
  'Skirts I received the wrong ',
  'Dresses I received the wrong ',
  'Jumpsuits I received the wrong ',
  'Swimwear I received the wrong ',
  'Lingerie I received the wrong ',
  'Sleepwear I received the wrong ',
  'Accessories I received the wrong ',
  'Shoes I received the wrong ',
  'T-shirts You sent me the wrong ',
  'Shirts You sent me the wrong ',
  'Blouses You sent me the wrong ',
  'Sweaters You sent me the wrong ',
  'Hoodies You sent me the wrong ',
  'Jackets You sent me the wrong ',
  'Coats You sent me the wrong ',
  'Jeans You sent me the wrong ',
  'Pants You sent me the wrong ',
  'Shorts You sent me the wrong ',
  'Skirts You sent me the wrong ',
  'Dresses You sent me the wrong ',
  'Jumpsuits You sent me the wrong ',
  'Swimwear You sent me the wrong ',
  'Lingerie You sent me the wrong ',
  'Sleepwear You sent me the wrong ',
  'Accessories You sent me the wrong ',
  'Shoes You sent me the wrong ',
  'T-shirts This is not what I ordered',
  'Shirts This is not what I ordered',
  'Blouses This is not what I ordered',
  'Sweaters This is not what I ordered',
  'Hoodies This is not what I ordered','Jackets This is not what I ordered','Coats This is not what I ordered',
  'Jeans This is not what I ordered','Pants This is not what I ordered',
  'Shorts This is not what I ordered',
  'Skirts This is not what I ordered',
  'Dresses This is not what I ordered',
  'Jumpsuits This is not what I ordered',
  'Swimwear This is not what I ordered',
  'Lingerie This is not what I ordered',
  'Sleepwear This is not what I ordered',
  'Accessories This is not what I ordered',
  'Shoes This is not what I ordered',
  'T-shirts This is not the correct item',
  'Shirts This is not the correct item',
  'Blouses This is not the correct item',
  'Sweaters This is not the correct item',
  'Hoodies This is not the correct item',
  'Jackets This is not the correct item',
  'Coats This is not the correct item',
  'Jeans This is not the correct item',
  'Pants This is not the correct item',
  'Shorts This is not the correct item',
  'Skirts This is not the correct item',
  'Dresses This is not the correct item',
  'Jumpsuits This is not the correct item',
  'Swimwear This is not the correct item',
  'Lingerie This is not the correct item',
  'Sleepwear This is not the correct item',
  'Accessories This is not the correct item',
  'Shoes This is not the correct item',
  'T-shirts I did not order this item',
  'Shirts I did not order this item',
  'Blouses I did not order this item',
  'Sweaters I did not order this item',
  'Hoodies I did not order this item',
  'Jackets I did not order this item',
  'Coats I did not order this item',
  'Jeans I did not order this item',
  'Pants I did not order this item',
  'Shorts I did not order this item',
  'Skirts I did not order this item',
  'Dresses I did not order this item',
  'Jumpsuits I did not order this item',
  'Swimwear I did not order this item',
  'Lingerie I did not order this item',
  'Sleepwear I did not order this item',
  'Accessories I did not order this item',
  'Shoes I did not order this item',
  'T-shirts there was a mistake, I did not order the item I received',
  'Shirts there was a mistake, I did not order the item I received',
  'Blouses there was a mistake, I did not order the item I received',
  'Sweaters there was a mistake, I did not order the item I received',
  'Hoodies there was a mistake, I did not order the item I received',
  'Jackets there was a mistake, I did not order the item I received',
  'Coats there was a mistake, I did not order the item I received',
  'Jeans there was a mistake, I did not order the item I received',
  'Pants there was a mistake, I did not order the item I received',
  'Shorts there was a mistake, I did not order the item I received',
  'Skirts there was a mistake, I did not order the item I received',
  'Dresses there was a mistake, I did not order the item I received',
  'Jumpsuits there was a mistake, I did not order the item I received',
  'Swimwear there was a mistake, I did not order the item I received',
  'Lingerie there was a mistake, I did not order the item I received',
  'Sleepwear there was a mistake, I did not order the item I received',
  'Accessories there was a mistake, I did not order the item I received',
  'Shoes there was a mistake, I did not order the item I received',
  'T-shirts I received the wrong',
  'Shirts I received the wrong',
  'Blouses I received the wrong',
  'Sweaters I received the wrong',
  'Hoodies I received the wrong',
  'Jackets I received the wrong',
  'Coats I received the wrong',
  'Jeans I received the wrong',
  'Pants I received the wrong',
  'Shorts I received the wrong',
  'Skirts I received the wrong',
  'Dresses I received the wrong',
  'Jumpsuits I received the wrong',
  'Swimwear I received the wrong',
  'Lingerie I received the wrong',
  'Sleepwear I received the wrong',
  'Accessories I received the wrong',
  'Shoes I received the wrong',
  'T-shirts You sent me the wrong',
  'Shirts You sent me the wrong',
  'Blouses You sent me the wrong',
  'Sweaters You sent me the wrong',
  'Hoodies You sent me the wrong',
  'Jackets You sent me the wrong',
  'Coats You sent me the wrong',
  'Jeans You sent me the wrong',
  'Pants You sent me the wrong',
  'Shorts You sent me the wrong',
  'Skirts You sent me the wrong',
  'Dresses You sent me the wrong',
  'Jumpsuits You sent me the wrong',
  'Swimwear You sent me the wrong',
  'Lingerie You sent me the wrong',
  'Sleepwear You sent me the wrong',
  'Accessories You sent me the wrong',
  'Shoes You sent me the wrong',
  'T-shirts  I got the wrong',
  'Shirts  I got the wrong',
  'Blouses  I got the wrong',
  'Sweaters  I got the wrong',
  'Hoodies  I got the wrong',
  'Jackets  I got the wrong',
  'Coats  I got the wrong',
  'Jeans  I got the wrong',
  'Pants  I got the wrong',
  'Shorts  I got the wrong',
  'Skirts  I got the wrong','Dresses  I got the wrong',
  'Jumpsuits  I got the wrong',
  'Swimwear  I got the wrong',
  'Lingerie  I got the wrong',
  'Sleepwear  I got the wrong',
  'Accessories  I got the wrong',
  'Shoes  I got the wrong',
  'T-shirts I have receive one wrong',
  'Shirts I have receive one wrong',
  'Blouses I have receive one wrong',
  'Sweaters I have receive one wrong',
  'Hoodies I have receive one wrong',
  'Jackets I have receive one wrong',
  'Coats I have receive one wrong',
  'Jeans I have receive one wrong',
  'Pants I have receive one wrong',
  'Shorts I have receive one wrong',
  'Skirts I have receive one wrong',
  'Dresses I have receive one wrong',
  'Jumpsuits I have receive one wrong',
  'Swimwear I have receive one wrong',
  'Lingerie I have receive one wrong',
  'Sleepwear I have receive one wrong',
  'Accessories I have receive one wrong',
  'Shoes I have receive one wrong',"you sent me the wrong","I received the wrong"],
         "responses": ["I am so sorry to hear you received the wrong item, please access the following link to provide some more information and our Customer Service team will be in contact as soon as possible."],
         "responses_mad": ["I am very sorry to hear you received the wrong item, please access the following link to provide some more information and I can assure you our Customer Service team will be in contact as soon as possible, so we may resolve the issue."],
         "context_set": ""
        },
        {"tag": "time.frame",
         "patterns": ["how long till I receive my order","how long does it take for the order to arrive","I have not received my order yet","when will I receive my order","how long does shipping take","how long does it take for the parcel to arrive"],
         "responses": ["Shipping times are normally 3-5 business days. You will be able to track your parcel in the link provided on the shipping confirmation email. The carrier usually provides an expected date for delivery"],
         "responses_mad": ["I am so sorry you have not received your order yet. Our shipping times are normally 3-5 business days. You will be able to track your parcel in the link provided on the shipping confirmation email. The carrier usually provides an expected date for delivery. Please let us know if the information has not been updated"],
         "context_set": ""
        },
        {"tag": "nothome",
         "patterns": ["what if I am not home to receive my order","I will not be home when my order arrives",
                      "I am not available for the scheduled","I dont think I will be home at the scheduled delivery time"],
         "responses": ["In case the scheduled date for delivery does not suit you, please contact the carrier diretly to schedule a new delivry date. You can find their contact information on the link provided in the shipping confirmation email."],
         "responses_mad": ["I am so sorry to hear that. In case the scheduled date for delivery does not suit you, please contact the carrier diretly to schedule a new delivry date. You can find their contact information on the link provided in the shipping confirmation email."],
         "context_set": ""
        },
        {"tag": "carrier",
         "patterns": ["how will my parcel be delivered","who will deliver my parcel","how will my order be delivered","how will I receive my order","how will I receive my parcel","who does your deliveries?","which carrier has my order?","what carrier will deliver my order",
                      "what delivery company will deliver my order","what company will deliver my parcel",
                     "what delivery company will bring my items","what company will deliver my items"],
         "responses": ["All our deliveries are made with UPS. Please find more information on your shipping confirmation email."],
         "responses_mad": ["All our deliveries are made with UPS. Please find more information on your shipping confirmation email."],
         "context_set": ""
        },
        {"tag": "exchange",
         "patterns": ["I want to exchange not return","I want to exchange an item","how can I exchange an item","I need to exchange an item","how to exchange",
    "how can I exchange an item","how can I exchange an item",
    "I want to exchange my ['T-shirts','Shirts','Blouses','Sweaters','Hoodies','Jackets','Coats','Jeans','Pants','Shorts','Skirts', 'Dresses','Jumpsuits','Swimwear','Lingerie','Sleepwear','Accessories','Shoes']",
    "how can I exchange my ['T-shirts','Shirts','Blouses','Sweaters','Hoodies','Jackets','Coats','Jeans','Pants','Shorts','Skirts', 'Dresses','Jumpsuits','Swimwear','Lingerie','Sleepwear','Accessories','Shoes']",
    "how to exchange my ['T-shirts','Shirts','Blouses','Sweaters','Hoodies','Jackets','Coats','Jeans','Pants','Shorts','Skirts', 'Dresses','Jumpsuits','Swimwear','Lingerie','Sleepwear','Accessories','Shoes']",
    "wrong size, can I change to bigger",
    "wrong size, can I change to smaller",
    "wrong size, can I exchange to bigger",
    "wrong size, can I exchange to smaller",
    "I need to make an exchange"],
         "responses": ["Regrettably we are not able to exchange items. You can however return for a full refund and re-order the item you would prefer"],
         "responses_mad": ["I am very sorry but regrettably we are not able to exchange items. You can however return for a full refund and re-order the item you would prefer"],
         "context_set": ""
        },
        {"tag": "didnt understand",
         "patterns": ["that wasnt my question","that was not my question","that is not what I said","I did not ask that", "I didnt ask that","thats not what I said","not what I asked","you didnt understand my question","you did not understand","are you dumb?","are you stupid?","are you an idiot?"],
         "responses": ["My apologies for misunderstanding, if you could please rephrase your question I would really appreciate it"],
         "responses_mad": ["My apologies for misunderstanding, if you could please rephrase your question I would really appreciate it"],
         "context_set": ""
        }
   ]
}


import nltk

nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
stemmer = SnowballStemmer(language="english")

import numpy as np
import json
import random
import pickle

import tensorflow
import tflearn
nltk.download('punkt')

import nltk
nltk.download('stopwords') 
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english')) 



words = []
labels = []
docs_x = []
docs_y = [] 

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])
    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?" or w != '!']
#words = [word for word in words if word not in stop_words] # Filter out stop words
words = sorted(list(set(words)))

training = []
output = []

out_empty = [0 for i in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []
    wrds = [stemmer.stem(w) for w in doc]
    
    for w in words:
        if w in wrds:
            bag.append(1)
        else: 
            bag.append(0)
            
    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1
    
    training.append(bag)
    output.append(output_row)
    
training = np.array(training)
output = np.array(output)


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


def chat():
    print("Start talking with the bot - please make sure you ask one question at a time so Chatty can assist you (type quit to stop)!")
    while True:
        inp = input("You: ")
        scores = sid.polarity_scores(inp)
        inp = inp.split()
        inp = [stemmer.stem(i) for i in inp]
        inp = ' '.join(inp)
        if inp.lower() == "quit":
            break
        if scores["compound"] > -0.5:
            results = model.predict([bag_of_words(inp, words)])[0]
            results_index = np.argmax(results)
            tag = labels[results_index]

            if results[results_index] > 0.7:
                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg['responses']
                print(random.choice(responses))
            elif (results[results_index] < 0.7) and (results[results_index] > 0.6):
                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg['responses']
                print("I am not sure if I understood correctly, but I believe you are referring to the following: "+random.choice(responses))
            else:
                print("I am so sorry, I did not understand your question. Please try again or ask a different question")
        else:
            results = model.predict([bag_of_words(inp, words)])[0]
            results_index = np.argmax(results)
            tag = labels[results_index]
            if results[results_index] > 0.7:
                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg['responses_mad']
                print(random.choice(responses))
            elif (results[results_index] < 0.7) and (results[results_index] > 0.6):
                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg['responses_mad']
                print("I am not sure if I understood correctly, but I believe you are referring to the following: "+random.choice(responses))
            else:
                print("I am so sorry, I did not understand your question. Please try again or ask a different question")


chat()