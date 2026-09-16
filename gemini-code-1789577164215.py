# Generate Jekyll site directory structure and files
import os

jekyll_structure = {
    "_config.yml": """title: Rejoice Customs
description: Personalized Keepsakes, Custom Stationery & Tailored Gifts
baseurl: ""
url: ""
instagram_username: rejoice_customs

collections:
  products:
    output: true
    permalink: /products/:name/

defaults:
  - scope:
      path: ""
      type: "products"
    values:
      layout: "product"
""",
    "_layouts/default.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title | default: site.title }}</title>
    <link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
</head>
<body>

    <header>
        <img src="{{ '/assets/images/logo.png' | relative_url }}" alt="{{ site.title }}" class="logo">
        <p>{{ site.description }}</p>
        <a href="https://instagram.com/{{ site.instagram_username }}" target="_blank" class="cta-btn">Order on Instagram (@{{ site.instagram_username }})</a>
    </header>

    {{ content }}

    <footer>
        <p>&copy; {{ site.time | date: '%Y' }} {{ site.title }}. All Rights Reserved.</p>
        <p>Direct Message us on Instagram: <a href="https://instagram.com/{{ site.instagram_username }}" target="_blank">@{{ site.instagram_username }}</a></p>
    </footer>

</body>
</html>
""",
    "assets/css/style.css": """:root {
    --primary: #0056b3;
    --primary-dark: #003d80;
    --secondary: #007bff;
    --bg-color: #f4f8fb;
    --card-bg: #ffffff;
    --text-color: #1a2530;
    --text-light: #4a5d6e;
    --accent: #e6f0fa;
    --border: #d0e1f9;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
}

body {
    background-color: var(--bg-color);
    color: var(--text-color);
    line-height: 1.6;
}

header {
    background-color: #ffffff;
    color: var(--text-color);
    text-align: center;
    padding: 40px 20px;
    border-bottom: 2px solid var(--border);
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}

.logo {
    max-width: 220px;
    height: auto;
    margin-bottom: 15px;
}

header p {
    font-size: 1.1rem;
    color: var(--text-light);
    margin-bottom: 20px;
}

.cta-btn {
    display: inline-block;
    background-color: var(--secondary);
    color: #ffffff;
    padding: 12px 28px;
    text-decoration: none;
    border-radius: 25px;
    font-weight: 600;
    transition: background 0.3s ease;
    box-shadow: 0 4px 12px rgba(0, 123, 255, 0.25);
}

.cta-btn:hover {
    background-color: var(--primary-dark);
}

.container {
    max-width: 1100px;
    margin: 40px auto;
    padding: 0 20px;
}

.section-title {
    text-align: center;
    font-size: 1.8rem;
    color: var(--primary);
    margin-bottom: 30px;
    position: relative;
}

.section-title::after {
    content: '';
    display: block;
    width: 50px;
    height: 3px;
    background-color: var(--secondary);
    margin: 10px auto 0;
    border-radius: 2px;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 25px;
    margin-bottom: 50px;
}

.card {
    background-color: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 4px 8px rgba(0, 86, 179, 0.04);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 18px rgba(0, 86, 179, 0.1);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 12px;
}

.card-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--primary);
}

.card-price {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--secondary);
    white-space: nowrap;
}

.badge {
    display: inline-block;
    background-color: var(--accent);
    color: var(--primary);
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    padding: 4px 8px;
    border-radius: 4px;
    margin-bottom: 12px;
    align-self: flex-start;
}

.card-desc {
    font-size: 0.95rem;
    color: var(--text-light);
    margin-bottom: 15px;
}

.view-btn {
    background-color: transparent;
    color: var(--secondary);
    border: 1.5px solid var(--secondary);
    padding: 8px 16px;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    align-self: flex-start;
}

.view-btn:hover {
    background-color: var(--secondary);
    color: #ffffff;
}

.modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.65);
    backdrop-filter: blur(4px);
    align-items: center;
    justify-content: center;
}

.modal-content {
    background-color: #ffffff;
    margin: auto;
    padding: 25px;
    border-radius: 12px;
    max-width: 520px;
    width: 90%;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    position: relative;
    text-align: center;
    animation: modalFadeIn 0.25s ease-out;
}

@keyframes modalFadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

.close-btn {
    position: absolute;
    top: 12px;
    right: 18px;
    color: var(--text-light);
    font-size: 24px;
    font-weight: bold;
    cursor: pointer;
}

.close-btn:hover {
    color: var(--primary);
}

