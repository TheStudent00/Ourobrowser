#include "v8/include/v8.h"

v8::Local<v8::String> ReturnV8String(v8::Isolate* isolate, const char* str) {
    v8::Local<v8::String> v8_str = v8::String::NewFromUtf8(isolate, str).ToLocalChecked();
    return v8_str;
}
