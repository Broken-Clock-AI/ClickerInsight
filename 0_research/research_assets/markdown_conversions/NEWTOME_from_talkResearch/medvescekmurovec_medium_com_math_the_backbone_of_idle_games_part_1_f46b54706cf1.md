Sitemap

Open in app

Sign up

Sign in

Medium Logo

Write

Search

Sign up

Sign in

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Math — the backbone of Idle Games

![Dik Medvešček
Murovec](https://miro.medium.com/v2/resize:fill:64:64/2*_rckBSZmvJuXo6ZTPwBnmg.jpeg)

Dik Medvešček Murovec

8 min read

·

Mar 6, 2021

\--

Listen

Share

Press enter or click to view image in full size

> The main idea behind math in idle games is exponentiality.

Idle or Clicker games are games typically meant to be played passively with
the goal of amassing incredible wealth, defeating increasingly difficult
monsters, building empires — you name it.

This wasn’t always a popular genre, but its roots go back quite a while. The
first Idle game created is attributed to Progress Quest, released in 2002 and
the community flourished from then on. With titles like _AdVenture Capitalist,
Cookie Clicker, AFK Arena, Clicker Heroes, Almost a Hero, Realm Grinder,_ and
others breathing life into the genre and bringing it to the mainstream
audience.

While they are all different and unique in their own way, they have one thing
in common. Math as the backbone. This article will give you an insight into
how it all works and show you the exact equations used in your favorite games.

Clicker Heroes. An example of a popular idle game.

## Game loop

Let’s take a look at some basics before diving deep into the belly of the
beast. Idle games tend to feel very similar one to another but in their
essence, they all follow the same game loop. In this article, we focus on the
games without a specific victory condition, but rather the games focusing on
constant progression.

The basic loop of an idle game is simple. The player performs an action like
clicking a button (cookie), attacking a monster, or building a currency
generator. By clicking or building, the player starts generating the game’s
primary currency which can be spent for further upgrades and additional or
better generators.

Upgrades can range from simple things like more currency granted per
second/click or more damage dealt per click, to more complex like global game
speed increase. With each upgrade, the progression speeds up and the player
starts amassing an ever-increasing fortune which is then spent for further
upgrades.

This rapid growth continues until a so-called “progression wall” is reached.
This is a point in the game where the upgrades become too expensive and not
accessible to the player. That’s usually when the game offers a “New Game
Plus” in the form of ascension, tribute, prestige, or something similar.

New Game Plus is used to reset the player's progress but offers extremely
powerful permanent upgrades, such as permanently increased currency gain,
permanently increased damage, significantly cheaper upgrades, and similar.
With these upgrades the player can start his game over and progress further
than he was able to in the previous run until he reaches a second progression
wall, where he prestiges again, repeating ad infimum.

Press enter or click to view image in full size

Basic game loop visualized.

## Patterns and building blocks

To achieve this game loop, most idle games boil down to the same patterns.
Let’s take a look at some of the most common ones.

  * **Clicking:** You can’t escape clicking in idle games. It is usually only used at the beginning of the run after which you buy upgrades and auto generators, which your game into idle play (although sometimes you play actively throughout the entire game)
  * **Currency:** The main mode of purchasing upgrades, generators, multipliers, and bonuses. Also usually the main goal of the game. You want as much currency as possible.
  * **Upgrades:** Ways to improve currency production in exchange for large sums of currency. Upgrades can increase currency generation per click, give bonuses to generators, provide various multipliers, and much more.
  * **Generators:** Tools that generate currency on a specified time interval. Or sometimes they click in your stead or slay monsters for your benefit. Some games even include generator generators — generators that generate new generators of a weaker tier/level.
  * **Multipliers/Bonuses:** Many games provide the player with multipliers for various achievements, prestigeing, owning multiples of 10/25 of a specific upgrade or generator, … Some even offer Rewarded Ads as a way to earn temporary multipliers — eg. watch a 30-second ad in return for 4 hours of 2x more income.
  * **Prestige/Ascencion/New Game Plus:** Reset all current progress in exchange for powerful upgrades, mighty multipliers, or hefty bonuses on the next run that are otherwise not available to the player.
  * **Run:** A run in an idle game is the gameplay from game start to the prestige. So whenever a player performs a prestige, they start a new run.

## Math basics

Now that we understand the underlying mechanisms and game flow, we can look at
the math governing them. The goal of the developer is to create a fine balance
between the cost of upgrades or generators and the increase in currency
income. To make the game fun and exciting you want to have currency production
high in the beginning, but you have to make sure that the cost of upgrades
grows faster than the income increase.

By doing so, the player can buy multiple upgrades quickly, progress fast, and
get hooked on the game. If the cost of upgrades increases too quickly or is
too high, to begin with, the player doesn’t even get a chance to play the game
before they drop it. And by having upgrades cost much more than their income
per second, you eventually force the player to idle for longer and longer
times or to eventually prestige and start a new run.

To ensure this eventually happens it is easiest to visualize costs and
production as a mathematical function. The costs will overtake the production
rate as long as the growth rate of the production function is lower than the
growth rate of the cost function. For example, you could have the production
function grow polynomially and the cost function grows exponentially. Or have
the production grow linearly and the cost polynomially. You could even just
play around with the exponents in your polynomial or exponential functions and
see what happens.

### Function Growth

Growth of a function _f(x)_ is a simple way to explain how fast the value of
the function (cost of upgrades, generators, income per second, …) increases
with _x_(number of generators, level of upgrades, …)_._

All functions grow at a different pace. Let’s compare _y = x_ and _y = 0.1x²_.
The linear function (first) will start off at a bigger slope, but it will grow
at a constant rate. The polynomial function (second) on the other hand will
start off with a smaller slope but will grow faster and faster until it
eventually overcomes the linear one. This is always true when comparing linear
to polynomial. Even with _y = 1000x_ and _y = 0.00001x²_. The second one will
eventually start growing faster (at approximately _x = 100 million_).

Obviously, equations in games are rarely as simple as the ones we used in our
example, but as a rule of thumb, you can always look at an equation and ignore
everything but the fastest-growing part of the equation. _1 + log(x) + 123*x³_
is pretty much the same as _123*x³_ , which in turn is pretty much the same as
_x³_ , which we have in the table below under the name Polynomial.

If you want to go into detail on function growth, look into The Big O
notation, otherwise, you can look at the table for a simple reference guide.

Growth of functions. The lower you go on the list, the faster the function
grows.

We can look at another example where we compare a linear, polynomial and an
exponential function and plot them on a graph. As you can see, the linear
starts off strong, growing much faster than both the polynomial and the
exponential. But in the end, the exponential overtakes both.

Press enter or click to view image in full size

Comparing x (purple), 0.1x² (pink) and 1.15^x (green)

### Big Number Notations

This constant growth of numbers in idle games brings us to the various
notations— simple ways to write down large numbers.

When we look at big numbers, we all know thousands (k), millions (M), billions
(B), trillions (T) … what comes after that though? Most games resort to two
different mechanics. Either they decide on an **arbitrary notation** , for
example, a thousand times trillion is now _a,_ a thousand times _a_ is _b_ ,
and so on. Something the creator makes up on the spot.

Or they resort to **Scientific or E notation —** a standardized way of
expressing numbers that are too large or too small to be conveniently written
in decimal form. E notation follows the form of _xen_ , where _x_ is an
arbitrary number multiplied by 10 to the power of _n_. 6,320,000 would for
example be 6.32e6 or 6.32*10⁶

Arbitrary vs E notation

## Example: Woodchuck Idle

Let’s take this theory and put it into practice. Have you ever wondered how
much wood would a woodchuck chuck if a woodchuck could chuck wood?

This example is a simple game with only one goal. Gather as much wood as
possible. You start off as a simple woodchuck with a log in front of you. Each
time you click it you generate 1 wood.

The game offers you two upgrades:

> **Strong Tooth Upgrade** → Each click generates an additional wood  
> ∙ Initial cost: 10  
> ∙ Growth rate: 15% per level  
> ∙ Cost at level 5/20/100:
>
> **Hire a Woodchuck** → Generate 10 wood per second per woodchuck  
>  _∙ Initial cost:_ 100  
>  _∙ Growth rate:_ 7% per level  
>  _∙ Cost at 5/20/100 Woodchucks:_ 131/361/81.095

By using an exponential function to calculate the cost of upgrades at a
certain level, we can provide the user great value for money early on and also
guarantee that the user will eventually hit a wall in their progression since
both upgrades only offer a linear increase in income. Now since the user
playing Woodchuck Idle can’t earn fractional wood, we should always round our
costs up or down.

The equation used to calculate the cost of upgrades at a certain level.

Example: Cost of Hiring a Woodchuck, when you already have 19.

We can also see just how fast the costs increase because of a simple
exponential equation in the table below.

Looking at the costs we can see that progression in Woodchuck Idle will be
extremely easy in the beginning, but will get increasingly hard with each
level of Strong Tooth and Woodchuck hired. Which is exactly what we wanted.

At first, the player will click 10 times for one level of Strong Tooth, at
level two, the player will need just 6 clicks giving them a sense of
progression, but at level 30 and onwards, things become more and more
difficult with the player needing 20 clicks, then 59 clicks at level 40, 189
clicks at level 50 and so on. Maybe this is not the most optimal curve, but it
serves well as an example.

We’ll take a look at prestigeing, multipliers, and more complex examples in
part 2. Stay tuned!

## Sources

Way too many hours spent playing idle games  
https://en.wikipedia.org/wiki/Incremental_game  
https://en.wikipedia.org/wiki/Scientific_notation  
https://mobilefreetoplay.com/why-you-should-care-about-idle-games/  
https://www.gamasutra.com/blogs/AnthonyPecorella/20161013/282422/The_Math_of_Idle_Games_Part_I.php

Idle Games

Math

Game Development

Clicker Game

\--

\--

![Dik Medvešček
Murovec](https://miro.medium.com/v2/resize:fill:96:96/2*_rckBSZmvJuXo6ZTPwBnmg.jpeg)

![Dik Medvešček
Murovec](https://miro.medium.com/v2/resize:fill:128:128/2*_rckBSZmvJuXo6ZTPwBnmg.jpeg)

## Written by Dik Medvešček Murovec

16 followers

·5 following

UI&UX Designer | Frontend developer

## No responses yet

Help

Status

About

Careers

Press

Blog

Privacy

Rules

Terms

Text to speech

