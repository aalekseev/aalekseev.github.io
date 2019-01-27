Title: Blog Optimization
Date: 2018-05-07T17:36:33+03:00
Summary: Recently I started to mess around with Hugo, a static-site generator, written in GO. I got some pitfalls with it, but overall it is a nice piece of software. I intend to develop a theme for this engine with semantic and accessibility in mind. So this is a plan of optimization that I composed.

Recently I started to mess around with Hugo, a static-site generator, written in GO. I got some pitfalls with it, but overall it is a nice piece of software. I intend to develop a theme for this engine with semantic and accessibility in mind.

So this is a plan of optimization that I composed.

## 1. Inline and minify crucial CSS
For blog theme I tried to write a minimal possible CSS (~150 lines), so why not inline it in a page? So browser won't needed to fetch it from the server.

## 2. Enable gzip
Found a neat [article](https://www.digitalocean.com/community/tutorials/how-to-add-the-gzip-module-to-nginx-on-ubuntu-14-04 "GZip Nginx module on Ubuntu 14") on DO about enabling gzip

1. Check that all lines with `gzip` are enabled
    
    ```console
    $ sudo vim /etc/nginx/nginx.conf
    ```

2. Add this line to not compress a very small files
    
    ```nginx
    gzip_min_length 256;
    ```

3. Replace line with types with larger one
    
    ```nginx
    gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript application/vnd.ms-fontobject application/x-font-ttf font/opentype image/svg+xml image/x-icon;
    ```

And finally, check that `Content-Encoding: gzip` is there

```console
$ curl -H "Accept-Encoding: gzip" -I http://localhost/test.css
```

## 3. Set Expires and Cache-Control Headers.

I found a good solution on [ServerFault](https://serverfault.com/questions/23157/setting-expires-headers-for-static-content-served-from-nginx#334871 "Setting expires headers for static content Nginx"). Basically you need to add a block like this:

```nginx
location ~* \.(?:ico|css|js|gif|jpe?g|png)$ {
    expires 30d;
    add_header Pragma public;
    add_header Cache-Control "public";
}
```

Check that headers added

```console
$ curl -I https://example.com/css/styles.css
```

## 4. Redirect index.html files to / urls
After some googling I found this snippet that can do exactly this:

```nginx
# block access to /index.(php|htm|html)
if ($request_uri ~ "/index.(php|html?)") {
    rewrite (.*)/ /$1 permanent;
}
```

## 5. Add a nice page for server errors
Adding custom error page is super easy

```nginx
location / {
    try_files $uri $uri/ =404;
    error_page 404 /404.html;
}
```

## Nice helpfull resources
This resources can help check site performance and accessibility issues.

### Speed

+ https://www.sitespeed.io
+ http://www.webpagetest.org
+ https://developers.google.com/speed/pagespeed/insights/

### Accessibility theory

+ http://webaim.org/resources/
+ http://a11yproject.com/
+ http://webaim.org/standards/508/checklist
+ https://github.com/brunopulis/awesome-a11y

### Accessibility testing

+ http://wave.webaim.org/
+ http://colororacle.org/
+ https://chrome.google.com/webstore/detail/accessibility-developer-t/fpkknkljclfencbdbgkenhalefipecmb?hl=en
+ http://www.checkmycolours.com/
+ http://webaim.org/resources/contrastchecker/

### Images

+ https://imageoptim.com/
+ https://pngmini.com/
+ https://github.com/svg/svgo
+ https://developers.google.com/speed/webp/

### Css

+ http://cssstats.com/
+ http://cssdig.com/
