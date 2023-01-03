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


