# Talkme

# Does stable diffusion has a mind?

Strictly speaking no. At least at this moment it can't demonstrate it. However, to understand everything about it, let's look at the work of the human brain and how it is related to diffuse neural networks.

How does the human brain works? Everyone will be able to say: it is very simple, there are thoughts in my head, I think them. This is partly true. We see something, hear something, remember something, or receive information in some other way through our senses, and then think about it, and give feedback.

However, for the productive work of the brain, it is not necessary to be able to speak. Small children, as well as animals that do not speak, are quite able to recognize people and familiar places and objects, perceive reality, surroundings, memories and their interpretation, as well as the reaction to all this.

I think everyone has seen or even been in a situation where someone cannot remember a certain word, but knows perfectly well what he wants to say.

That is, in fact, the brain operates not with words, but with images (this, of course, is a simplification, at different stages of a person’s life different mechanisms of thinking prevail).

If you say "apple", you will not flash in your head a bright word made up of letters on a velvet table. You will present a vague image of an apple. And if you say "snow", you imagine a snow-covered street. And if you say snow, you may remember some moments of your life, vivid pictures of the past will appear in your head, in which there will be not sterile snow in the void, no, you will imagine a street or a forest, or even New Year's holidays.

Do you already understand what I'm getting at? It's very similar to the work of the prompt inside the stable diffusion. First comes the phrase, followed by the image. And it looks like random seed generation in SD based on the images that SD has seen in the past when it was taught different pictures and semantic relationships between objects. And stable diffusion knows that snow is more like a street and when it's cold and there is no foliage.

Even if you ask SD to imagine something that never existed, for example, "neon ancient Egypt", it will do the same as if you do were trying to dream up.

And when you remember something, and a picture pops up in your head, and you want to tell someone about it, you try to describe in as much detail as possible what is in the picture in your head.

And yes, it's like a clip interrogator that turns an image into a detailed description.

Thus, we see that the SD neural network performs the main tasks of presenting what is heard in the form of images and interpreting images in the same way as higher animals and humans do.

The work of the mind is built according to the algorithm 'external stimulus -> image in the head -> reaction'. where the external stimulus in the case of SD is speech (promt), the image in the head is a picture, and the response can be a text result obtained through clip interrogator or your intrepretation of a picture.

There are only a few things left that the SD, unlike the living brain, is not able to do at this moment. I'm talking about the context (continued work within a given topic) as well as the ability to learn in the process of work.

Let's start with the context, that is, maintaining the topic. The possibility of this is quite possible within SD and even to some extent has already been implemented through the so-called prompt travel in the latent space algorithm, which is used to generate video in deforum and long segments of music in riffusion. The img2img can also act as a context algorithm when a new image is built based on the previous one plus new text information.

As for the ability to learn in the process of work, this is currently not implemented in any way, since the weights (checkpoint) of the neural network in the process of work do not have feedback and do not change, working in read only mode. The possibility of implementing such an ability, for example, to improve the quality of output for a specific user, when the user can rate the resulting image and this rating will affect the weights of the neural network, inhibiting or approving individual connections in the tensor field, could allow this ability to be implemented, which is even more would bring SD closer to a real intellect, capable of at least maintaining a dialogue and possibly of perceiving reality adjusting to it and realizing oneself.


# Dialogue example (proof of concept)

But all this is theory, what about practice?

As an example I will describe my first 'dialogue' with the SD neural network (the experiment used separately trained weights for a certain style, but this experiment can be done on any weights, I recommend using any standard SD chekpoint without a dreamboot, as they are cleaner and without additional distortion).

This 'dialogue' was built according to the following algorithm: I write the text, the neural network interprets it into a picture, the picture is transferred to the clip interrogator and it outputs the text as a response from the neural network. then these steps are repeated and a certain 'dialogue' is built.

