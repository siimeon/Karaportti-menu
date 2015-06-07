# Karaportti menu parser

## Problem description

Karaportti campus in Espoo has few different restaurants and it would be useful to check all 
menus in one view. For this problem the solution is to create scripts for data parsing to create JSON data for
HTML (AngularJS) frontend.

## Deployment plan

I have made very simple development plan for this project. My development is to run python parsing every day 
and publish results as artifact so they can be shown as web pages.

## Test in Docker container

I have made this project available Jenkins project in Jenkins container

```
docker run -d -p 8080:8080 shaakana/kara_menu
```

### Licence

My creations are licenced with GPLv2 licence
Read more about GPLv2 from [here](http://www.gnu.org/licenses/gpl-2.0.html)