.carousel-container {
    position: relative;
    margin: 15px 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.modal-img {
    width: 100%;
    max-height: 320px;
    object-fit: cover;
    border-radius: 8px;
    border: 1px solid var(--border);
}

.nav-arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0, 86, 179, 0.75);
    color: white;
    border: none;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.2s;
    user-select: none;
}

.nav-arrow:hover {
    background: var(--primary-dark);
}

.nav-arrow.prev { left: 10px; }
.nav-arrow.next { right: 10px; }

.thumbnail-strip {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-top: 10px;
}

.thumb {
    width: 50px;
    height: 50px;
    object-fit: cover;
    border-radius: 6px;
    cursor: pointer;
    border: 2px solid transparent;
    opacity: 0.6;
    transition: all 0.2s ease;
}

.thumb.active, .thumb:hover {
    opacity: 1;
    border-color: var(--secondary);
}

.modal-title {
    color: var(--primary);
    font-size: 1.4rem;
    margin-bottom: 5px;
}

.modal-price {
    color: var(--secondary);
    font-size: 1.2rem;
    font-weight: bold;
}

.modal-desc {
    color: var(--text-light);
    font-size: 0.95rem;
    margin-top: 10px;
}

.order-section {
    background-color: #eaf2fb;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 40px;
    margin-bottom: 50px;
}

.order-steps {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-top: 25px;
}

.step {
    background: var(--card-bg);
    padding: 20px;
    border-radius: 8px;
    text-align: center;
    border: 1px solid var(--border);
}

.step-num {
    width: 35px;
    height: 35px;
    background-color: var(--primary);
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    margin: 0 auto 12px;
}

footer {
    text-align: center;
    padding: 30px 20px;
    background-color: var(--primary);
    color: #e6f0fa;
    font-size: 0.9rem;
}

footer a {
    color: #ffffff;
    text-decoration: underline;
    font-weight: bold;
}
""",
    "assets/js/gallery.js": """let currentImages = [];
let currentImageIndex = 0;

function openGallery(title, price, imageArray, desc) {
    document.getElementById('modalTitle').innerText = title;
    document.getElementById('modalPrice').innerText = price;
    document.getElementById('modalDesc').innerText = desc;
    
    currentImages = imageArray;
    currentImageIndex = 0;
    
    updateGalleryView();
    
    const modal = document.getElementById('productModal');
    modal.style.display = 'flex';
}

function updateGalleryView() {
    document.getElementById('modalImg').src = currentImages[currentImageIndex];
    
    const thumbStrip = document.getElementById('thumbStrip');
    thumbStrip.innerHTML = '';
    
    const prevBtn = document.querySelector('.nav-arrow.prev');
    const nextBtn = document.querySelector('.nav-arrow.next');
    if (currentImages.length <= 1) {
        prevBtn.style.display = 'none';
        nextBtn.style.display = 'none';
    } else {
        prevBtn.style.display = 'flex';
        nextBtn.style.display = 'flex';
    }

    currentImages.forEach((imgSrc, index) => {
        const thumb = document.createElement('img');
        thumb.src = imgSrc;
        thumb.className = 'thumb' + (index === currentImageIndex ? ' active' : '');
        thumb.onclick = function() {
            currentImageIndex = index;
            updateGalleryView();
        };
        thumbStrip.appendChild(thumb);
    });
}

function changeSlide(direction) {
    currentImageIndex += direction;
    if (currentImageIndex < 0) {
        currentImageIndex = currentImages.length - 1;
    } else if (currentImageIndex >= currentImages.length) {
        currentImageIndex = 0;
    }
    updateGalleryView();
}

function closeModal() {
    document.getElementById('productModal').style.display = 'none';
}

function closeModalOutside(event) {
    const modal = document.getElementById('productModal');
    if (event.target === modal) {
        closeModal();
    }
}
""",
    "index.html": """---
layout: default
title: Rejoice Customs | Personalized Keepsakes & Gifts
---

