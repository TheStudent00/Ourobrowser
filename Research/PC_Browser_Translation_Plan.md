# PC Strategy: Swapping V8 for Python in Chromium

## 1. The True Objective
The goal is **not** to rewrite the browser into Python. The goal is to keep the entire mature C++ browser intact (its UI, its rendering engine, its network stack) but use PseudoCoup (PC) to surgically extract the JavaScript engine (V8) and wire a Python execution engine in its place.

We want a standard, fully-featured Chromium browser that natively executes `<script type="text/python">` and fundamentally does not understand JavaScript.

## 2. The Anatomy of the Entanglement (The Target)
In Chromium, the rendering engine (Blink) and the JavaScript engine (V8) are separate entities, but they are glued together by a massive, complex layer called **V8 Bindings**. 

Every single DOM element (`document.getElementById`, `window.onload`, `HTMLButtonElement`) has a C++ binding that translates the internal Blink C++ object into a V8 JavaScript object. These bindings are largely auto-generated from **WebIDL** (Web Interface Definition Language) files.

If a human tried to manually sever V8 and write CPython bindings for the entire HTML5 DOM spec, it would take decades. 

## 3. The PC Processing Pipeline

### Phase A: Ingress (Processing the Bindings)
Instead of feeding PC the Chromium UI, we feed PC the **Blink-to-V8 Binding Layer** and the **WebIDL definitions**. 
PC parses the structural intent of the DOM bindings: it learns exactly how Chromium exposes its internal C++ DOM to an external scripting engine.

### Phase B: Egress (Emitting Python Bindings)
We configure PC to swap the target. Instead of generating C++ code that bridges Blink to V8, PC emits C++ code (like `pybind11` wrappers or native CPython C-API code) that bridges Blink directly to **Python**.

PC systematically traverses the entire W3C DOM spec within Chromium and auto-generates the exact equivalent Python bindings.

### Phase C: Hub Integration
With the bindings swapped, Chromium's internal event loop no longer passes `<script>` tags or `onclick` events to V8. It passes them through the newly PC-generated bindings to an embedded CPython runtime (or streams them out to the **PCHQ Hub**).

## 4. The Result
We compile this processed version of Chromium.
1. The user launches the application. It looks, feels, and operates exactly like Google Chrome, completely retaining the "basic UI skeleton" (downloads, history, tabs, address bar).
2. The UI is still running natively in highly-optimized C++.
3. But the moment the browser engine parses a webpage, JavaScript is dead on arrival. The entire DOM is strictly controllable via native Python.
