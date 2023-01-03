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

But all this is theory, what about practice?

As an example I will describe my first 'dialogue' with the SD neural network (the experiment used separately trained weights for a certain style, but this experiment can be done on any weights, I recommend using any standard SD chekpoint without a dreamboot, as they are cleaner and without additional distortion).

This 'dialogue' was built according to the following algorithm: I write the text, the neural network interprets it into a picture, the picture is transferred to the clip interrogator and it outputs the text as a response from the neural network. then these steps are repeated and a certain 'dialogue' is built.

# Dialogue example (proof of concept)

![212358-3918082497](https://user-images.githubusercontent.com/14146520/210339144-1f640a72-6cb8-48db-a8df-a452a623054b.png)
I'm: hello there
the neural network draws a picture (1), interrogator interprets it as:
'a cartoon character with a shirt on and a shirt on, with a caption that reads hello hello st martin, by Hiromu Arakawa'
where we can highlight the words hello, the rest is actually a feature of the clip interrogator, for example, indicating the supposed author of the picture and doubling parts of the description ‘a shirt on’

