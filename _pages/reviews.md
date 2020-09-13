---
title: Reviews
layout: page
permalink: /en/reviews/
breadcrumb: 
  - label: Home
    url: /
ref: reviews
lang: en
---

<style type="text/css">

.fa-star{
  color: #2C98F0;
}
.review-name {
  letter-spacing: 0;
}
</style>

<div>

 {% for review in site.data.reviews %}
  <div>
    <div>
        <span class="float-right">
              <i class="fas fa-star fa-xs"></i>
              <i class="fas fa-star fa-xs"></i>
              <i class="fas fa-star fa-xs"></i>
              <i class="fas fa-star fa-xs"></i>
              <i class="fas fa-star fa-xs"></i>
        </span>
        <h4 class="review-name">{{review.name}}</h4>
        <p>{{review.date}}</p>
    </div>
    <div>
        <p>{{review.text}}</p>
    </div>
  </div>
  <hr>
  {% endfor %}
</div>

<p>More reviews <a target="_blank" href="https://www.healthgrades.com/physician/dr-daniel-gologorsky-y9qfc2z">here</a></p>