#include "v8/include/v8.h"

void CreateV8Object(v8::Isolate* isolate) {
    v8::Local<v8::Context> context = isolate->GetCurrentContext();
    v8::Local<v8::Object> obj = v8::Object::New(isolate);
    
    v8::Local<v8::String> key = v8::String::NewFromUtf8(isolate, "hello").ToLocalChecked();
    v8::Local<v8::String> value = v8::String::NewFromUtf8(isolate, "world").ToLocalChecked();
    
    obj->Set(context, key, value).Check();
}
