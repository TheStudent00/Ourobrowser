#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <any>
#include <stdexcept>

void ReturnV8String(PyInterpreterState* isolate, const char* str) {
        PyObject* v8_str = v8::String::NewFromUtf8(isolate, str).ToLocalChecked();
        return v8_str;
}