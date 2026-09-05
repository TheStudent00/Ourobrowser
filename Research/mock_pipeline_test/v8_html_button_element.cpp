#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <any>
#include <stdexcept>

void ClickMethodCallback(PyObject* info) {
        PyInterpreterState* isolate = info.GetIsolate();
        PyObject* handle_scope = nullptr;
        PyDictObject* context = isolate.GetCurrentContext();
        HTMLButtonElement* impl = V8HTMLButtonElement::ToImpl(info.Holder());
    impl.click();
}