#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <any>
#include <stdexcept>

void ClickMethodCallback(v8::FunctionCallbackInfo<v8::Value> info) {
        v8::Isolate isolate = info.GetIsolate();
        v8::HandleScope handle_scope = nullptr;
        v8::Local<v8::Context> context = isolate.GetCurrentContext();
        HTMLButtonElement impl = V8HTMLButtonElement::ToImpl(info.Holder());
    impl.click();
}