Title: Javascript reformating magic
Date: 2017-09-29
Summary: This post is about recently found amazing tool to make javascript (be readable) again.

How often site contains tons of unbearable, unreadable, worst ever javascript code?
This post is about recently found amazing tool to make javascript (be readable) again.

I often find myself trying to debug through auto-generated, and therefore badly formatted
javascript code like this:

```javascript
(function (){
    var win = (function(){
    var win = new Ext.Window({
        id: 'cmp_d4044a20'

 ,hidden: true
 ,width: 700
 ,height: 400






 ,boxMinHeight: 400

 ,boxMinWidth: 700

// ~2000 lines of pain down here
```

Isn't it be great to magically *re*-format it? As always, Google has a bunch of garbage links
and packages, that did no good, and I'm event won't link to that resources.

I'm present you a [Dirty Markup](https://dirtymarkup.com "Online markup cleaup tool") by
[Cory LaViska](https://www.patreon.com/claviska "Patreon page") that can format code from above to this beauty:

```javascript
(function() {
    var win = (function() {
        var win = new Ext.Window({
            id: 'cmp_d4044a20',
            hidden: true,
            width: 700,
            height: 400,
            boxMinHeight: 400,
            boxMinWidth: 700,
```