# PC Translation Strategy: Extracting a Standard Browser UI Skeleton

## 1. The Objective
Our current `Ourobrowser` prototype uses a custom PyQt6 interface. While functional, it is missing decades of standard browser QoL features (Find-in-page, robust download managers, history trees, bookmark organizers, context menus, SSL certificate viewers, etc.). 

Instead of reinventing these from scratch, we will use **PseudoCoup (PC)** to ingest the C++ source code of a mature open-source browser, extract its UI framework, and transpile it into a native Python skeleton. This skeleton will serve as the frontend for the PCHQ Hub.

## 2. Target Selection: Chromium
**Target Codebase:** Chromium (`chrome/browser/ui/views/` and `ui/views/`)
**Source Language:** C++
**Target Language:** Python

*Why Chromium?* 
Chromium's UI is written in a custom C++ framework called "Views" (Aura). Because it is strictly C++, it is an ideal target for PC's `tree-sitter` ingress. (Firefox's UI, by contrast, is a tangled mix of HTML, CSS, and JS, making direct translation to a native Python desktop app much messier).

## 3. The PC Translation Pipeline

### Phase A: Isolation & Boundary Definition
We cannot feed the entire 30GB Chromium repo into PC, or we will accidentally translate the V8 JavaScript engine into Python. We must define strict boundaries.
- **Keep:** Code dealing with window management, tabs, address bars, buttons, and menus (`chrome/browser/ui/`).
- **Sever:** Code dealing with DOM rendering, JavaScript execution, and network stacks (`third_party/blink`, `v8`, `net`).
- **Action:** We will configure PC's `Ledger` to recognize calls to Blink/V8 as "Dead Ends". When PC encounters a call to the engine, it will wrap it in a stub/abstract method rather than trying to follow the reference.

### Phase B: Ingress (UR-AST Construction)
PC will parse the C++ UI code. 
- C++ classes like `BrowserView`, `TabStrip`, and `LocationBarView` will be mapped into the UR-AST.
- PC's Ledger will resolve the massive C++ inheritance trees into concrete structural graphs.

### Phase C: Egress (Python Emission)
PC emits idiomatic Python. 
- The C++ pointer management and memory allocation will be abstracted away by PC into standard Python object references.
- We will be left with a massive, feature-complete Python module containing the entire visual logic and layout math of Google Chrome, completely decoupled from its web engine.

### Phase D: Rewiring to the PCHQ Hub & QtWebEngine
Once we have the translated Python UI skeleton, we plug it into our existing Ourobrowser backend:
1. **The Canvas:** We take the area where Chrome normally paints Blink, and we drop our `QWebEngineView` into it.
2. **The Logic:** When a user clicks the "Back" button, the translated Python `ToolbarView::BackButtonPressed()` method will fire. We wire that method to send an RPC signal to the **PCHQ Hub**.
3. **The JS-Stripping:** We maintain our `OurobrowserSchemeHandler` so that anything rendered inside the canvas remains strictly JS-free.

## 4. Unsolved Questions for the Pipeline
1. **UI Framework Translation:** Chromium's `ui/views` draws pixels directly using the Skia graphics library. When PC translates this C++ to Python, does PC map Skia drawing commands to PyQt6 equivalents (Map -> Wrap), or do we keep the Skia dependency and use `skia-python`?
2. **Event Loop Integration:** Chromium has a highly custom C++ message loop. PC will need to map this to standard Python `asyncio` or the Qt Event Loop so the UI remains non-blocking.