<div class="container">
    {% assign categories = site.products | map: "category" | uniq %}
    
    {% for category in categories %}
    <h2 class="section-title">{{ category }}</h2>
    <div class="grid">
        {% assign items = site.products | where: "category", category %}
        {% for item in items %}
        <div class="card">
            <div>
                <div class="card-header">
                    <div class="card-title">{{ item.title }}</div>
                    <div class="card-price">${{ item.price }}</div>
                </div>
                <span class="badge">{{ item.badge }}</span>
                <p class="card-desc">{{ item.description }}</p>
            </div>
            <button class="view-btn" onclick="openGallery('{{ item.title | escape }}', '${{ item.price }}', [{% for img in item.images %}'{{ img | relative_url }}'{% unless forloop.last %}, {% endunless %}{% endfor %}], '{{ item.description | escape }}')">
                🖼️ View Gallery ({{ item.images.size }} Photo{% if item.images.size > 1 %}s{% endif %})
            </button>
        </div>
        {% endfor %}
    </div>
    {% endfor %}

    <!-- How to Order -->
    <div class="order-section">
        <h2 class="section-title" style="margin-bottom: 10px;">How to Place an Order</h2>
        <p style="text-align: center; color: var(--text-light);">Ordering your custom items is quick and simple!</p>
        
        <div class="order-steps">
            <div class="step">
                <div class="step-num">1</div>
                <strong>Browse & Select</strong>
                <p style="font-size: 0.85rem; color: var(--text-light); margin-top: 6px;">Choose your favorite custom items from our catalogue.</p>
            </div>
            <div class="step">
                <div class="step-num">2</div>
                <strong>Send a DM</strong>
                <p style="font-size: 0.85rem; color: var(--text-light); margin-top: 6px;">Message us on Instagram at @{{ site.instagram_username }}.</p>
            </div>
            <div class="step">
                <div class="step-num">3</div>
                <strong>Share Details</strong>
                <p style="font-size: 0.85rem; color: var(--text-light); margin-top: 6px;">Provide your photos, names, text, or chosen themes.</p>
            </div>
            <div class="step">
                <div class="step-num">4</div>
                <strong>Approve & Pay</strong>
                <p style="font-size: 0.85rem; color: var(--text-light); margin-top: 6px;">Review design layout proof and confirm your order!</p>
            </div>
        </div>
    </div>
</div>

<!-- Product Image Gallery Popup Modal -->
<div id="productModal" class="modal" onclick="closeModalOutside(event)">
    <div class="modal-content">
        <span class="close-btn" onclick="closeModal()">&times;</span>
        <h3 id="modalTitle" class="modal-title"></h3>
        <div id="modalPrice" class="modal-price"></div>
        
        <div class="carousel-container">
            <button class="nav-arrow prev" onclick="changeSlide(-1)">&#10094;</button>
            <img id="modalImg" src="" alt="Product Sample" class="modal-img">
            <button class="nav-arrow next" onclick="changeSlide(1)">&#10095;</button>
        </div>
        
        <div id="thumbStrip" class="thumbnail-strip"></div>
        
        <p id="modalDesc" class="modal-desc"></p>
    </div>
</div>

<script src="{{ '/assets/js/gallery.js' | relative_url }}"></script>
"""
}

# Add sample products collection files
sample_products = [
    ("rock-stone-frame.md", "Home Decor & Keepsakes", "Custom Rock Stone Photo Frame", 45, "Premium Collection", "Unique natural rock stone slates customized with high-definition photo printing. Includes display stands.", ["/assets/images/rock_frame_1.jpg", "/assets/images/rock_frame_2.jpg", "/assets/images/rock_frame_3.jpg"]),
    ("photo-frame.md", "Home Decor & Keepsakes", "Custom Photo Frame (with Photo)", 15, "Best Seller", "Classic framing option featuring high-quality photo print included. Ready to display or gift.", ["/assets/images/photo_frame_1.jpg", "/assets/images/photo_frame_2.jpg"]),
    ("ceramic-mugs.md", "Home Decor & Keepsakes", "Custom Ceramic Mugs", 20, "Everyday Favorite", "Durable 11oz ceramic mug personalized with custom photos, quotes, or graphics. Microwave & dishwasher safe.", ["/assets/images/mug_front.jpg", "/assets/images/mug_back.jpg"]),
    ("theme-coloring-book.md", "Stationery & Activities", "Custom Theme Coloring Book", 5, "Kids Favorite", "Mini customizable line-art coloring book crafted around your selected theme with a personalized name cover.", ["/assets/images/coloring_cover.jpg", "/assets/images/coloring_page1.jpg", "/assets/images/coloring_page2.jpg"])
]

for filename, cat, title, price, badge, desc, imgs in sample_products:
    imgs_str = "\n".join([f"  - {img}" for img in imgs])
    jekyll_structure[f"_products/{filename}"] = f"""---
title: "{title}"
category: "{cat}"
price: {price}
badge: "{badge}"
description: "{desc}"
images:
{imgs_str}
---
"""

# Output summary
print(f"Prepared {len(jekyll_structure)} Jekyll project files.")