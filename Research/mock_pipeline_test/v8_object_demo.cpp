#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <any>
#include <stdexcept>

void CreateV8Object(PyInterpreterState* isolate) {
        PyDictObject* context = isolate.GetCurrentContext();
        PyObject* obj = v8::Object::New(isolate);
        PyObject* key = v8::String::NewFromUtf8(isolate, "hello").ToLocalChecked();
        PyObject* value = v8::String::NewFromUtf8(isolate, "world").ToLocalChecked();
    obj.Set(context, key, value).Check();
}