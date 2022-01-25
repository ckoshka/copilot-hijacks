NOTE: This requires you to actively engage in a dialogue with Copilot. All technical specifics including code were written by Copilot, all of the filler words (i.e "Let's do X") were written by me. Type partial sentences and let it complete them for you, it's quicker than typing out a full question.

# Vue in 90 Minutes
## Tutorial 1: Getting Started

In this tutorial, we're going to learn Vue from scratch. We'll start with simple examples then build on them, demonstrating essential concepts along the way. Specifically, from Tutorial 1 to 6, we'll cover the following:
* Declarative rendering
* Data binding
* Computed properties
* Event listeners
* Components
* Directives
* Filters
* Mixins

Let's set up a page with a single button on it. The button will contain a number that slowly increments up. We need a template for this.
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Grid Component</title>
    <script src="https://unpkg.com/vue"></script>
    <link rel="stylesheet" type="text/css" href="/style.css" />
    </head>
    <body>
        <div id="app">
            <button @click="increment">Click Me</button>
            <span>{{ counter }}</span>
        </div>
    <script>
        var app = new Vue({
            el: '#app',
            data: {
                counter: 0
            },
            methods: {
                increment: function() {
                    this.counter += 1;
                }
            }
        });
    </script>
</body>
</html>
```
Okay, cool. Now let's change the script so that it increases the width of the button itself as the counter increases.
```js
var better_app = new Vue({
    el: '#app',
    data: {
        counter: 0
    },
    methods: {
        increment: function() {
            this.counter += 1;
        }
    },
    computed: {
        buttonStyle: function() {
            return {
                width: this.counter * 10 + 'px'
            }
        }
    }
});
```
Then we change the html to:
```html
<button :style="buttonStyle" @click="increment">Click Me</button>
<span>{{ counter }}</span>  
```
Now, we can see that the button is now the same size as the counter.
Alright, so let's look at the full range of event listeners that Vue supports. We already know @click, but there's also @mouseover, @mouseout, @mouseenter, @mouseleave, @keydown, @keyup, @focus, @blur, @change, @input, @submit, @dblclick, @wheel, @drag, @dragstart, and @dragend. 

## Tutorial 2: Components
Components are a way to reuse code. They are a way to group together data and methods that are related. How do we do that? Simply just go:
```html
<div id="app">
    <my-component></my-component>
</div>
```
And then in the script, we can create a component:
```js
Vue.component('my-component', {
    template: '<p>This is a component</p>'
});

Now, what are filters? Filters are a way to manipulate data. For example, we can use a filter to make a string uppercase:
```js
Vue.filter('uppercase', function(value) {
    return value.toUpperCase();
});
```
Now, we can use the filter in our template:
```html
<p>{{ message | uppercase }}</p>
```
Now, we can use the filter in our component:
```js
Vue.component('my-component', {
    template: '<p>{{ message | uppercase }}</p>',
    data: function() {
        return {
            message: 'hello'
        }
    }
});
```
The | just means "pipe", and the uppercase filter is called on the message.

Wow. Straightforward, right? Let's look at directives. Directives are a way to add functionality to elements. For example, we can add a class to an element when it is clicked:
```html
<div id="app">
    <p v-on:click="addClass">Click me</p>
</div>
```
And then in the script:
```js
Vue.directive('add-class', {
    bind: function(el, binding, vnode) {
        el.classList.add(binding.value);
    }
});
```
Notice that we're using the bind method. This method is called when the directive is first bound to the element. In this case, we're adding a class to the element. We can also use the inserted method, which is called when the element is inserted into the DOM.

Great, but how do we invoke the directive in our component and add a useful class?
```js
Vue.component('my-component', {
    template: '<p v-on:click="addClass">Click me</p>',
    data: function() {
        return {
            message: 'hello'
        }
    },
    methods: {
        addClass: function() {
            this.$el.classList.add('important');
        }
    }
});
```

Again, Vue is designed to be simple to learn like this. Let's look at mixins. What mixins do is they allow you to add functionality to components. For example, we can add a class to all components:
```js
Vue.mixin({
    methods: {
        addClass: function() {
            this.$el.classList.add('important');
        }
    }
});
```

Okay, so now you might feel confident using Vue. But how do we import modules?
```js
import Vue from 'vue';
import VueRouter from 'vue-router';
import VueResource from 'vue-resource';
import App from './App.vue';
import routes from './routes';
```
 To spice things up, we're going to import Tailwind and use it to style our app.
```html
<link rel="stylesheet" href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css">
```
Now let's import the components we need:
```js
import MyComponent from './components/MyComponent.vue';
import MyOtherComponent from './components/MyOtherComponent.vue';
```
And then we can add them to our routes:
```js
routes: [
    { path: '/', component: MyComponent },
    { path: '/other', component: MyOtherComponent }
]
```
After that, we can start our app:
```js
new Vue({
    el: '#app',
    router: new VueRouter(routes),
    render: h => h(App)
});
```
Let's get messy and look at dynamic components, and some other v-bind directives. Full list of directives:
* v-bind:class
* v-bind:style
* v-bind:key
* v-on:click
* v-on:mouseover
* etc.
* v-bind:html
* v-bind:text
* v-bind:show
* v-bind:value
* v-bind:src
* v-bind:href
