#include "v8/include/v8.h"

void demo() {
    v8::Isolate* isolate = v8::Isolate::GetCurrent();
    v8::Local<v8::String> str = v8::String::NewFromUtf8(isolate, "hello");
}