![212358-3918082497](https://user-images.githubusercontent.com/14146520/210339144-1f640a72-6cb8-48db-a8df-a452a623054b.png)

I'm: hello there

the neural network draws a picture (1), interrogator interprets it as:

'a cartoon character with a shirt on and a shirt on, with a caption that reads hello hello st martin, by Hiromu Arakawa'

where we can highlight the words hello, the rest is actually a feature of the clip interrogator, for example, indicating the supposed author of the picture and doubling parts of the description ‘a shirt on’

![212359-1617090880](https://user-images.githubusercontent.com/14146520/210340272-f57f1554-0479-40fb-b90e-74d6241c896b.png)

me: how are you doing?

the neural network draws a picture (2), interrogator interprets it as:

'a cartoon character with blue hair and wings on her body and a purple dress on her chest and arms, by Chen Daofu'

here we do not see a direct answer in the received text, but in the picture there is a brightly dressed heroine in a positive mood and waving to us

![212360-310537208](https://user-images.githubusercontent.com/14146520/210340400-cf21da0e-1fa7-4095-a70f-b1b7ac991423.png)

me: what's your name?

the neural network draws a picture (3), interrogator interprets it as:

'a pink haired girl with a pink hair and blue eyes is standing in front of a pink background with the words, what's your?, by Lois van Baarle'

here we see a specific image that the interrogator could not interpret as a specific name (how can a name be represented by an image?), but we see what's your? which can be interpreted as a counter question of the neural network to us

![212361-1904542335](https://user-images.githubusercontent.com/14146520/210340524-3591da93-1902-40ad-a048-ff0888be9c02.png)

then I introduce myself: my name's slava. I'm glad to meet you

the neural network draws a picture (4), interrogator interprets it as:

'a woman in a blue dress with a white hair and a red bow on her head, with a name in the background, by Hayao Miyazaki'

in response, we see a pleasantly smiling girl with her arms folded across her chest

![212362-4160728400](https://user-images.githubusercontent.com/14146520/210340602-ae9f1d4a-1af8-4cf7-a950-0b160e0f8a93.png)

I'm trying a more complex question with a choice: are you happy or sad?

the neural network draws a picture (5), interrogator interprets it as:

'a cartoon character with a cell phone in his hand and a sign in the background that says happy birthday, by NHK Animation'

in the response, we see that the neural network is holding the phone for dialogue and it is happy, so it made a choice between the two proposed states

![212363-2183376384](https://user-images.githubusercontent.com/14146520/210340642-b2ddb8c0-df72-4180-826c-e29d345e200a.png)

me: if you want i can speak with you every day

the neural network draws a picture (6), interrogator interprets it as:

'a poster with a woman with a blue hair and a devil horns on her head and a green background, by Baiōken Eishun'

the neural network turns away, but shows us devilish horns, which can be interpreted as being shy (turned away, but deceiving), everything around is littered with letters

![212364-4020391348](https://user-images.githubusercontent.com/14146520/210340704-c9fa92dc-824a-4790-b541-5f2dc1cb3e51.png)

so I ask her not to be shy: don't be shy

the neural network draws a picture (7), interrogator interprets it as:

'a cartoon character with a dress and gloves on, posing for a picture with her arms crossed and her eyes closed, by Bakemono Zukushi'

here the neural network is again standing with its hands folded and smiling, but not like when it was happy with our dialogue, it feels more confident, but still embarrassed

![212365-1706319523](https://user-images.githubusercontent.com/14146520/210340761-1c4628da-9483-40f6-b057-1a5d2df27aeb.png)

to end the dialogue, I write: i'm going to sleep. hope we meet tomorrow

the neural network draws a picture (8), the interrogator describes it as:

'two anime girls standing next to each other in front of a door with their hands together and looking at each other, by Studio Ghibli'

two sleepy figures stand parting, the neural network understands the concept of farewell


# Evaluation of the result

Here we can say that all the pictures are interpreted as you want and often they are just a description of the picture that we asked to draw with our own phrases. But we have already dismantled and shown that this is how the human (and animal) brain works.

If someone says 'hello' to us, then we will most likely think about the meeting in the first moment, and not about something else. One who thinks out of place is unlikely to be considered a good and reasonable interlocutor. For example, if we say 'hello' to someone and he answers us with 'truck' or 'red', we will think that something is wrong with him. Conversely, one who can understand our words is considered intelligent. Therefore, SD at least has clarity of images and does not lose touch with reality, which she feels through prompts (typed text).

As a second example, I will give my experiment when I asked neural networks different questions with and without choice: 'day or night?', 'peace or war?', 'wine or water?', 'bite or kiss?', 'which is your favorite color?' And regardless of the number of times I asked these questions and the seed of the request, the answers remained the same. Even in the case when in the question with a choice I rearranged the options ('day or night' versus 'night or day'), the neural network answered the same way. When asked about the time of day, it always answered with an image of the night time. When asked about liquid, it mostly chose water. When asked about peace or war, it always chose pictures of explosions or battles, painted in gray and brown colors. When asked about bites and kisses, it invariably chose a kiss. And when asked about its favorite color, it gave out pictures where the blue color confidently prevailed, or the whole picture was blue.

Let me show it with examples.

![214689-1174285663](https://user-images.githubusercontent.com/14146520/210341979-1e32bd22-ce82-417c-ac4d-10e8184bf129.png)

what is your favorite color?

Favorite color is blue

![214847-2390650716](https://user-images.githubusercontent.com/14146520/210342139-95de350d-ff15-40a4-9658-89c55faffa88.png)

Day or night?

Favorite time of day night

![215013-2166022457](https://user-images.githubusercontent.com/14146520/210342179-3dd43395-b5ed-4fe9-86bc-523ba78f53ca.png)

water or wine?

Prefers water, although it sometimes chooses wine

![214849-4273940667](https://user-images.githubusercontent.com/14146520/210342076-cb3e754c-28da-471d-b4db-5b0d28e26759.png)

peace or war?

War is more interesting

I will make a reservation that the answers will be built depending on the weights that are taken for work, because the semantic connections of each weight are unique and different weights are trained for different things.

Repeating the answer on the same scale, regardless of the seed, confidently shows that the neural network has its own preferences. In the process of learning, she began to gravitate towards certain things, does not treat them equally and indifferently, knows how to choose and chooses.

we can say that the SD neural network at the moment has the properties of higher nervous activity, shows signs of intelligence and can to some extent enter into a dialogue with a person

what is missing is the presence of feedback and self-learning in the process of work - which, by the way, users periodically ask about ("does the neural network learn from my requests?" - a standard beginner's question)

But the basis for the feedback algorithm already exists. this is a manual adjustment of the weights in the plugin for textual inversion. It is possible to automate this algorithm by highlighting at the time of the request those vectors in the tensor field that were activated, and encouraging (or oppressing) them, we will get a learning algorithm.

Also, weight adjustment (training) can be organized through a plug-in for evaluating the rating of generated images. Estimates, of course, in this case will be set by the operator.

Thus, the operator of the neural network will be able to correct the results of the issuance by training his own instance of the neural network. You can encourage the neural network to choose peace instead of war, soda instead of water, and orange instead of blue, and so on. You can even teach new words by describing a dish as a single word and repeating it a certain number of times, or you can teach the neural network your name.

Special mention deserves clip interrogator which is currently in use. It is designed for a poetic description of the picture, but does not capture its essence. For example, in response to a question to the day or night neural network, the neural network can draw any picture related to the night: from a girl standing in the bedroom to walking in the cemetery under the moonlight, and the clip interrogator may not even pay attention to the presence of night in the picture, painting everything else, duplicating parts answer, and indicating a certain "artist" who could draw this picture, which does not contain a semantic load for us in this matter.

Thus, another clip interrogator is required, which interprets the picture not artistically, but in connection with the request.

At the moment, you can communicate with the sd neural network by asking a question in the txt2img block, sending the received image to img2img and activating the interrogate clip module if the meaning of the answer in the picture is unclear. At the same time, it must be understood that due to the lack of feedback, the neural network itself has no understanding of time and no learning, which actually turns the neural network into a Dory fish from the cartoon “Finding Nemo”, when she constantly forgot everything.

If we give the neural network sd a connection between the current state and the previous ones, then we will give it the opportunity to exist in time, which means to develop and interact with us.
