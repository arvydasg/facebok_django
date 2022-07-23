# Interface for facebook automation script

Inspiration:
* Create a form - https://www.youtube.com/watch?v=uz5gyXemak0
* Run a script with django - https://www.youtube.com/watch?v=4VHtGm-4iBwPeXg

How it works: https://www.loom.com/share/4fcab1e5de5b4077a2b9eaeea5d079ba

* 2022-01-24 - DONE - allow to choose a number of groups to be posted to.
* NOT - Choose the types of groups to post to. (excel sheet)
* NOT - Images instead of coordinates
* NOT - Confirmation window
* NOT - database instead of excel sheet

# What is it for

A recently started smoothie drink powder business that is testing
itself out in the field. Instead of purchasing ads on facebook, the
client first wanted to post their content to various facebook groups
to see the engagement. Over time this tasks proved to be too tedious,
since it requires a lot of manual clicking.

I have decided to help them out by creating this automation bot that
posts to various facebook groups by itself, with client needing to
click only a few clicks. There were various facebook bots on the
internet, but you had to pay fro those. It was interesting for me to
see if I can create something like it myself.

#  How it works

All the user need is a link to the facebook post and a call to action
message. He then needs to input these two into the browser window and
click start.

Here is a short presentation of how it works.

##  Cons

There are a few cons of using this script.
1. You can not really use the computer while it runs since it occupies
   your mouse and you shouldn't be clicking on other windows while it
   is running. You can run this script while you are having a break,
   step away from your computer for 15min or so and come back with
   having your post shared to 30 or so groups.
2. Your facebook account gets restricted. Often. If you are posting to
   too many groups at a time. 20 or so is fine, but more than that (in
   one sitting) and you are risking to get a temporary ban by
   facebook.

## What to fix

- if the script breaks - take a screenshot of the whole screen (easier
  to debug what happened)
- when the script finishes posting to one group - take a screenshot
  (easier to track the activity)
- If group has pending posts - stop the for loop, run next group
- Rebuild facebook_django app with modules
