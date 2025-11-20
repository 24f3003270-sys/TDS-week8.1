---
marp: true
title: Product Documentation
author: 24f3003270@ds.study.iitm.ac.in
theme: custom-tech
paginate: true
---

<!-- Custom theme and styling -->
<style>
:root {
  --main-color: #003366;
  --accent-color: #00aaff;
  --bg-color: #f5f7fa;
}

section {
  background: var(--bg-color);
  color: var(--main-color);
  font-family: Arial, sans-serif;
}

h1, h2 {
  color: var(--accent-color);
}

.footer-text {
  position: absolute;
  bottom: 20px;
  font-size: 14px;
}
</style>

---

<!-- _class: lead -->
<!-- _paginate: true -->

# Product Documentation

**Technical Writer:**  
24f3003270@ds.study.iitm.ac.in  

<div class="footer-text">
Confidential – Internal Software Documentation
</div>

---

<!-- _class: default -->

# System Overview

Our product platform provides scalable, secure, and modular services.

- Cloud native architecture  
- Microservices based  
- Deployed with CI/CD pipelines  

---

<!-- _backgroundImage: url("https://images.unsplash.com/photo-1537432376769-00a4c4ca8cd4") -->
<!-- _backgroundSize: cover -->

# Platform Features

- Real-time processing  
- Secure authentication  
- Scalable microservices  
- Integrated monitoring  

This slide uses a background image.

---

<!-- _class: default -->

# Algorithmic Complexity

### Time Complexity of Merge Sort

\[
T(n) = O(n \log n)
\]

### Space Complexity

\[
S(n) = O(n)
\]

This ensures efficiency for large scale systems.

---

<!-- _class: default -->

# Developer API Example

```python
def compute_latency(requests):
    base_latency = 50
    return base_latency + (2 * requests)
